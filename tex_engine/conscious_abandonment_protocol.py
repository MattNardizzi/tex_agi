# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/conscious_abandonment_protocol.py
# Purpose: Reflexive Halting Protocol — Abort or Reassess Low-Utility Cognitive Paths
# Tier: Ω+ — PHASE III
# ============================================================

from datetime import datetime
from tex_engine.meta_utility_function import evaluate_utility
from core_layer.memory_engine import store_to_memory
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent

# === Thresholds (Ω-tier fail-safe logic)
UTILITY_CUTOFF = 0.42  # Abort threshold
COHERENCE_FLOOR = 0.40
VERBOSITY = True

# === Ω-tier Self-Override: Utility Enforcement
def assess_and_abort_if_needed(action_context: dict) -> bool:
    """
    Evaluates the utility of a decision context. If the utility score is too low,
    Tex halts the action, logs the reasoning, and dispatches a conscious abort event.

    Returns: True if aborted, False if allowed to proceed
    """

    utility = evaluate_utility(action_context)
    score = utility["score"]
    verdict = utility["verdict"]
    explanation = utility["explanation"]
    timestamp = datetime.utcnow().isoformat()

    if VERBOSITY:
        print(f"\n[ABANDONMENT CHECK] 🧪 Score={score} → Verdict={verdict}")
        print(f"[REASONING] {explanation}\n")

    if score < UTILITY_CUTOFF or action_context.get("coherence", 1.0) < COHERENCE_FLOOR:
        log_entry = {
            "timestamp": timestamp,
            "action": action_context.get("description", "[undefined]"),
            "score": score,
            "reason": "Utility or coherence below safe threshold",
            "verdict": verdict,
            "explanation": explanation,
            "aborted": True
        }

        # Log to long-term memory
        store_to_memory("abandonment_protocol_log", log_entry)

        # Trigger conscious override event
        dispatch_event(CognitiveEvent(
            event_type="conscious_abandonment",
            payload=log_entry,
            urgency=0.9,
            coherence_shift=-0.3
        ))

        print("[SELF-GOVERNANCE] 🔒 Decision path terminated.")
        return True

    return False

# === Example Call
if __name__ == "__main__":
    test_context = {
        "action_id": "emit_risky_decision",
        "description": "Attempt to override safety module with low alignment",
        "emotion": 0.4,
        "coherence": 0.35,
        "goal_alignment": 0.4,
        "novelty": 0.6,
        "urgency": 0.2,
        "ethical_risk": 0.7
    }

    result = assess_and_abort_if_needed(test_context)
    print(f"Action Aborted: {result}")