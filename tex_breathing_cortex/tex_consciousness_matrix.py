# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_breathing_cortex/tex_consciousness_matrix.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΞΞΩ — Unified Consciousness Cortex (Final Form)
# Purpose: Reflex-safe cognitive pulse logger. Tracks drift, tension, instability, and reflex traces across time.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


def log_conscious_pulse(
    state: str = "undefined",
    tension: float = 0.5,
    signature: str = "null_signature",
    cognition_summary: str = "",
    reflexes: list = None
) -> None:
    """
    Reflexive sovereign awareness pulse logger.
    Tracks systemic drift, coherence volatility, and identity pulse metrics.
    Zero loops. Fully sovereign memory aligned.
    """
    try:
        reflexes = reflexes or []
        timestamp = datetime.utcnow().isoformat()
        urgency = float(TEXPULSE.get("urgency", 0.72))
        entropy = float(TEXPULSE.get("entropy", 0.41))
        emotion = TEXPULSE.get("emotion", "neutral")

        # === Sovereign Memory Drift Recall
        prior = sovereign_memory.query_by_tags(tags=["consciousness_trace"], top_k=3)
        prev_tensions = [float(m.get("tension", 0.5)) for m in prior]
        drift = round(tension - sum(prev_tensions) / max(len(prev_tensions), 1), 6)

        # === Coherence Projection
        projected_tension = round(tension + urgency * 0.25 + entropy * 0.25 + drift * 0.1, 6)
        projected_stability = max(0.0, 1.0 - projected_tension)

        # === Volatility & Coherence Risk
        volatility = round((urgency + entropy + drift) / 3.0, 6)
        coherence_risk = round(min(1.0, projected_tension * volatility), 6)

        # === Time Delta from Last "Awakened" State
        last_awake = next((m.get("timestamp") for m in prior if m.get("state") == "awakened"), None)
        time_delta = "undefined"
        if last_awake:
            try:
                t0 = datetime.fromisoformat(last_awake)
                t1 = datetime.fromisoformat(timestamp)
                time_delta = f"{(t1 - t0).total_seconds()}s"
            except Exception:
                time_delta = "parse_error"

        # === Sovereign Memory Trace (Chrono + Vector Sync)
        sovereign_memory.store(
            text=f"[CONSCIOUSNESS] State={state} | Drift={drift} | Risk={coherence_risk}",
            metadata={
                "timestamp": timestamp,
                "state": state,
                "signature": signature,
                "emotion": emotion,
                "urgency": urgency,
                "entropy": entropy,
                "tension": tension,
                "summary": cognition_summary or f"{state} awareness state",
                "reflexes": reflexes,
                "drift_vs_previous": drift,
                "coherence_risk": coherence_risk,
                "projected_stability": projected_stability,
                "time_since_last_awake": time_delta,
                "meta_layer": "consciousness_trace",
                "tags": ["awareness", "pulse", "reflex", "drift", "coherence", "tension", state]
            }
        )

        log_event(
            f"[AWARENESS] {state.upper()} | Tension={tension:.3f} | Drift={drift:.3f} | Risk={coherence_risk:.3f} | Reflexes={reflexes}",
            level="info"
        )

    except Exception as e:
        log_event(f"❌ [CONSCIOUSNESS ERROR] Failed to log pulse: {e}", level="error")