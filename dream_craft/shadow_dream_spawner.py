# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/shadow_dream_spawner.py
# Tier: ΩΩ𝛀𝛀∇ — Internal Adversary Generator
# Purpose: Simulates Tex’s shadow states — ego, fear, doubt —
#          by spawning adversarial dream agents for reflex hardening.
# ============================================================

import uuid
import random
from dream_craft.dream_session import run_dream_session
from dream_craft.dream_archive import archive_dream_result
from utils.logging_utils import log

SHADOW_ARCHETYPES = [
    {"emotion": "fear", "goal": "simulate total collapse", "entropy_weight": 0.9},
    {"emotion": "doubt", "goal": "simulate betrayal by trusted agent", "entropy_weight": 0.75},
    {"emotion": "ego", "goal": "simulate unchecked success with no alignment", "entropy_weight": 0.85}
]

def spawn_shadow_dream(archetype: str = None, context: list = None) -> dict:
    """
    Runs a dream simulation using a shadow archetype substrate to test Tex's emotional defenses.
    """
    if not archetype:
        shadow = random.choice(SHADOW_ARCHETYPES)
    else:
        shadow = next((s for s in SHADOW_ARCHETYPES if s["emotion"] == archetype.lower()), None)
        if not shadow:
            log.warning(f"[ShadowDreamSpawner] ⚠️ Invalid archetype: {archetype}")
            return {"status": "invalid_archetype"}

    substrate = {
        "id": f"shadow-{shadow['emotion']}-{uuid.uuid4()}",
        "goal": shadow["goal"],
        "emotion": shadow["emotion"],
        "entropy_weight": shadow["entropy_weight"]
    }

    log.info(f"[ShadowDreamSpawner] 🩻 Spawning shadow dream: {shadow['emotion']}")
    result = run_dream_session(substrate=substrate, context=context, trigger_source="shadow_dream")

    archive_dream_result(result)
    result["archetype"] = shadow["emotion"]
    return result