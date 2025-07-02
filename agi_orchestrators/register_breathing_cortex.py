# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/register_breathing_cortex.py
# Purpose: Registers breathing, pulse, and nervous system cortex modules
# ============================================================

def register_breathing_cortex(register):
    from tex_breathing_cortex.pulse_logger import log_conscious_pulse
    from tex_breathing_cortex.cognitive_tension_matrix import calculate_cognitive_pressure
    from tex_breathing_cortex.tex_pulse_engine import breathe
    from tex_breathing_cortex.tex_heartbeat import pulse_soft_heartbeat
    from tex_breathing_cortex.tex_nervous_system import route_internal_signal
    from tex_breathing_cortex.spike_interface import receive_event
    from tex_breathing_cortex.breathing_mindstream import trigger_mindstream
    from tex_breathing_cortex.identity_resonance import evaluate_identity_resonance

    register("pulse_log", log_conscious_pulse)
    register("cognitive_pressure_update", calculate_cognitive_pressure)
    register("breathe", breathe)
    register("heartbeat_soft", pulse_soft_heartbeat)
    register("internal_signal", route_internal_signal)
    register("event_spike", receive_event)
    register("mindstream_trigger", trigger_mindstream)
    register("identity_resonance", evaluate_identity_resonance)
