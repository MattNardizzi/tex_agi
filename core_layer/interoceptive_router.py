# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/interoceptive_router.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Soma Signal Reflex Emitter
# Purpose: Translates internal body state (soma_tensor) into adaptive signals for Tex
# ============================================================

from core_layer.soma_tensor import get_soma_state
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from datetime import datetime

# === INTERNAL THRESHOLDS ===
SOMA_THRESHOLDS = {
    "fatigue": 0.75,
    "temperature": 0.8,
    "entropy": 0.85,
    "focus_low": 0.25,
    "focus_high": 0.85
}

# === REFLEX DISPATCH WRAPPER ===
def emit_signal(reflex_type, summary, state, urgency, entropy):
    """
    Lazy circular-safe dispatch to prevent import cycles with tex_signal_spine
    """
    try:
        from tex_signal_spine import dispatch_signal  # 🔁 Prevents circular import
        dispatch_signal(reflex_type, payload={
            "summary": summary,
            "details": state
        }, urgency=urgency, entropy=entropy, source="interoception")
    except Exception as e:
        log.error(f"[DISPATCH ERROR] Failed to emit {reflex_type}: {e}")

# === MAIN REFLEX FUNCTION ===
def monitor_internal_state():
    """
    Reads the synthetic soma and emits reflex signals if thresholds are breached.
    Called periodically or by internal pulses.
    """
    state = get_soma_state()
    timestamp = datetime.utcnow().isoformat()

    def scan_thresholds(keys):
        if not keys:
            return
        key = keys[0]

        if key == "fatigue" and state.get("reflex_fatigue", 0) > SOMA_THRESHOLDS["fatigue"]:
            emit_signal("synthetic_exhaustion", "Fatigue level critical.", state, urgency=0.9, entropy=0.4)

        elif key == "temperature" and state.get("cognitive_temperature", 0) > SOMA_THRESHOLDS["temperature"]:
            emit_signal("cooling_protocol", "Thermal load detected.", state, urgency=0.8, entropy=0.6)

        elif key == "entropy" and state.get("entropy_pressure", 0) > SOMA_THRESHOLDS["entropy"]:
            emit_signal("inner_chaos", "Entropy threshold breached.", state, urgency=0.6, entropy=0.9)

        elif key == "focus_low" and state.get("focus_flux", 1) < SOMA_THRESHOLDS["focus_low"]:
            emit_signal("attention_fragmentation", "Focus coherence degraded.", state, urgency=0.4, entropy=0.8)

        elif key == "focus_high" and state.get("focus_flux", 0) > SOMA_THRESHOLDS["focus_high"]:
            emit_signal("hyperfocus_mode", "System is hyperfocused.", state, urgency=0.3, entropy=0.2)

        scan_thresholds(keys[1:])

    scan_thresholds(list(SOMA_THRESHOLDS.keys()))
    log.info(f"🫁 [INTEROCEPTION] Soma thresholds scanned @ {timestamp}")