# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/soulgraph_memory_reflector.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Soulgraph Memory Reflection + Identity Insight Compression
# Purpose: Queries past soul states and reflects on memory to refine coherence trajectory
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def reflect_on_soul_history(limit: int = 10) -> dict:
    """
    Pulls recent symbolic traces tagged as soul_signature and synthesizes a reflection summary.
    Updates TEXPULSE with coherence alignment trajectory.
    """
    try:
        soul_entries = [
            entry for entry in sovereign_memory.recall_recent(minutes=120, top_k=50)
            if entry.get("tags") and "soul_signature" in entry["tags"]
        ][:limit]

        summaries = [entry.get("summary", "") for entry in soul_entries]
        coherence = [entry.get("alignment_score", 1.0) for entry in soul_entries]
        entropy = [entry.get("entropy", 0.4) for entry in soul_entries]
        contradiction = [entry.get("contradiction_score", 0.0) for entry in soul_entries]

        reflection = {
            "timestamp": datetime.utcnow().isoformat(),
            "soul_summary": summaries[-1] if summaries else "No prior soul states found.",
            "coherence_trend": round(sum(coherence) / len(coherence or [1]), 4),
            "entropy_trend": round(sum(entropy) / len(entropy or [1]), 4),
            "contradiction_trend": round(sum(contradiction) / len(contradiction or [1]), 4),
            "snapshots_reflected": len(summaries)
        }

        TEXPULSE["soul_reflection"] = reflection
        log.info(f"🪞 [SOULGRAPH] Soul reflection complete. Coherence={reflection['coherence_trend']}")
        return reflection

    except Exception as e:
        log.error(f"[SOULGRAPH REFLECTOR ERROR] {e}")
        return {
            "status": "error",
            "reason": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }