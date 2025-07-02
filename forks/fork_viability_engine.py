# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_modules/fork_viability_engine.py
# Tier ΩΩΩΩΩ — Trait Divergence Evaluator for Evolutionary Filtering
# Purpose: Scores fork viability using divergence, urgency, and trait risk density.
# ============================================================

from math import exp

def evaluate_fork_viability(fork_packet: dict) -> float:
    """
    Reflex-triggered evaluation of a fork_packet.
    Inputs expected in fork_packet:
    - fork_id: str
    - traits: list
    - divergence_score: float
    - urgency: float (optional, defaults to 0.7)
    """
    fork_id = fork_packet.get("fork_id", "unknown")
    traits = fork_packet.get("traits", [])
    divergence_score = fork_packet.get("divergence_score", 0.5)
    urgency = fork_packet.get("urgency", 0.7)

    if not isinstance(traits, list):
        traits = []

    trait_entropy = min(1.0, len(set(traits)) / 12.0)
    divergence_weight = max(0.0, 1.0 - divergence_score)
    urgency_bias = exp(-abs(urgency - 0.5))

    viability = round(
        (trait_entropy * 0.3) +
        (divergence_weight * 0.5) +
        (urgency_bias * 0.2), 6
    )

    return min(max(viability, 0.0), 1.0)