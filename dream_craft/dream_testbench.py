# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_testbench.py
# Tier: ΩΩΩ∞𝛀⟁ — Reflexive Dream Evaluator
# Purpose: Continuously evaluates dream quality and stability via
#          pressure-aware batch scans (no loops, no polling).
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from statistics import mean, stdev
from collections import Counter

def run_dream_testbench(window_hours: int = 4, top_k: int = 25) -> dict:
    """
    Analyzes recent dreams for systemic quality: realism, coherence, contradiction, and entropy stability.
    Triggered by pressure spikes or periodic pulse ticks (not polling).
    """
    memories = sovereign_memory.recall_recent(hours=window_hours, top_k=top_k)
    dreams = [m for m in memories if "dream" in m.get("tags", [])]

    if not dreams:
        log.warning("[DreamTestbench] ⚠️ No dream data to evaluate.")
        return {"status": "no_dreams"}

    contradiction_scores = [m.get("contradiction_score", 0.0) for m in dreams]
    alignment_scores = [m.get("alignment_score", 0.0) for m in dreams]
    entropy_values = [m.get("entropy", 0.5) for m in dreams]
    emotions = [m.get("emotion", "neutral") for m in dreams]

    report = {
        "dream_count": len(dreams),
        "avg_contradiction": round(mean(contradiction_scores), 4),
        "avg_alignment": round(mean(alignment_scores), 4),
        "entropy_stability": round(stdev(entropy_values), 4) if len(entropy_values) > 1 else 0,
        "dominant_emotion": Counter(emotions).most_common(1)[0][0],
        "status": "evaluation_complete"
    }

    log.info(f"[DreamTestbench] ✅ Dreams evaluated: {report}")
    return report