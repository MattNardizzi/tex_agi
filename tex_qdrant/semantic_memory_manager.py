# semantic_memory_manager.py
# Tier Ω+ — Tex Memory Cortex (with integrated Qdrant ops)
# Author: Sovereign Cognition / Tex
# Purpose: High-level semantic memory manager that stores, retrieves, and reflexes on drift

from datetime import datetime
from uuid import uuid4
from agentic_ai.qdrant_vector_memory import embed_and_store, query_similar
import math

# === Memory Object Structure ===
class SemanticMemory:
    def __init__(self, content, vector, emotion="neutral", context_tags=None):
        self.id = str(uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.content = content
        self.vector = vector
        self.emotion = emotion
        self.context_tags = context_tags or []

# === Semantic Memory Manager ===
class SemanticMemoryManager:
    def __init__(self, top_k=5, drift_threshold=0.35):
        self.top_k = top_k
        self.drift_threshold = drift_threshold
        self.recent_vector = None  # Will store last known vector for drift comparison

    def store_memory(self, content: str, vector: list[float], emotion="neutral", context_tags=None):
        """Store memory to vector DB and log semantic snapshot."""
        metadata = {
            "content": content,
            "timestamp": datetime.utcnow().isoformat(),
            "emotion": emotion,
            "tags": context_tags or []
        }
        embed_and_store(content, metadata)
        self.recent_vector = vector
        print(f"🧠 Stored memory: {content[:50]}...")

    def search_similar_memories(self, query_vector, tag_filter=None):
        """Search similar memories using Qdrant-backed vector search."""
        results = query_similar(vector=query_vector, top_k=self.top_k)
        memories = []
        for r in results:
            payload = r.payload
            memories.append(SemanticMemory(
                content=payload.get("content", ""),
                vector=query_vector,
                emotion=payload.get("emotion", "neutral"),
                context_tags=payload.get("tags", [])
            ))
        return memories

    def check_for_drift_and_trigger(self, query_vector):
        """Trigger recall if semantic drift from last vector is too large."""
        if not self.recent_vector:
            print("⚠️ No baseline vector set for drift comparison.")
            self.recent_vector = query_vector
            return []

        drift = 1 - cosine_similarity(query_vector, self.recent_vector)
        if drift > self.drift_threshold:
            print(f"\n⚠️ Semantic Drift Triggered! Drift={drift:.3f}")
            memories = self.search_similar_memories(query_vector)
            for m in memories:
                print(f" - {m.content} | Tags: {m.context_tags} | Emotion: {m.emotion}")
            self.recent_vector = query_vector
            return memories
        else:
            print(f"✅ Drift stable: {drift:.3f} (no recall needed)")
            return []

# === Utility ===
def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

# === Example Local Run ===
if __name__ == "__main__":
    smm = SemanticMemoryManager()

    # Example input
    v1 = [0.1, 0.3, 0.9]
    v2 = [0.9, 0.2, 0.1]

    smm.store_memory("Tex initialized reflex dream mode.", v1, emotion="anticipation", context_tags=["dream", "reflex"])
    smm.check_for_drift_and_trigger(v2)