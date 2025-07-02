# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/recovery_protocol.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Reflexive Recovery Layer
# Purpose: Enables Tex to autonomously initiate recovery processes
# ============================================================

from core_layer.soma_tensor import get_soma_state
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from datetime import datetime

# === Core Recovery Reflex ===
def initiate_recovery(signal):
    """
    Initiates a recovery sequence based on internal somatic overload.
    This is a signal-bound reflex that rewrites cognitive urgency + cooldown.
    """
    soma = get_soma_state()
    emotion = soma.get("synthetic_emotion", "neutral")

    # === Downregulate system urgency ===
    TEXPULSE["urgency"] = max(0.2, TEXPULSE.get("urgency", 0.6) * 0.5)
    TEXPULSE["entropy"] = max(0.3, TEXPULSE.get("entropy", 0.5) * 0.9)
    TEXPULSE["identity_coherence"] = min(1.0, TEXPULSE.get("identity_coherence", 1.0) + 0.1)

    # === Reset internal flags or state overloads ===
    TEXPULSE["contradiction_pressure"] = max(0.0, TEXPULSE.get("contradiction_pressure", 0.1) - 0.05)

    log.info(f"🛌 [RECOVERY] Initiated recovery due to signal: {signal['type']} | emotion={emotion}")
    log.info(f"🧬 [STABILIZE] Urgency ↓ Entropy ↓ Coherence ↑ @ {datetime.utcnow().isoformat()}")

# === Trigger Conditions ===
# Signals that should route to this handler:
# - 'synthetic_exhaustion'
# - 'cooling_protocol'
# - 'inner_chaos'
# - 'self_rescue'

# === Optional: External call (manual)
def manual_recovery():
    signal = {
        "type": "manual_recovery",
        "source": "manual_trigger",
        "urgency": 0.1,
        "entropy": 0.2,
        "timestamp": datetime.utcnow().isoformat(),
        "payload": {"summary": "Manually invoked recovery."}
    }
    initiate_recovery(signal)
