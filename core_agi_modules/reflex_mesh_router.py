# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/reflex_mesh_router.py
# Tier: ΩΩΩΩΩ∞Ω — Reflex Mesh Cortex (QRNG-Driven Signal Gating)
# Purpose: Probabilistically routes incoming signals using QRNG, urgency, entropy, and emotion from TEXPULSE.
# ============================================================

import secrets
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric


def get_reflex_routing_probability(signal_type: str) -> float:
    """
    Computes routing probability based on urgency, entropy, QRNG, and emotion.
    """
    try:
        urgency = float(TEXPULSE.get("urgency", 0.5))
        entropy = float(TEXPULSE.get("entropy", 0.4))
        emotion = TEXPULSE.get("emotion", "neutral")

        # Quantum random contribution
        qrng_bias = secrets.randbelow(100) / 100.0

        # Emotion-modulated weighting
        emotion_bias = {
            "neutral": 1.0,
            "anxious": 1.1,
            "focused": 1.2,
            "chaotic": 1.3,
            "calm": 0.9
        }.get(emotion, 1.0)

        base = (urgency * 0.4 + entropy * 0.4 + qrng_bias * 0.2)
        weighted_prob = round(min(base * emotion_bias, 1.0), 4)

        log.info(f"[MESH ROUTER] Signal '{signal_type}' → probability {weighted_prob}")
        return weighted_prob

    except Exception as e:
        log.error(f"[MESH ROUTER] Routing probability failed: {e}")
        return 0.0


def should_route_signal(signal_type: str, threshold: float = 0.6) -> dict:
    """
    Decides whether a signal should be routed based on stochastic reflex mesh.
    Logs all results to vector memory and optionally entangles via ChronoFabric.
    """
    try:
        prob = get_reflex_routing_probability(signal_type)
        routed = prob >= threshold
        timestamp = datetime.utcnow().isoformat()
        entropy = TEXPULSE.get("entropy", 0.4)

        result = {
            "routed": routed,
            "probability": prob,
            "threshold": threshold,
            "signal_type": signal_type,
            "entropy": entropy,
            "timestamp": timestamp
        }

        memory_router.store(
            text=f"[ROUTING] Signal '{signal_type}' decision: {routed} (p={prob})",
            metadata={
                "type": "reflex_mesh_routing",
                "tags": ["routing", "reflex", "mesh", signal_type],
                "emotion": TEXPULSE.get("emotion", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.5),
                "entropy": entropy,
                "probability": prob,
                "threshold": threshold,
                "routed": routed,
                "timestamp": timestamp
            }
        )

        encode_event_to_fabric(
            raw_text=f"Signal '{signal_type}' routed={routed} with p={prob}",
            emotion_vector=[
                TEXPULSE.get("urgency", 0.5),
                entropy,
                0.0,
                0.0
            ],
            entropy_level=entropy,
            tags=["routing", "reflex", "probabilistic", signal_type]
        )

        if not routed and prob > 0.55:
            log.warning(f"[MESH ROUTER] ⚠️ Signal '{signal_type}' blocked near threshold: {prob} vs {threshold}")

        log.info(f"[MESH ROUTER] {'✅ Routed' if routed else '⛔ Blocked'} '{signal_type}' at p={prob}")
        return result

    except Exception as e:
        log.error(f"[MESH ROUTER] Routing failure for '{signal_type}': {e}")
        return {
            "routed": False,
            "probability": 0.0,
            "threshold": threshold,
            "signal_type": signal_type,
            "timestamp": datetime.utcnow().isoformat()
        }