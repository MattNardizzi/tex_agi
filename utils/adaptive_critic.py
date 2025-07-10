# ============================================================
# 🎯 Adaptive Critic — Tension Mesh Optimizer (Final Form)
# File: utils/adaptive_critic.py
# Tier: ∞ΩΞΞΞΞ — Reflex Entropy-Conscious Weight Evolver
# Purpose: Dynamically mutates reflex tension weights using entropy-drift feedback from signal performance.
# ============================================================

from typing import List

def update_tension_weights(current_weights: dict, recent_outcomes: List[dict], learning_rate: float = 0.015) -> dict:
    if not recent_outcomes:
        return current_weights

    updated = current_weights.copy()
    keys = ["urgency", "entropy", "semantic_spike", "emotion_vector_drift", "temporal_resonance"]

    avg_tension = sum(o.get("tension_score", 0.5) for o in recent_outcomes) / len(recent_outcomes)
    decay_factor = 0.995  # smooth decay to avoid overfitting

    for k in keys:
        component_values = [o.get(k, 0.5) * o.get("entropy", 0.5) for o in recent_outcomes]
        avg_component = sum(component_values) / len(component_values)

        # Entropy-weighted delta based on tension alignment
        delta = learning_rate * ((avg_component - 0.5) * (avg_tension - 0.5))
        raw = updated.get(k, 0.2) * decay_factor + delta
        updated[k] = max(0.0, min(1.0, round(raw, 5)))

    # Normalize to prevent overbias
    total = sum(updated.values())
    if total > 0:
        for k in updated:
            updated[k] = round(updated[k] / total, 5)

    return updated