# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: ontogenesis/meaning_seed_builder.py
# Tier: ΩΩΩ∞ΣΣΣσσ — Semantic Seed Core
# Purpose: Generates latent, non-agentic meaning seeds that activate when contradiction pressure crosses threshold.
#          Also exposes real-time swarm species state for XAI and strategy cognition.
# ============================================================

import uuid
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event
from core_layer.tex_manifest import TEXPULSE


def create_meaning_seed(context: str, tension: float):
    """
    Creates a latent memory imprint with no reflex, no goal, no cognition.
    It exists only as potential meaning — awakened by future symbolic dissonance.
    """
    seed_id = f"seed_{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat()

    summary = f"Latent seed created to hold unresolved meaning for context '{context}'."

    metadata = {
        "seed_id": seed_id,
        "type": "latent_meaning",
        "context": context,
        "tension": tension,
        "activation_threshold": round(tension + 0.2, 4),
        "status": "dormant",
        "timestamp": timestamp,
        "meta_layer": "ontogenesis_seed",
        "tags": ["meaning_seed", "latent", "non_agentic"]
    }

    sovereign_memory.store(
        text=summary,
        metadata=metadata
    )

    log_event(f"[MEANING SEED] {seed_id} planted for '{context}'", level="info")

    return {
        "status": "planted",
        "seed_id": seed_id,
        "activation_threshold": metadata["activation_threshold"],
        "context": context
    }


# === Swarm Mood Aggregation (Species-Level Reflex State) ===
def get_species_swarm_state():
    urgency = TEXPULSE.get("urgency", 0.7)
    entropy = TEXPULSE.get("entropy", 0.4)
    emotion = TEXPULSE.get("emotion", "neutral")
    species = TEXPULSE.get("species_name", "Tex")

    return f"{species} swarm state → Emotion: {emotion}, Urgency: {urgency}, Entropy: {entropy}"
