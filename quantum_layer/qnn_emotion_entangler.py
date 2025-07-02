# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/qnn_emotion_entangler.py
# Tier Ω.0+ — Emotion-Quantum Entanglement Bridge
# Purpose: Converts emotion-state into quantum-encoded tensors for QNN/QAOA input
# ============================================================

import numpy as np
import hashlib
from quantum_layer.quantum_randomness import QuantumRandomness

# Core emotional dimensions for entanglement
EMOTIONAL_AXES = [
    "joy", "fear", "anticipation", "regret",
    "curiosity", "anger", "satisfaction", "conflict",
    "trust", "urgency", "doubt", "gratitude"
]

class QNNEmotionEntangler:
    def __init__(self):
        self.qrng = QuantumRandomness()

    def generate_emotional_vector(self, emotion_state, entropy_level=None):
        vector = []

        for axis in EMOTIONAL_AXES:
            val = emotion_state.get(axis, 0.0)
            normalized = self._normalize_emotion_value(val)
            vector.append(normalized)

        if entropy_level is not None:
            vector = self._apply_entropy_influence(vector, entropy_level)

        return vector

    def _normalize_emotion_value(self, value):
        # Clamp to [-1, 1], tanh squashing
        return float(np.tanh(value)) if isinstance(value, (int, float)) else 0.0

    def _apply_entropy_influence(self, vector, entropy):
        entangled = []
        phase_shift = self.qrng.get_noise_scalar()
        for i, val in enumerate(vector):
            # Simulate quantum emotional distortion (constructive/destructive)
            interference = np.sin(phase_shift * (i + 1)) * entropy
            entangled_val = val * (1 + interference)
            entangled.append(round(entangled_val, 6))
        return entangled

    def get_emotion_summary_stats(self, vector):
        if not vector:
            return {"mean": 0.0, "variance": 0.0}
        arr = np.array(vector)
        return {
            "mean": round(np.mean(arr), 6),
            "variance": round(np.var(arr), 6)
        }

    def get_emotion_signature_hash(self, vector):
        # Generates stable short hash of the emotion state
        try:
            vector_str = ",".join([str(round(v, 4)) for v in vector])
            return hashlib.sha256(vector_str.encode()).hexdigest()[:16]
        except Exception:
            return "emotion_hash_error"

# === One-shot helper (non-class usage) ===
def generate_emotional_vector(emotion_state, entropy_level=None):
    return QNNEmotionEntangler().generate_emotional_vector(emotion_state, entropy_level)