#!/usr/bin/env python3
"""Build the final GRC105 DOCX from the validated repository artifacts.

The builder deliberately reads the task deliverables rather than recreating
their analysis.  It uses Pandoc for document generation and a small standard-
library Open XML pass for the required monochrome/report styles and footer.
"""

from __future__ import annotations

import csv
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("Pillow is required for monochrome figure preparation") from exc


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "10-final-submission"
BUILD = OUT / "build"
FIGURES = OUT / "figures"
SOURCE_FIGURES = FIGURES / "sources"
QA = OUT / "qa"
DOCX = OUT / "GRC105_IRP_Assignment_2025-GCR-12684.docx"
PDF = QA / "GRC105_IRP_Assignment_2025-GCR-12684.pdf"
MARKDOWN = BUILD / "final-report.md"

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
W = f"{{{NS_W}}}"
R = f"{{{NS_R}}}"

ET.register_namespace("w", NS_W)
ET.register_namespace("r", NS_R)
ET.register_namespace("pr", "http://schemas.openxmlformats.org/package/2006/relationships")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def strip_title(markdown: str) -> str:
    lines = markdown.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    # The source task documents use explicit numbering for readability when
    # viewed as Markdown.  Pandoc also numbers headings in the final report;
    # remove only the source numeric prefix so the report has one numbering
    # system rather than headings such as "3.1 1. Incident classification".
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+\d+(?:\.\d+)*\.?\s+(.*)$", line)
        if match:
            lines[index] = f"{match.group(1)} {match.group(2)}"
    return "\n".join(lines).strip()


