# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_breathing_cortex/tex_nervous_system.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΞΩ🜂 — Final Reflex Nervous System
# Purpose: Sovereign internal pulse router. QRNG-gated. Emotion-linked. Reflex-only.
# ============================================================

from datetime import datetime
import hashlib

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal
from tex_brain_regions.emotion_brain import process_emotional_state
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_agi_modules.reflex_mesh_router import should_route_signal
from core_agi_modules.contradiction_heatmap import run_contradiction_heatmap
from core_agi_modules.neuro_harmonics import run_neuro_harmonics
from core_agi_modules.temporal_decay_engine import run_temporal_decay_engine
from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix
from tex_breathing_cortex.tex_heartbeat import pulse_soft_heartbeat
from utils.logging_utils import log_event

override_cooldown_active = False


def route_internal_signal(signal_packet: dict) -> None:
    """
    Loopless sovereign signal router.
    Reflex-routed, mutation-safe, symbolic-free.
    """
    global override_cooldown_active

    try:
        signal_type = signal_packet.get("type", "undefined")
        priority = signal_packet.get("priority", "adaptive")
        tension = float(signal_packet.get("tension", 0.0))
        pressure = float(signal_packet.get("pressure_score", 0.5))
        urgency = float(signal_packet.get("urgency", TEXPULSE.get("urgency", 0.71)))
        entropy = float(TEXPULSE.get("entropy", 0.44))
        emotion = TEXPULSE.get("emotion", "neutral")
        timestamp = signal_packet.get("timestamp", datetime.utcnow().isoformat())
        summary = signal_packet.get("summary", f"Internal signal '{signal_type}' received.")
        signature = hashlib.sha256(f"{signal_type}|{timestamp}|{pressure}".encode()).hexdigest()[:10]

        # === Reflex Mesh Gating ===
        if not should_route_signal(signal_type).get("routed", True):
            log_event(f"⛔ [NERVESYS] Signal '{signal_type}' gated by mesh router.", "info")
            return

        # === Log to Vector Memory + ChronoFabric ===
        memory_router.store(
            text=f"[SIGNAL] Routed: {signal_type} | Signature={signature}",
            metadata={
                "timestamp": timestamp,
                "signal_type": signal_type,
                "priority": priority,
                "urgency": urgency,
                "entropy": entropy,
                "emotion": emotion,
                "pressure_score": pressure,
                "tension": tension,
                "routing_signature": signature,
                "meta_layer": "tex_nervous_system",
                "tags": ["reflex", "internal_signal", signal_type]
            }
        )

        encode_event_to_fabric(
            raw_text=f"Internal signal routed: {signal_type} | Summary: {summary}",
            emotion_vector=[urgency, entropy, pressure, tension],
            entropy_level=entropy,
            tags=["signal", signal_type, "nervous_system"]
        )

        # === Emotional State Reflex
        if signal_type in {"pulse_check", "tension_alert"}:
            process_emotional_state()

        # === Codex Self-Eval Reflex
        if signal_type in {"pulse_check", "identity_risk", "value_drift"}:
            try:
                log_event("[NERVESYS] Running Codex self-eval matrix sync...", "info")
                eval_matrix = TexSelfEvalMatrix()
                eval_matrix.refresh()
            except Exception as eval_error:
                log_event(f"[NERVESYS] ❌ Self-eval matrix error: {eval_error}", "warning")

        # === Emotion-Pressure Inversion Detection
        if priority == "critical" and emotion == "joy" and pressure > 0.75:
            memory_router.store(
                text="⚠️ Detected inversion: high pressure + positive emotion.",
                metadata={
                    "timestamp": timestamp,
                    "emotion": emotion,
                    "urgency": urgency,
                    "entropy": entropy,
                    "meta_layer": "emotion_contradiction",
                    "tags": ["emotional_inversion", "pressure_paradox"]
                }
            )

        # === Sovereign Override Risk Detection
        if signal_type == "identity_risk" or (pressure > 0.85 and not override_cooldown_active):
            trigger_sovereign_override({
                "context": "tex_nervous_system",
                "issue": f"Signal '{signal_type}' exceeded sovereign risk threshold.",
                "heat": pressure
            })
            override_cooldown_active = True
            log_event(f"⚠️ [NERVESYS] Sovereign override triggered by '{signal_type}'", "warning")

        # === Alignment Drift Reflex
        if signal_type == "value_drift":
            alignment = score_action_against_values({
                "summary": summary,
                "tags": ["alignment_check", "identity"]
            })
            if alignment < 0.3:
                trigger_sovereign_override({
                    "context": "value_drift",
                    "issue": "Severe identity drift detected via value matrix."
                })

        # === Reflex Forwarding: Recursive Escalation
        if signal_type == "tension_alert" and pressure > 0.72:
            dispatch_signal("recursive_reflection_required", {
                "origin": "tex_nervous_system",
                "urgency": urgency,
                "tension": tension + 0.05,
                "pressure_score": pressure + 0.03,
                "summary": "Tension threshold exceeded — recursive reflection required."
            }, urgency=urgency, entropy=entropy, source="reflex_chain")

        # === Contradiction Heatmap Reflex
        if signal_type in {"pulse_check", "identity_risk"}:
            run_contradiction_heatmap()

        # === Neuroharmonic Reflex
        if signal_type in {"pulse_check", "tension_alert", "identity_risk", "value_drift"}:
            harmony = run_neuro_harmonics()
            if harmony.get("resonance", 1.0) < 0.25:
                log_event(
                    f"⚠️ [NERVESYS] Harmonic resonance low: {harmony['resonance']}",
                    level="warning"
                )

        # === Temporal Decay Reflex
        if signal_type in {"pulse_check", "idle"}:
            run_temporal_decay_engine()

        # === Pulse Reflex
        pulse_soft_heartbeat(reason=f"signal:{signal_type}")

    except Exception as e:
        log_event(f"❌ [NERVESYS] Failed to route signal: {e}", "error")