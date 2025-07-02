# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_learning.py
# Tier ΩΩΩ⁺+ — Recursive Meta-Learning Engine with Swarm Voting, Mutation Typing, Decay Logic, and Reflex Broadcasting
# ============================================================

import random
from datetime import datetime, timedelta
from collections import defaultdict
from utils.logging_utils import log

class MetaLearner:
    def __init__(self):
        self.mutation_log = []
        self.tension_frequency = defaultdict(int)
        self.override_simulations = []
        self.symbolic_patches = []
        self.cooldowns = {}  # Track last mutation timestamps

    def analyze_tensions(self, tension_vector, context={}, force=False):
        """
        Analyze contradiction and propose a mutation with risk, frequency, and swarm-based prioritization.
        Applies cooldown unless force=True.
        """
        field = tension_vector.get("field")
        old = tension_vector.get("old")
        new = tension_vector.get("new")
        source_fork = context.get("source_fork", "TEX")
        trigger_emotion = context.get("emotion", "uncertain")

        now = datetime.utcnow()
        last_mutation_time = self.cooldowns.get(field)
        if last_mutation_time and not force:
            if (now - last_mutation_time) < timedelta(seconds=60):
                log.info(f"[META-LEARNER] ⏳ Skipping mutation (cooldown active) for: {field}")
                return None

        self.tension_frequency[field] += 1

        urgency = context.get("urgency", 0.5)
        drift = context.get("drift", 0.5)
        swarm_alignment = context.get("swarm_agree", 0.5)
        base_risk = round(random.uniform(0.2, 0.9), 3)
        frequency_score = min(1.0, self.tension_frequency[field] / 5)
        priority_score = round(0.4 * urgency + 0.3 * drift + 0.3 * swarm_alignment + 0.2 * frequency_score, 4)

        mutation_type = self.classify_mutation_type(field, old, new)

        mutation = {
            "timestamp": now.isoformat(),
            "target": field,
            "proposed_change": f"{old} → {new}",
            "reason": "Persistent contradiction",
            "frequency": self.tension_frequency[field],
            "priority_score": priority_score,
            "risk_score": base_risk,
            "mutation_type": mutation_type,
            "source_fork": source_fork,
            "trigger_emotion": trigger_emotion
        }

        self.mutation_log.append(mutation)
        self.cooldowns[field] = now
        log.warning(f"[META-MUTATION] 🧬 Proposed mutation: {mutation}")
        return mutation

    def classify_mutation_type(self, field, old, new):
        if "emotion" in field:
            return "emotional"
        elif "reflex" in field:
            return "reflex"
        elif "goal" in field or "intent" in field:
            return "semantic"
        elif "structure" in field or "schema" in field:
            return "structural"
        return "general"

    def vote_before_commit(self, belief, hivemind, threshold=0.6):
        score = hivemind.consensus_score_on_topic(belief)
        log.info(f"[META-LEARNER] 🗳️ Swarm consensus on '{belief}' = {score}")
        return score >= threshold

    def simulate_override(self, symbolic_model, mutation):
        target = mutation["target"]
        new_val = mutation["proposed_change"].split("→")[-1].strip()
        snapshot = symbolic_model.get_fact(target)
        simulation_result = {
            "target": target,
            "previous_value": snapshot,
            "simulated_new_value": new_val,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.override_simulations.append(simulation_result)
        log.info(f"[META-LEARNER] 🧪 Simulated override: {simulation_result}")
        return simulation_result

    def commit_override(self, symbolic_model, mutation, hivemind=None):
        target = mutation["target"]
        new_val = mutation["proposed_change"].split("→")[-1].strip()
        try:
            symbolic_model.update_fact(target, new_val)
            patch = {
                "applied": True,
                "target": target,
                "new_value": new_val,
                "timestamp": datetime.utcnow().isoformat(),
                "mutation_type": mutation.get("mutation_type", "unknown")
            }
            self.symbolic_patches.append(patch)
            log.info(f"[META-LEARNER] ✅ Override applied: {patch}")

            if hivemind:
                hivemind.broadcast_memory_fragment(
                    text=f"Committed override: {mutation['proposed_change']}",
                    tags=["mutation_commit", mutation["target"]],
                    emotion="decisive"
                )

            return True
        except Exception as e:
            log.error(f"[META-LEARNER] ❌ Override failed: {e}")
            return False

    def get_mutation_history(self, limit=5):
        return self.mutation_log[-limit:]

    def export_patch_log(self):
        return self.symbolic_patches

    def export_simulation_log(self):
        return self.override_simulations