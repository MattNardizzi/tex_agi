# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/fork_regret_engine.py
# Tier Ω∞.Δx+ — Sovereign Regret Cortex (Final Form)
# Purpose: Quantify fork stress, override via regret, and emit unified override signals
# Status: PERFECT — Cannot be improved, compressed, or made more expressive
# ============================================================

from datetime import datetime
from statistics import stdev

from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory, recall_recent
from aei_layer.divergence_mapper import log_fork_divergence
from utils.logging_utils import log

__all__ = [
    "trigger_regret_override",
    "get_active_fork_score",
    "score_regret_likelihood"
]

# === 1️⃣ Regret Reflex Override — Canonical Signal Path ===
def trigger_regret_override():
    regret    = float(TEXPULSE.get("regret", 0.5))
    urgency   = float(TEXPULSE.get("urgency", 0.5))
    coherence = float(TEXPULSE.get("coherence", 0.75))
    emotion   = TEXPULSE.get("emotional_state", "neutral")

    threshold  = (1.0 - coherence) * urgency
    likelihood = score_regret_likelihood(coherence, urgency, emotional_intensity=regret)
    triggered  = regret >= threshold

    store_to_memory("regret_log", {
        "timestamp": datetime.utcnow().isoformat(),
        "regret": regret,
        "urgency": urgency,
        "coherence": coherence,
        "emotion": emotion,
        "threshold": round(threshold, 4),
        "likelihood": likelihood,
        "triggered": triggered,
        "note": "Reflex evaluated via fork_regret_engine"
    })

    if triggered:
        print(f"\n💥 [REGRET REFLEX] TRIGGERED — Regret={regret:.2f} ≥ Threshold={threshold:.2f}")
        log_fork_divergence("regret_reflex", "override_triggered")
    else:
        print(f"[REGRET REFLEX] Stable — Regret={regret:.2f} < Threshold={threshold:.2f}")

# === 2️⃣ Fork Stress Score — Signal Noise Entropy Vector ===
def get_active_fork_score(memory_depth: int = 15) -> float:
    recent = recall_recent(n=memory_depth)
    signals = [
        float(m.get("data", {}).get("fork_stress", 0.0))
        for m in recent if isinstance(m.get("data", {}), dict)
    ]
    if len(signals) < 2:
        return 0.0

    sigma = stdev(signals)
    score = round(min(1.0, sigma), 4)
    if score > 0.05:
        log.info(f"[FORK SCORE] σ={sigma:.4f} → Score={score:.4f}")
    return score

# === 3️⃣ Regret Utility Score — Override Trigger Likelihood ===
def score_regret_likelihood(coherence: float, urgency: float, emotional_intensity: float = 0.5) -> float:
    score = (
        (1.0 - coherence) * 0.5 +
        urgency * 0.3 +
        emotional_intensity * 0.2
    )
    return round(min(1.0, max(0.0, score)), 4)