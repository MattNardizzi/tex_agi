# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/self_rewriting_loop.py
# Tier: Ω∞ — Self-Mutating AGI Cortex (Final Form)
# Purpose: Reflexive rewriting triggered by contradiction, regret, memory drift, and blocked goals
# ============================================================

from datetime import datetime
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from core_layer.tex_manifest import TEXPULSE
from core_layer.tex_self_eval_matrix import integrity_score
from tex_engine.meta_utility_function import evaluate_utility
from core_layer.memory_engine import store_to_memory, recall_latest
from sovereign_evolution.codex_mutation_reflex import evaluate_codex_mutation
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine
from sovereign_evolution.auto_fork_heuristics import generate_patch_proposal
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from aei_layer.fork_regret_engine import trigger_regret_override
from core_agi_modules.reflex_stability_model import ReflexStabilityModel

class SelfRewritingLoop:
    def __init__(self):
        self.self_model = RecursiveSelfModel()
        self.patcher = TexPatcherEngine()

    def check_for_rewrite_trigger(self, current_goal: str = None) -> bool:
        """
        Determines whether internal mutation should occur based on contradiction, drift, emotion, and reflex instability.
        """
        state = self.self_model.evaluate_self_state()
        contradiction_pressure = 1.0 - state.get("integrity", 1.0)
        drift = state.get("drift_score", 0.0)
        emotion = state.get("emotion_vector", [0])[0]

        trigger_score = (
            0.4 * contradiction_pressure +
            0.4 * drift +
            0.2 * abs(emotion)
        )

        # Reflex failure pressure
        recent_failures = ReflexStabilityModel().get_recent_rejections()
        if "mutation_reflex" in recent_failures or "goal_reflex" in recent_failures:
            trigger_score += 0.15

        return trigger_score > 0.5

    def attempt_self_patch(self, goal_context: str = "goal_alignment_failure"):
        """
        Executes the sovereign rewrite based on internal memory, soulgraph, reflex logs, and mutation heuristics.
        """

        # Lineage block check
        if hasattr(TEXPULSE, "ancestry_trace"):
            if "mutation_block" in TEXPULSE.ancestry_trace:
                print(f"[⛔] Mutation blocked by ancestry constraint.")
                return {"status": "blocked", "reason": "lineage policy"}

        # Prevent repeat failed context
        recent = recall_latest("self_patch_log", n=10)
        for entry in recent:
            if entry.get("context") == goal_context and entry.get("score", 0) < 0.5:
                print(f"[⛔] Rewrite blocked: past patch for '{goal_context}' failed.")
                return {"status": "blocked", "reason": "repeat failure"}

        # Intent Logging
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Tex is preparing to rewrite internal logic due to: {goal_context}.",
            source="self_rewriting_loop",
            emotion="tense",
            tags=["mutation", "goal_conflict", "self_overwrite"]
        )

        print(f"🛠️ [SELF-REWRITE] Triggered by {goal_context}")

        # Reflexive regret trigger
        trigger_regret_override()

        # Codex mutation
        evaluate_codex_mutation()

        # Generate and apply patch
        patch = generate_patch_proposal(context=goal_context)
        self.patcher.apply_patch(patch)

        # Utility scoring
        utility = evaluate_utility({
            "action_id": f"self_patch_{datetime.utcnow().isoformat()}",
            "goal_alignment": 0.4,
            "novelty": 1.0,
            "reversibility": 0.6,
            "ethical_risk": 0.1,
            "contradiction_pressure": 0.8
        })

        # Store event in memory
        store_to_memory("self_patch_log", {
            "context": goal_context,
            "score": utility["score"],
            "verdict": utility["verdict"],
            "timestamp": datetime.utcnow().isoformat()
        })

        print(f"[SELF-REWRITE] Verdict: {utility['verdict']} | Score={utility['score']:.3f}")
        return patch