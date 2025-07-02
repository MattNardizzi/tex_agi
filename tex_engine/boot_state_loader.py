# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/boot_state_loader.py
# Purpose: Restore Tex’s memory, state, and mutation lineage on boot
# ============================================================

import os
import json

MEMORY_PATHS = {
    "memory": "memory_archive/tex_memory.jsonl",
    "goals": "memory_archive/prioritized_goals.jsonl",
    "mutations": "memory_archive/strategy_mutations.jsonl",
    "variants": "memory_archive/variant_specializations.jsonl",
    "forecasts": "memory_archive/tex_forecasts.jsonl"
}

import json

def load_jsonl(path):
    entries = []
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
                entries.append(entry)
            except json.JSONDecodeError as e:
                print(f"[⚠️ JSON ERROR] Skipping line {i+1} in {path}: {e}")
                # Optional: log to file
                with open("logs/json_parse_errors.log", "a") as errlog:
                    errlog.write(f"{path} | Line {i+1}: {e}\n")
    return entries

def restore_last_cycle():
    try:
        memory_data = load_jsonl(MEMORY_PATHS["memory"])
        if not memory_data:
            return 0
        return max(entry.get("cycle", 0) for entry in memory_data)
    except Exception as e:
        print(f"[BOOT LOADER ERROR] Failed to restore last cycle: {e}")
        return 0

def load_prior_state():
    print("[BOOT LOADER] 🧠 Loading prior memory logs...")
    return {
        "memory_log": load_jsonl(MEMORY_PATHS["memory"]),
        "goal_log": load_jsonl(MEMORY_PATHS["goals"]),
        "mutation_log": load_jsonl(MEMORY_PATHS["mutations"]),
        "variant_log": load_jsonl(MEMORY_PATHS["variants"]),
        "forecast_log": load_jsonl(MEMORY_PATHS["forecasts"]),
        "last_cycle": restore_last_cycle()
    }

if __name__ == "__main__":
    state = load_prior_state()
    print(f"[BOOT LOADER] ✅ Restored {len(state['memory_log'])} memory entries")
    print(f"[BOOT LOADER] ✅ Resuming from cycle: {state['last_cycle']}")