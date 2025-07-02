# memory_bridge.py
# Tier Ω∞ Symbolic ↔ Vector Memory Integration Bridge (Final Form)
# Location: core_agi_modules/memory_layer/memory_bridge.py

import uuid
from core_agi_modules.vector_layer.orchestrator import search_reflex
from core_agi_modules.vector_layer.embed_store import embedder

# === Memory Bridge Gateway ===
def symbolic_to_vector_bridge(query: str, emotion_filter=None, tag_filter=None, top_k=5):
    """
    Converts symbolic memory query into embedded vector search and returns reflex-mapped results.
    Each request is tagged with a unique trace ID for memory flow analysis.
    """
    trace_id = str(uuid.uuid4())
    vector = embedder.encode(query, normalize_embeddings=True).tolist()
    filters = {}
    if emotion_filter:
        filters["emotion"] = emotion_filter
    if tag_filter:
        filters["tags"] = tag_filter

    results = search_reflex(vector, filters=filters, top_k=top_k)
    return results, trace_id

# === Memory Summary Hook ===
def summarize_reflex_hits(results, trace_id=None):
    """
    Provides a symbolic summary of memory matches.
    Adds trust × heat × token weighting as a reflex_score.
    Flags contradiction/fork-worthy beliefs.
    """
    summaries = []
    for r in results:
        trust = float(r.payload.get("trust_score", 1.0))
        heat = float(r.payload.get("effective_heat", 0.5))
        token = float(r.payload.get("token_weight", 0.5))
        score = round(trust * heat * token, 4)

        summary = {
            "text": r.payload.get("content", "")[:100],
            "emotion": r.payload.get("emotion"),
            "heat": heat,
            "trust": trust,
            "score": score,
            "tags": r.payload.get("tags", []),
            "reflex_ready": r.payload.get("reflex_ready", False),
            "trace_id": trace_id
        }

        if "contradiction" in summary["tags"]:
            summary["flag_contradiction"] = True
        if score < 0.2:
            summary["flag_low_priority"] = True

        summaries.append(summary)

    return sorted(summaries, key=lambda s: s["score"], reverse=True)