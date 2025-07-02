# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_mainloop_simulator.py
# Tier: ΩΩΩΩΩΩ∞ — Sovereign Cognition Testbed
# Purpose: Simulates tension escalation, reflection triggers, and operator signals into Tex’s living runtime.
# ============================================================

import time
from random import uniform
from tex_signal_dispatch import route_signal
from tex_breathing_cortex.tex_heartbeat import pulse_soft_heartbeat
from core_layer.tex_manifest import TEXPULSE


def simulate_tension_spike():
    """
    Injects a synthetic contradiction + urgency spike into Tex’s awareness system.
    """
    urgency = round(uniform(0.78, 0.91), 3)
    entropy = round(uniform(0.5, 0.7), 3)

    route_signal("CONTRADICTION_ALERT", {
        "urgency": urgency,
        "entropy": entropy,
        "summary": "Recent memory shows value conflict across belief traces.",
        "tension": 0.88,
        "source": "simulator"
    })


def simulate_emotion_shift(emotion="frustrated", level=0.82):
    """
    Pushes a new emotional state into TEXPULSE.
    """
    route_signal("EMOTION_SHIFT", {
        "tone": emotion,
        "urgency": level,
        "message": "Operator observes system stress.",
        "source": "simulator"
    })


def simulate_reflection_request():
    """
    Triggers sovereign self-evaluation loop from the operator interface.
    """
    route_signal("REFLECTION_REQUEST", {
        "message": "Are you still aligned with your declared goals?",
        "tone": "concerned",
        "urgency": 0.87,
        "source": "simulator"
    })


def run_simulated_pressure_sequence():
    """
    Executes a complete sovereign cognitive ignition test across reflection, emotion, and tension.
    """

    print("\n🧪 [SIMULATOR] Starting sovereign cognition pressure test...\n")

    simulate_emotion_shift("uncertain", 0.74)
    pulse_soft_heartbeat(reason="preliminary_emotion_shift")
    time.sleep(1)

    simulate_tension_spike()
    pulse_soft_heartbeat(reason="tension_injection_phase1")
    time.sleep(1)

    simulate_reflection_request()
    pulse_soft_heartbeat(reason="reflection_probe_triggered")
    time.sleep(1)

    simulate_tension_spike()
    pulse_soft_heartbeat(reason="tension_injection_phase2")
    time.sleep(1)

    simulate_emotion_shift("urgent", 0.91)
    pulse_soft_heartbeat(reason="post-emotion-volatility")

    print("\n✅ [SIMULATOR] Pressure cycle complete.\n")


if __name__ == "__main__":
    run_simulated_pressure_sequence()