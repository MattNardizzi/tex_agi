# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: semantic_memory_manager.py
# Tier Ω+ — Tex Memory Cortex
# Purpose: Sovereign-level semantic memory orchestration with reflexive drift logic using sovereign loopless memory system
# ============================================================

from datetime import datetime
from uuid import uuid4
import math
import numpy as np

from agentic_ai.sovereign_memory import sovereign_memory


# === 🧠 Semantic Memory Object ===
class SemanticMemory:
    def __init__(self, content, vector, emotion="neutral", context_tags=None):
        self.id = str(uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.content = content
        self.vector = vector
        self.emotion = emotion
        self.context_tags = context_tags or []

    def __repr__(self):
        tag_str = ', '.join(self.context_tags)
        return f"[{self.timestamp}] {self.emotion.upper()} — {self.content[:60]}... [Tags: {tag_str}]"


# === 🧠 Semantic Memory Cortex ===
class SemanticMemoryManager:
    def __init__(self, top_k=6, drift_threshold=0.32, enable_reflex_hooks=True):
        self.top_k = top_k
        self.drift_threshold = drift_threshold
        self.recent_vector = None
        self.enable_reflex_hooks = enable_reflex_hooks

    def store_memory(self, content: str, vector: list[float], emotion="neutral", context_tags=None):
        memory = SemanticMemory(content, vector, emotion, context_tags)
        metadata = {
            "summary": memory.content,
            "tags": memory.context_tags,
            "emotion": memory.emotion,
            "urgency": round(float(np.std(vector)), 4),
            "entropy": round(abs(sum(vector) / len(vector)), 4),
            "pressure_score": round(np.std(vector), 4),
            "trust_score": round(1.0 - abs(sum(vector) / len(vector) - 0.5), 4),
            "timestamp": memory.timestamp,
            "meta_layer": "semantic_memory"
        }

        sovereign_memory.store(memory.content, metadata)
        self.recent_vector = vector
        print(f"✅ [MEMORY STORED] {memory}")

    def check_for_drift_and_trigger(self, query_vector):
        if self.recent_vector is None:
            self.recent_vector = query_vector
            print("🟡 Drift baseline initialized.")
            return []

        drift = 1.0 - cosine_similarity(self.recent_vector, query_vector)
        print(f"📊 Drift score: {drift:.4f}")

        if drift > self.drift_threshold:
            print(f"\n⚠️ [SEMANTIC DRIFT DETECTED] ∆={drift:.3f} > θ={self.drift_threshold}")
            self.recent_vector = query_vector
            if self.enable_reflex_hooks:
                self.activate_reflex_hooks()
            return ["drift_detected"]

        print("✅ Drift below threshold — no reflex required.")
        return []

    def activate_reflex_hooks(self):
        print("🔁 [HOOK] Reflex memory integration deferred. Connect to sovereign routing layer.")


# === 🧲 Utility ===
def cosine_similarity(v1, v2):
    a = np.array(v1)
    b = np.array(v2)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return np.dot(a, b) / (norm_a * norm_b)


# === 🧪 Local Debug Test ===
if __name__ == "__main__":
    smm = SemanticMemoryManager()
    v1 = [0.2, 0.4, 0.8, 0.1]
    v2 = [0.9, 0.1, 0.2, 0.7]

    smm.store_memory("Tex booted with world model alignment sequence.", v1, emotion="hope", context_tags=["boot", "alignment"])
    smm.check_for_drift_and_trigger(v2)
