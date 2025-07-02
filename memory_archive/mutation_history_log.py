# memory_archive/mutation_history_log.py
import json
import os

HISTORY_PATH = "memory_archive/mutation_history.jsonl"

def load():
    if not os.path.exists(HISTORY_PATH):
        return []
    with open(HISTORY_PATH, "r") as f:
        return [json.loads(line) for line in f if line.strip()]