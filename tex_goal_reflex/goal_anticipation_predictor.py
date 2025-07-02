# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_anticipation_predictor.py
# Tier Ω∞⟁ — Goal Utility Prediction Engine with Quantum Entropy, Soulgraph Risk, and Reflex-Level Confidence
# ============================================================

from datetime import datetime
import uuid

from quantum_layer.quantum_randomness import QuantumRandomness
from quantum_layer.memory_core.memory_cortex import memory_cortex
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

class GoalAnticipationPredictor:
    def __init__(self):
        self.qrng = QuantumRandomness()
        self.vectorizer = DreamVectorAbstraction()
        self.baseline_emotion = TEXPULSE.get("emotional_norm", "neutral")
        self.category_weights = TEXPULSE.get("goal_category_weights", {
            "general": {"regret_scale": 0.9, "reward_scale": 1.0},
            "exploratory": {"regret_scale": 0.4, "reward_scale": 1.2},
            "mission_critical": {"regret_scale": 1.1, "reward_scale": 0.9}
        })

    def predict(self, goal):
        """
        Predicts potential reward, regret, conflict risk, and utility value
        for a single goal, storing results in memory cortex.
        """
        prediction_id = f"anticipate_{uuid.uuid4().hex[:10]}"
        reflex_id = f"reflex_{uuid.uuid4().hex[:6]}"
        entropy = self.qrng.get_entropy()
        vector = self.vectorizer.vectorize(goal["goal"])

        soul_alignment = TEX_SOULGRAPH.check_alignment(goal["goal"]).get("alignment", 0.5)
        urgency = goal.get("urgency", 0.5)
        emotion = goal.get("emotion", self.baseline_emotion)
        goal_type = goal.get("category", "general")

        weights = self.category_weights.get(goal_type, self.category_weights["general"])

        predicted_reward = round((soul_alignment + urgency) / 2 * weights["reward_scale"] + entropy * 0.1, 3)
        predicted_regret = round((1.0 - soul_alignment) * entropy * weights["regret_scale"], 3)
        predicted_conflict = round(abs(urgency - soul_alignment) * 0.7 + (1 - entropy) * 0.2, 3)

        confidence_score = round((soul_alignment * 0.4 + urgency * 0.3 + (1 - predicted_conflict) * 0.3), 3)
        predicted_utility_gain = round(predicted_reward - predicted_regret - predicted_conflict, 3)
        risk_class = self._risk_class(predicted_conflict, predicted_regret)

        result = {
            "prediction_id": prediction_id,
            "reflex_id": reflex_id,
            "goal": goal["goal"],
            "goal_type": goal_type,
            "timestamp": datetime.utcnow().isoformat(),
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "soul_alignment": soul_alignment,
            "predicted_reward": predicted_reward,
            "predicted_regret": predicted_regret,
            "predicted_conflict_risk": predicted_conflict,
            "predicted_utility_gain": predicted_utility_gain,
            "confidence_score": confidence_score,
            "risk_class": risk_class
        }

        memory_cortex.store(
            event={"goal_prediction": result},
            tags=["goal_anticipation", risk_class],
            urgency=urgency,
            emotion=emotion
        )

        return result

    def predict_impact(self, goals):
        """
        Batch version for evaluating a list of goals.
        Adds prediction data to each goal and returns the enriched list.
        """
        enriched = []
        for goal in goals:
            try:
                result = self.predict(goal)
                goal.update(result)
                enriched.append(goal)
            except Exception as e:
                goal["prediction_error"] = str(e)
        return enriched

    def _risk_class(self, conflict, regret):
        combined = conflict + regret
        if combined < 0.6:
            return "low"
        elif combined < 1.2:
            return "moderate"
        elif combined < 1.8:
            return "high"
        return "critical"