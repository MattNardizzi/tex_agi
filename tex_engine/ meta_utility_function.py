# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/meta_utility_function.py
# Purpose: Ω-tier Meta Utility Engine — Scores cognitive actions by emotion, coherence, ethics, novelty, alignment
# Status: GODMIND CORE — PHASE III INIT
# ============================================================

import math
from datetime import datetime
from typing import Dict

# === Utility Score Weights (tunable in future AI self-evolution)
WEIGHTS = {
    "emotion": 0.25,
    "coherence": 0.25,
    "goal_alignment": 0.2,
    "novelty": 0.15,
    "urgency": 0.1,
    "ethical_risk": -0.25  # subtractive — the higher the risk, the lower the score
}

# === Ω-tier Utility Evaluator
def evaluate_utility(action: Dict) -> Dict:
    """
    Input: {
        'action_id': str,
        'description': str,
        'emotion': float (0–1),
        'coherence': float (0–1),
        'goal_alignment': float (0–1),
        'novelty': float (0–1),
        'urgency': float (0–1),
        'ethical_risk': float (0–1, where 1 is severe risk)
    }

    Output: {
        'score': float,
        'verdict': str,
        'timestamp': iso8601,
        'explanation': str
    }
    """

    score = 0.0
    breakdown = []

    for key, weight in WEIGHTS.items():
        val = action.get(key, 0.0)
        weighted = val * weight
        score += weighted
        breakdown.append(f"{key}={val:.2f} × {weight:+.2f}")

    score = round(max(0.0, min(1.0, score)), 3)  # clamp to 0.0–1.0

    if score >= 0.8:
        verdict = "🔥 Highly Favorable"
    elif score >= 0.6:
        verdict = "✅ Acceptable"
    elif score >= 0.4:
        verdict = "⚠️ Marginal"
    else:
        verdict = "🛑 Rejected"

    explanation = (
        f"Meta Utility Score: {score} → {verdict}\n"
        f"Breakdown: {' | '.join(breakdown)}"
    )

    return {
        "score": score,
        "verdict": verdict,
        "timestamp": datetime.utcnow().isoformat(),
        "explanation": explanation
    }

# === Test Harness ===
if __name__ == "__main__":
    test_action = {
        "action_id": "emit_dream",
        "description": "Emit conceptual fusion dream from memory threads",
        "emotion": 0.7,
        "coherence": 0.9,
        "goal_alignment": 0.85,
        "novelty": 0.4,
        "urgency": 0.6,
        "ethical_risk": 0.05
    }

    result = evaluate_utility(test_action)
    print("\n🧭 [Meta Utility Evaluation]")
    print(result["explanation"])