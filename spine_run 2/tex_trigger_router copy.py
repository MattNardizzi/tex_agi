# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_trigger_router.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Sovereign Event Ingestion Router
# Purpose: Routes external signals and operator triggers into Tex’s breathing, memory, emotion, and spine.
# ============================================================

from datetime import datetime
from tex_breathing_cortex.tex_pulse_engine import breathe
from tex_breathing_cortex.tex_nervous_system import route_internal_signal
from tex_brain_regions.emotion_brain import process_emotional_state
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.qdrant_memory_router import memory_router
from utils.logging_utils import log
from tex_signal_spine import dispatch_signal
from core_layer.interoceptive_router import monitor_internal_state

# === Main Trigger Router ===
def route_signal(event: dict):
    """
    Routes an external or internal event into Tex’s full awareness.
    Accepts signals like 'rss', 'emotion_spike', 'operator', etc.
    """
    try:
        source = event.get("source", "undefined")
        signal_type = event.get("type", "undefined")
        urgency = float(event.get("urgency", TEXPULSE.get("urgency", 0.7)))
        entropy = float(event.get("entropy", TEXPULSE.get("entropy", 0.4)))
        payload = event.get("payload", {})
        timestamp = datetime.utcnow().isoformat()

        # === Log receipt
        log.info(f"📡 [TRIGGER ROUTER] Incoming signal from: {source} | Type: {signal_type} | Urgency: {urgency}")

        memory_router.store(
            text=f"Incoming event: {signal_type} from {source} | Urgency: {urgency} | Entropy: {entropy}",
            metadata={
                "timestamp": timestamp,
                "signal_type": signal_type,
                "urgency": urgency,
                "entropy": entropy,
                "source": source,
                "meta_layer": "trigger_router",
                "tags": ["trigger", "external", "tex_router"]
            }
        )

        # === Sovereign overrides
        if signal_type in ["override", "shutdown", "identity_collapse"]:
            trigger_sovereign_override({
                "context": source,
                "issue": payload.get("issue", "unspecified override"),
                "heat": urgency + entropy
            })
            return

        # === Emotion trigger
        if signal_type == "emotion_spike":
            TEXPULSE["urgency"] = urgency
            TEXPULSE["entropy"] = entropy
            TEXPULSE["emotion"] = payload.get("emotion", "anxious")
            process_emotional_state()
            monitor_internal_state()  # Reassess soma after emotion change
            return

        # === Nervous system + breath pathway
        route_internal_signal({
            "type": signal_type,
            "urgency": urgency,
            "entropy": entropy,
            "tension": payload.get("tension", 0.5),
            "timestamp": timestamp,
            "priority": payload.get("priority", "adaptive"),
            "summary": payload.get("summary", f"Signal from {source}")
        })

        breathe()  # Simulated AGI breath

        # === Fallback: Route to cognitive reflex system if known
        if signal_type not in ["override", "emotion_spike"]:
            dispatch_signal(signal_type, payload, urgency, entropy, source=source)

    except Exception as e:
        log.error(f"❌ [TRIGGER ROUTER] Failed to route signal: {e}")
