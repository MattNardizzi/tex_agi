
# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/regret_based_self_mutator.py
# Purpose: Trigger mutation logic when regret signals exceed defined thresholds
# Tier: Sovereign AEI Mutation Logic – Regret Policy Router + Lineage Logging
# ============================================================

import hashlib
import json
import os
from datetime import datetime, timezone

from sovereign_evolution.mutation_policy_router import MutationPolicyRouter
from evolution_layer.self_mutator import SelfMutator
from aei_layer.mutation_lineage_tracker import log_mutation_lineage
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

REGRET_MUTATION_LOG = "memory_archive/regret_mutation_trigger_log.jsonl"

class RegretBasedSelfMutator:
    def __init__(self):
        self.threshold = 0.65
        self.executor = SelfMutator()
        self.policy = None  # Optional policy router

    def mutate_if_needed(self, regret_score, context="unknown"):
        if isinstance(regret_score, list):
            regret_score = round(sum(regret_score) / len(regret_score), 3) if regret_score else 0.0

        if regret_score < self.threshold:
            print(f"[SELF-MUTATOR] 💧 Regret ({regret_score:.3f}) below mutation threshold ({self.threshold}).")
            return None

        if not self.policy or not self.policy.is_mutation_allowed(reason=f"regret > {self.threshold}"):
            reason = self.policy.get_last_reason() if hasattr(self.policy, 'get_last_reason') else "Unknown"
            print(f"[SELF-MUTATOR] ❌ Mutation disallowed by policy. Reason: {reason}")
            return None

        print(f"[SELF-MUTATOR] ⚠️ Triggering mutation — regret = {regret_score:.3f}")
        try:
            mutation_result = self.executor.force_mutation(
                reason=f"regret_triggered @ {regret_score:.3f} from {context}"
            )
        except Exception as e:
            print(f"[SELF-MUTATOR ERROR] Mutation execution failed: {e}")
            return None

        lineage_data = {
            "genome": {
                "regret": regret_score,
                "origin": "regret_based_self_mutator"
            },
            "score": 1.0 - regret_score,
            "cycle": TEXPULSE.get("cycle", -1),
            "mutation_type": "regret_mutation",
            "emotion": TEXPULSE.get("emotional_state", "neutral"),
            "arena": "regret_mutator"
        }

        lineage_result = log_mutation_lineage(
            variant_id=mutation_result.get("mutation_id", "unknown_variant"),
            metadata=lineage_data,
            operator="RegretBasedSelfMutator"
        )

        log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "trigger": "regret",
            "regret_score": regret_score,
            "mutation": mutation_result,
            "context": context,
            "agent_id": TEXPULSE.get("id", "TEX"),
            "policy_class": self.policy.__class__.__name__ if self.policy else "None",
            "arena": "regret_mutator",
            "lineage_hash": lineage_result.get("genome_hash") if lineage_result else "none"
        }

        self._store_reflex_log(log)
        store_to_memory("regret_mutation_event", log)
        return log

    def attach_router(self, router):
        self.policy = router

    def _store_reflex_log(self, entry: dict):
        try:
            os.makedirs(os.path.dirname(REGRET_MUTATION_LOG), exist_ok=True)
            with open(REGRET_MUTATION_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"[DISK LOG ERROR] Failed to write regret log: {e}")
