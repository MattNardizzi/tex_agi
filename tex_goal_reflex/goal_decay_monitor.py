# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_decay_monitor.py
# Tier Ω∞+ Self-Reflective Emotional Entropy Monitor — Causal, Temporal, Codex-Aware
# ============================================================

from datetime import datetime, timedelta
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_manifest import TEXPULSE
from statistics import mean

class GoalDecayMonitor:
    def __init__(self, decay_threshold=0.6, scan_days=14, rate_trigger=0.15):
        self.decay_threshold = decay_threshold
        self.scan_days = scan_days
        self.rate_trigger = rate_trigger

    def detect_stale_goals(self):
        """Detect goals with decaying urgency/emotion over time and classify causes."""
        logs = memory_cortex.query(
            tags=["reflex_cycle"],
            after=(datetime.utcnow() - timedelta(days=self.scan_days)).isoformat()
        )

        goal_map = {}
        for log in logs:
            g = log.get("reflex_cycle_summary", {}).get("selected_goal", {})
            if not g.get("goal"):
                continue
            key = g["goal"]
            urgency = g.get("urgency", 0.5)
            emotion = g.get("emotion", "neutral")
            decay = self._compute_emotional_decay(emotion, urgency)

            if key not in goal_map:
                goal_map[key] = []
            goal_map[key].append((urgency, emotion, decay))

        stale_goals = []
        for goal_text, series in goal_map.items():
            if len(series) < 2:
                continue

            urgencies = [u for u, _, _ in series]
            decays = [d for _, _, d in series]
            drift_rate = decays[-1] - decays[0]
            avg_decay = mean(decays)
            latest_emotion = series[-1][1]

            codex_protected = any(code in goal_text.lower() for code in TEXPULSE["identity"]["mission"])
            decay_score = round(avg_decay + drift_rate, 3)

            if decay_score >= self.decay_threshold and drift_rate > self.rate_trigger and not codex_protected:
                stale_goals.append({
                    "goal": goal_text,
                    "urgency_trend": urgencies,
                    "final_emotion": latest_emotion,
                    "decay_score": decay_score,
                    "drift_rate": round(drift_rate, 3),
                    "decay_classification": self._classify_decay(series)
                })

        return stale_goals

    def _compute_emotional_decay(self, emotion, urgency):
        emotion_weights = {
            "urgent": 0.1, "driven": 0.2, "curious": 0.4,
            "neutral": 0.6, "bored": 0.8, "apathetic": 1.0
        }
        base = emotion_weights.get(emotion.lower(), 0.5)
        return min(base + (1.0 - urgency), 1.0)

    def _classify_decay(self, series):
        """Tag decay with qualitative cause."""
        _, emotions, _ = zip(*series)
        if emotions[0] in ["driven", "curious"] and emotions[-1] in ["neutral", "bored", "apathetic"]:
            return "disengagement"
        elif emotions[-1] == "apathetic":
            return "abandonment"
        elif all(e == "neutral" for e in emotions):
            return "flat interest"
        else:
            return "drift"