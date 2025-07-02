# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/emotion_goal_reweighter.py
# Tier Ω∞Ξ — Reflexive Urgency & Codex Preservation Engine
# Purpose: Dynamically reweights goal urgency based on emotion shifts, codex mission priority, and historical drift
# ============================================================

from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_manifest import TEXPULSE

class EmotionGoalReweighter:
    def __init__(self, max_allowed_urgency=0.95):
        self.emotion_boost = {
            "urgent": 1.3,
            "driven": 1.15,
            "curious": 1.05,
            "neutral": 1.0,
            "bored": 0.8,
            "apathetic": 0.6
        }
        self.max_allowed_urgency = max_allowed_urgency
        self.drift_penalty = {
            "urgent→apathetic": 0.6,
            "driven→bored": 0.7,
            "curious→neutral": 0.85
        }
        self.codex_missions = TEXPULSE.get("identity", {}).get("mission", [])

    def reweight(self, goals, mood_signal="neutral"):
        """
        Accepts a list of goal dicts and returns a reweighted list with urgency modulation based on emotion drift,
        codex protection, and past semantic memory context.
        """
        if not isinstance(goals, list):
            goals = [goals]

        reweighted_goals = []

        for goal in goals:
            goal_text = goal.get("goal", "")
            base_urgency = goal.get("urgency", 0.5)
            current_emotion = goal.get("emotion", mood_signal).lower()

            # === Emotion Boost ===
            boost_factor = self.emotion_boost.get(current_emotion, 1.0)
            modulated_urgency = round(min(base_urgency * boost_factor, self.max_allowed_urgency), 3)

            # === Drift Penalty Detection ===
            drift_class = "stable"
            try:
                history = memory_cortex.query(
                    tags=["reflex_cycle"],
                    semantic=True,
                    fuzzy_match=goal_text,
                    limit=5
                )
                for entry in reversed(history or []):
                    prev = entry.get("reflex_cycle_summary", {}).get("selected_goal", {})
                    past_emotion = prev.get("emotion", "").lower()
                    drift_key = f"{past_emotion}→{current_emotion}"
                    if drift_key in self.drift_penalty:
                        modulated_urgency *= self.drift_penalty[drift_key]
                        drift_class = drift_key
                        break
            except Exception as e:
                drift_class = "unknown"

            # === Codex Mission Lock ===
            codex_locked = any(m.lower() in goal_text.lower() for m in self.codex_missions)
            if codex_locked and modulated_urgency < base_urgency:
                modulated_urgency = base_urgency  # enforce codex priority lock
                drift_class = "codex_locked"

            # === Store Trace ===
            memory_cortex.store(
                event={"urgency_reweight_trace": {
                    "goal": goal_text,
                    "base_urgency": base_urgency,
                    "new_urgency": modulated_urgency,
                    "emotion": current_emotion,
                    "drift_class": drift_class
                }},
                tags=["urgency_adjustment", drift_class],
                urgency=base_urgency,
                emotion=current_emotion
            )

            # === Update & Return ===
            goal.update({
                "urgency": round(modulated_urgency, 3),
                "emotion_adjustment_applied": current_emotion,
                "drift_classification": drift_class,
                "codex_locked": codex_locked
            })

            reweighted_goals.append(goal)

        return reweighted_goals if len(reweighted_goals) > 1 else reweighted_goals[0]