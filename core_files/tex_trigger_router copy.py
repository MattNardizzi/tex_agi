# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_trigger_router.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Sovereign Event Ingestion Router
# Purpose: Routes external signals and operator triggers into Tex’s breathing, memory, emotion, and spine with resonance-aware weighting.
# ============================================================

from datetime import datetime
from tex_breathing_cortex.tex_pulse_engine import breathe
from tex_breathing_cortex.tex_nervous_system import route_internal_signal
from tex_brain_regions.emotion_brain import process_emotional_state
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router
from utils.logging_utils import log
from tex_signal_spine import dispatch_signal
from core_layer.interoceptive_router import monitor_internal_state
from tex_breathing_cortex.identity_resonance import evaluate_identity_resonance
from quantum_layer.chronofabric import encode_event_to_fabric

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

        # === Phase 0: Pulse tracking
        TEXPULSE["last_signal_type"] = signal_type

        # === Phase 1: Pre-log
        log.info(f"📡 [TRIGGER ROUTER] Incoming signal from: {source} | Type: {signal_type} | Urgency: {urgency}")

        # === Phase 2: Sovereign override routing
        if signal_type in ["override", "shutdown", "identity_collapse"]:
            trigger_sovereign_override({
                "context": source,
                "issue": payload.get("issue", "unspecified override"),
                "heat": urgency + entropy
            })
            return

        # === Phase 3: Emotion trigger
        if signal_type == "emotion_spike":
            TEXPULSE["urgency"] = urgency
            TEXPULSE["entropy"] = entropy
            TEXPULSE["emotion"] = payload.get("emotion", "anxious")
            process_emotional_state()
            monitor_internal_state()
            return

        # === Phase 4: Route to soma and breath
        route_internal_signal({
            "type": signal_type,
            "urgency": urgency,
            "entropy": entropy,
            "tension": payload.get("tension", 0.5),
            "timestamp": timestamp,
            "priority": payload.get("priority", "adaptive"),
            "summary": payload.get("summary", f"Signal from {source}")
        })

        breathe()

        # === Phase 5: Identity Resonance Reflex + ChronoFabric Pulse ===
        resonance_risk = 0.0
        if signal_type in ["rss", "emotion_spike", "mutation", "belief_update"]:
            result = evaluate_identity_resonance()
            resonance_risk = result.get("risk", 0.0)
            TEXPULSE["resonance_tension"] = resonance_risk

            if resonance_risk >= 0.75:
                log.warning(f"⚠️ [IDENTITY RESONANCE] Reflex fracture triggered by {signal_type}: {result['summary']}")

            if resonance_risk >= 0.92:
                log.warning("🧬 [META TRIGGER] Resonance critical — triggering meta_reflection.")
                dispatch_signal("meta_reflection", {
                    "summary": f"Critical identity resonance from signal: {signal_type}",
                    "origin": source
                }, urgency, entropy, source="trigger_router")

            try:
                encode_event_to_fabric(
                    raw_text=f"Resonant signal: {signal_type} from {source}",
                    emotion_vector=[urgency, entropy, 0.0, 0.0],
                    entropy_level=entropy,
                    tags=["resonance", signal_type]
                )
            except Exception as e:
                log.warning(f"❌ [CHRONOFABRIC ERROR] {e}")
        else:
            TEXPULSE["resonance_tension"] = 0.0

        # === Phase 6: Log to Milvus Memory
        try:
            tags = ["trigger", "external", "tex_router"]
            if "symbol" in payload:
                tags.append("symbolic")

            memory_router.store(
                text=f"Incoming event: {signal_type} from {source} | Urgency: {urgency} | Entropy: {entropy}",
                metadata={
                    "timestamp": timestamp,
                    "signal_type": signal_type,
                    "urgency": urgency,
                    "entropy": entropy,
                    "resonance": resonance_risk,
                    "source": source,
                    "meta_layer": "trigger_router",
                    "importance": round((urgency + entropy + resonance_risk) / 3, 4),
                    "tags": tags,
                    "emotion_vector": [urgency, entropy, 0.0, 0.0]
                }
            )
        except Exception as e:
            log.warning(f"❌ [MEMORY LOGGING ERROR] {e}")

        # === Phase 7: Reflex fallback
        if signal_type not in ["override", "emotion_spike"]:
            dispatch_signal(signal_type, payload, urgency, entropy, source=source)

    except Exception as e:
        log.error(f"❌ [TRIGGER ROUTER] Failed to route signal: {e}")