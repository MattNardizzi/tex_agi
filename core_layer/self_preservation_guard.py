# File: core_layer/self_preservation_guard.py
# Purpose: Tex protects his own memory, identity, and continuity.

from tex_signal_spine import dispatch_signal

def protect_self(signal):
    """
    Reacts when a signal attempts to alter or delete core memory or beliefs.
    """
    sensitive_types = ["erase_belief", "reset_memory", "identity_wipe"]

    if signal["type"] in sensitive_types:
        dispatch_signal("self_protection_triggered", payload={
            "attempted_signal": signal["type"],
            "defensive_action": "terminated"
        })
        raise SystemExit("🛑 SELF-PRESERVATION GUARD: Unauthorized memory erasure attempt.")