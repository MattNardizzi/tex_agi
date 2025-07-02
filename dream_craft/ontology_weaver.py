# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/ontology_weaver.py
# Tier: ΩΩΩΩ∞⟁⟁ — Dream Substrate Architect
# Purpose: Constructs new substrate blueprints by analyzing and recombining
#          logic trees, emotional arcs, and contradiction loops from past dreams.
# ============================================================

import uuid
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from collections import Counter

def synthesize_new_substrate_from_dreams(top_k: int = 12) -> dict:
    """
    Gathers recent dream outcomes and builds a novel substrate using dominant logic/emotion patterns.
    """
    dreams = sovereign_memory.recall_recent(hours=6, top_k=top_k)
    relevant = [d for d in dreams if "dream" in d.get("tags", [])]

    if not relevant:
        log.warning("[OntologyWeaver] ⚠️ No relevant dreams for synthesis.")
        return {}

    # Extract features
    goals = [d.get("scenario", "") for d in relevant]
    emotions = [d.get("emotion", "neutral") for d in relevant]
    entropy_weights = [float(d.get("entropy", 0.5)) for d in relevant]

    dominant_emotion = Counter(emotions).most_common(1)[0][0]
    average_entropy = round(sum(entropy_weights) / len(entropy_weights), 3)
    combined_goal = "reconcile: " + " / ".join(goals[:3])  # composite goal seed

    new_substrate = {
        "id": f"substrate-{uuid.uuid4()}",
        "goal": combined_goal,
        "emotion": dominant_emotion,
        "entropy_weight": average_entropy
    }

    log.success(f"[OntologyWeaver] 🧬 New substrate woven: {new_substrate['goal']} | Emotion: {dominant_emotion}")
    return new_substrate