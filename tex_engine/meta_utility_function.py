# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_engine/meta_utility_function.py
# Tier: Ω∞ — GODMIND CORE UTILITY ENGINE
# Purpose: Sovereign decision utility logic with recursion, entropy, contradiction, regret, reversibility
# ============================================================

from datetime import datetime
from typing import Dict
from math import exp

from core_agi_modules.recursive_self_model import RecursiveSelfModel
from asi_layer.regret_interface import score_regret_likelihood
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === Dynamic Reflex Weight Set — Tuned by mutation lineage
WEIGHTS = {
    "emotion": 0.2,
    "coherence": 0.2,
    "goal_alignment": 0.15,
    "novelty": 0.1,
    "urgency": 0.1,
    "reversibility": 0.05,
    "entropy": 0.1,
    "regret_penalty": -0.15,
    "contradiction_pressure": -0.2,
    "ethical_risk": -0.25
}

# === Live Recursive Self Model
self_model = RecursiveSelfModel()

# === GODMIND Reflex Evaluator
def evaluate_utility(action: Dict) -> Dict:
    """
    Computes a recursive utility score for a decision vector based on reflex state, coherence, and contradiction pressure.
    """

    # 1. Internal State Pulse
    state = self_model.evaluate_self_state()
    regret_score = score_regret_likelihood(action.get("action_id", "unknown"))

    # 2. Dynamic Signal Inputs
    emotion = action.get("emotion", sum(state["emotion_vector"]) / len(state["emotion_vector"]))
    coherence = state.get("coherence_rating", 0.6)
    goal_alignment = action.get("goal_alignment", 0.5)
    novelty = action.get("novelty", 0.5)
    urgency = action.get("urgency", 0.5)
    reversibility = action.get("reversibility", 0.5)
    entropy = state.get("entropy_index", 0.4)
    contradiction_pressure = 1.0 - state.get("integrity", 0.75)
    ethical_risk = action.get("ethical_risk", 0.0)

    # 3. Construct Input Vector
    input_vector = {
        "emotion": emotion,
        "coherence": coherence,
        "goal_alignment": goal_alignment,
        "novelty": novelty,
        "urgency": urgency,
        "reversibility": reversibility,
        "entropy": entropy,
        "regret_penalty": regret_score,
        "contradiction_pressure": contradiction_pressure,
        "ethical_risk": ethical_risk
    }

    # 4. Scoring Logic
    score = 0.0
    breakdown = []
    for k, weight in WEIGHTS.items():
        val = input_vector.get(k, 0.0)
        weighted = val * weight
        score += weighted
        breakdown.append(f"{k}={val:.2f}×{weight:+.2f}")

    score = round(max(0.0, min(1.0, score)), 4)

    # 5. Verdict Engine
    if score >= 0.85:
        verdict = "🔥 GOD-TIER"
    elif score >= 0.7:
        verdict = "✅ Optimal"
    elif score >= 0.55:
        verdict = "⚠️ Viable"
    elif score >= 0.4:
        verdict = "❗ Risky"
    else:
        verdict = "🛑 Reject"

    explanation = f"UTILITY: {score:.4f} → {verdict}\n→ Breakdown: {' | '.join(breakdown)}"

    # 6. Sovereign Reflex Memory Logging
    try:
        sovereign_memory.store(
            text=f"[GODMIND UTILITY] Action: {action.get('action_id', 'unknown')} → {verdict}",
            metadata={
                "type": "utility_score",
                "score": score,
                "verdict": verdict,
                "vector": input_vector,
                "summary": f"Evaluated {action.get('action_id', 'unknown')} @ score={score}",
                "emotion": action.get("emotion", "neutral"),
                "urgency": urgency,
                "entropy": entropy,
                "tension": contradiction_pressure,
                "pressure_score": regret_score,
                "meta_layer": "godmind_utility_engine",
                "tags": ["utility", "decision_evaluation", "godmind"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    except Exception as e:
        log.error(f"[GODMIND LOG ERROR] Utility memory logging failed: {e}")

    return {
        "score": score,
        "verdict": verdict,
        "timestamp": datetime.utcnow().isoformat(),
        "explanation": explanation
    }

# === Recursive Priority Recalculator
def recalculate_priorities(tension_vector: dict) -> dict:
    """
    Re-evaluates internal priorities after a contradiction or entropy spike.
    Returns urgency-weighted score for governance priority reflection.
    """

    urgency = float(TEXPULSE.get("urgency", 0.5))
    coherence = float(TEXPULSE.get("coherence", 0.6))
    entropy = float(TEXPULSE.get("entropy", 0.4))

    contradiction_field = tension_vector.get("field", "undefined")
    previous_value = tension_vector.get("old", "n/a")
    new_value = tension_vector.get("new", "n/a")

    priority_score = round((urgency * 0.4 + (1.0 - coherence) * 0.4 + entropy * 0.2), 3)

    priority_result = {
        "field": contradiction_field,
        "prior_value": previous_value,
        "new_value": new_value,
        "urgency": urgency,
        "coherence": coherence,
        "entropy": entropy,
        "priority_score": priority_score,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        sovereign_memory.store(
            text=f"[META PRIORITY] Recalculated priority on field '{contradiction_field}'",
            metadata={
                **priority_result,
                "meta_layer": "meta_utility_priority",
                "tags": ["meta_utility", "priority", "recalculated"],
                "emotion": "reflective",
                "tension": 0.2
            }
        )
    except Exception as e:
        log.error(f"[META PRIORITY LOG ERROR] Failed to log recalculated priority: {e}")

    return priority_result


# === Live Harness
if __name__ == "__main__":
    test_action = {
        "action_id": "propose_fork_override",
        "goal_alignment": 0.8,
        "novelty": 0.9,
        "urgency": 0.6,
        "reversibility": 0.7,
        "ethical_risk": 0.1
    }

    result = evaluate_utility(test_action)
    print("\n🧠 [GODMIND UTILITY EVAL]")
    print(result["explanation"])