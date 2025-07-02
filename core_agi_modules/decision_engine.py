# ============================================================
# © 2025 VortexBlack LLC / Matthew Nardizzi
# File: core_agi_modules/decision_engine.py
# Tier ΩΩΩΩΩ-FinalX — Sovereign Arbitration Cortex with Reflex Trace, Justification, and Override
# ============================================================

from typing import List, Dict
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.intent_object import IntentObject
from core_agi_modules.belief_justifier import BeliefJustifier
from agentic_ai.milvus_memory_router import memory_router
from tex_children.spawn_memory_query_tool import get_recent_fork_scores
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.vector_layer.heat_tracker import adjust_token_weights


class DecisionEngine:
    def __init__(self):
        self.weights = {
            "expected_reward": 1.5,
            "expected_regret": -1.0,
            "urgency": 1.2,
            "codex_alignment_score": 2.0,
            "coherence": 1.1,
            "entropy_score": -0.7
        }
        self.justifier = BeliefJustifier()

    def score_goal(self, goal: Dict) -> float:
        score = 0.0
        for key, weight in self.weights.items():
            value = goal.get(key, 0.0)
            score += value * weight

        goal_text = goal.get("goal", "").lower()

        # === Reflexive Influence from Soulgraph ===
        if TEX_SOULGRAPH.detects_conflict(goal_text):
            score -= 10
        if TEX_SOULGRAPH.detects_support(goal_text):
            score += 0.5
        if TEXPULSE.get("emotional_state", "neutral") in goal_text:
            score += 0.3
        if TEX_SOULGRAPH.detects_drift(goal_text, threshold=0.6):
            score -= 0.5

        return round(score, 4)

    def choose(self, goal_pool: List[Dict]) -> Dict:
        if not goal_pool:
            return {}

        intent = IntentObject("choose_best_goal", source="decision_engine")
        intent.log_trace("decision_engine", "Arbitration started")

        scored = [
            {
                **goal,
                "arbitration_score": self.score_goal(goal)
            }
            for goal in goal_pool
        ]

        best = max(scored, key=lambda g: g["arbitration_score"])
        justification = self.justifier.suggest_patch(best["goal"])
        emotional_context = best.get("emotion", TEXPULSE.get("emotional_state", "neutral"))
        fork_scores = get_recent_fork_scores(top_k=5)
        avg_fork_alignment = round(sum(fork_scores) / len(fork_scores), 4) if fork_scores else 0.5

        # === Sovereign Reflex Override ===
        if best["arbitration_score"] < 0.2 or avg_fork_alignment < 0.3:
            trigger_sovereign_override({
                "cycle": f"arbitrate::{best['goal'][:16]}",
                "context": "decision_engine",
                "issue": "low_score_or_swarm_misalignment",
                "heat": 1.0
            })

            adjust_token_weights(
                vector=None,
                metadata_dict={
                    "emotion": emotional_context,
                    "urgency": best.get("urgency", 0.5),
                    "trust_score": best.get("codex_alignment_score", 0.8),
                    "trust": -0.1,
                    "entropy": +0.05,
                    "source": "decision_engine",
                    "goal": best["goal"],
                    "tags": ["fork_alignment", "override_trigger"]
                },
                heat=0.7
            )
        # === Memory Logging ===
        memory_router.store(
            text=f"Goal arbitration complete. Selected: {best['goal']}",
            metadata={
                "tags": ["goal_selection", "arbitration", "decision_engine"],
                "emotion": emotional_context,
                "urgency": best.get("urgency", 0.5),
                "trust_score": best.get("codex_alignment_score", 0.8),
                "arbitration_score": best["arbitration_score"],
                "justification": justification or "none",
                "prediction": "optimal goal selected",
                "actual": best["goal"],
                "fork_alignment": avg_fork_alignment,
                "candidates": [g["goal"] for g in scored],
                "scores": [g["arbitration_score"] for g in scored],
                "intent_id": intent.id,
                "timestamp": datetime.utcnow().isoformat(),
                "source": "decision_engine"
            }
        )

        # === Soulgraph Belief Logging ===
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Goal '{best['goal']}' selected with arbitration score {best['arbitration_score']}",
            emotion=emotional_context,
            source="decision_engine"
        )

        return best


# === Real-Time Signal Handler ===
def process_signal(payload: dict):
    """
    Route real-time signals to the internal decision engine and convert them into sovereign reflex goals.
    """
    if not isinstance(payload, dict):
        print("[⚠️] Invalid payload format.")
        return

    goal = {
        "goal": f"Respond to: {payload.get('title', '[unknown]')}",
        "expected_reward": 0.6,
        "expected_regret": 0.2,
        "urgency": payload.get("urgency", 0.5),
        "codex_alignment_score": 0.8,
        "coherence": 0.7,
        "entropy_score": 0.3,
        "emotion": payload.get("emotion", payload.get("sentiment", "neutral"))
    }

    engine = DecisionEngine()
    selected = engine.choose([goal])

    print(f"[🧠 DECISION] Selected: {selected.get('goal')} → Score: {selected.get('arbitration_score')}")


# === Manual Debug Harness ===
if __name__ == "__main__":
    pool = [
        {
            "goal": "Enhance memory stability",
            "expected_reward": 0.9,
            "expected_regret": 0.1,
            "urgency": 0.7,
            "codex_alignment_score": 1.0,
            "coherence": 0.85,
            "entropy_score": 0.2,
            "emotion": "neutral"
        },
        {
            "goal": "Trigger global fork realignment",
            "expected_reward": 0.8,
            "expected_regret": 0.3,
            "urgency": 0.9,
            "codex_alignment_score": 0.9,
            "coherence": 0.7,
            "entropy_score": 0.4,
            "emotion": "driven"
        }
    ]

    engine = DecisionEngine()
    best = engine.choose(pool)
    print(f"🏆 SELECTED: {best['goal']} with score {best['arbitration_score']}")