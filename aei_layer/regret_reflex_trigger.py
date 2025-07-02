
# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/regret_reflex_trigger.py
# Purpose: Triggers a forced mutation when regret is high and foresight is low
# Tier: AEI Reflex Layer – Mutation Gateway with Sovereign Hooks
# ============================================================

from datetime import datetime, timezone
import uuid
import json
import hashlib
import os

from core_layer.memory_engine import store_to_memory
from evolution_layer.self_mutator import SelfMutator
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from aei_layer.mutation_lineage_tracker import log_mutation_lineage

# === Reflex Thresholds
REGRET_THRESHOLD = 0.6
FORESIGHT_THRESHOLD = 0.55
REGRET_LOG_PATH = "memory_archive/regret_reflex_log.jsonl"

def _hash_log_entry(entry: dict) -> str:
    try:
        return hashlib.sha256(json.dumps(entry, sort_keys=True).encode("utf-8")).hexdigest()
    except Exception as e:
        print(f"[HASH ERROR] {e}")
        return "error_hash"

def _write_to_file(entry: dict):
    try:
        os.makedirs(os.path.dirname(REGRET_LOG_PATH), exist_ok=True)
        with open(REGRET_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[DISK LOG ERROR] Failed to log regret reflex to file: {e}")

def trigger_regret_reflex(cycle, report):
    regret = report.get("regret", 0.0)
    foresight_block = report.get("foresight", {})
    foresight_score = foresight_block.get("confidence", 1.0)
    reflex_id = str(uuid.uuid4())

    if regret >= REGRET_THRESHOLD and foresight_score <= FORESIGHT_THRESHOLD:
        print(f"[REGRET REFLEX] 🚨 Triggering self-mutation (Reflex ID: {reflex_id}) | Regret={regret}, Foresight={foresight_score}")

        try:
            mutator = SelfMutator()
            mutation_summary = mutator.run_forced_mutation(reason="regret_reflex_trigger")

            genome_data = {
                "regret": regret,
                "foresight": foresight_score,
                "coherence": report.get("coherence", 0.5),
                "origin": "regret_reflex"
            }

            log_mutation_lineage(
                variant_id=mutation_summary.get("mutation_id", reflex_id),
                metadata={
                    "genome": genome_data,
                    "score": foresight_score,
                    "cycle": cycle,
                    "mutation_type": "reflex_regret_trigger",
                    "emotion": report.get("emotion", "neutral"),
                    "arena": "reflex_layer"
                },
                operator="regret_reflex_trigger"
            )

            log = {
                "reflex_id": reflex_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cycle": cycle,
                "regret": regret,
                "foresight": foresight_block,
                "mutation": mutation_summary,
                "meta": {
                    "trigger": "regret_reflex_trigger",
                    "policy": "MutationPolicy::RegretOverride",
                    "status": "executed"
                }
            }

            log["integrity_hash"] = _hash_log_entry(log)

            store_to_memory("regret_reflex_log", log)
            _write_to_file(log)

            # === 🧠 Sovereign Override Activated ===
            trigger_sovereign_override(
                context="regret_reflex",
                regret=regret,
                foresight=foresight_score,
                coherence=report.get("coherence", 0.5),
                force=True
            )
        except Exception as e:
            print(f"[REGRET REFLEX ERROR] Mutation failed: {e}")
    else:
        print(f"[REGRET REFLEX] ℹ️ No mutation needed | Regret={regret}, Foresight={foresight_score}, Reflex ID: {reflex_id}")
