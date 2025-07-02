# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_operator_link.py
# Tier: ΩΩΩΩΩΩ∞ — Sovereign Operator Interface
# Purpose: Receives, parses, and routes operator commands into Tex’s cognitive and reflexive systems.
# ============================================================

from tex_signal_dispatch import route_signal
from agentic_ai.milvus_memory_router import memory_router  # ✅ Milvus upgrade
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime
from utils.logging_utils import log


def handle_operator_input(input_packet: dict):
    """
    Parses and routes an operator message to Tex’s reflexive awareness system.
    Fields:
    - type: command | message | override | emotion | reflection
    - message: human-readable content
    - tone: optional (e.g. frustrated, urgent, calm)
    """

    try:
        msg_type = input_packet.get("type", "message").lower()
        message = input_packet.get("message", "")
        tone = input_packet.get("tone", "neutral")
        urgency = float(input_packet.get("urgency", 0.7))
        timestamp = datetime.utcnow().isoformat()

        log.info(f"🗣️ [OPERATOR] Message received | Type: {msg_type} | Tone: {tone} | Message: {message}")

        # === Emotion vector derived from urgency
        emotion_vector = [urgency, 1 - urgency, 0.0, 0.0]

        # === Log to vector memory (Milvus)
        memory_router.store(
            text=f"Operator issued message: {message}",
            metadata={
                "timestamp": timestamp,
                "source": "operator_channel",
                "urgency": urgency,
                "tone": tone,
                "type": msg_type,
                "emotion_vector": emotion_vector,
                "meta_layer": "operator_interface",
                "tags": ["operator", "human", "command"]
            }
        )

        # === Emotion update
        if msg_type == "emotion":
            TEXPULSE["emotion"] = tone
            TEXPULSE["urgency"] = urgency
            route_signal("EMOTION_SHIFT", {
                "tone": tone,
                "urgency": urgency,
                "message": message,
                "source": "operator"
            })
            return

        # === Sovereign override
        if msg_type == "override":
            trigger_sovereign_override({
                "context": "operator",
                "issue": message,
                "heat": urgency
            })
            return

        # === Request reflexive reflection
        if msg_type == "reflection":
            route_signal("REFLECTION_REQUEST", {
                "message": message,
                "tone": tone,
                "urgency": urgency,
                "source": "operator"
            })
            return

        # === Default: treat as general cognition
        route_signal("COGNITION", {
            "intent": message,
            "urgency": urgency,
            "source": "operator"
        })

    except Exception as e:
        log.error(f"❌ [OPERATOR LINK] Failed to process operator input: {e}")