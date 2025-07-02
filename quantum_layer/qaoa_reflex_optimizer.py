# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/qaoa_reflex_optimizer.py
# Tier Ω.0+ — Quantum Reflex Prioritization Engine
# Purpose: QAOA-driven reflex activation with synergy, entropy-emotion curvature, justification
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
        self.last_run_trace = None
        self.uuid = TEXPULSE.get("uuid", "UNDEFINED")

    def optimize_reflex_path(self, emotional_vector, active_goals, entropy_level=0.5):
        cost_map = self.build_cost_landscape(emotional_vector, active_goals)
        weighted_cost = self.apply_emotional_pressure(cost_map, emotional_vector, entropy_level)
        reflex_scores = {reflex: 1.0 - weighted_cost.get(reflex, 1.0) for reflex in AVAILABLE_REFLEXES}
        reflex_scores = self.adjust_for_synergy(reflex_scores)

        sorted_reflexes = sorted(reflex_scores.items(), key=lambda x: x[1], reverse=True)

        reflex_justifications = {
            reflex: {
                "score": score,
                "entropy_level": entropy_level,
                "mood_bias": float(np.mean(emotional_vector)) if emotional_vector else 0.5
            }
            for reflex, score in sorted_reflexes
            if score >= 0.55
        }

        self.last_run_trace = {
            "uuid": self.uuid,
            "timestamp": datetime.utcnow().isoformat(),
            "reflex_scores": reflex_scores,
            "justifications": reflex_justifications,
            "entropy": entropy_level
        }

        return list(reflex_justifications.keys()), reflex_justifications

    def build_cost_landscape(self, emotional_vector, goals):
        goal_weight = 1.0 if goals else 0.3
        entropy_noise = self.qrng.get_entropy_strength()

        cost = {}
        for reflex in AVAILABLE_REFLEXES:
            base = 1.0 - (random.random() * 0.2)
            penalty = random.random() * (1 - goal_weight)
            cost[reflex] = round(base + penalty + entropy_noise, 4)
        return cost

    def apply_emotional_pressure(self, cost_map, emotional_vector, entropy_level):
        adjusted = {}
        mood_bias = np.mean(emotional_vector) if emotional_vector else 0.5
        pressure_factor = 1.0 + (mood_bias ** 2.2) * entropy_level

        for reflex, base_cost in cost_map.items():
            adjusted_cost = base_cost / pressure_factor
            adjusted[reflex] = round(adjusted_cost, 4)
        return adjusted

    def adjust_for_synergy(self, reflex_scores):
        for reflex, score in reflex_scores.items():
            synergistic_refs = REFLEX_SYNERGY_MATRIX.get(reflex, [])
            for sref in synergistic_refs:
                if sref in reflex_scores:
                    reflex_scores[reflex] += 0.05 * reflex_scores[sref]
        return reflex_scores

    def suggest_reflexes(self):
        if not self.last_run_trace:
            return []
        return list(self.last_run_trace.get("justifications", {}).keys())

    def log_quantum_field_signature(self):
        if not self.last_run_trace:
            return
        print(f"[QAOA Reflex Trace] {self.last_run_trace}")