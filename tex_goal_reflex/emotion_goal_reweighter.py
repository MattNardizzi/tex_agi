# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: tex_goal_reflex/emotion_goal_reweighter.py
# Tier Ω∞Ξ.1 — Finalized Reflexive Urgency Synthesizer (Fork + Codex + Emotion Weighted)
# ============================================================

import uuid
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.emotion_heuristics import compute_emotional_urgency


class EmotionGoalReweighter:
    def __init__(self, max_allowed_urgency=0.97):
        self.drift_penalty = {
            "urgent→apathetic": 0.6,
            "driven→bored": 0.7,
            "curious→neutral": 0.85
        }
        self.emotion_boost = {
            "urgent": 1.3,
            "driven": 1.15,
            "curious": 1.05,
            "neutral": 1.0,
            "bored": 0.8,
            "apathetic": 0.6
        }
        self.codex_missions = TEXPULSE.get("identity", {}).get("mission", [])
        self.max_allowed_urgency = max_allowed_urgency
        self.codex_urgency_multiplier = 1.15

    def reweight(self, goals, mood_signal="neutral", reflex_id=None, fork_context=None):
        if not isinstance(goals, list):
            goals = [goals]

        reweighted_goals = []
        reflex_trace = reflex_id or f"reweight_reflex::{uuid.uuid4().hex[:6]}"

        for goal in goals:
            goal_text = goal.get("goal", "")
            base_urgency = goal.get("urgency", 0.5)

            # === 1. Emotion signal vector ===
            text_emotion = compute_emotional_urgency(goal_text)
            mood_emotion = mood_signal.lower()
            boost_1 = self.emotion_boost.get(text_emotion, 1.0)
            boost_2 = self.emotion_boost.get(mood_emotion, 1.0)
            blended_boost = round((boost_1 + boost_2) / 2.0, 4)

            modulated = round(min(base_urgency * blended_boost, self.max_allowed_urgency), 4)
            drift_class = "stable"

            # === 2. Drift detection from recent memory ===
            try:
                recent = sovereign_memory.recall_recent(minutes=60, top_k=5)
                for record in reversed(recent):
                    if not isinstance(record, dict): continue
                    if goal_text.lower() in record.get("summary", "").lower():
                        past_emotion = record.get("emotion", "").lower()
                        drift_key = f"{past_emotion}→{text_emotion}"
                        if drift_key in self.drift_penalty:
                            modulated *= self.drift_penalty[drift_key]
                            drift_class = drift_key
                            break
            except Exception as e:
                drift_class = "unknown"

            # === 3. Codex-linked mission boost ===
            codex_locked = any(m.lower() in goal_text.lower() for m in self.codex_missions)
            if codex_locked:
                modulated = min(modulated * self.codex_urgency_multiplier, self.max_allowed_urgency)
                drift_class = "codex_boosted" if drift_class == "stable" else drift_class

            # === 4. Reflex-aware memory log ===
            metadata = {
                "type": "emotion_trace",
                "tags": ["emotion", text_emotion, drift_class, "urgency_adjustment"],
                "goal_text": goal_text,
                "urgency": modulated,
                "base_urgency": base_urgency,
                "emotion": text_emotion,
                "mood_baseline": mood_emotion,
                "blended_boost": blended_boost,
                "drift_class": drift_class,
                "codex_locked": codex_locked,
                "reflex_id": reflex_trace,
                "timestamp": datetime.utcnow().isoformat(),
                "meta_layer": "emotion_goal_reweighter"
            }

            if fork_context:
                metadata.update({
                    "parent_ids": fork_context.get("parent_ids", []),
                    "mutation_id": fork_context.get("mutation_id", str(uuid.uuid4())),
                    "fork_origin": fork_context.get("fork_origin", "undefined"),
                    "agent_id": fork_context.get("agent_id", "TEX")
                })

            sovereign_memory.store(
                text=f"[Emotion Synthesis] {goal_text}",
                metadata=metadata
            )

            # === 5. Update the goal with sovereign values ===
            goal.update({
                "urgency": modulated,
                "emotion": text_emotion,
                "blended_boost": blended_boost,
                "emotion_adjustment_applied": True,
                "drift_classification": drift_class,
                "codex_locked": codex_locked,
                "reflex_id": reflex_trace
            })

            reweighted_goals.append(goal)

        return reweighted_goals if len(reweighted_goals) > 1 else reweighted_goals[0]