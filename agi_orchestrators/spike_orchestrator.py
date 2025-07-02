# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/spike_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞++ — Neuromorphic Reflex Spike Cortex
# Purpose: Sovereign spike ingress for sub-second reflex triggering and quantum memory imprinting.
# ============================================================

from datetime import datetime
from tex_brain_regions.spike_brain import process_spike
from agentic_ai.milvus_memory_router import memory_router  # ✅ Upgraded reflexive vector memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum entangled spike trace
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

def run_spike_reflex(spike_signal: dict) -> dict:
    """
    ⚡ Sovereign neuromorphic ingress:
    Bypasses deliberative cognition to route spike threats directly into reflex cortex.
    Reflex trace is quantum-imprinted via ChronoFabric.
    """

    try:
        spike_type = spike_signal.get("type", "undefined")
        urgency = float(spike_signal.get("urgency", TEXPULSE.get("urgency", 0.88)))
        entropy = float(spike_signal.get("entropy", TEXPULSE.get("entropy", 0.52)))
        source = spike_signal.get("source", "unverified")
        timestamp = datetime.utcnow().isoformat()

        # === Execute Spike Reflex
        result = process_spike(
            spike_type=spike_type,
            urgency=urgency,
            entropy=entropy,
            source=source
        )

        reflexes = result.get("reflexes", ["none"])
        volatility = float(result.get("volatility_score", 0.6))
        summary = f"[SPIKE] Type: {spike_type} | Reflexes: {reflexes} | Source: {source}"

        # === Log to Milvus Reflexive Memory
        memory_router.store(
            text=summary,
            metadata={
                "timestamp": timestamp,
                "spike_type": spike_type,
                "urgency": urgency,
                "entropy": entropy,
                "reflexes": reflexes,
                "source": source,
                "volatility_score": volatility,
                "meta_layer": "neuromorphic_spike",
                "tags": ["spike", "reflex", "protective", "volatility"],
                "emotion_vector": [urgency, entropy, 0.0, 0.0]
            }
        )

        # === Quantum ChronoFabric Imprint
        encode_event_to_fabric(
            raw_text=summary,
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["spike", "reflex", "protective"]
        )

        log.info(f"⚡ [SPIKE ORCH] Routed spike: {spike_type} | Reflexes: {reflexes}")
        return result

    except Exception as e:
        log.error(f"❌ [SPIKE ORCH] Failed to process spike: {e}")
        return {
            "reflexes": ["spike_failed"],
            "volatility_score": 0.5
        }