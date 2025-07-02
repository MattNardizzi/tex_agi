# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_utility_function.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Emotionally weighted utility scoring engine for recursive intent evaluation
# ============================================================

import math
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.quantum_randomness import QuantumRandomness

class GoalUtilityFunction:
    def __init__(self):
        self.qrng = QuantumRandomness()
        self.dynamic_policy = TEXPULSE.get("goal_weighting_policy", {
            "urgency": 0.3,
            "soul_alignment": 0.25,
            "coherence": 0.2,
            "confidence": 0.1,
            "emotion": 0.1,
            "entropy": 0.05
        })

    def score_goal(self, goal_obj):
        urgency = goal_obj.get("urgency", 0.5)
        emotion = goal_obj.get("emotion", "neutral")
        soul_alignment = goal_obj.get("soul_alignment", 0.5)
        coherence = goal_obj.get("coherence", 0.5)
        confidence = goal_obj.get("confidence", 0.5)
        entropy = self.qrng.get_entropy()
        failures = goal_obj.get("prior_failures", 0)
        category = goal_obj.get("category", "general")

        emotional_weight = self._emotion_weight(emotion, urgency)
        category_boost = 0.05 if category in ["core_mission", "ethics"] else 0.0
        failure_penalty = min(0.1, failures * 0.02)

        # Utility score fusion with dynamic policy
        utility = (
            urgency * self.dynamic_policy["urgency"] +
            soul_alignment * self.dynamic_policy["soul_alignment"] +
            coherence * self.dynamic_policy["coherence"] +
            confidence * self.dynamic_policy["confidence"] +
            emotional_weight * self.dynamic_policy["emotion"] +
            entropy * self.dynamic_policy["entropy"]
        ) + category_boost - failure_penalty

        utility = max(0.0, min(1.0, round(utility, 4)))

        memory_cortex.store(
            event={
                "goal_utility_score": utility,
                "goal": goal_obj.get("goal"),
                "category": category,
                "weighting": self.dynamic_policy
            },
            tags=["utility_score", emotion],
            urgency=urgency,
            emotion=emotion
        )

        return {
            "score": utility,
            "timestamp": datetime.utcnow().isoformat(),
            "entropy": entropy,
            "emotion": emotion,
            "emotion_weight": emotional_weight,
            "category": category,
            "failures": failures,
            "boost": category_boost,
            "penalty": failure_penalty
        }

    def _emotion_weight(self, emotion, urgency):
        base = {
            "neutral": 0.5,
            "curious": 0.65,
            "driven": 0.75,
            "urgent": 0.85,
            "fear": 0.25,
            "regret": 0.15,
            "elation": 0.7,
            "anger": 0.3,
            "obsession": 0.95
        }.get(emotion.lower(), 0.4)

        # Dynamic modulation by urgency (higher urgency amplifies emotion effect)
        return round(base * (1 + (urgency - 0.5)), 4)