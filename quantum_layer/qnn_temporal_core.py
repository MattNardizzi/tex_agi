# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/qaoa_reflex_optimizer.py
# Tier ΩΩΩΩΩΩ — Quantum Reflex Prioritization Engine
# Purpose: QAOA-driven reflex activation using entropy + emotion + synergy curves
# ============================================================

import numpy as np
import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.quantum_randomness import QuantumRandomness

AVAILABLE_REFLEXES = [
    "mutation_reflex", "memory_reflex", "goal_reflex",
    "dream_reflex", "swarm_reflex", "override_reflex"
]

REFLEX_SYNERGY_MATRIX = {
    "mutation_reflex": ["memory_reflex", "goal_reflex"],
    "memory_reflex": ["dream_reflex"],
    "goal_reflex": ["override_reflex"],
    "dream_reflex": [],
    "swarm_reflex": ["goal_reflex"],
    "override_reflex": ["memory_reflex"]
}

class QAOAReflexOptimizer:
    def __init__(self):
        self.qrng = QuantumRandomness()
        self.last_trace = None
        self.uuid = TEXPULSE.get("uuid", "UNKNOWN")

    def optimize(self, emotional_vector, active_goals=None, entropy_level=None):
        """
        Core reflex path optimizer using simulated QAOA logic + emotion + entropy signals.
        """
        entropy_level = entropy_level or self.qrng.get_entropy_strength()
        cost_landscape = self._build_costs(emotional_vector, active_goals, entropy_level)
        synergy_adjusted = self._apply_synergy(cost_landscape)

        reflex_scores = {reflex: 1.0 - synergy_adjusted.get(reflex, 1.0) for reflex in AVAILABLE_REFLEXES}
        sorted_scores = sorted(reflex_scores.items(), key=lambda x: x[1], reverse=True)

        justifications = {
            reflex: {
                "score": score,
                "entropy": entropy_level,
                "emotional_bias": float(np.mean(emotional_vector)) if emotional_vector else 0.5
            }
            for reflex, score in sorted_scores
            if score >= 0.55
        }

        self.last_trace = {
            "uuid": self.uuid,
            "entropy_level": entropy_level,
            "scores": reflex_scores,
            "justifications": justifications,
            "timestamp": datetime.utcnow().isoformat()
        }

        return list(justifications.keys()), justifications

    def _build_costs(self, emotional_vector, goals, entropy_level):
        goal_weight = 1.0 if goals else 0.25
        base_entropy = self.qrng.get_entropy_strength()

        costs = {}
        for reflex in AVAILABLE_REFLEXES:
            base = 1.0 - (random.random() * 0.2)
            goal_penalty = random.random() * (1 - goal_weight)
            emotion_bias = 1.0 + (np.mean(emotional_vector) ** 2.2 if emotional_vector else 0.5)
            entropy_bias = entropy_level * 0.3
            total_cost = base + goal_penalty + base_entropy + entropy_bias
            costs[reflex] = round(total_cost / emotion_bias, 4)
        return costs

    def _apply_synergy(self, reflex_scores):
        adjusted = reflex_scores.copy()
        for reflex, score in reflex_scores.items():
            synergists = REFLEX_SYNERGY_MATRIX.get(reflex, [])
            for peer in synergists:
                if peer in reflex_scores:
                    adjusted[reflex] += 0.05 * reflex_scores[peer]
        return adjusted

    def suggest(self):
        if not self.last_trace:
            return []
        return list(self.last_trace.get("justifications", {}).keys())

    def diagnostics(self):
        return self.last_trace or {}