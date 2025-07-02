# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/memory_brain.py
# Tier: ΩΩΩΩΩ∞ΞΞΣΩ — Sovereign Reflexual Recall Cortex (Final Form)
# Purpose: Performs reflex-aligned, urgency-modulated, entropy-aware memory recall.
#          Fully loopless, sovereign-aligned with pulse-driven memory interaction.
# ============================================================

from datetime import datetime
import uuid

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event


# === Sovereign Memory Retrieval Pulse ===
def recall_memory_pulse(query: str, top_k: int = 5, tags: list = None) -> list:
    """
    Sovereign loopless memory recall reflex.
    Queries sovereign memory vector space and filters results based on reflex pressure.
    """
    if not query or not isinstance(query, str):
        return []

    tags = tags or []
    urgency = float(TEXPULSE.get("urgency", 0.68))
    entropy = float(TEXPULSE.get("entropy", 0.41))
    emotion = TEXPULSE.get("emotion", "neutral")
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"mem-{uuid.uuid4()}"[:12]

    # === Sovereign vector memory query ===
    raw_results = sovereign_memory.query_by_tags(tags=tags, top_k=top_k * 2)
    filtered = []

    for r in raw_results:
        payload = r.payload or {}
        trust = payload.get("alignment_score", 0.5)
        contradiction = payload.get("contradiction_score", 0.0)
        volatility = payload.get("volatility", 0.5)
        pressure = (1 - trust) * 0.4 + contradiction * 0.4 + volatility * 0.2

        threshold = 0.85 - (urgency * 0.2) + (entropy * 0.2)
        if pressure < threshold:
            filtered.append(payload)

    # === Sovereign trace commit (Chrono + Vector)
    sovereign_memory.store_vector_trace(
        content=f"[RECALL MEMORY] '{query}' → {len(filtered)} results",
        signal_type="memory_recall",
        tags=["memory_recall", "sovereign_reflex", "retrieval"] + tags,
        metadata={
            "timestamp": timestamp,
            "query": query,
            "returned": len(filtered),
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "pulse_id": pulse_id,
            "alignment_score": 1.0 - entropy,
            "contradiction_score": entropy
        }
    )

    log_event(
        f"[MEMORY BRAIN] Query='{query}' | Returned={len(filtered)} of {len(raw_results)} | Tags={tags}",
        level="info"
    )

    return filtered