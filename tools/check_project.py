#!/usr/bin/env python3
from pathlib import Path
import csv,hashlib,sys
root=Path(__file__).resolve().parents[1]
fail=[]
with (root/'00-project-management/source-manifest.csv').open(newline='') as fp:
 for row in csv.DictReader(fp):
  p=root/row['Relative path']
  if not p.is_file():fail.append('Missing '+str(p))
  elif hashlib.sha256(p.read_bytes()).hexdigest()!=row['SHA256']:fail.append('Hash mismatch '+str(p))
with (root/'00-project-management/requirements-traceability.csv').open(newline='') as fp:
 tasks=list(csv.DictReader(fp))
if len(tasks)!=7:fail.append('Unexpected traceability row count')
print('Source originals verified.' if not fail else '\n'.join(fail))
print(f'{len(tasks)} rubric sections tracked.')
sys.exit(bool(fail))
