# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/variant_map.py
# Purpose: Global live dictionary for tracking agent variants
# Tier: Ω+ Reflex Tracking Store
# ============================================================

import datetime
import json
import os

variant_map = {}

DIVERGENCE_LOG_PATH = "memory_archive/variant_divergence_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

def log_fork_divergence(entry: dict):
    """
    Stores fork metadata in variant_map and logs to disk for audit.
    """
    agent_id = entry.get("agent_id", f"anon-{datetime.datetime.utcnow().timestamp()}")
    variant_map[agent_id] = entry

    try:
        with open(DIVERGENCE_LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[VARIANT MAP ERROR] ❌ Failed to log fork divergence: {e}")