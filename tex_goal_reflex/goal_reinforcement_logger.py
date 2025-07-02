# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_reinforcement_logger.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Logs outcome of executed goals to adjust predictive, utility, and memory alignment over time
# ============================================================

from datetime import datetime
import uuid

from quantum_layer.memory_core.memory_cortex import memory_cortex

class GoalReinforcementLogger:
    def __init__(self):
        self.records = []

    def log_outcome(self, executed_goal, result):
        """
        Logs the final outcome of a completed goal execution.
        Adds delta tracking between predicted vs actual outcomes for adaptive reflexive learning.
        """
        reinforcement_id = f"reinforce_{uuid.uuid4().hex[:10]}"
        reflex_id = executed_goal.get("reflex_id", f"reflex_{uuid.uuid4().hex[:6]}")

        predicted_reward = executed_goal.get("predicted_reward", 0.0)
        predicted_regret = executed_goal.get("predicted_regret", 0.0)
        predicted_conflict = executed_goal.get("predicted_conflict_risk", 0.0)

        observed_reward = result.get("reward", 0.0)
        observed_regret = result.get("regret", 0.0)
        observed_conflict = result.get("conflict", predicted_conflict)

        reward_error = round(observed_reward - predicted_reward, 3)
        regret_error = round(observed_regret - predicted_regret, 3)
        conflict_error = round(observed_conflict - predicted_conflict, 3)

        impact_score = round(observed_reward - observed_regret - observed_conflict, 3)
        impact_label = self._classify_impact(impact_score)

        outcome_record = {
            "reinforcement_id": reinforcement_id,
            "reinforcement_reflex_id": f"rfx_{uuid.uuid4().hex[:6]}",
            "goal": executed_goal.get("goal"),
            "goal_type": executed_goal.get("goal_type", "general"),
            "trace_id": executed_goal.get("trace_id"),
            "reflex_id": reflex_id,
            "timestamp": datetime.utcnow().isoformat(),
            "predicted_reward": predicted_reward,
            "predicted_regret": predicted_regret,
            "predicted_conflict": predicted_conflict,
            "observed_reward": observed_reward,
            "observed_regret": observed_regret,
            "observed_conflict": observed_conflict,
            "reward_error": reward_error,
            "regret_error": regret_error,
            "conflict_error": conflict_error,
            "alignment_shift": result.get("alignment_shift", 0.0),
            "success": result.get("success", False),
            "impact_score": impact_score,
            "impact_label": impact_label,
            "actual_result": result.get("outcome")
        }

        self.records.append(outcome_record)

        memory_cortex.store(
            event={"goal_reinforcement": outcome_record},
            tags=["reinforcement", impact_label, outcome_record["goal_type"]],
            urgency=result.get("urgency", 0.5),
            emotion=result.get("emotion", "neutral")
        )

        return reinforcement_id

    def _classify_impact(self, score):
        if score >= 0.5:
            return "positive"
        elif score > -0.3:
            return "neutral"
        return "negative"