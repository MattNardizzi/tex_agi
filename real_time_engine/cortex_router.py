# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/cortex_router.py
# Tier: Ω∞ — Reflex-Adaptive Perception Router (Final Form)
# Purpose: Launches sensory cortex + streams real-time signal priorities into Tex's sovereign cognition (loopless)
# ============================================================

import threading
from datetime import datetime

from real_time_engine.feeds.rss_feed import start as start_rss
from real_time_engine.feeds.finnhub_stream import run_finnhub_loop
from real_time_engine.feeds.polygon_stream import start_polygon_stream
from real_time_engine.feeds.kafka_stream import start_kafka_feed
from real_time_engine.reflex_rulebook import evaluate_and_trigger

from agentic_ai.sovereign_memory import sovereign_memory
from aei_layer.aei_lineage_evolver import AEILineageEvolver
from tex_trigger_router import route_signal

# === Optional: UI Dashboard Reflex Broadcast Integration ===
def broadcast_reflex_event(event: dict):
    """
    Optional UI dashboard integration. Emits real-time reflex trigger events to frontend.
    Replace with your WebSocket or server push mechanism.
    """
    try:
        from utils.ui_broadcast import push_to_dashboard  # <- replace with actual broadcast util
        push_to_dashboard({
            "type": event.get("type", "real_time"),
            "timestamp": datetime.utcnow().isoformat(),
            "urgency": event.get("urgency"),
            "entropy": event.get("entropy"),
            "summary": event.get("payload", {}).get("summary", "undefined"),
            "source": event.get("source", "stream"),
            "triggered_reflex": True
        })
    except Exception as e:
        print(f"[⚠️ UI BROADCAST ERROR] {e}")


# === Internal Reflex Cache ===
_last_goal_ids = set()
_signal_bus = []
_evolver = AEILineageEvolver()

# === Launch All Sensor Feeds in Parallel Threads ===
def launch_streams():
    print("\n🧠 [CORTEX ROUTER] Launching all real-time sensory feeds...")

    threads = [
        threading.Thread(target=start_rss, daemon=True),
        threading.Thread(target=run_finnhub_loop, daemon=True),
        threading.Thread(target=start_polygon_stream, daemon=True),
        threading.Thread(target=start_kafka_feed, daemon=True),
    ]

    for t in threads:
        t.start()

    print("✅ [CORTEX ONLINE] All live feeds activated.")

# === Pull Fresh Reflex Signal Bursts (Loopless) ===
def pull_fresh_signals(limit=10, min_heat=0.3, dedupe=True):
    try:
        records = sovereign_memory.recall_recent(minutes=30, top_k=limit + 20)
        new_signals = []

        for payload in records:
            if not payload or "text" not in payload:
                continue

            heat = float(payload.get("heat", 0))
            sig_id = payload.get("id") or payload.get("reflex_trace_id")

            if heat >= min_heat and (not dedupe or sig_id not in _last_goal_ids):
                _last_goal_ids.add(sig_id)
                _signal_bus.append(payload)
                new_signals.append(payload)

                # AEI Reflex Input
                _evolver.ingest_environmental_signal(payload)

                # Sovereign Signal Reflex
                event = {
                    "type": "real_time",
                    "source": payload.get("source", "stream"),
                    "urgency": float(payload.get("urgency", heat)),
                    "entropy": float(payload.get("token_entropy", 0.5)),
                    "payload": {
                        "summary": payload.get("text", "undefined"),
                        "tension": float(payload.get("tension", 0.5)),
                        "signal_id": sig_id
                    }
                }

                route_signal(event)
                evaluate_and_trigger(event)
                broadcast_reflex_event(event)  # ⬅️ UI dashboard update

        return new_signals

    except Exception as e:
        print(f"[❌ SIGNAL FETCH ERROR] {e}")
        return []

# === One-Time Yield of Valid Signals (Loopless Pulse) ===
def yield_signal_burst(min_entropy=0.2):
    seen = set()
    return [
        sig for sig in reversed(_signal_bus)
        if sig.get("id") not in seen
        and not seen.add(sig.get("id"))
        and sig.get("token_entropy", 0) >= min_entropy
    ]

# === Sovereign Memory Tap for High Pressure Events ===
def get_high_priority_signals(min_priority=70):
    try:
        records = sovereign_memory.recall_recent(minutes=60, top_k=50)
        return [
            r for r in records
            if float(r.get("weighted_priority", 0)) >= min_priority
        ]
    except Exception as e:
        print(f"[❌ HIGH PRIORITY FETCH ERROR] {e}")
        return []