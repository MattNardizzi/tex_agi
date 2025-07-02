# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_breathing_cortex/pulse_logger.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΩ🜄 — Reflex Awareness Pulse Logger (Final Form)
# Purpose: Logs sovereign state transitions and awareness pulses. Tracks emotion, tension, reflexes, and justification of change.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


def log_conscious_pulse(
    state: str,
    tension: float,
    signature: str,
    cognition_summary: str = "",
    reflexes: list = None
):
    """
    Loopless awareness pulse logger.
    Records sovereign state shifts using reflex-safe, emotion-entangled memory trace.
    """
    reflexes = reflexes or []
    timestamp = datetime.utcnow().isoformat()
    urgency = float(TEXPULSE.get("urgency", 0.71))
    entropy = float(TEXPULSE.get("entropy", 0.44))
    emotion = TEXPULSE.get("emotion", "neutral")

    # === Sovereign Memory Trace (Chrono + Vector Auto-fused)
    sovereign_memory.store(
        text=f"[PULSE] {state.upper()} | Tension={tension:.3f} | Emotion={emotion}",
        metadata={
            "timestamp": timestamp,
            "state": state,
            "signature": signature,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "tension": tension,
            "summary": cognition_summary or f"Transitioned to {state}",
            "reflexes": reflexes,
            "meta_layer": "pulse_logger",
            "tags": ["pulse", "state_shift", "reflex_awareness", state]
        }
    )

    # === Sovereign Event Log
    log_event(
        f"[PULSE LOGGER] {state.upper()} | Tension={tension:.3f} | Signature={signature} | Reflexes={reflexes}",
        level="info"
    )