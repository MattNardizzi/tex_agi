# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/stability_mutator.py
# Purpose: Handles logic repair when coherence is unstable
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory  # Optional memory logging if needed

class StabilityMutator:
    def mutate_if_needed(self, coherence_score, context=""):
        if coherence_score > 0.6:
            print(f"[STABILITY MUTATOR] ✅ Coherence stable ({coherence_score:.2f}) — no action taken.")
            return None  # No mutation needed

        result = {
            "mutator": "StabilityMutator",
            "strategy": "coherence_patch",
            "context": context,
            "coherence_score": coherence_score,
            "timestamp": datetime.utcnow().isoformat(),
            "description": "Coherence was low — triggered stabilizing logic patch",
            "meta": {
                "trigger_type": "stability_repair",
                "policy": "MutationPolicy::LowCoherenceAutoPatch"
            }
        }

        print(f"[STABILITY MUTATOR] 🛡️ Applied patch due to low coherence ({coherence_score:.2f})")
        return result

    def evaluate(self, context):
        """
        Evaluates contextual stability and returns score + action flag.
        Compatible with AGI oversight and mutation routers.
        """
        coherence = context.get("coherence", 1.0)
        regret = context.get("regret", 0.0)
        contradiction = context.get("contradiction", 0.0)

        # Basic weighted instability model
        stability_score = max(0.0, 1.0 - (0.5 * (1 - coherence) + 0.3 * regret + 0.2 * contradiction))
        action_required = stability_score < 0.7

        result = {
            "stability_score": round(stability_score, 3),
            "action_required": action_required,
            "status": "unstable" if action_required else "stable",
            "timestamp": datetime.utcnow().isoformat()
        }

        print(f"[STABILITY MUTATOR] 📊 Evaluation → Score: {result['stability_score']} | Status: {result['status']}")
        store_to_memory("stability_evaluation", result)

        return result