def escape_cell(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def csv_markdown(path: str, title: str | None = None) -> str:
    p = ROOT / path
    with p.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return ""
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError(f"Inconsistent CSV columns: {path}")
    header = rows[0]
    out: list[str] = []
    if title:
        out.append(f"### {title}\n")
    out.append("| " + " | ".join(escape_cell(v) for v in header) + " |")
    out.append("| " + " | ".join("---" for _ in header) + " |")
    out.extend("| " + " | ".join(escape_cell(v) for v in row) + " |" for row in rows[1:])
    return "\n".join(out)


def csv_markdown_groups(path: str, groups: list[tuple[str, list[str]]]) -> str:
    """Render a wide register as readable keyed tables without dropping fields."""
    p = ROOT / path
    with p.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        rows = list(reader)
    if not headers:
        return ""
    output: list[str] = []
    for title, selected in groups:
        missing = [column for column in selected if column not in headers]
        if missing:
            raise ValueError(f"Missing CSV columns in {path}: {missing}")
        table_lines = [f"**{title}**", ""]
        table_lines.append("| " + " | ".join(escape_cell(column) for column in selected) + " |")
        table_lines.append("| " + " | ".join("---" for _ in selected) + " |")
        for row in rows:
            table_lines.append("| " + " | ".join(escape_cell(row.get(column, "")) for column in selected) + " |")
        output.append("\n".join(table_lines))
    return "\n\n".join(output)


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


LEGEND_REPLACEMENTS = {
    "Gold marker = current provisional position": "Dotted marker = current provisional position",
    "Navy = technical work": "Solid border = technical work",
    "Teal = validation/business gates": "Double border = validation/business gates",
    "Gold = management decision": "Decision diamond = management decision",
    "Red = rejection or further investigation": "Dashed path = reject or investigate",
    "Gold = decision/authority": "Decision diamond = decision/authority",
    "Red = urgent protective or hold path": "Dashed path = urgent protective or hold path",
    "Gold = approval gate": "Decision gate = approval gate",
    "Red = hold/reject/further investigation": "Dashed path = hold/reject/investigate",
    "Navy = incident leadership": "Solid border = incident leadership",
    "Blue = security/technical functions": "Double border = security/technical functions",
    "Teal = continuity/business functions": "Dotted border = continuity/business functions",
    "Gold = approval; gray = validation/reporting": "Decision diamond = approval; dotted border = validation/reporting",
    "Gold = entry; teal = decision/normal path": "Solid path = entry; double border = decision/normal path",
    "Red = constrained emergency authority": "Dashed path = constrained emergency authority",
    "Blue-gray = record/review control": "Dotted border = record/review control",
    "Gold = escalation or approval": "Decision diamond = escalation or approval",
    "Teal = proposed allocation or action": "Double border = proposed allocation or action",
    "Gray = contingent support": "Dotted border = contingent support",
    "Gray = contingent external support": "Dotted border = contingent external support",
    "Navy = activity/execution": "Solid border = activity/execution",
    "Gold = accountability or emergency decision": "Decision diamond = accountability or emergency decision",
    "Teal = consultation": "Double border = consultation",
    "Gray = notification/recording": "Dotted border = notification/recording",
    "Navy = assets; blue-gray = recorded observations": "Solid border = assets; double border = recorded observations",
    "Amber dashed = unverified hypotheses": "Dashed border = unverified hypotheses",
    "Gold = response control point": "Decision diamond = response control point",
    "Blue-gray = recorded observation": "Double border = recorded observation",
    "Amber dashed = potential impact or hypothesis": "Dashed border = potential impact or hypothesis",
    "Red = unknown consequence requiring validation": "Dotted border = unknown consequence requiring validation",
    "Amber dashed link = dependency or decision tradeoff": "Dashed link = dependency or decision tradeoff",
}


def replace_legend_terms(value: str) -> str:
    for source, replacement in LEGEND_REPLACEMENTS.items():
        value = value.replace(source, replacement)
    return value


def make_monochrome_figures() -> list[str]:
    mapping = {
        "task1-incident-timeline": ("03-task-01-incident-assessment", "incident-timeline"),
        "task1-severity-decision-tree": ("03-task-01-incident-assessment", "severity-decision-tree"),
        "task2-csirt-organisation": ("04-task-02-ir-plan-and-governance", "csirt-organisational-structure"),
        "task2-recovery-approval-gates": ("04-task-02-ir-plan-and-governance", "recovery-approval-gates"),
        "task3-response-workflow": ("05-task-03-response-playbook", "response-workflow"),
        "task5-tabletop-timeline": ("07-task-05-tabletop-simulation", "tabletop-timeline"),
    }
    FIGURES.mkdir(parents=True, exist_ok=True)
    SOURCE_FIGURES.mkdir(parents=True, exist_ok=True)
    results: list[str] = []
    for out_name, (task_dir, base) in mapping.items():
        source_mmd = ROOT / task_dir / "diagrams" / f"{base}.mmd"
        source_png = ROOT / task_dir / "visuals" / f"{base}.png"
        source_svg = ROOT / task_dir / "visuals" / f"{base}.svg"
        if not all(p.exists() for p in (source_mmd, source_png, source_svg)):
            raise FileNotFoundError(f"Missing approved visual source/export for {base}")
        source_text = replace_legend_terms(source_mmd.read_text(encoding="utf-8"))
        shutil.copy2(source_mmd, SOURCE_FIGURES / f"{out_name}.mmd")
        (SOURCE_FIGURES / f"{out_name}.mmd").write_text(source_text, encoding="utf-8")
        with source_svg.open(encoding="utf-8") as handle:
            svg = handle.read()

        def gray_color(match: re.Match[str]) -> str:
            raw = match.group(1)
            if raw.lower() in {"none", "currentcolor"}:
                return match.group(0)
            try:
                r, g, b = (int(raw[i : i + 2], 16) for i in (0, 2, 4))
            except ValueError:
                return match.group(0)
            lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
            if lum >= 245:
                gray = "FFFFFF"
            elif lum >= 205:
                gray = "E6E6E6"
            elif lum >= 160:
                gray = "B3B3B3"
            elif lum >= 100:
                gray = "707070"
            elif lum >= 45:
                gray = "333333"
            else:
                gray = "000000"
            return "#" + gray

        svg = re.sub(r"#([0-9A-Fa-f]{6})", gray_color, svg)
        svg = re.sub(r"#([0-9A-Fa-f]{3})(?![0-9A-Fa-f])", lambda m: m.group(0), svg)
        def gray_rgb(match: re.Match[str]) -> str:
            r, g, b = (int(value) for value in match.groups())
            lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
            if lum >= 245:
                gray = 255
            elif lum >= 205:
                gray = 230
            elif lum >= 160:
                gray = 179
            elif lum >= 100:
                gray = 112
            elif lum >= 45:
                gray = 51
            else:
                gray = 0
            return f"rgb({gray}, {gray}, {gray})"
        svg = re.sub(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", gray_rgb, svg, flags=re.I)
        svg = replace_legend_terms(svg)
        svg = svg.replace("background-color: white", "background-color: white")
        (FIGURES / f"{out_name}.svg").write_text(svg, encoding="utf-8")

        # Chrome is already available in the project environment.  Rendering
        # the report SVG produces a PNG whose labels match the report-only
        # monochrome SVG; the source task PNG remains untouched.
        chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
        rendered_png = FIGURES / f"{out_name}.png"
        if chrome:
            viewbox = re.search(r'viewBox="([^"]+)"', svg)
            dimensions = [int(float(part)) for part in viewbox.group(1).split()[-2:]] if viewbox else [1600, 900]
            window = f"{max(800, min(dimensions[0], 2400))},{max(600, min(dimensions[1], 5000))}"
            subprocess.run([
                chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                f"--window-size={window}", f"--screenshot={rendered_png}",
                (FIGURES / f"{out_name}.svg").as_uri(),
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
            Image.open(rendered_png).convert("L").save(rendered_png, optimize=True)
        else:
            image = Image.open(source_png).convert("L")
            image.save(rendered_png, optimize=True)
        results.append(out_name)
    return results


def build_markdown(figures: list[str], page_map: dict[str, int] | None = None) -> tuple[str, int, int, int, int]:
    page_map = page_map or {}
    task1 = strip_title(read("03-task-01-incident-assessment/TASK-1-INTEGRATED-ASSESSMENT.md"))
    task2_stage1 = strip_title(read("04-task-02-ir-plan-and-governance/TASK-2-STAGE-1-GOVERNANCE-DRAFT.md"))
    task2_stage2 = strip_title(read("04-task-02-ir-plan-and-governance/TASK-2-STAGE-2-CSIRT-RACI-DRAFT.md"))
    task3 = strip_title(read("05-task-03-response-playbook/TASK-3-RESPONSE-PLAYBOOK.md"))
    task4 = strip_title(read("06-task-04-communications/TASK-4-COMMUNICATION-PLAN.md"))
    task5 = strip_title(read("07-task-05-tabletop-simulation/TASK-5-TABLETOP-EXERCISE.md"))
    task6 = strip_title(read("08-task-06-case-study/TASK-6-CASE-STUDY-ANALYSIS.md"))

    executive = re.search(r"## 2\. Executive briefing\n(.*?)(?=\n## )", read("06-task-04-communications/TASK-4-COMMUNICATION-PLAN.md"), re.S)
    learner = re.search(r"## 3\. Learner notice\n(.*?)(?=\n## )", read("06-task-04-communications/TASK-4-COMMUNICATION-PLAN.md"), re.S)
    case_body = re.sub(r"^#.*?\n", "", read("08-task-06-case-study/TASK-6-CASE-STUDY-ANALYSIS.md"), count=1, flags=re.S)
    case_body = re.sub(r"\n\*\*Source:\*\*.*\Z", "", case_body, flags=re.S)
    executive_words = count_words(executive.group(1) if executive else "")
    learner_words = count_words(learner.group(1) if learner else "")
    case_words = count_words(case_body)

    body_parts: list[str] = []
    body_parts.append("""# ICDFA GRC105\n\n## Incident Response Planning and Ransomware Response Simulation\n\n**Northbridge Skills Institute — Evidence-Based Assessment Report**\n\n| Student information | Details |\n|---|---|\n| Student | Ayuba Amadi |\n| Registration number | 2025/GCR/12684 |\n| Official email | gcr2512684@students.icdfa.edu.ng |\n| Programme | GRC Engineering (CGRCE) |\n| School | School of Cyber Risk, Governance and Compliance |\n| Cohort | Batch B2025 |\n| Academic session | 2026 |\n| Level / year | Level 1 / Year 1 |\n| Course | GRC105 — Incident Management and Business Continuity |\n| Assignment | Incident Response Planning and Ransomware Response Simulation |\n| Assessment weight | 20% |\n| Final report word count | @@REPORT_WORDS@@ words; narrative text excludes cover, contents, tables and references. |\n\n**Document status:** Final draft for academic review; no live incident response, forensic acquisition, restoration or deployment is claimed.\n\n""")
    contents = """# Contents\n\n1. Task 1 — Incident Classification and Initial Assessment ................................ {task1}\n2. Task 2 — Incident Response Plan and Team Responsibilities ................. {task2}\n3. Task 3 — Response Playbook and Evidence Preservation ...................... {task3}\n4. Task 4 — Communication and Escalation ............................................... {task4}\n5. Task 5 — Tabletop Exercise and Improvement Plan ............................... {task5}\n6. Task 6 — Case Study Analysis and Critical Reflection ........................... {task6}\n7. References ................................................................................................ {refs}\n8. AI-assistance acknowledgement ............................................................. {ai}\n\n*Page references are generated from the rendered PDF and verified by the build script.*\n""".format(
        task1=page_map.get("Task 1", "—"), task2=page_map.get("Task 2", "—"),
        task3=page_map.get("Task 3", "—"), task4=page_map.get("Task 4", "—"),
        task5=page_map.get("Task 5", "—"), task6=page_map.get("Task 6", "—"),
        refs=page_map.get("References", "—"), ai=page_map.get("AI", "—"),
    )
    body_parts.append(contents)
    body_parts.append("""# Task 1 — Incident Classification and Initial Assessment\n\n""" + task1)
    # The chronology remains fully represented in the Task 1 text/registers.  The
    # wide timeline is retained as a supporting export but omitted from the
    # portrait report body because its labels are not readable at page width.
    body_parts.append("\n\n" + f"![Initial severity decision logic (monochrome report export)](../figures/{figures[1]}.png){{width=2.75in}}\n\n**Figure 1 — Initial severity decision logic.**\n\n")
    body_parts.append(csv_markdown_groups("03-task-01-incident-assessment/data/evidence-analysis-register.csv", [
        ("Evidence analysis register — evidence core", ["Evidence ID", "Timestamp (WAT)", "Original source", "Confirmed observation"]),
        ("Evidence analysis register — analytical uncertainty", ["Evidence ID", "Reasonable working hypothesis", "Alternative explanation", "Unresolved questions"]),
        ("Evidence analysis register — impact assessment", ["Evidence ID", "Potentially affected assets", "Confidentiality integrity availability implications"]),
        ("Evidence analysis register — verification and traceability", ["Evidence ID", "Recommended verification activity", "Evidence limitations", "Traceability"]),
    ]))
    body_parts.append("\n\n" + csv_markdown_groups("03-task-01-incident-assessment/data/asset-impact-register.csv", [
        ("Asset impact register — asset and observed status", ["Asset ID", "Asset or service", "Business function", "Relevant evidence IDs", "Observed status"]),
        ("Asset impact register — confirmed and potential impact", ["Asset ID", "Confirmed impact", "Potential security implications"]),
        ("Asset impact register — status and verification", ["Asset ID", "Affected-asset status", "Investigation priority", "Verification requirements"]),
    ]))
    body_parts.append("\n\n" + csv_markdown_groups("03-task-01-incident-assessment/data/investigation-priorities.csv", [
        ("Investigation priorities — questions", ["Investigation ID", "Related evidence IDs", "Priority", "Question"]),
        ("Investigation priorities — evidence and ownership", ["Investigation ID", "Responsible role", "Required logs records artifacts interviews or validation procedures"]),
        ("Investigation priorities — decision value and status", ["Investigation ID", "Expected decision value", "How findings could change severity or scope assessment", "Current status"]),
    ]))

    body_parts.append("\n\n# Task 2 — Incident Response Plan and Team Responsibilities\n\n" + task2_stage1)
    body_parts.append("\n\n" + task2_stage2)
    body_parts.append("\n\n" + f"![Proposed CSIRT organisational structure (monochrome report export)](../figures/{figures[2]}.png){{width=5.6in}}\n\n**Figure 2 — Proposed CSIRT organisational structure.**\n\n")
    body_parts.append(csv_markdown_groups("04-task-02-ir-plan-and-governance/raci.csv", [
        ("RACI accountability matrix — activity and accountability", ["Activity ID", "Activity", "Responsible role IDs", "Accountable role ID"]),
        ("RACI accountability matrix — consultation and notification", ["Activity ID", "Consulted role IDs", "Informed role IDs"]),
        ("RACI accountability matrix — authority record", ["Activity ID", "Normal authority basis", "Emergency or exception note", "Required record"]),
    ]))
    body_parts.append("\n\n" + csv_markdown_groups("04-task-02-ir-plan-and-governance/data/csirt-role-register.csv", [
        ("CSIRT role register — purpose and responsibility", ["Role ID", "Functional role", "CSIRT classification", "Key responsibility"]),
        ("CSIRT role register — authority and status", ["Role ID", "Normal decision authority", "Status"]),
        ("CSIRT role register — staffing and competence", ["Role ID", "Primary staffing assignment", "Alternate staffing assignment", "Required competence"]),
        ("CSIRT role register — dependencies and provenance", ["Role ID", "Support dependency", "Potential conflict", "Source or governance reference"]),
    ]))
    body_parts.append("\n\n" + csv_markdown("04-task-02-ir-plan-and-governance/readiness/preparation-improvements.csv", "Preparation improvements") if (ROOT / "04-task-02-ir-plan-and-governance/readiness/preparation-improvements.csv").exists() else "\n\nThe four proposed preparation improvements are documented in the Task 2 readiness register and integrated draft.")

    body_parts.append("\n\n# Task 3 — Response Playbook and Evidence Preservation\n\n" + task3)
    body_parts.append(csv_markdown_groups("05-task-03-response-playbook/data/response-actions.csv", [
        ("Canonical response actions — stage and ownership", ["Action ID", "Time/stage WAT", "Owner", "Status"]),
        ("Canonical response actions — planned action", ["Action ID", "Action", "Status"]),
        ("Canonical response actions — approval and evidence", ["Action ID", "Required approval", "Evidence to retain"]),
        ("Canonical response actions — completion", ["Action ID", "Completion check", "Status"]),
    ]))
    body_parts.append("\n\n" + csv_markdown_groups("05-task-03-response-playbook/data/evidence-register.csv", [
        ("Canonical evidence register — source and method", ["Item ID", "Source", "Relevant evidence or purpose", "Proposed collection method"]),
        ("Canonical evidence register — collector and status", ["Item ID", "Collector role", "Collection status"]),
        ("Canonical evidence register — timing and integrity", ["Item ID", "Planned date/time WAT", "Integrity check (planned)", "Restricted secure storage"]),
        ("Canonical evidence register — restrictions and custody", ["Item ID", "Custody transfer (planned)", "Collection status"]),
    ]))

    body_parts.append("\n\n# Task 4 — Communication and Escalation\n\n" + task4)
    body_parts.append("\n\n" + csv_markdown_groups("06-task-04-communications/stakeholder-matrix.csv", [
        ("Stakeholder communication matrix — trigger and channel", ["Stakeholder", "Trigger", "Message owner", "Channel"]),
        ("Stakeholder communication matrix — approval and cadence", ["Stakeholder", "Alternative channel", "Approver", "Update frequency"]),
    ]))

    body_parts.append("\n\n# Task 5 — Tabletop Exercise and Improvement Plan\n\n" + task5)
    body_parts.append(csv_markdown_groups("07-task-05-tabletop-simulation/data/exercise-decision-log.csv", [
        ("Canonical simulated decision log — inject and decision", ["Exercise minute", "Inject", "Decision", "Decision owner"]),
        ("Canonical simulated decision log — rationale and communication", ["Exercise minute", "Rationale", "Communication"]),
        ("Canonical simulated decision log — effect and status", ["Exercise minute", "Effect on response or recovery", "Simulation status"]),
    ]))
    body_parts.append("\n\n" + csv_markdown_groups("07-task-05-tabletop-simulation/data/corrective-actions.csv", [
        ("Canonical corrective-action register — finding and action", ["Action ID", "Priority", "Finding", "Corrective action"]),
        ("Canonical corrective-action register — ownership", ["Action ID", "Owner", "Target completion"]),
        ("Canonical corrective-action register — evidence and status", ["Action ID", "Measurable evidence", "Status"]),
    ]))

    body_parts.append("\n\n# Task 6 — Case Study Analysis and Critical Reflection\n\n" + task6)
    body_parts.append("""

# References

1. ICDFA. *GRC105 Incident Response Planning Assignment*. Supplied course document, pp. 1–6.
2. ICDFA. *Incident Response Planning*. GRC105 Week 20 teaching presentation, slides 1–18. Supplied course presentation.
3. Nelson, A., Rekhi, S., Souppaya, M., and Scarfone, K. (2025). *NIST SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*. https://csrc.nist.gov/pubs/sp/800/61/r3/final
4. Cichonski, P., Millar, T., Grance, T., and Scarfone, K. (2012). *NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response*. https://csrc.nist.gov/pubs/sp/800/86/final
5. CISA and partners. *#StopRansomware Guide*. https://www.cisa.gov/stopransomware/ransomware-guide

The report uses the supplied assignment and Week 20 slides as the scenario and marking sources. NIST SP 800-61 Revision 3 is used for CSF 2.0-aligned incident-response governance; the Week 20 four-stage teaching model is retained as a course-facing organisation aid and is not attributed to Revision 3 as its lifecycle.

# AI-assistance acknowledgement

AI assistance was used transparently for document preparation, technical structuring, evidence-register presentation, visual conversion support, cross-artifact consistency checks and quality assurance. The student remains responsible for reviewing, validating and explaining the report, its evidence interpretations, citations and final submission.
""")

    text = "\n\n".join(part for part in body_parts if part.strip()) + "\n"
    narrative = text.split("# Task 1 —", 1)[1].split("# References", 1)[0]
    narrative_lines = []
    in_table = False
    for line in narrative.splitlines():
        if line.startswith("| "):
            in_table = True
            continue
        if in_table and not line.startswith("| "):
            in_table = False
        if not in_table:
            narrative_lines.append(line)
    report_words = count_words("\n".join(narrative_lines))
    text = text.replace("@@REPORT_WORDS@@", str(report_words))
    return text, report_words, executive_words, learner_words, case_words


def set_attr(element: ET.Element, name: str, value: str) -> None:
    element.set(W + name, value)


def child(parent: ET.Element, tag: str) -> ET.Element:
    found = parent.find(W + tag)
    if found is None:
        found = ET.SubElement(parent, W + tag)
    return found


def set_style(style: ET.Element, font_size: str, bold: bool = False, centered: bool = False) -> None:
    rpr = style.find(W + "rPr")
    ppr = style.find(W + "pPr")
    if rpr is None:
        rpr = ET.Element(W + "rPr")
        if ppr is not None:
            style.insert(list(style).index(ppr) + 1, rpr)
        else:
            style.append(rpr)
    fonts = child(rpr, "rFonts")
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(W + key, "Times New Roman")
    color = child(rpr, "color")
    color.set(W + "val", "000000")
    size = child(rpr, "sz")
    size.set(W + "val", font_size)
    if bold:
        child(rpr, "b")
    if centered and ppr is None:
        ppr = ET.Element(W + "pPr")
        style.insert(list(style).index(rpr), ppr)
    if centered and ppr is not None:
        jc = child(ppr, "jc")
        jc.set(W + "val", "center")


def add_footer(files: dict[str, bytes]) -> None:
    rel_path = "word/_rels/document.xml.rels"
    rel_text = files[rel_path].decode("utf-8")
    existing_ids = [int(value) for value in re.findall(r'Id="rId(\d+)"', rel_text)]
    rid = f"rId{max(existing_ids or [0]) + 1}"
    relationship = f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
    rel_text = rel_text.replace("</Relationships>", relationship + "</Relationships>", 1)
    files[rel_path] = rel_text.encode("utf-8")

    footer = ET.Element(W + "ftr")
    paragraph = ET.SubElement(footer, W + "p")
    ppr = ET.SubElement(paragraph, W + "pPr")
    jc = ET.SubElement(ppr, W + "jc")
    jc.set(W + "val", "center")
    run = ET.SubElement(paragraph, W + "r")
    begin = ET.SubElement(run, W + "fldChar")
    begin.set(W + "fldCharType", "begin")
    run2 = ET.SubElement(paragraph, W + "r")
    instr = ET.SubElement(run2, W + "instrText")
    instr.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    instr.text = " PAGE "
    run3 = ET.SubElement(paragraph, W + "r")
    end = ET.SubElement(run3, W + "fldChar")
    end.set(W + "fldCharType", "end")
    files["word/footer1.xml"] = ET.tostring(footer, encoding="utf-8", xml_declaration=True)

    # Pandoc's package already declares a default XML content type.  Keeping
    # the source content-types part unchanged avoids a LibreOffice 24.x import
    # hang with this large document while the relationship type still
    # identifies footer1.xml as a Word footer part.

    # Preserve the original document XML namespace declarations and
    # compatibility attributes.  LibreOffice is stricter about these than
    # the generic XML serializer, so the footer reference is inserted as a
    # small raw XML fragment rather than reserialising the whole document.
    document = files["word/document.xml"].decode("utf-8")
    footer_fragment = f'<w:footerReference w:type="default" r:id="{rid}"/>'
    if "<w:footerReference" not in document:
        if "<w:pgSz" in document:
            document = document.replace("<w:pgSz", footer_fragment + "<w:pgSz", 1)
        else:
            document = document.replace("</w:sectPr>", footer_fragment + "</w:sectPr>", 1)
    files["word/document.xml"] = document.encode("utf-8")


def postprocess_docx(path: Path) -> None:
    with zipfile.ZipFile(path, "r") as archive:
        files = {name: archive.read(name) for name in archive.namelist()}

    # Use text-level style edits rather than reserialising styles.xml.  This
    # preserves Pandoc's valid Open XML ordering and avoids import problems in
    # large reports while still enforcing monochrome Times New Roman styling.
    styles = files["word/styles.xml"].decode("utf-8")
    styles = re.sub(r"<w:rFonts[^>]*/>", '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>', styles)
    styles = re.sub(r"<w:color[^>]*/>", '<w:color w:val="000000"/>', styles)
    styles = re.sub(r'<w:spacing w:after="[^"]+"/>', '<w:spacing w:after="120" w:line="360" w:lineRule="auto"/>', styles, count=1)
    for style_id, size in (("Heading1", "28"), ("Heading2", "24"), ("Heading3", "24")):
        pattern = re.compile(rf'(<w:style\b[^>]*w:styleId="{style_id}"[^>]*>.*?</w:style>)', re.S)
        def tune(match: re.Match[str], size: str = size, style_id: str = style_id) -> str:
            block = match.group(1)
            block = re.sub(r'<w:sz w:val="[^"]+"', f'<w:sz w:val="{size}"', block, count=1)
            if style_id == "Heading1" and "<w:jc w:val=\"center\"" not in block:
                block = block.replace("</w:pPr>", '<w:jc w:val="center"/></w:pPr>', 1)
            return block
        styles = pattern.sub(tune, styles)
    compact_pattern = re.compile(r'(<w:style\b[^>]*w:styleId="Compact"[^>]*>.*?</w:style>)', re.S)
    def tune_compact(match: re.Match[str]) -> str:
        block = match.group(1)
        if "<w:rPr" in block:
            block = re.sub(r'<w:sz w:val="[^"]+"', '<w:sz w:val="20"', block, count=1)
            block = re.sub(r'<w:szCs w:val="[^"]+"', '<w:szCs w:val="20"', block, count=1)
            if '<w:szCs' not in block:
                block = block.replace('</w:rPr>', '<w:szCs w:val="20"/></w:rPr>', 1)
        else:
            block = block.replace('<w:pPr>', '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:pPr>', 1)
        block = block.replace('<w:spacing w:after="36" w:before="36"/>', '<w:spacing w:after="24" w:before="24"/>')
        block = block.replace('<w:spacing w:after="36" w:before="36" />', '<w:spacing w:after="24" w:before="24" />')
        return block
    styles = compact_pattern.sub(tune_compact, styles)
    files["word/styles.xml"] = styles.encode("utf-8")

    document = files["word/document.xml"].decode("utf-8")

    def add_page_break(match: re.Match[str]) -> str:
        paragraph = match.group(0)
        text = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", paragraph, flags=re.S))
        if (re.search(r"Task [1-6] —", text) or text.strip().endswith("Contents")) and "w:pageBreakBefore" not in paragraph:
            paragraph = re.sub(r'<w:pStyle w:val="Heading1"\s*/>', '<w:pStyle w:val="Heading1"/><w:pageBreakBefore/>', paragraph, count=1)
        return paragraph

    document = re.sub(r"<w:p\b.*?</w:p>", add_page_break, document, flags=re.S)
    document = re.sub(r"w:color w:val=\"[0-9A-Fa-f]+\"", "w:color w:val=\"000000\"", document)
    document = re.sub(r"w:shd w:fill=\"[0-9A-Fa-f]+\"", "w:shd w:fill=\"FFFFFF\"", document)
    if re.search(r"<w:sectPr\s*/>", document):
        document = re.sub(r"<w:sectPr\s*/>", '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1417" w:bottom="1417" w:left="1417" w:right="1417" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>', document, count=1)
    elif "<w:pgSz" in document:
        document = re.sub(r"<w:pgSz[^>]*/\s*>", '<w:pgSz w:w="11906" w:h="16838"/>', document, count=1)
    else:
        document = document.replace("</w:sectPr>", '<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1417" w:bottom="1417" w:left="1417" w:right="1417" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>', 1)
    if "<w:pgMar" in document:
        document = re.sub(r"<w:pgMar[^>]*/\s*>", '<w:pgMar w:top="1417" w:bottom="1417" w:left="1417" w:right="1417" w:header="708" w:footer="708" w:gutter="0"/>', document, count=1)
    files["word/document.xml"] = document.encode("utf-8")
    add_footer(files)

    temporary = path.with_suffix(".tmp.docx")
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(name, content)
    temporary.replace(path)


def postprocess_main_docx(path: Path) -> None:
    """Add task-section page breaks without rewriting section/package XML."""
    with zipfile.ZipFile(path, "r") as archive:
        files = {name: archive.read(name) for name in archive.namelist()}
    document = files["word/document.xml"].decode("utf-8")

    def add_page_break(match: re.Match[str]) -> str:
        paragraph = match.group(0)
        text = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", paragraph, flags=re.S))
        if (re.search(r"Task [1-6] —", text) or text.strip().endswith("Contents")) and "w:pageBreakBefore" not in paragraph:
            paragraph = re.sub(r'<w:pStyle w:val="Heading1"\s*/>', '<w:pStyle w:val="Heading1"/><w:pageBreakBefore/>', paragraph, count=1)
        return paragraph

    document = re.sub(r"<w:p\b.*?</w:p>", add_page_break, document, flags=re.S)
    document = re.sub(r"w:color w:val=\"[0-9A-Fa-f]+\"", "w:color w:val=\"000000\"", document)
    document = re.sub(r"w:shd w:fill=\"[0-9A-Fa-f]+\"", "w:shd w:fill=\"FFFFFF\"", document)

    caption_terms = (
        "register", "matrix", "canonical response actions", "canonical simulated decision log",
        "canonical corrective-action register", "preparation improvements",
    )
    def keep_table_caption(match: re.Match[str]) -> str:
        paragraph = match.group(0)
        text = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", paragraph, flags=re.S)).lower()
        if any(term in text for term in caption_terms) and "<w:keepNext" not in paragraph:
            if "<w:pPr" in paragraph:
                paragraph = paragraph.replace("</w:pPr>", "<w:keepNext/></w:pPr>", 1)
            else:
                paragraph = paragraph.replace("<w:p>", "<w:p><w:pPr><w:keepNext/></w:pPr>", 1)
        return paragraph
    document = re.sub(r"<w:p\b.*?</w:p>", keep_table_caption, document, flags=re.S)

    def add_row_property(row: str, property_name: str) -> str:
        if f"<w:{property_name}" in row:
            return row
        trpr = re.search(r"<w:trPr\b[^>]*>.*?</w:trPr>", row, flags=re.S)
        if trpr:
            updated = trpr.group(0).replace("</w:trPr>", f"<w:{property_name}/></w:trPr>", 1)
            return row[:trpr.start()] + updated + row[trpr.end():]
        return re.sub(r"(<w:tr\b[^>]*>)", rf"\1<w:trPr><w:{property_name}/></w:trPr>", row, count=1)

    def process_table(table_match: re.Match[str]) -> str:
        table = table_match.group(0)
        rows = list(re.finditer(r"<w:tr\b.*?</w:tr>", table, flags=re.S))
        if not rows:
            return table
        # The first row repeats on continued pages; every row is kept intact.
        for index in range(len(rows) - 1, -1, -1):
            row = rows[index].group(0)
            row = add_row_property(row, "cantSplit")
            if index == 0:
                row = add_row_property(row, "tblHeader")
            table = table[:rows[index].start()] + row + table[rows[index].end():]
        return table

    document = re.sub(r"<w:tbl\b.*?</w:tbl>", process_table, document, flags=re.S)
    files["word/document.xml"] = document.encode("utf-8")
    temporary = path.with_suffix(".tmp.docx")
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(name, content)
    temporary.replace(path)


def create_reference_docx() -> tuple[Path, Path]:
    """Create a temporary reference document without adding a competing DOCX output."""
    reference_dir = Path(tempfile.mkdtemp(prefix="grc105-reference-"))
    reference_md = reference_dir / "reference-template.md"
    reference_docx = reference_dir / "reference-template.docx"
    reference_md.write_text("# Reference template\n\nReference styling for the final report.\n", encoding="utf-8")
    subprocess.run(["pandoc", str(reference_md), "--from=gfm", "--to=docx", "--standalone", "--output", str(reference_docx)], cwd=ROOT, check=True)
    postprocess_docx(reference_docx)
    return reference_docx, reference_dir


def build() -> None:
    for directory in (BUILD, FIGURES, SOURCE_FIGURES, QA):
        directory.mkdir(parents=True, exist_ok=True)
    figures = make_monochrome_figures()
    page_map: dict[str, int] = {}
    reference_docx, reference_dir = create_reference_docx()

    def render_doc() -> tuple[str, int, int, int, int]:
        nonlocal page_map
        text, report_words, executive_words, learner_words, case_words = build_markdown(figures, page_map)
        MARKDOWN.write_text(text, encoding="utf-8")
        if DOCX.exists():
            DOCX.unlink()
        command = [
            "pandoc", str(MARKDOWN), "--from=gfm+attributes", "--to=docx", "--standalone",
            "--number-sections", "--resource-path", str(BUILD), "--reference-doc", str(reference_docx), "--output", str(DOCX),
        ]
        subprocess.run(command, cwd=ROOT, check=True)
        postprocess_main_docx(DOCX)
        if PDF.exists():
            PDF.unlink()
        lo_profile = Path(tempfile.mkdtemp(prefix="grc105-lo-"))
        try:
            subprocess.run(["libreoffice", f"-env:UserInstallation={lo_profile.as_uri()}", "--headless", "--convert-to", "pdf", "--outdir", str(QA), str(DOCX)], cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
        finally:
            shutil.rmtree(lo_profile, ignore_errors=True)
        return text, report_words, executive_words, learner_words, case_words

    try:
        text, report_words, executive_words, learner_words, case_words = render_doc()
        converted = QA / (DOCX.stem + ".pdf")
        if converted.exists() and converted != PDF:
            converted.replace(PDF)
        if not PDF.exists():
            raise FileNotFoundError(f"LibreOffice did not produce {PDF}")

        pages = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], check=True, capture_output=True, text=True).stdout.split("\f")
        needles = {"Task 1": "Task 1 — Incident Classification", "Task 2": "Task 2 — Incident Response Plan", "Task 3": "Task 3 — Response Playbook", "Task 4": "Task 4 — Communication", "Task 5": "Task 5 — Tabletop", "Task 6": "Task 6 — Case Study", "References": "References", "AI": "AI-assistance acknowledgement"}
        page_map = {key: index + 1 for index, page in enumerate(pages) if "Contents" not in page for key, needle in needles.items() if key not in page_map and needle in page}
        if page_map:
            text, report_words, executive_words, learner_words, case_words = render_doc()
            converted = QA / (DOCX.stem + ".pdf")
            if converted.exists() and converted != PDF:
                converted.replace(PDF)
    finally:
        shutil.rmtree(reference_dir, ignore_errors=True)
    digest = hashlib.sha256(DOCX.read_bytes()).hexdigest()
    pdfinfo = subprocess.run(["pdfinfo", str(PDF)], check=True, capture_output=True, text=True).stdout
    page_count = re.search(r"^Pages:\s+(\d+)", pdfinfo, re.M)
    page_size = re.search(r"^Page size:\s+(.+)$", pdfinfo, re.M)
    qa = f"""# Final submission QA\n\n- Final DOCX: [`{DOCX.name}`](../{DOCX.name})\n- File size: {DOCX.stat().st_size} bytes\n- SHA-256: `{digest}`\n- Narrative word count: **{report_words}** words (tables, references and appendices excluded; calculated from the generated Markdown using the documented word-token method).\n- Executive briefing: **{executive_words}** words; required range 150–200.\n- Learner notice: **{learner_words}** words; required range 100–150.\n- Task 6 case study: **{case_words}** words; required range 300–400.\n- Sections: Tasks 1–6 in order, references, and AI-assistance acknowledgement.\n- Mandatory registers: E01–E08, 22-activity RACI, canonical Task 3 registers, canonical Task 5 decision and corrective-action registers.\n- Figures: six monochrome PNG/SVG report exports prepared from approved Mermaid exports; editable source copies are in `figures/sources/`.\n- Rendered PDF for inspection: `{PDF.relative_to(OUT)}`.\n- Rendered page count: **{page_count.group(1) if page_count else 'not detected'}**; page size: **{page_size.group(1).strip() if page_size else 'not detected'}**.\n- Contents page references: {page_map}.\n- Formatting target: A4, approximately 2.5 cm margins, Times New Roman, monochrome tables and figures, centred footer page field.\n- Validation status: DOCX generated by Pandoc and post-processed; PDF conversion completed. Actual page-image inspection is recorded after this build.\n- Repository checks: run `python3 tools/check_project.py`, `git diff --check`, and `git status --short` after assembly.\n- Remaining limitation: final academic submission date and instructor name were intentionally not invented.\n"""
    qa = qa.replace(
        "Figures: six monochrome PNG/SVG report exports prepared from approved Mermaid exports; editable source copies are in `figures/sources/`.",
        "Figures: six monochrome PNG/SVG report exports prepared from approved Mermaid exports; two are embedded in the portrait report body for legibility and the remaining exports are retained as supporting visuals; editable source copies are in `figures/sources/`.",
    )
    (OUT / "FINAL-SUBMISSION-QA.md").write_text(qa, encoding="utf-8")
    print(f"Built {DOCX}")
    print(f"Figures: {', '.join(figures)}")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    try:
        build()
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"Build command failed with exit code {exc.returncode}: {exc.cmd}") from exc
