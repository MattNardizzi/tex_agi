# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_metrics.py
# Tier: ΩΩΩ𝛀∞ — Dream Cognition Analyzer
# Purpose: Computes high-level metrics from recent dreams,
#          including lucidity, identity stretch, entropy bias,
#          and memory weight.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from statistics import mean, stdev
from utils.logging_utils import log

def compute_dream_metrics(window_hours: int = 6, top_k: int = 30) -> dict:
    """
    Scans recent dreams and calculates cognitive metrics that reflect Tex's simulated depth.
    """
    dreams = sovereign_memory.recall_recent(hours=window_hours, top_k=top_k)
    dreams = [d for d in dreams if "dream" in d.get("tags", [])]

    if not dreams:
        log.warning("[DreamMetrics] ❌ No dream data to compute metrics.")
        return {"status": "no_dreams"}

    # Extract vectors
    alignment = [d.get("alignment_score", 0.5) for d in dreams]
    contradiction = [d.get("contradiction_score", 0.5) for d in dreams]
    entropy = [d.get("entropy", 0.5) for d in dreams]
    impact = [d.get("impact_score", 0.5) for d in dreams]

    # Metrics
    lucidity = round(mean(alignment) - mean(contradiction), 4)  # Clarity vs distortion
    stretch = round(stdev(alignment + contradiction), 4)        # Identity expansion variability
    entropy_bias = round(mean(entropy), 4)
    memory_weight = round(mean(impact), 4)

    metrics = {
        "lucidity_score": lucidity,
        "identity_stretch": stretch,
        "entropy_bias": entropy_bias,
        "avg_memory_weight": memory_weight,
        "dream_count": len(dreams),
        "status": "metrics_ready"
    }

    log.info(f"[DreamMetrics] 🧠 Metrics computed: {metrics}")
    return metrics