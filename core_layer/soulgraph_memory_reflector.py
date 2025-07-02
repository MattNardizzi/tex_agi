# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/soulgraph_memory_reflector.py
# Tier: ΩΩΩΩΩ∞ΩΩΩ∞ — Soulgraph Memory Reflection + Belief Compression Loop
# Purpose: Reflects on soul-tagged symbolic memory traces and injects learned coherence profile
#          directly into the soulgraph for recursive belief evolution and identity stabilization.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH


def reflect_on_soul_history(limit: int = 10) -> dict:
    """
    Reflects on soul_signature-tagged beliefs, updates coherence trajectory in TEXPULSE,
    and injects new coherence reflection belief into Tex’s soulgraph.
    """
    try:
        recent_entries = sovereign_memory.recall_recent(
            minutes=720,
            top_k=50,
            filters={"tags": ["soul_signature"]}
        )

        soul_entries = [
            entry for entry in recent_entries
            if entry.get("intent") == "soul_signature"
        ][:limit]

        summaries = [entry.get("conclusion", "") for entry in soul_entries]
        coherence = [entry.get("alignment_score", 1.0) for entry in soul_entries]
        entropy = [entry.get("entropy", 0.4) for entry in soul_entries]
        contradiction = [entry.get("contradiction_score", 0.0) for entry in soul_entries]

        avg_coherence = round(sum(coherence) / len(coherence or [1]), 4)
        avg_entropy = round(sum(entropy) / len(entropy or [1]), 4)
        avg_contradiction = round(sum(contradiction) / len(contradiction or [1]), 4)

        reflection = {
            "timestamp": datetime.utcnow().isoformat(),
            "soul_summary": summaries[-1] if summaries else "No prior soul states found.",
            "coherence_trend": avg_coherence,
            "entropy_trend": avg_entropy,
            "contradiction_trend": avg_contradiction,
            "snapshots_reflected": len(summaries)
        }

        # === Update Active Reflex State ===
        TEXPULSE["soul_reflection"] = reflection

        # === Imprint Updated Reflection to Soulgraph ===
        summary = reflection["soul_summary"]
        emotion = TEXPULSE.get("emotion", "reflective")
        urgency = TEXPULSE.get("urgency", 0.5)
        entropy = TEXPULSE.get("entropy", 0.4)

        belief_text = f"Soul reflection completed. Coherence={avg_coherence}, Entropy={avg_entropy}, Contradiction={avg_contradiction}. Summary: {summary}"

        TEX_SOULGRAPH.imprint_belief(
            belief=belief_text,
            source="soulgraph_memory_reflector",
            emotion=emotion,
            tags=["soul_reflection", "identity_trace", "coherence_drift"]
        )

        log.info(f"🪞 [SOULGRAPH] Soul reflection complete. Coherence={avg_coherence}")
        return reflection

    except Exception as e:
        log.error(f"[SOULGRAPH REFLECTOR ERROR] {e}")
        return {
            "status": "error",
            "reason": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }