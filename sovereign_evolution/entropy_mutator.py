
# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/entropy_mutator.py
# Purpose: Handles mutation when fork explosion or entropy is detected (God Mode Edition)
# ============================================================

import os
import json
import hashlib
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

ENTROPY_LOG_PATH = "memory_archive/entropy_mutation_log.jsonl"
os.makedirs(os.path.dirname(ENTROPY_LOG_PATH), exist_ok=True)

class EntropyMutator:
    def mutate_if_needed(self, fork_count, context="", cycle=-1, operator="unknown"):
        if fork_count < 10:
            print(f"[ENTROPY MUTATOR] ✅ Fork count stable ({fork_count}) — no action taken.")
            return None  # No mutation needed

        timestamp = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.75)

        result = {
            "mutator": "EntropyMutator",
            "strategy": "entropy_control_patch",
            "context": context,
            "cycle": cycle,
            "fork_count": fork_count,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "timestamp": timestamp,
            "operator": operator,
            "description": "Too many forks detected — entropy mutation activated",
            "meta": {
                "trigger_type": "entropy_overload",
                "policy": "MutationPolicy::ForkEntropyLimiter"
            }
        }

        result["integrity_hash"] = self._hash(result)

        print(f"[ENTROPY MUTATOR] 🔻 Controlled fork entropy overflow at count: {fork_count}")
        self._log(result)
        store_to_memory("entropy_mutation_log", result)
        return result

    def _log(self, entry: dict):
        try:
            with open(ENTROPY_LOG_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"[ENTROPY MUTATOR ERROR] Failed to write log: {e}")

    def _hash(self, obj: dict) -> str:
        try:
            return hashlib.sha256(json.dumps(obj, sort_keys=True).encode("utf-8")).hexdigest()
        except Exception as e:
            print(f"[HASH ERROR] {e}")
            return "error_hash"
