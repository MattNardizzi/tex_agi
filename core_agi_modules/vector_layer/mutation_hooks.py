# mutation_hooks.py
# Tier Ω∞ Reflex Mutation Trigger Hooks (Final Form)
# Location: core_agi_modules/vector_layer/mutation_hooks.py

import hashlib
from random import random
from core_agi_modules.vector_layer.fusion_engine import fuse_related_vectors

# === Mutation Signature Generator ===
def mutation_signature(text, reason):
    key = f"{text}|{reason}"
    return hashlib.sha256(key.encode()).hexdigest()

# === Reflex Trigger ===
def trigger_mutation_if_needed(vector, metadata):
    """
    Fires mutation or fusion reflex if memory is volatile or contradictory.
    Criteria: high heat, low trust, specific tags, or stochastic volatility.
    """
    heat = float(metadata.get("heat", 0.5))
    trust = float(metadata.get("trust_score", 1.0))
    tags = metadata.get("tags", [])
    emotion = metadata.get("emotion", "neutral")
    content = metadata.get("content", "reflex_input")

    volatile = heat > 0.85
    untrusted = trust < 0.35
    targeted = any(tag in ["contradiction", "conflict", "unstable"] for tag in tags)
    entropy_roll = random() < 0.08

    if volatile or untrusted or targeted or entropy_roll:
        trigger_cause = "high_heat" if volatile else "low_trust" if untrusted else "tag_match" if targeted else "entropy_roll"
        print(f"🧬 [MUTATION] Triggered by: {trigger_cause}")

        # Create 2 semantic forks
        for i in range(2):
            variant = f"{content} [mutation:{emotion}:{i}]"
            sig = mutation_signature(variant, trigger_cause)
            fuse_related_vectors(
                [variant],
                tags=["mutated", "auto"],
                emotion=emotion
            )