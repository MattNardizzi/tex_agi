# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/exploration_mutator.py
# Purpose: Triggers exploratory logic paths during high-curiosity states
# ============================================================

from datetime import datetime
import random
from core_layer.memory_engine import store_to_memory  # Optional logging

class ExplorationMutator:
    def mutate_if_needed(self, curiosity_score=0.0, context=""):
        if curiosity_score < 0.6:
            print(f"[EXPLORATION MUTATOR] 🧩 Curiosity too low ({curiosity_score}) — skipping exploration.")
            return None  # Not curious enough to justify mutation

        novel_patch = f"explore_path_{random.randint(1000, 9999)}"
        result = {
            "mutator": "ExplorationMutator",
            "strategy": novel_patch,
            "context": context,
            "curiosity_score": curiosity_score,
            "timestamp": datetime.utcnow().isoformat(),
            "description": "Curiosity triggered exploratory patch",
            "meta": {
                "trigger_type": "curiosity_activation",
                "policy": "MutationPolicy::ExploratoryThreshold"
            }
        }

        print(f"[EXPLORATION MUTATOR] 🌱 Trying novel logic: {novel_patch} | Curiosity = {curiosity_score}")
        return result

    def evaluate(self, context):
        """
        Evaluates if exploration is warranted based on curiosity, novelty, and surprise.
        """
        curiosity = context.get("curiosity", 0.0)
        novelty = context.get("novelty", 0.0)
        surprise = context.get("surprise", 0.0)

        # Weight curiosity more heavily than novelty/surprise
        score = 0.6 * curiosity + 0.25 * novelty + 0.15 * surprise
        action_required = score > 0.65

        result = {
            "exploration_score": round(score, 3),
            "action_required": action_required,
            "status": "explore" if action_required else "hold",
            "timestamp": datetime.utcnow().isoformat()
        }

        print(f"[EXPLORATION MUTATOR] 🔍 Evaluation → Score: {result['exploration_score']} | Status: {result['status']}")
        store_to_memory("exploration_evaluation", result)

        return result