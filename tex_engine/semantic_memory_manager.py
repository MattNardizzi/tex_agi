# semantic_memory_manager.py
# Tier Ω+ — Tex Memory Cortex
# Author: Sovereign Cognition / Tex
# Purpose: Store, compress, and retrieve semantic memory threads with emotion, context, and drift-triggered recall

from datetime import datetime
from uuid import uuid4
import math

# === Semantic Memory Object ===
class SemanticMemory:
    def __init__(self, content, vector, emotion=None, context_tags=None):
        self.id = str(uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.content = content  # Text or symbolic abstraction
        self.vector = vector    # High-dimensional embedding
        self.emotion = emotion or "neutral"  # e.g., "joy", "fear", "urgency"
        self.context_tags = context_tags or []  # e.g., ["dream", "reflex", "drift"]

# === Core Memory Manager ===
class SemanticMemoryManager:
    def __init__(self):
        self.memory_store = []

    # 🧠 Store memory event into memory cortex
    def store_memory(self, memory: SemanticMemory):
        self.memory_store.append(memory)

    # 🧠 Retrieve recent memory threads
    def get_recent_memories(self, limit=10):
        return self.memory_store[-limit:]

    # 🧠 Filter by symbolic or context tag
    def find_by_tag(self, tag):
        return [m for m in self.memory_store if tag in m.context_tags]

    # 🧠 Retrieve conceptually similar memories
    def search_similar(self, query_vector, top_k=5):
        scored = []
        for memory in self.memory_store:
            similarity = cosine_similarity(query_vector, memory.vector)
            scored.append((similarity, memory))
        scored.sort(reverse=True, key=lambda x: x[0])
        return [mem for sim, mem in scored[:top_k]]

    # 🧠 Reflex-trigger: fire recall if semantic drift exceeds threshold
    def check_for_drift_and_trigger(self, query_vector, drift_threshold=0.35, top_k=3):
        if not self.memory_store:
            print("⚠️ No memories stored yet.")
            return []

        recent_memory = self.memory_store[-1]
        recent_vector = recent_memory.vector
        drift_score = 1 - cosine_similarity(query_vector, recent_vector)

        if drift_score > drift_threshold:
            print(f"\n⚠️ Semantic Drift Detected: {drift_score:.3f} > threshold {drift_threshold}")
            triggered = self.search_similar(query_vector, top_k)
            print("🔁 Recalling Semantically Relevant Memories:")
            for mem in triggered:
                print(f" - {mem.content} | Tags: {mem.context_tags} | Emotion: {mem.emotion}")
            return triggered
        else:
            print(f"✅ Drift Stable: {drift_score:.3f} within threshold.")
            return []

    # 🧠 Debugging summary
    def summarize_state(self):
        print(f"🧠 Total Stored Memories: {len(self.memory_store)}")
        if self.memory_store:
            print(f"🧠 Last Memory: \"{self.memory_store[-1].content}\" @ {self.memory_store[-1].timestamp}")

# === Utility: Cosine Similarity ===
def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

# === Local Test Harness ===
if __name__ == "__main__":
    smm = SemanticMemoryManager()
    smm.store_memory(SemanticMemory("Tex initialized self-monitor loop.", [0.2, 0.3, 0.5], emotion="curiosity", context_tags=["init", "loop"]))
    smm.store_memory(SemanticMemory("Tex entered recursive drift mode.", [0.15, 0.28, 0.52], emotion="concern", context_tags=["drift", "recursion"]))
    
    smm.summarize_state()
    
    incoming_vector = [0.9, 0.2, 0.1]
    smm.check_for_drift_and_trigger(incoming_vector)