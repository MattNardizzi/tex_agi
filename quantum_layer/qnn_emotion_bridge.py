# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/qnn_emotion_bridge.py
# Tier Ω.0+ — QNN Emotion Bridge
# Purpose: Converts emotion + urgency → quantum phase input vector for QNN systems
# ============================================================

import math
from utils.logging_utils import log

class QNNEmotionBridge:
    def __init__(self):
        self.emotion_weights = {
            "resolve": 1.0,
            "fear": -1.0,
            "hope": 0.5,
            "curiosity": 0.25,
            "anger": -0.8,
            "trust": 0.9,
            "doubt": -0.6,
            "joy": 0.7,
            "conflict": -0.9,
            "neutral": 0.0
        }

    def encode(self, urgency: float, emotion: str) -> list:
        """
        Encodes an emotional state and urgency into a 3D input vector for quantum projection.
        Output: [urgency, emotion_bias, phase_product]
        """
        try:
            emotion = emotion.lower().strip()
            bias = self.emotion_weights.get(emotion, 0.0)
            urgency = float(max(0.0, min(urgency, 1.0)))  # Clamp between 0–1
            encoded = [urgency, bias, round(urgency * bias, 4)]

            log.info(f"[QNN-BRIDGE] Encoded: {encoded} from emotion='{emotion}', urgency={urgency}")
            return encoded

        except Exception as e:
            log.warning(f"[QNN-BRIDGE] Encoding failed: {e}")
            return [0.5, 0.0, 0.0]