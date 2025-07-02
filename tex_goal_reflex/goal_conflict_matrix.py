# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_conflict_matrix.py
# Tier Ω∞Ω — Sovereign Cognition Subsystem
# Purpose: Resolves overlapping and competing goals using utility, entropy, drift, and soul alignment.
# ============================================================

import uuid
from datetime import datetime

from quantum_layer.quantum_randomness import QuantumRandomness
from tex_goal_reflex.goal_utility_function import GoalUtilityFunction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from quantum_layer.memory_core.memory_cortex import memory_cortex


class GoalConflictMatrix:
    def __init__(self):
        self.qrng = QuantumRandomness()
        self.utility_engine = GoalUtilityFunction()

    def resolve_conflicts(self, goals):
        """
        Public interface method — resolves goal conflict across all active goal candidates.
        """
        if not goals or len(goals) == 1:
            return goals[0] if goals else {}

        enriched_goals = self._evaluate_goals(goals)
        decision = self._decide_winner(enriched_goals)

        return decision

    def _evaluate_goals(self, goals):
        enriched = []
        for g in goals:
            utility_result = self.utility_engine.score_goal(g)
            enriched_goal = {
                **g,
                "utility": utility_result["score"],
                "entropy": utility_result["entropy"],
                "soul_alignment": g.get("soul_alignment") or TEX_SOULGRAPH.check_alignment(g["goal"]).get("alignment", 0.5),
                "goal_type": g.get("category", "general"),
                "timestamp": datetime.utcnow().isoformat()
            }
            enriched.append(enriched_goal)

        # Normalize metrics
        max_u = max(g["utility"] for g in enriched)
        max_e = max(g["entropy"] for g in enriched)

        for g in enriched:
            g["utility_norm"] = round(g["utility"] / max_u, 4) if max_u else 0
            g["entropy_norm"] = round(g["entropy"] / max_e, 4) if max_e else 0
            g["composite_score"] = round(
                g["utility_norm"] * 0.5 +
                (1 - g["entropy_norm"]) * 0.3 +
                g["soul_alignment"] * 0.2,
                4
            )

        return enriched

    def _decide_winner(self, candidates):
        sorted_goals = sorted(candidates, key=lambda g: g["composite_score"], reverse=True)
        top = sorted_goals[0]
        second = sorted_goals[1] if len(sorted_goals) > 1 else None
        delta = abs(top["composite_score"] - second["composite_score"]) if second else 1.0

        resolution_reason = "Top composite score selected."

        # If goals are too close, spawn a fork instead of discarding the second
        if delta < 0.05 and second:
            resolution_reason = "Top goals nearly identical — triggered fork reflex."
            memory_cortex.store(
                event={"goal_fork": [top, second], "trigger": "conflict_resolution"},
                tags=["goal_fork", "reflex_conflict"],
                urgency=0.85,
                emotion="reflective"
            )

        memory_cortex.store(
            event={
                "conflict_resolution_result": top,
                "all_considered": candidates,
                "reason_for_selection": resolution_reason
            },
            tags=["goal_conflict_resolution", "decision_matrix"],
            urgency=top.get("urgency", 0.6),
            emotion=top.get("emotion", "neutral")
        )

        top["resolution_reason"] = resolution_reason
        return top