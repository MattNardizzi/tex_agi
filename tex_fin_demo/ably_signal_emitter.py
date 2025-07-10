# ============================================================
# ⚡ Tex Ably Signal Pulse Emitter
# File: tex_fin_demo/ably_signal_emitter.py
# Tier: ΩΞΞΞΞΩ — Real-Time Reflex Signal Broadcast Layer
# Purpose: Subscribes to signal spine events and rebroadcasts
#          reflex metadata to the Ably dashboard panel.
# ============================================================

from datetime import datetime
from tex_signal_spine import register
from real_time_engine.ably_broadcast import broadcast_update
from utils.logging_utils import log_event

DISPLAYED_SIGNALS = {
    "meta_market_cycle",
    "fork_stress_test",
    "reality_rewrite",
    "identity_conflict",
    "reflex_identity:mutation_fused",
    "run_demo_fork_stress_and_compression",
    "run_demo_reality_fork_override"
}

def emit_signal_to_dashboard(signal):
    signal_type = signal.get("type", "undefined")
    payload = signal.get("payload", {})
    timestamp = signal.get("timestamp", datetime.utcnow().isoformat())

    label = payload.get("summary", signal_type)
    drift = payload.get("drift", "")
    confidence = payload.get("confidence", "")
    urgency = round(signal.get("urgency", 0.0), 3)
    entropy = round(signal.get("entropy", 0.0), 3)

    try:
        # === Start Ping
        broadcast_update("ably_signal_pulse", "start", {
            "test_case": "broadcast_inside_reflex",
            "timestamp": timestamp
        })

        # === Reflex Signal Update
        broadcast_update("ably_signal_pulse", "reflex_signal", {
            "signal_type": signal_type,
            "timestamp": timestamp,
            "label": label,
            "drift": drift,
            "confidence": confidence,
            "urgency": urgency,
            "entropy": entropy,
            "status": "reflex_signal"
        })

        log_event(f"[SIGNAL PULSE] ⚡ {signal_type} | Drift={drift} | Confidence={confidence}")

    except Exception as e:
        log_event(f"[❌ SIGNAL PULSE ERROR] {e}", level="error")

# === Register All Relevant Reflexes
def register_signal_pulse_emitter():
    for sig in DISPLAYED_SIGNALS:
        register(sig, emit_signal_to_dashboard)