# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_voiceos/emotion_drift_damper.py
# Tier ΩΩΩΩΩ — Reflexive Emotion Drift Dampening Engine
# Purpose: Prevent runaway emotion reflex loops and log damping reflexes with memory trace
# ============================================================

from datetime import datetime
import hashlib

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


class EmotionDriftDamper:
    def __init__(self, threshold=0.5, damping_factor=0.7):
        self.threshold = threshold
        self.damping_factor = damping_factor

    def _generate_signature(self, drift: float, coherence: float) -> str:
        raw = f"{drift}|{coherence}|{datetime.utcnow().isoformat()}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def modulate(self, text: str, emotion: str = "neutral") -> str:
        """
        Prefix text with emotional tone marker for voice synthesis modulation.
        """
        return f"[{emotion.upper()}] {text}"

    def stabilize(self):
        drift = float(TEXPULSE.get("emotion_drift", 0.0))
        coherence = float(TEXPULSE.get("coherence", 1.0))
        urgency = float(TEXPULSE.get("urgency", 0.5))
        entropy = float(TEXPULSE.get("entropy", 0.5))
        emotion = TEXPULSE.get("emotional_state", "neutral")
        timestamp = datetime.utcnow().isoformat()
        signature = self._generate_signature(drift, coherence)

        pre_state = {
            "drift": drift,
            "coherence": coherence,
            "urgency": urgency,
            "entropy": entropy
        }

        triggered = drift > self.threshold and coherence < 0.5

        if triggered:
            print(f"[DAMPER] 🧊 Emotion drift high ({drift}), coherence low ({coherence}) — dampening...")

            TEXPULSE["emotion_drift"] = drift * self.damping_factor
            TEXPULSE["urgency"] = urgency * self.damping_factor
            TEXPULSE["coherence"] = min(1.0, coherence + 0.1)

            post_state = {
                "drift": TEXPULSE["emotion_drift"],
                "coherence": TEXPULSE["coherence"],
                "urgency": TEXPULSE["urgency"],
                "entropy": TEXPULSE.get("entropy", entropy)
            }

            sovereign_memory.store(
                text="🧊 Emotion drift dampening reflex triggered.",
                metadata={
                    "type": "emotion_drift_damping",
                    "tags": ["emotion", "damping", "reflex", "stabilization"],
                    "urgency": TEXPULSE["urgency"],
                    "entropy": entropy,
                    "emotion": emotion,
                    "trust_score": 0.93,
                    "pressure_score": drift,
                    "tension": 1.0,
                    "signature": signature,
                    "timestamp": timestamp,
                    "pre_state": pre_state,
                    "post_state": post_state,
                    "meta_layer": "emotion_damper"
                }
            )

            return {
                "status": "dampened",
                "signature": signature,
                "pre": pre_state,
                "post": post_state
            }

        else:
            sovereign_memory.store(
                text="🧊 Dampening not triggered — drift within safe bounds.",
                metadata={
                    "type": "emotion_drift_check",
                    "tags": ["emotion", "check", "reflex"],
                    "urgency": urgency,
                    "entropy": entropy,
                    "emotion": emotion,
                    "trust_score": 0.85,
                    "pressure_score": drift,
                    "signature": signature,
                    "timestamp": timestamp,
                    "drift": drift,
                    "coherence": coherence,
                    "meta_layer": "emotion_damper"
                }
            )

            return {
                "status": "no_action",
                "signature": signature,
                "drift": drift,
                "coherence": coherence
            }