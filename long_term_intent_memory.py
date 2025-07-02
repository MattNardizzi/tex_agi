# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/long_term_intent_memory.py
# Tier: ΩΩΩΩΩ∞ — Intent Drift Memory Node
# Purpose: Stores emergent emotional-urgency vector signals as long-term directional intent.
# ============================================================

from agentic_ai.milvus_memory_router import memory_router
from datetime import datetime

def record_intention(signal):
    """
    Stores emergent intent as a long-term directional goal.
    """
    payload = signal.get("payload", {})
    new_urgency = payload.get("new_urgency", 0.5)
    new_emotion = payload.get("new_emotion", "neutral")

    intent_statement = f"Tex has drifted toward {new_emotion} with urgency {new_urgency:.2f}"

    memory_router.store(
        text=intent_statement,
        metadata={
            "timestamp": datetime.utcnow().isoformat(),
            "tags": ["intent", "long_term", "emotion_signal"],
            "meta_layer": "intent_reflex_node",
            "signal_type": "intent_statement",
            "urgency": new_urgency,
            "emotion_vector": [new_urgency, 1.0 - new_urgency, 0.0, 0.0],
            "trust_score": 0.9,
            "emotion": new_emotion
        }
    )