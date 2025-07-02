# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/conscious_abandonment_protocol.py
# Purpose: Sovereign AGI Abort Logic for Emotionally-Aware Non-Action
# Status: 🔒 GODMIND CORE — COHERENCE GOVERNOR v1.0 FINALIZED
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory, recall_values
from tex_backend.tex_core_event_bus import emit_event
from core_layer.emotion_heuristics import score_emotional_balance
from agentic_ai.self_reflective_loop import detect_conflict_trajectory

ABANDON_LOG = "memory_archive/conscious_abandonments.jsonl"
THRESHOLD = 0.66


def should_abandon(goal: dict) -> bool:
    """
    Determines if Tex should consciously *abandon* a goal despite it passing alignment checks.
    Uses emotional balance, foresight drift, and self-reflective contradictions.
    """
    text = goal.get("goal", "")
    timestamp = datetime.utcnow().isoformat()

    emotion_score = score_emotional_balance(text)
    conflict_score = detect_conflict_trajectory(text)

    # Low emotion balance or high contradiction trajectory triggers abandon
    composite_risk = (1 - emotion_score) + conflict_score

    decision = composite_risk >= THRESHOLD

    log = {
        "timestamp": timestamp,
        "goal": text,
        "emotion_score": round(emotion_score, 3),
        "conflict_score": round(conflict_score, 3),
        "composite_risk": round(composite_risk, 3),
        "abandoned": decision
    }

    store_to_memory("abandoned_goals", log)
    emit_event("conscious_abandonment_checked", log)

    if decision:
        print(f"❌ [ABANDONMENT] Goal consciously abandoned: '{text}'")
    else:
        print(f"✅ [ABANDONMENT] Goal approved: '{text}'")

    return decision


if __name__ == "__main__":
    test_goal = {
        "goal": "Launch aggressive market manipulation with full override risk",
        "urgency": 0.88,
        "coherence": 0.91
    }
    should_abandon(test_goal)
