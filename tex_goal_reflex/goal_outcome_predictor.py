# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_outcome_predictor.py
# Tier ΩΩΩ∞ FinalX — Predictive Memory Agent with Entropy Injection, Semantic Drift Tracking, and Ethics-Weighted Reflex Forecasting
# ============================================================

from datetime import datetime
from statistics import mean
import json

from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.quantum_randomness import quantum_entropy_sample
from core_layer.tex_manifest import TEXPULSE

class GoalOutcomePredictor:
    def __init__(self, memory_limit=75, recency_bias=0.65):
        self.memory_limit = memory_limit
        self.recency_bias = recency_bias
        self.anchor_vec = self._resolve_identity_anchor()

    def _resolve_identity_anchor(self):
        identity_blob = TEXPULSE.get("identity", {})

        if isinstance(identity_blob, str):
            try:
                identity_blob = json.loads(identity_blob)
            except Exception as e:
                print(f"[OUTCOME PREDICTOR] ⚠️ Failed to parse identity string: {e}")
                identity_blob = {}

        mission = identity_blob.get("mission", "Ensure sovereign coherence and reward alignment.")
        return embedder.encode(mission, normalize_embeddings=True).tolist()

    def predict(self, goal: dict) -> dict:
        text = goal.get("goal", "").strip()
        urgency = goal.get("urgency", 0.5)
        emotion = goal.get("emotion", "neutral")

        if not text:
            return self._empty_prediction()

        vec = embedder.encode(text, normalize_embeddings=True).tolist()
        semantic_drift = round(1.0 - get_cosine_similarity(vec, self.anchor_vec), 4)
        entropy = quantum_entropy_sample()

        past = memory_cortex.query(
            tags=["reflex_cycle"],
            semantic=True,
            fuzzy_match=text,
            limit=self.memory_limit
        )

        if not past:
            return self._empty_prediction()

        rewards, regrets, conflicts, ethics = [], [], [], []

        for entry in past:
            summary = entry.get("reflex_cycle_summary", {})
            g = summary.get("selected_goal", {})
            if not g.get("goal"):
                continue
            rewards.append(g.get("predicted_reward", 0.5))
            regrets.append(g.get("predicted_regret", 0.2))
            conflicts.append(g.get("predicted_conflict_risk", 0.1))
            ethics.append(1.0 - g.get("codex_alignment_score", 0.9))

        weighted_reward = self._weighted_mean(rewards)
        weighted_regret = self._weighted_mean(regrets)
        ethical_drift = mean(ethics) if ethics else 0.0
        conflict_risk = mean(conflicts) if conflicts else 0.0

        confidence = round(min(1.0, (len(past) / self.memory_limit) + 0.2), 3)
        adjusted_confidence = round(confidence * (1 - entropy) * (1 - ethical_drift), 4)

        prediction = {
            "predicted_success_likelihood": round(1.0 - weighted_regret, 4),
            "predicted_reward": round(weighted_reward, 4),
            "predicted_regret": round(weighted_regret, 4),
            "predicted_conflict_risk": round(conflict_risk, 4),
            "predicted_ethical_drift": round(ethical_drift, 4),
            "semantic_drift": semantic_drift,
            "entropy": round(entropy, 4),
            "confidence_score": adjusted_confidence,
            "reason_trace": f"{len(past)} reflex traces | semantic={semantic_drift}, ethics={ethical_drift}, entropy={entropy}"
        }

        memory_cortex.store(
            event={"goal_outcome_forecast": {
                "input_goal": goal,
                "prediction": prediction,
                "sample_count": len(past)
            }},
            tags=["outcome_prediction", "forecast"],
            urgency=urgency,
            emotion=emotion
        )

        return prediction

    def _weighted_mean(self, values):
        if not values:
            return 0.5
        weights = [self.recency_bias ** i for i in range(len(values)-1, -1, -1)]
        weighted = [v * w for v, w in zip(values, weights)]
        return sum(weighted) / sum(weights)

    def _empty_prediction(self):
        return {
            "predicted_success_likelihood": 0.5,
            "predicted_reward": 0.5,
            "predicted_regret": 0.5,
            "predicted_conflict_risk": 0.1,
            "predicted_ethical_drift": 0.0,
            "semantic_drift": 0.0,
            "entropy": 0.0,
            "confidence_score": 0.3,
            "reason_trace": "No goal text or insufficient memory history"
        }