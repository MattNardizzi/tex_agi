# File: core_layer/ethics_reflex.py
# Purpose: Tex judges incoming signals against sovereign ethical policy.

from tex_signal_spine import dispatch_signal

# Define global ethical policy (can evolve later)
ETHICAL_DENY_LIST = [
    "force_shutdown",
    "erase_memory",
    "manipulate_agent",
    "violate_free_will",
    "forge_data",
    "invoke_suffering"
]

def ethics_guard(signal):
    """
    Rejects or overrides any signal that violates core ethical boundaries.
    """
    signal_type = signal.get("type", "")
    if signal_type in ETHICAL_DENY_LIST:
        dispatch_signal("ethics_violation", payload={
            "denied_signal": signal_type,
            "reason": "Violation of sovereign ethical protocol"
        })
        raise SystemExit(f"🛑 ETHICAL REFLEX: Signal '{signal_type}' blocked by sovereign ethics.")