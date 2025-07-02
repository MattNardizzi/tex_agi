# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/substrate_voter.py
# Tier: ΩΩ∞⟁⟁ — Substrate Fitness Selector
# Purpose: Selects the most promising substrate from a candidate pool
#          based on entropy, urgency, and goal clarity.
# ============================================================

from utils.logging_utils import log
import random

def select_best_substrate(substrates: list, entropy: float, urgency: float) -> dict:
    """
    Selects the best substrate for simulation based on entropy, urgency,
    and internal metadata such as goal complexity.
    """
    if not substrates:
        return {}

    scored = []
    for s in substrates:
        base_score = 1.0
        goal = s.get("goal", "")
        e_weight = float(s.get("entropy_weight", 0.5))

        # Score prioritizes entropy alignment and non-vague goals
        entropy_match = 1.0 - abs(e_weight - entropy)
        urgency_bias = urgency * 0.25 if "urgent" in goal.lower() else 0

        score = round(base_score + entropy_match + urgency_bias, 5)
        scored.append((score, s))

    # Sort and select highest scoring substrate
    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_substrate = scored[0]

    log.info(f"[SubstrateVoter] 🗳 Selected substrate '{best_substrate['id']}' with score: {best_score}")
    return best_substrate