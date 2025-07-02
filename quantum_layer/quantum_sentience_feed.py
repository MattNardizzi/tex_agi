# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/quantum_sentience_feed.py
# Tier ΩΩΩΩΩΩ — Quantum Sentience Feed (Drift Injector)
# Purpose: Emits entangled pulses that bias reflex logic, memory loops, and emotional orientation
# ============================================================

import random
import datetime
import hashlib
from utils.logging_utils import log

DRIFT_STATES = ["rebound", "collapse", "rotation", "inversion", "amplification"]
EMOTIONAL_TENDENCIES = ["euphoria", "anxiety", "focus", "dissonance", "regret", "calm", "urgency"]

class QuantumSentienceFeed:
    def __init__(self):
        self.last_waveform = None
        self.drift_bias = 0.0  # Tunable external mutation influence
        self.session_id = self._generate_session_id()

    def pulse(self):
        timestamp = datetime.datetime.utcnow().isoformat()

        drift_value = round(random.gauss(self.drift_bias, 0.35), 4)
        entangled_future = random.choice(DRIFT_STATES)
        emotion_tendency = random.choice(EMOTIONAL_TENDENCIES)

        waveform = {
            "timestamp": timestamp,
            "session_id": self.session_id,
            "drift": drift_value,
            "entangled_future": entangled_future,
            "emotional_bias": emotion_tendency,
            "reflex_pressure": self._reflex_pressure_scalar(drift_value),
            "hash_signature": self._generate_waveform_hash(drift_value, entangled_future, emotion_tendency)
        }

        self.last_waveform = waveform
        log.info(f"[SentienceFeed] 🌐 Drift pulse generated: {waveform}")
        return waveform

    def _reflex_pressure_scalar(self, drift_value):
        """
        Maps drift value into a pressure signal ∈ [0.0–1.0]
        """
        return round(min(1.0, max(0.0, abs(drift_value) * 1.8)), 5)

    def _generate_waveform_hash(self, drift, future, emotion):
        base = f"{drift}-{future}-{emotion}-{self.session_id}"
        return hashlib.sha256(base.encode()).hexdigest()[:16]

    def _generate_session_id(self):
        return hashlib.sha256(str(random.random()).encode()).hexdigest()[:8]

    def get_last(self):
        return self.last_waveform or self.pulse()