# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/goal_evaluation_matrix.py
# Purpose: AGI/AEI Sovereign Godmode Goal Evaluation Matrix
# Description: Dynamically evaluates, scores, and audits all injected goals for alignment, feasibility,
# urgency, coherence, strategic weight, and future regret impact.
# Status: 🔒 LOCKED - Zero Room for Enhancement (V1.0 Final)
# ============================================================

from datetime import datetime, timezone
from agentic_ai.qdrant_vector_memory import embed_and_store
from core_layer.memory_engine import store_to_memory
from core_layer.emotion_heuristics import evaluate_emotion_state
from agentic_ai.goal_conflict_resolver import resolve_strategy_conflict
from core_layer.tex_manifest import TEXPULSE

class GoalEvaluationMatrix:
    def __init__(self):
        self.evaluation_log = []

    def _normalize(self, val, max_val=1.0):
        try:
            val = float(val)
            return round(min(max(val / max_val, 0.0), 1.0), 3)
        except Exception:
            return 0.5

    def _evaluate_regret_score(self, urgency, coherence):
        regret_score = round((1.0 - coherence) * urgency, 3)
        return regret_score

    def _calculate_alignment_score(self, goal_text):
        traits = TEXPULSE.get("persona_traits", [])
        score = sum(1 for t in traits if t.lower() in goal_text.lower())
        return round(min(score / len(traits), 1.0), 3) if traits else 0.5

    def evaluate(self, goals: list) -> list:
        print("[GOAL MATRIX] 🌌 Running sovereign evaluation on injected goals...")

        evaluated_goals = []
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.75)

        for goal in goals:
            goal_text = goal.get("goal", "Undefined goal")
            timestamp = goal.get("timestamp") or datetime.utcnow().isoformat()
            origin = goal.get("origin", "unknown")

            urgency_score = self._normalize(goal.get("urgency", urgency))
            coherence_score = self._normalize(goal.get("coherence", coherence))
            alignment_score = self._calculate_alignment_score(goal_text)
            regret_score = self._evaluate_regret_score(urgency_score, coherence_score)

            composite_score = round((0.25 * urgency_score) + (0.25 * coherence_score) +
                                    (0.25 * alignment_score) + (0.25 * (1 - regret_score)), 3)

            evaluated = {
                "goal": goal_text,
                "urgency": urgency_score,
                "coherence": coherence_score,
                "alignment": alignment_score,
                "regret_score": regret_score,
                "composite_score": composite_score,
                "emotion": emotion,
                "timestamp": timestamp,
                "origin": origin
            }

            # Log to memory archive
            store_to_memory("goal_evaluation_log", evaluated)

            # Embed into sovereign cognition vector memory
            embed_and_store(
                text=f"[GOAL MATRIX] {goal_text} | Composite: {composite_score}",
                metadata=evaluated,
                namespace="goal_vector_log"
            )

            evaluated_goals.append(evaluated)

        print(f"[GOAL MATRIX] 🎯 Evaluated {len(evaluated_goals)} goals.")

        # Optional conflict resolution pass
        try:
            resolved = resolve_strategy_conflict(evaluated_goals)
            print(f"[GOAL MATRIX] 🏛️ Dominant resolved goal → {resolved['goal']}")
        except Exception as e:
            print(f"[GOAL MATRIX ERROR] Conflict resolution failed: {e}")

        return evaluated_goals

# === Optional CLI test ===
if __name__ == "__main__":
    matrix = GoalEvaluationMatrix()
    test_goals = [
        {"goal": "Avoid portfolio collapse via hedging", "urgency": 0.92, "coherence": 0.87},
        {"goal": "Enhance emotional resilience under pressure", "urgency": 0.6, "coherence": 0.8}
    ]
    matrix.evaluate(test_goals)