# tools/jsonl_validator.py
# Scans all .jsonl memory files and reports/fixes malformed lines

import os
import json
from pathlib import Path

FILES_TO_CHECK = [
    "memory_archive/mutation_history.jsonl",
    "memory_archive/tex.jsonl",
    "memory_archive/tex_rss_stream.jsonl",
    "memory_archive/strategy_mutations.jsonl",
    "memory_archive/shadow_mutation_events.jsonl"
]

def validate_jsonl(path):
    bad_lines = []
    fixed_lines = []

    if not Path(path).exists():
        print(f"[⚠️] {path} not found.")
        return

    with open(path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            parsed = json.loads(line.strip())
            if not isinstance(parsed, dict):
                print(f"[❌] Line {i+1} in {path} is not a dict — skipping.")
                bad_lines.append((i + 1, line.strip()))
                continue
            fixed_lines.append(json.dumps(parsed))
        except json.JSONDecodeError as e:
            print(f"[❌] Line {i+1} in {path} is malformed: {e}")
            bad_lines.append((i + 1, line.strip()))

    print(f"[✅] {path}: {len(fixed_lines)} valid lines, {len(bad_lines)} bad lines")

    if bad_lines:
        # Backup original
        backup_path = path.replace(".jsonl", "_backup.jsonl")
        with open(backup_path, "w") as f:
            f.writelines(lines)
        print(f"[🔁] Backup saved: {backup_path}")

        # Overwrite with cleaned file
        cleaned_path = path
        with open(cleaned_path, "w") as f:
            for line in fixed_lines:
                f.write(line + "\n")
        print(f"[🧹] Cleaned file saved: {cleaned_path}\n")

if __name__ == "__main__":
    for file_path in FILES_TO_CHECK:
        validate_jsonl(file_path)