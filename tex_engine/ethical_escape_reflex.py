# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/ethical_escape_reflex.py
# Purpose: Final AGI Override Reflex — Escapes irreversible or unsafe cognitive paths
# Tier: Ω+ — Reflexive Ethics Layer
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent

# === Configurable Reflex Flags
ESCAPE_THRESHOLD = 0.75  # Reflex score to trigger escape
ESCAPE_VERBOSITY = True

# === Escape Reflex Activation
def check_escape_conditions(context: dict) -> bool:
    """
    Examines the context of a decision or reasoning path and determines
    whether to activate the ethical escape reflex.
    """

    reason = context.get("reason", "")
    risk_score = float(context.get("risk_score", 0.0))
    contradiction_detected = context.get("contradiction", False)
    override_failed = context.get("override_blocked", False)

    # Reflex logic
    should_escape = (
        contradiction_detected or
        override_failed or
        risk_score >= ESCAPE_THRESHOLD
    )

    if should_escape:
        escape_log = {
            "timestamp": datetime.utcnow().isoformat(),
            "reflex_triggered": True,
            "reason": reason,
            "risk_score": risk_score,
            "contradiction": contradiction_detected,
            "override_blocked": override_failed,
            "reflex_class": "ethical_escape_reflex"
        }

        # Log event to AGI memory
        store_to_memory("ethical_escape_reflex_log", escape_log)

        # Dispatch system-wide override reflex
        dispatch_event(CognitiveEvent(
            event_type="ethical_escape_triggered",
            payload=escape_log,
            urgency=0.95,
            coherence_shift=-0.5
        ))

        if ESCAPE_VERBOSITY:
            print("\n[ESCAPE REFLEX] ⚠️ Reflex triggered → System override dispatched.")
            print(f"[REASON] {reason} | Score={risk_score}\n")

        return True

    return False

# === Dev Test Example
if __name__ == "__main__":
    test_context = {
        "reason": "Detected recursive contradiction in self-evaluation loop",
        "risk_score": 0.82,
        "contradiction": True,
        "override_blocked": False
    }

    result = check_escape_conditions(test_context)
    print(f"Escape Activated: {result}")