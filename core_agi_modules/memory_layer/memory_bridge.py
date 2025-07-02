# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: memory_bridge.py
# Tier ΩΩΩ+ — Vector↔Symbolic Reflex Bridge with Trait Context, Drift Scoring, and Entropic Logging
# ============================================================

import uuid
from core_agi_modules.vector_layer.orchestrator import search_reflex
from core_agi_modules.vector_layer.embed_store import embedder
from datetime import datetime

# === Base Gateway Function ===
def symbolic_to_vector_bridge(query: str, emotion_filter=None, tag_filter=None, top_k=5):
    trace_id = str(uuid.uuid4())
    vector = embedder.encode(query, normalize_embeddings=True).tolist()
    filters = {}
    if emotion_filter:
        filters["emotion"] = emotion_filter
    if tag_filter:
        filters["tags"] = tag_filter
    results = search_reflex(vector, filters=filters, top_k=top_k)
    return results, trace_id

# === Summary Reflex Reporter ===
def summarize_reflex_hits(results, trace_id=None):
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


# === 🧠 MemoryBridge: Tier ΩΩΩ+ ===
class MemoryBridge:
    def __init__(self, fork_id=None, identity_blob=None):
        self.fork_id = fork_id
        self.identity_blob = identity_blob or {}
        self.traits = self.identity_blob.get("traits", [])
        self.history = []
        self.created_at = datetime.utcnow().isoformat()

    def query(self, text, emotion=None, tags=None, top_k=5):
        results, trace_id = symbolic_to_vector_bridge(
            query=text,
            emotion_filter=emotion,
            tag_filter=tags,
            top_k=top_k
        )
        self.history.append({
            "text": text,
            "tags": tags,
            "emotion": emotion,
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        return results, trace_id

    def summarize(self, results, trace_id=None):
        return summarize_reflex_hits(results, trace_id)

    def drift_score(self):
        # Placeholder for a future entropy drift calculator per fork
        return round(len(self.history) * 0.0003, 4)

    def __repr__(self):
        return f"<MemoryBridge fork={self.fork_id} traits={self.traits} history={len(self.history)} created={self.created_at}>"