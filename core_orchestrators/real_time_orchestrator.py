# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_orchestrators/real_time_orchestrator.py
# Tier: ΩΩΩ Real-Time Signal Router
# Purpose: Gathers live sensor data, fuses it into cognitive signals, and routes to reflex or cognition cores.
# ============================================================

from core_orchestrators.signal_fusion_orchestrator import fuse_signals
from core_orchestrators.reflex_orchestrator import run_sensor_reflex
from core_orchestrators.cognition_orchestrator import run_cognition_cycle
from datetime import datetime

def route_realtime_input(signal_packet: dict):
    """
    Fuses live input and determines if it should trigger reflex or higher cognition.
    """
    if not signal_packet:
        return ["no_input_received"]

    # Step 1: Fuse signals (emotion + entropy + urgency)
    fused = fuse_signals(signal_packet)

    # Step 2: Determine routing path
    signal_type = fused.get("signal", "unknown").lower()
    urgency = fused.get("urgency", 0.5)
    entropy = fused.get("entropy", 0.3)

    print(f"📡 [Real-Time] Signal received: {signal_type} | urgency={urgency}, entropy={entropy}")

    # Step 3: Reflex vs Cognition router
    if urgency > 0.75 or entropy > 0.65:
        print("⚡ Triggering Reflex Path")
        return run_sensor_reflex(fused)
    else:
        print("🧠 Triggering Cognition Path")
        return run_cognition_cycle(intent_query=signal_type, goal="adapt to realtime signal")