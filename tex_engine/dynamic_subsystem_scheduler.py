"""
Ω-tier Module: dynamic_subsystem_scheduler.py
Author: Sovereign Cognition / Tex
Purpose: Schedules subsystem activation based on urgency, memory drift, emotional volatility, contradiction, and foresight confidence.
"""

import time
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent

# === Global thresholds (can be dynamically updated by Tex later)
COHERENCE_THRESHOLD = 0.65
URGENCY_SPIKE = 0.85
DRIFT_INTERVAL_SECONDS = 90
OVERRIDE_CONFIDENCE_THRESHOLD = 0.4

# === Internal timing map ===
last_trigger_times = {
    "memory": 0,
    "reflex": 0,
    "sovereign_override": 0,
    "breathing": 0,
    "coherence": 0,
    "pulse": 0
}

def pulse_scheduler(cycle: int, emotion: str, urgency: float, coherence: float, last_drift: float):
    now = time.time()

    # === 🧠 Trigger memory threading if drift threshold passed ===
    if now - last_drift > DRIFT_INTERVAL_SECONDS:
        dispatch_event(CognitiveEvent("memory_drift", {"cycle": cycle}))
        last_trigger_times["memory"] = now

    # === 🛡 Trigger sovereign override reflex if coherence fails ===
    if coherence < OVERRIDE_CONFIDENCE_THRESHOLD:
        dispatch_event(CognitiveEvent("override_trigger", {
            "cycle": cycle,
            "coherence": coherence
        }))
        last_trigger_times["sovereign_override"] = now

    # === 🔄 Coherence degradation trigger
    if coherence < COHERENCE_THRESHOLD:
        dispatch_event(CognitiveEvent("coherence_drop", {
            "cycle": cycle,
            "coherence": coherence
        }))
        last_trigger_times["coherence"] = now

    # === ❤️ Emotional surge reflex (e.g. greed, panic)
    if urgency > URGENCY_SPIKE:
        dispatch_event(CognitiveEvent("emotional_spike", {
            "emotion": emotion,
            "cycle": cycle
        }, urgency=urgency))
        last_trigger_times["reflex"] = now

    # === 🫁 Breathing tick every 10s (pulse event)
    if now - last_trigger_times["pulse"] > 10:
        dispatch_event(CognitiveEvent("pulse_tick", {"cycle": cycle}))
        last_trigger_times["pulse"] = now

    return now  # Used to update drift tracking in main orchestrator