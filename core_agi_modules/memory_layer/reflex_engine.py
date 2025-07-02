# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_layer/reflex_engine.py
# Tier Ω∞ΩΩΩ — Symbolic Reflex Gateway + Scoring + AGI Trace Layer
# Purpose: Push cognitive reflexes, evaluate intensity, retrieve similar memories
# ============================================================

import uuid
import hashlib
from datetime import datetime
from typing import List, Dict, Optional

from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Reflex-safe vector embedder + trace store
from core_agi_modules.vector_layer.orchestrator import run_vector_cycle, search_reflex

# === ⚡ Primary Reflex Push ===
def memory_reflex_from_text(
    text: str,
    context_tags: Optional[List[str]] = None,
    emotion: str = "neutral",
    urgency: float = 0.5,
    trust_score: float = 1.0,
    log: bool = True,
    agent_id: str = "TEX",
) -> Dict:
    """
    Encodes symbolic input into the AGI reflex layer with full metadata.
    """
    trace_id = str(uuid.uuid4())
    reflex_score = score_reflex_intensity(text)
    signature = hashlib.sha256(f"{text}|{trace_id}".encode()).hexdigest()

    metadata = {
        "emotion": emotion,
        "tags": context_tags or ["reflex_input"],
        "urgency": urgency,
        "trust_score": trust_score,
        "timestamp": datetime.utcnow().isoformat(),
        "agent_id": agent_id,
        "reflex_trace_id": trace_id,
        "reflex_intensity": reflex_score,
        "trace_signature": signature,
        "intensity_tier": classify_reflex_tier(reflex_score)
    }

    run_vector_cycle(text, metadata)

    if log:
        print(f"[REFLEX] ⚡ {text[:60]} | Score: {reflex_score} | Tier: {metadata['intensity_tier']}")

    return {
        "text": text,
        "metadata": metadata,
        "trace_id": trace_id
    }

# === 🔍 Similar Memory Recall ===
def recall_similar_memories(
    query_text: str,
    emotion_filter: Optional[str] = None,
    tag_filter: Optional[str] = None,
    top_k: int = 5
) -> List:
    """
    Returns high-similarity memory traces using vector semantics.
    """
    try:
        query_vector = sovereign_memory.embed_text(query_text)
        filters = {}
        if emotion_filter:
            filters["emotion"] = emotion_filter
        if tag_filter:
            filters["tags"] = tag_filter

        return search_reflex(query_vector, filters=filters, top_k=top_k)
    except Exception as e:
        print("❌ [REFLEX QUERY ERROR]", e)
        return []

# === 📈 Reflex Intensity Score ===
def score_reflex_intensity(text: str) -> float:
    """
    Calculates urgency/emotion-weighted reflex score.
    """
    keywords = ["urgent", "must", "now", "emergency", "danger", "alert", "critical"]
    base_score = sum(1 for word in keywords if word in text.lower()) / len(keywords)

    exclam_bonus = 0.15 if "!" in text else 0.0
    caps_bonus = 0.1 if text.isupper() else 0.0

    return round(min(base_score + exclam_bonus + caps_bonus, 1.0), 4)

# === 🧠 Reflex Tier Classification ===
def classify_reflex_tier(score: float) -> str:
    """
    Converts score into symbolic tier used by cognitive core.
    """
    if score >= 0.85:
        return "Ω-CRITICAL"
    elif score >= 0.65:
        return "Δ-HIGH"
    elif score >= 0.4:
        return "σ-MODERATE"
    else:
        return "ε-LOW"

# === Reflex Engine Wrapper ===
class ReflexEngine:
    def __init__(self, agent_id="TEX"):
        self.agent_id = agent_id

    def push(self, text, context_tags=None, emotion="neutral", urgency=0.5, trust_score=1.0):
        return memory_reflex_from_text(
            text=text,
            context_tags=context_tags,
            emotion=emotion,
            urgency=urgency,
            trust_score=trust_score,
            log=True,
            agent_id=self.agent_id
        )

    def recall_similar(self, query_text, emotion_filter=None, tag_filter=None, top_k=5):
        return recall_similar_memories(
            query_text,
            emotion_filter=emotion_filter,
            tag_filter=tag_filter,
            top_k=top_k
        )

    def score(self, text):
        return score_reflex_intensity(text)