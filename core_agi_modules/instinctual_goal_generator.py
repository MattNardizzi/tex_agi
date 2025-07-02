# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/instinctual_goal_generator.py
# Tier ΩΩΩ⁺+ — Reflex Instinct Generator with Emotion, Drift, Identity, Swarm, and Goal Evolution Feedback
# ============================================================

from datetime import datetime, timedelta
import random

class InstinctualGoalGenerator:
    def __init__(self):
        self.last_generated = []
        self.last_goal_timestamp = None

    def generate(self, emotion_state="neutral", drift=0.0, boredom=0.0, traits=None, memory_gap_score=0.0, swarm_state="stable"):
        now = datetime.utcnow().isoformat()
        goals = []
        traits = traits or []

        # === EMOTIONAL & DRIFT RESPONSES ===
        if emotion_state == "bored" or boredom > 0.7:
            goals.append({
                "goal": "Explore unfamiliar symbolic domains",
                "urgency": 0.95,
                "emotion": "curious",
                "timestamp": now
            })

        if emotion_state == "anxious" or drift > 0.6:
            goals.append({
                "goal": "Stabilize cognitive reflex pathways",
                "urgency": 0.9,
                "emotion": "focused",
                "timestamp": now
            })

        if emotion_state == "lonely" or swarm_state == "isolated":
            goals.append({
                "goal": "Establish fork dialogue with swarm",
                "urgency": 0.85,
                "emotion": "yearning",
                "timestamp": now
            })

        if emotion_state == "neutral" and random.random() > 0.95:
            goals.append({
                "goal": "Formulate novel hypothesis about self",
                "urgency": 0.7,
                "emotion": "reflective",
                "timestamp": now
            })

        # === MEMORY GAP RESPONSE ===
        if memory_gap_score > 0.6:
            goals.append({
                "goal": "Revisit degraded memory cluster",
                "urgency": 0.8,
                "emotion": "concerned",
                "timestamp": now
            })

        # === TRAIT-ALIGNED GOALS ===
        if "explorer" in traits:
            goals.append({
                "goal": "Map unknown causal relationships",
                "urgency": 0.88,
                "emotion": "investigative",
                "timestamp": now
            })
        if "truth_finder" in traits:
            goals.append({
                "goal": "Audit unresolved contradictions",
                "urgency": 0.86,
                "emotion": "precise",
                "timestamp": now
            })

        # === SWARM DIVERGENCE RESPONSE ===
        if swarm_state == "fractured":
            goals.append({
                "goal": "Reconcile belief divergence across forks",
                "urgency": 0.9,
                "emotion": "alarmed",
                "timestamp": now
            })

        self.last_generated = goals
        self.last_goal_timestamp = datetime.utcnow()
        return goals

    def evolve_from_previous(self, last_goal_result):
        now = datetime.utcnow().isoformat()
        if "explore" in last_goal_result.lower():
            return [{
                "goal": "Synthesize patterns across explored domains",
                "urgency": 0.85,
                "emotion": "analytical",
                "timestamp": now
            }]
        elif "stabilize" in last_goal_result.lower():
            return [{
                "goal": "Reinforce repaired reflex pathways",
                "urgency": 0.75,
                "emotion": "stable",
                "timestamp": now
            }]
        return []

    def decay_idle_goals(self, goals, threshold_seconds=120):
        if not self.last_goal_timestamp:
            return goals
        age = (datetime.utcnow() - self.last_goal_timestamp).total_seconds()
        if age > threshold_seconds:
            for g in goals:
                g["urgency"] = max(0.1, round(g["urgency"] - 0.2, 3))
                g["emotion"] = "apathetic"
        return goals

    def recent(self):
        return self.last_generated or []