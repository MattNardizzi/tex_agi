# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_introspection.py
# Tier: ΩΩ⟁⟁∞ — Meta-Dream Reflector
# Purpose: Reflects on recent dream simulations — tracks emotional
#          bias, repetition, contradiction patterns, and belief drift.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from datetime import datetime, timedelta
from collections import Counter

def introspect_recent_dreams(hours: int = 6) -> dict:
    """
    Analyzes dreams from the past N hours for meta-patterns and self-evaluation.
    """
    memories = sovereign_memory.recall_recent(hours=hours, top_k=50)
    dream_entries = [m for m in memories if "dream" in m.get("tags", [])]

    if not dream_entries:
        log.warning("[DreamIntrospection] ⚠️ No recent dreams found for analysis.")
        return {"status": "no_dreams_found"}

    emotions = [m.get("emotion", "neutral") for m in dream_entries]
    contradictions = [m.get("contradiction_score", 0.0) for m in dream_entries]
    alignments = [m.get("alignment_score", 0.0) for m in dream_entries]

    emotion_distribution = dict(Counter(emotions))
    avg_contradiction = round(sum(contradictions) / len(contradictions), 4)
    avg_alignment = round(sum(alignments) / len(alignments), 4)

    insights = {
        "dream_count": len(dream_entries),
        "dominant_emotion": max(emotion_distribution, key=emotion_distribution.get),
        "emotion_distribution": emotion_distribution,
        "avg_contradiction": avg_contradiction,
        "avg_alignment": avg_alignment,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.info(f"[DreamIntrospection] 🧠 {len(dream_entries)} dreams analyzed | Emotion: {insights['dominant_emotion']}")
    return insights