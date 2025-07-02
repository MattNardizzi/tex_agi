# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/memory/archive_writer.py
# Purpose: Append structured entries to local JSONL memory archive
# Tier: ΩΩΩ — Sovereign Historical Memory Logger
# ============================================================

import json
from pathlib import Path
from datetime import datetime

ARCHIVE_DIR = Path("memory_archive")
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

def write_to_archive(payload: dict, filename: str = "tex_realtime_signals"):
    """
    Appends a structured dict to a JSONL archive file.
    Creates the file if it does not exist.
    """
    try:
        path = ARCHIVE_DIR / f"{filename}.jsonl"
        archive_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": payload
        }
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(archive_entry) + "\n")
        return True
    except Exception as e:
        print(f"[ARCHIVE ERROR] ❌ Failed to write to {filename}.jsonl: {e}")
        return False

# === Debug Mode ===
if __name__ == "__main__":
    sample = {
        "title": "Fed raises rates",
        "summary": "The Federal Reserve has raised interest rates by 0.25%...",
        "sentiment": "negative",
        "urgency_score": 0.9
    }
    write_to_archive(sample, filename="test_feed")