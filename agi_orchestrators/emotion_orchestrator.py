# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/emotion_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — Emotional Volatility Router
# Purpose: Routes emotional shifts into the sovereign affect cortex and triggers volatility reflexes.
# ============================================================

from datetime import datetime
import numpy as np

from tex_brain_regions.emotion_brain import process_emotional_state
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def route_emotional_update(emotion: str, urgency: float = 0.7, entropy: float = 0.4) -> dict:
    """
    Routes an emotional shift into sovereign affective processing.
    Logs memory and identity imprint. Triggers reflex if volatility exceeds threshold.
    """
    try:
        timestamp = datetime.utcnow().isoformat()

        # === Update sovereign state
        TEXPULSE["emotion"] = emotion
        TEXPULSE["urgency"] = urgency
        TEXPULSE["entropy"] = entropy

        # === Process emotional shift through cortex
        result = process_emotional_state()
        volatility = result.get("volatility_score", 0.5)
        reflexes = result.get("reflexes", [])

        # === Store to Milvus
        text = f"[EMOTION] State updated → {emotion}"
        metadata = {
            "timestamp": timestamp,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "volatility_score": volatility,
            "reflexes": reflexes,
            "meta_layer": "emotion_router",
            "tags": ["emotion", "reflex", "state", "modulation"]
        }
        memory_router.store(text, metadata)

        # === Imprint to ChronoFabric
        encode_event_to_fabric(
            raw_text=text,
            emotion_vector=np.array([urgency, entropy, 0.2, 0.1]),
            entropy_level=entropy,
            tags=metadata["tags"]
        )

        # === Trigger reflex if high volatility
        if volatility >= 0.7:
            dispatch_signal("emotional_spike", {
                "emotion": emotion,
                "volatility_score": volatility,
                "reflexes": reflexes
            }, urgency=urgency, entropy=entropy, source="emotion_orchestrator")

        log.info(f"[EMOTION ORCH] Emotion: {emotion} | Reflexes: {reflexes}")
        return result

    except Exception as e:
        log.error(f"❌ [EMOTION ORCH] Failed to process emotional update: {e}")
        return {
            "reflexes": ["emotion_error"],
            "volatility_score": 0.5
        }