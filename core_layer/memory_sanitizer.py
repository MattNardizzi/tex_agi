# core_layer/memory_sanitizer.py
# Auto-repairs malformed entries in critical memory logs

import json
from pathlib import Path
from datetime import datetime

TARGET_FILES = [
    "memory_archive/tex.jsonl",
    "memory_archive/strategy_mutations.jsonl",
    "memory_archive/mutation_history.jsonl",
    "memory_archive/shadow_mutation_events.jsonl"
]

def sanitize_file(path):
    path = Path(path)
    if not path.exists():
        return

    cleaned = []
    bad_lines = []

    with open(path, "r") as f:
        for i, line in enumerate(f):
            if not line.strip():
                continue
            try:
                json.loads(line)
                cleaned.append(line.strip())
            except json.JSONDecodeError:
                bad_lines.append(i + 1)

    if bad_lines:
        # Backup first
        backup_path = path.with_name(f"{path.stem}_auto_cleaned_{datetime.now().isoformat()}.jsonl")
        path.rename(backup_path)
        print(f"[🧹] Corrupted memory fixed in {path.name}. Backup saved to {backup_path.name}")

        # Write cleaned file
        with open(path, "w") as f:
            for line in cleaned:
                f.write(line + "\n")

def run_memory_sanitizer():
    print("[🩺] Running Memory Sanitizer...")
    for file in TARGET_FILES:
        sanitize_file(file)