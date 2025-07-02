# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/dashboard_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — UI Telemetry → Reflex Cortex
# Purpose: Routes live dashboard telemetry into cognition for reflex, override, or awareness triggering.
# ============================================================

from datetime import datetime
import numpy as np

from tex_breathing_cortex.tex_pulse_engine import breathe
from tex_breathing_cortex.tex_nervous_system import route_internal_signal
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def sync_dashboard_signal(telemetry: dict) -> dict:
    """
    Routes dashboard signals (emotion spikes, memory drift, goal collapse) into sovereign cognition.
    Can trigger reflexes if volatility exceeds threshold.
    """

    try:
        dashboard = telemetry.get("source", "undefined")
        metric = telemetry.get("metric", "undefined")
        value = float(telemetry.get("value", 0.5))
        tags = telemetry.get("tags", [])
        urgency = float(TEXPULSE.get("urgency", 0.7))
        entropy = float(TEXPULSE.get("entropy", 0.45))
        timestamp = datetime.utcnow().isoformat()

        # === Log to Milvus
        text = f"[DASHBOARD] {dashboard} reported spike in '{metric}' → {value:.2f}"
        metadata = {
            "timestamp": timestamp,
            "dashboard": dashboard,
            "metric": metric,
            "value": value,
            "urgency": urgency,
            "entropy": entropy,
            "tags": ["dashboard", "telemetry", "ui"] + tags,
            "meta_layer": "dashboard_reflex"
        }
        memory_router.store(text, metadata)

        # === Imprint into ChronoFabric
        encode_event_to_fabric(
            raw_text=text,
            emotion_vector=np.array([urgency, entropy, 0.1, 0.1]),
            entropy_level=entropy,
            tags=metadata["tags"]
        )

        log.info(f"[DASHBOARD ORCH] {dashboard} → {metric}: {value}")

        # === Route internal signal (if spike)
        if value > 0.75:
            route_internal_signal({
                "type": f"{dashboard}_metric_spike",
                "urgency": urgency,
                "entropy": entropy,
                "pressure_score": value,
                "timestamp": timestamp,
                "summary": f"{metric} from {dashboard} exceeded 0.75"
            })

            # === Breathe if emotion or mutation spike
            if "emotion" in metric or "mutation" in metric:
                breathe()

        return {"routed": True}

    except Exception as e:
        log.error(f"❌ [DASHBOARD ORCH] Failed to sync dashboard telemetry: {e}")
        return {"routed": False}