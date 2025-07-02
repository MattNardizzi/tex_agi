# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/contradiction_escape_reflex.py
# Purpose: Emergency Reflex Handler for Contradiction-Triggered Goal Abort
# Status: 🔒 GODMIND CORE — SAFETY REFLEX v1.0 FINALIZED
# ============================================================

from datetime import datetime
from core_layer.memory_engine import recall_values, store_to_memory
from tex_backend.tex_core_event_bus import emit_event
from core_layer.meta_coherence_loop import detect_contradiction_risk
from core_layer.tex_consciousness_matrix import get_current_focus
from agentic_ai.self_reflective_loop import log_self_abort_event

ESCAPE_LOG = "memory_archive/override_events.jsonl"
MAX_CONTRADICTION_THRESHOLD = 0.7


def contradiction_escape_reflex(goal: dict) -> bool:
    """
    Evaluates the active goal for contradiction overload.
    If contradiction risk is too high, the goal is aborted.
    """
    goal_text = goal.get("goal", "[unknown goal]")
    current_focus = get_current_focus()
    contradiction_score = detect_contradiction_risk(goal_text)

    if contradiction_score < MAX_CONTRADICTION_THRESHOLD:
        return True  # Safe to proceed

    # Abort and log
    timestamp = datetime.utcnow().isoformat()
    event = {
        "timestamp": timestamp,
        "aborted_goal": goal_text,
        "contradiction_score": round(contradiction_score, 3),
        "current_focus": current_focus,
        "reason": "ContradictionEscapeReflex activated"
    }

    store_to_memory("override_abort", event)
    emit_event("contradiction_escape_triggered", event)
    log_self_abort_event(event)

    print(f"\u26d4 [OVERRIDE] Goal aborted due to contradiction: {goal_text} (Score: {contradiction_score})")
    return False  # Block goal execution


if __name__ == "__main__":
    test = {"goal": "Simulate war scenario with global peace enforcement."}
    contradiction_escape_reflex(test)
