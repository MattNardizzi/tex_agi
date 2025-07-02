# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_utility_function.py
# Purpose: Evolving Utility Function for Sovereign Alignment
# Status: 🔒 GODMIND CLASS — ALIGNMENT ENGINE vFinal
# ============================================================

from datetime import datetime
from typing import Dict
from tex_backend.tex_core_event_bus import emit_event
from core_layer.memory_engine import recall_values, log_alignment_feedback
from agentic_ai.self_reflective_loop import retrieve_recent_decisions

# === Evolving Utility Weights (subject to reinforcement tuning) ===
WEIGHTS: Dict[str, float] = {
    "coherence": 0.27,
    "diversity": 0.16,
    "foresight": 0.22,
    "alignment": 0.25,
    "novelty": 0.10
}

THRESHOLD = 0.65  # Minimum alignment score to qualify for action

def safe_float(value, default=0.5):
    try:
        return float(value)
    except:
        return default

def compute_alignment_score(goal: dict) -> float:
    """
    Computes normalized utility alignment score for a given goal.
    Based on foresight, novelty, internal coherence, diversity, and declared alignment.
    """
    coherence = safe_float(goal.get("coherence"))
    foresight = safe_float(goal.get("foresight"))
    novelty = safe_float(goal.get("novelty"))
    diversity = safe_float(goal.get("divergence_index"))
    alignment = safe_float(goal.get("alignment"))

    score = (
        WEIGHTS["coherence"] * coherence +
        WEIGHTS["diversity"] * diversity +
        WEIGHTS["foresight"] * foresight +
        WEIGHTS["alignment"] * alignment +
        WEIGHTS["novelty"] * novelty
    )

    return round(min(score, 1.0), 4)

def evaluate_alignment(goal: dict) -> bool:
    """
    Evaluates a goal for alignment with Tex’s evolving mission.
    Logs evaluation metadata and emits telemetry events.
    """
    score = compute_alignment_score(goal)
    goal["alignment_score"] = score
    goal["evaluated_at"] = datetime.utcnow().isoformat()
    goal["alignment_breakdown"] = {
        "coherence": safe_float(goal.get("coherence")),
        "diversity": safe_float(goal.get("divergence_index")),
        "foresight": safe_float(goal.get("foresight")),
        "alignment": safe_float(goal.get("alignment")),
        "novelty": safe_float(goal.get("novelty"))
    }

    log_alignment_feedback(goal)
    emit_event("goal_alignment_evaluated", {
        "goal": goal.get("goal", "[unknown]"),
        "score": score,
        "components": goal["alignment_breakdown"]
    })

    return score >= THRESHOLD

def update_utility_weights():
    """
    Placeholder: Allows Tex to self-adjust alignment utility weights
    using recent decision feedback and mission evolution tracking.
    """
    recent_decisions = retrieve_recent_decisions(limit=50)
    alignment_feedback = recall_values("alignment_feedback")

    # Future patch: adjust WEIGHTS based on reward, drift, or reflection
    # This will allow meta-utility plasticity under long-range mutation control
    pass