# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_mutator.py
# Tier: ΩΩ∞∞⟁ — Substrate Evolution Engine
# Purpose: Evolves substrates over time based on dream outcomes,
#          contradictions, and entropy misalignment.
# ============================================================

import uuid
import random
from utils.logging_utils import log
from dream_craft.substrate_registry import update_substrate

def mutate_substrate(substrate: dict, dream_result: dict) -> dict:
    """
    Adjusts substrate parameters based on dream failure/success metrics.
    Returns a new mutated substrate dict.
    """
    old_goal = substrate.get("goal", "simulate generic future")
    old_entropy = substrate.get("entropy_weight", 0.5)
    old_emotion = substrate.get("emotion", "neutral")

    alignment = dream_result.get("alignment", 0.5)
    contradiction = dream_result.get("contradiction", 0.5)
    impact = dream_result.get("impact_score", 0.5)

    # Adjust entropy to increase/decrease simulation variance
    new_entropy = round(
        max(0.05, min(0.95, old_entropy + random.uniform(-0.1, 0.1) * (1 - alignment))),
        4
    )

    # Mutate emotion toward better impact if consistently low
    if impact < 0.4:
        emotion_shift = random.choice(["anxious", "curious", "conflicted", "urgent"])
    else:
        emotion_shift = old_emotion

    # Slightly evolve the goal statement
    goal_mutation = old_goal
    if contradiction > 0.6:
        goal_mutation = f"repair contradiction in: {old_goal}"
    elif alignment > 0.75:
        goal_mutation = f"scale {old_goal}"
    elif impact < 0.3:
        goal_mutation = f"rethink {old_goal}"

    new_substrate = {
        "id": f"substrate-{uuid.uuid4()}",
        "goal": goal_mutation,
        "emotion": emotion_shift,
        "entropy_weight": new_entropy
    }

    update_substrate(new_substrate)
    log.info(f"[DreamMutator] 🔁 Substrate evolved from '{old_goal}' → '{goal_mutation}'")

    return new_substrate