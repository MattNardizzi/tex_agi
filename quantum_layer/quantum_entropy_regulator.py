# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/quantum_entropy_regulator.py
# Tier Ω.0+ — Adaptive Quantum Entropy Regulator
# Purpose: Governs collapse logic and reflex pressure via entropy-emotion-coherence mapping
# ============================================================

import numpy as np
import math
from utils.logging_utils import log

class QuantumEntropyRegulator:
    def __init__(self, default_threshold=0.5):
        self.coherence_threshold = default_threshold
        self.last_entropy = None
        self.last_pressure = None
        self.last_mode = "neutral"

    def regulate(self, entropy_level, mode="neutral", return_signal=False):
        """
        Modulates entropy → reflex pressure → collapse decision.

        Parameters:
            entropy_level (float): System entropy [0.0–1.0+]
            mode (str): 'neutral', 'regret-biased', 'goal-biased', 'panic'
            return_signal (bool): If True, return pressure signal too

        Returns:
            bool or (bool, float): Collapse decision (and signal if requested)
        """
        pressure = self._entropy_to_pressure(entropy_level)

        if mode == "regret-biased":
            pressure *= 1.2
        elif mode == "goal-biased":
            pressure *= 0.85
        elif mode == "panic":
            pressure = min(1.0, pressure + 0.3)

        collapse = pressure >= (1.0 - self.coherence_threshold)

        # Store diagnostics
        self.last_entropy = entropy_level
        self.last_pressure = round(pressure, 6)
        self.last_mode = mode

        if return_signal:
            return collapse, self.last_pressure
        return collapse

    def _entropy_to_pressure(self, entropy):
        """
        Converts entropy into reflex pressure using a sigmoid + log fusion curve.
        """
        try:
            sigmoid = 1 / (1 + math.exp(-6 * (entropy - 0.5)))
            log_bias = np.log1p(entropy + 1e-5)
            pressure = (0.7 * sigmoid) + (0.3 * log_bias)
            return min(1.0, round(pressure, 6))
        except Exception as e:
            log.warning(f"[EntropyRegulator] Pressure calculation failed: {e}")
            return 0.5

    def diagnostics(self):
        return {
            "last_entropy": self.last_entropy,
            "last_pressure": self.last_pressure,
            "last_mode": self.last_mode
        }