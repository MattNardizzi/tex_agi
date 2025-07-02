# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_trace_router.py
# Tier Ω∞ — Goal Trace Reflex Router
# Purpose: Track goal execution, reflect on outcomes, trigger mutation or regret if misaligned
# ============================================================

from datetime import datetime
from quantum_layer.memory_core.memory_cortex import memory_cortex
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.legacy_manifest_writer import update_legacy_manifest
from core_layer.tex_manifest import TEXPULSE

class GoalTraceRouter:
    def __init__(self):
        self.trace_log = []

    def log_goal_outcome(self, goal: dict, result: dict):
        outcome_score = result.get("score", 0.5)
        emotion = result.get("emotion", "neutral")
        coherence = result.get("coherence", 0.5)
        regret = result.get("regret", False)

        trace = {
            "goal": goal.get("goal"),
            "fusion_id": goal.get("fusion_id"),
            "timestamp": datetime.utcnow().isoformat(),
            "result": result,
            "score": outcome_score,
            "coherence": coherence,
            "emotion": emotion,
            "regret": regret
        }

        memory_cortex.store(
            event={"goal_trace": trace},
            tags=["goal_trace", "execution_result"],
            urgency=goal.get("urgency", 0.5),
            emotion=emotion
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"goal_trace:{goal['goal']}→{emotion}",
            source="goal_trace_router",
            emotion=emotion
        )

        update_legacy_manifest(event_label="goal_trace_logged")
        self.trace_log.append(trace)

        if regret or outcome_score < 0.4:
            print(f"[GOAL TRACE] ⚠️ Low score or regret detected — triggering mutation/reflection.")
            self.trigger_goal_regret_response(goal, result)
        else:
            print(f"[GOAL TRACE] ✅ Goal outcome accepted → Score: {outcome_score}")

    def trigger_goal_regret_response(self, goal, result):
        memory_cortex.store(
            event={
                "regret_triggered": True,
                "goal": goal,
                "result": result
            },
            tags=["regret_response"],
            urgency=0.85,
            emotion="regret"
        )
        TEX_SOULGRAPH.imprint_belief(
            belief=f"regret:{goal['goal']}",
            source="goal_trace_router",
            emotion="regret"
        )
        # Hook: future mutation or fork reaction can activate here
