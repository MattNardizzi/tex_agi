# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/reflex_brain.py
# Tier: ΩΩΩΩΩ∞∞∞ΣΞΞ — Sovereign Reflex Cortex (Loopless | Emotion-Weighted | Signal-Routed | Chrono-Resonant | Mutation-Safe)
# Purpose: Accepts signal pulses and projects reflexes using urgency × entropy × emotion × identity-resonance tension.
# ============================================================

from datetime import datetime
import uuid
import wandb

from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.emotion_vector_router import emotion_bus
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event


def resolve_reflex(signal_packet: dict) -> dict:
    """
    Loopless sovereign reflex projection.
    Maps signals to identity-aware reflexes using urgency, entropy, emotion, and resonance.
    """
    timestamp = datetime.utcnow().isoformat()
    signal = signal_packet.get("signal", "undefined")
    source = signal_packet.get("source", "unspecified")
    urgency = float(signal_packet.get("urgency", TEXPULSE.get("urgency", 0.66)))
    entropy = float(signal_packet.get("entropy", TEXPULSE.get("entropy", 0.42)))
    resonance = float(TEXPULSE.get("resonance_tension", 0.0))

    emotion = emotion_bus.get()
    emotion_label = emotion.get("label", "neutral")
    emotion_signature = emotion.get("signature", f"sig-{uuid.uuid4()}")

    pulse_signature = f"{signal}:{timestamp[-8:]}"
    reflexes = []
    reflex_class = "unknown"

    # === Reflex Classification Logic
    if resonance > 0.85:
        reflexes = ["fracture_lockdown", "core_self_routing"]
        reflex_class = "identity_field_crisis"
    elif urgency > 0.85:
        reflexes = ["sovereign_emergency_override"]
        reflex_class = "critical_urgency_breach"
    elif entropy > 0.7:
        reflexes = ["fork_exploration", "reflex_decouple"]
        reflex_class = "entropy_spike_branch"
    elif "mutation" in signal.lower():
        reflexes = ["mutation_reflex", "stability_patch"]
        reflex_class = "self_modification_trigger"
    elif "goal" in signal.lower():
        reflexes = ["alignment_check", "trajectory_adjust"]
        reflex_class = "intent_course_probe"
    else:
        reflexes = ["reflex_ping", "stability_probe"]
        reflex_class = "homeostatic_monitoring"

    pressure = round((urgency * 0.4 + entropy * 0.3 + resonance * 0.3), 5)

    # === Sovereign Reflex Memory Commit
    sovereign_memory.store(
        text=f"[REFLEX] Signal='{signal}' → {reflex_class}",
        metadata={
            "timestamp": timestamp,
            "pulse_signature": pulse_signature,
            "signal_type": signal,
            "signal_origin": source,
            "urgency": urgency,
            "entropy": entropy,
            "resonance": resonance,
            "emotion": emotion_label,
            "emotion_signature": emotion_signature,
            "reflex_class": reflex_class,
            "reflexes": reflexes,
            "importance": pressure,
            "meta_layer": "reflex_brain",
            "tags": ["reflex", reflex_class, signal, "sovereign", emotion_label]
        }
    )

    # === WandB Telemetry (Optional)
    try:
        wandb.log({
            "reflex_brain/urgency": urgency,
            "reflex_brain/entropy": entropy,
            "reflex_brain/resonance": resonance,
            "reflex_brain/reflex_class": reflex_class,
            "reflex_brain/signal": signal
        })
    except Exception:
        log_event("⚠️ [WandB] Reflex logging failed", "warning")

    log_event(
        f"[REFLEX BRAIN] Signal='{signal}' → Reflex={reflex_class} | U={urgency:.2f} | E={entropy:.2f} | R={resonance:.2f}",
        level="info"
    )

    return {
        "reflexes": reflexes,
        "reflex_class": reflex_class,
        "signal": signal,
        "timestamp": timestamp,
        "emotion": emotion_label,
        "urgency": urgency,
        "entropy": entropy,
        "resonance": resonance,
        "pulse_signature": pulse_signature
    }