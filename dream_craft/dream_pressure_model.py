# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_pressure_model.py
# Tier: ΩΩ∞⟁ — Reflex Pressure Synthesizer
# Purpose: Calculates synthetic pressure from dream outcome contradiction,
#          misalignment, or entropy deviation. Used to trigger forks or belief updates.
# ============================================================

def calculate_synthetic_pressure(alignment: float, contradiction: float, entropy: float, urgency: float = 0.6) -> float:
    """
    Combines dream outcome metrics to compute overall reflex pressure.
    Range: 0.0 (no pressure) to 1.0 (maximum contradiction/dissonance).
    """
    pressure = (
        (1 - alignment) * 0.4 +
        contradiction * 0.4 +
        entropy * 0.1 +
        urgency * 0.1
    )
    return round(min(1.0, pressure), 6)


def should_trigger_dream_run(pressure: float, threshold: float = 0.65) -> bool:
    """
    Determines whether pressure is high enough to run a new substrate simulation.
    """
    return pressure >= threshold


def should_evolve_substrate(pressure: float, impact_score: float) -> bool:
    """
    Determines whether a substrate should mutate based on pressure and low dream impact.
    """
    return pressure > 0.7 and impact_score < 0.5