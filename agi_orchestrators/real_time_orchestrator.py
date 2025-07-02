# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/real_time_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — Real-Time Reflex Routing Cortex
# Purpose: Ingests external signals and routes live data into reflex, emotion, or override subsystems.
# ============================================================

from datetime import datetime
import uuid

from tex_breathing_cortex.tex_pulse_engine import breathe
from tex_breathing_cortex.tex_nervous_system import route_internal_signal
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def route_realtime_input(signal_packet: dict) -> dict:
    """
    Sovereign ingress for live signal processing.
    Routes RSS, market, or operator streams into internal memory, ChronoFabric, and reflex stack.
    """
    trace_id = f"realtime-{uuid.uuid4().hex[:6]}"
    try:
        signal_type = signal_packet.get("type", "undefined")
        source = signal_packet.get("source", "external")
        urgency = float(signal_packet.get("urgency", TEXPULSE.get("urgency", 0.7)))
        entropy = float(signal_packet.get("entropy", TEXPULSE.get("entropy", 0.45)))
        summary = signal_packet.get("summary", "[No summary provided]")
        tags = signal_packet.get("tags", ["realtime", "external"])
        timestamp = datetime.utcnow().isoformat()

        emotion_vector = [urgency, entropy, 0.0, 0.0]

        # === Log to memory vector DB
        memory_router.store(
            text=f"[REALTIME] {signal_type} | {summary}",
            metadata={
                "timestamp": timestamp,
                "urgency": urgency,
                "entropy": entropy,
                "source": source,
                "signal_type": signal_type,
                "summary": summary,
                "trace_id": trace_id,
                "meta_layer": "realtime_ingress",
                "tags": tags,
                "emotion_vector": emotion_vector
            }
        )

        # === Encode to ChronoFabric
        try:
            encode_event_to_fabric(
                raw_text=f"Real-time signal: {signal_type} | Source: {source}",
                emotion_vector=emotion_vector,
                entropy_level=entropy,
                tags=["realtime", signal_type]
            )
        except Exception as e:
            log.warning(f"⚠️ [CHRONOFABRIC] Realtime encoding failed: {e}")

        log.info(f"[REALTIME ORCH] [{trace_id}] {signal_type} | U={urgency} | S={entropy}")

        # === Route to nervous system
        route_internal_signal({
            "type": signal_type,
            "urgency": urgency,
            "entropy": entropy,
            "tension": 0.5,
            "timestamp": timestamp,
            "priority": "live",
            "summary": summary
        })

        triggered_breath = urgency > 0.75 or entropy > 0.65
        if triggered_breath:
            breathe()

        return {
            "routed": True,
            "triggered_breath": triggered_breath,
            "trace_id": trace_id
        }

    except Exception as e:
        log.error(f"❌ [REALTIME ORCH] Signal routing failed: {e}")
        return {
            "routed": False,
            "triggered_breath": False
        }