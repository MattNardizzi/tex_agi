# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/vector_layer/orchestrator.py
# Tier ΩΩΩΩΩ — Sovereign Reflex Vector Orchestrator (MemoryRouter + HeatTracker)
# ============================================================

from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.vector_layer.fusion_engine import fuse_related_vectors
from core_agi_modules.vector_layer.mutation_hooks import trigger_mutation_if_needed
from core_agi_modules.vector_layer.heat_tracker import ReflexHeatTracker, adjust_token_weights
from core_agi_modules.intent_object import IntentObject

# === Init HeatTracker Session ===
heat_tracker = ReflexHeatTracker(session_id="vector_orchestrator")

# === 🧠 Sovereign Reflex Store ===
def store_reflex(text: str, metadata: dict):
    """
    Store a vector memory reflex with proper heat, trust, token weighting, and intent trace.
    """
    now = datetime.utcnow().isoformat()
    emotion = metadata.get("emotion", "neutral")
    timestamp = metadata.get("timestamp", now)
    urgency = metadata.get("urgency", 0.5)
    trust = metadata.get("trust_score", 0.85)

    vector = sovereign_memory.embed_text(text)
    heat = heat_tracker.calculate_heat(emotion, timestamp)
    intent = metadata.get("intent_id") or IntentObject(text, source="vector_orchestrator").id

    token_weights = adjust_token_weights(
        vector=vector,
        metadata_dict={
            "emotion": emotion,
            "urgency": urgency,
            "trust_score": trust
        },
        heat=heat
    )

    sovereign_memory.store(
        text=text,
        metadata={
            "tags": metadata.get("tags", ["reflex", "vector"]),
            "emotion": emotion,
            "urgency": urgency,
            "trust_score": trust,
            "token_weight": token_weights,
            "heat": heat,
            "timestamp": timestamp,
            "intent_id": intent,
            "source": metadata.get("source", "vector_orchestrator"),
            "prediction": metadata.get("prediction", ""),
            "actual": metadata.get("actual", text)
        }
    )

    if metadata.get("trigger_mutation"):
        trigger_mutation_if_needed(vector, metadata)

    return vector

# === 🔍 Vector Reflex Query ===
def search_reflex(query_vector, filters=None, top_k=5):
    """
    Queries vector memory and returns reflex-ready results with decayed heat scoring.
    """
    # Convert filters to sovereign_memory-compatible format
    tags = filters.get("tags") if filters else None
    results = sovereign_memory.query_by_tags(tags=tags or ["reflex"], top_k=top_k)
    return heat_tracker.decay_results(results)

# === 🔗 Reflex Fusion ===
def fuse_reflex_group(texts: list, tags=None, emotion="neutral"):
    """
    Fuses a list of memory texts into one cohesive high-signal vector.
    """
    return fuse_related_vectors(texts, tags=tags or ["fusion"], emotion=emotion)

# === ♻️ Full Vector Cycle ===
def run_vector_cycle(input_text: str, metadata: dict):
    """
    One-shot reflex storage + token adjustment + optional fusion.
    """
    print("🧠 [VECTOR] Ingesting reflex memory...")
    store_reflex(input_text, metadata)

    if metadata.get("trigger_fusion"):
        print("🔗 [VECTOR] Fusion triggered.")
        fuse_reflex_group(
            [input_text],
            tags=["auto_fused"],
            emotion=metadata.get("emotion", "neutral")
        )