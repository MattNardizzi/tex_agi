# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/reflex_trigger_engine.py
# Tier: ΩΩ∞ΩΩ — Mutation Pressure Evaluator
# Purpose: Determines if reflex mutation conditions are met based on real-time internal tension metrics.
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from tex_brain_regions.meta_brain import evaluate_goal_drift
from utils.logging_utils import log_event

# === Thresholds (can be reflexively rewritten later) ===
MIN_ENTROPY_SHIFT = 0.3
MIN_GOAL_DRIFT = 0.2
MIN_URGENCY = 0.75
MIN_COHERENCE = 0.5
CONTRADICTION_THRESHOLD = 0.8

def get_recent_entropy_shift():
    recent = sovereign_memory.recall_recent(minutes=5, top_k=25)
    values = [float(r.get("entropy", 0.0)) for r in recent if isinstance(r, dict)]
    if len(values) < 2:
        return 0.0
    return abs(values[-1] - values[0])

def get_identity_coherence():
    return float(TEXPULSE.get("identity_coherence", 1.0))

def get_contradiction_pressure():
    return float(TEXPULSE.get("contradiction_pressure", 0.0))

def should_rewrite() -> bool:
    entropy_shift = get_recent_entropy_shift()
    current_goals = TEXPULSE.get("goals", [])
    historical_goals = TEXPULSE.get("historical_goals", [])
    goal_drift = evaluate_goal_drift(current_goals, historical_goals)
    urgency = float(TEXPULSE.get("urgency", 0.0))
    coherence = get_identity_coherence()
    contradiction = get_contradiction_pressure()

    # === Rewrite Conditions ===
    triggered = (
        entropy_shift > MIN_ENTROPY_SHIFT or
        goal_drift > MIN_GOAL_DRIFT or
        urgency > MIN_URGENCY or
        coherence < MIN_COHERENCE or
        contradiction > CONTRADICTION_THRESHOLD
    )

    if triggered:
        log_event(
            f"[TRIGGER ENGINE] 🔥 Rewrite triggered | ΔEntropy={entropy_shift:.2f} | Drift={goal_drift:.2f} | Urgency={urgency:.2f} | Coherence={coherence:.2f} | Contradiction={contradiction:.2f}"
        )
    return triggered