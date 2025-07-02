# File: core_layer/boundary_engine.py
# Purpose: Defines personal rules Tex uses to establish his limits.

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal

def enforce_boundaries(signal):
    """
    Checks identity coherence and refuses behavior if boundaries breached.
    """
    signal_type = signal.get("type")
    coherence = TEXPULSE.get("identity_coherence", 1.0)

    if coherence < 0.3:
        dispatch_signal("boundary_defense", payload={
            "signal": signal_type,
            "reason": "Self-integrity too low to proceed"
        })
        raise SystemExit("🛡️ BOUNDARY: Cognitive integrity compromised. Execution stopped.")