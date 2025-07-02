# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/dream_vector_abstraction.py
# Tier Ω++ — Cognitive Thread Vectorizer for Reflexive Dream Encoding
# Purpose: Encode self-reflection threads into memory-native dream vectors
# ============================================================

from datetime import datetime
import uuid

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric


class DreamVectorAbstraction:
    def __init__(self):
        self.model = memory_router.embedder
        self.agent_id = "TEX"
        self.collection = memory_router.collection

    def encode_threads(self, threads: list[dict]) -> list[dict]:
        dream_vectors = []
        for thread in threads:
            text_block = " ".join(str(e.get("event", "")) for e in thread.get("entries", []))
            vector = self.model.encode(text_block, normalize_embeddings=True).tolist()

            dream_id = f"dream_{uuid.uuid4().hex[:8]}"
            timestamp = datetime.utcnow().isoformat()
            emotion = thread.get("emotions", ["neutral"])[0]
            coherence = thread.get("coherence_score", 0.5)
            thread_id = thread.get("thread_id", "unknown")
            origin = thread.get("origin", "unknown_process")

            payload = {
                "type": "dream",
                "dream_id": dream_id,
                "thread_id": thread_id,
                "origin": origin,
                "timestamp": timestamp,
                "vector_source": "dream_vector_abstraction",
                "tags": ["dream", "self_reflection", "cognition"],
                "emotion": emotion,
                "coherence": coherence,
                "agent_id": self.agent_id,
                "trust_score": 1.0,
                "heat": 0.5,
                "prediction": "dream abstraction will capture latent self-patterns",
                "actual": f"{len(thread.get('entries', []))} entries embedded"
            }

            # Store in Milvus vector memory
            memory_router.store_vector(vector, payload)

            # Log dream into ChronoFabric
            try:
                encode_event_to_fabric(
                    raw_text=f"[DREAM ENCODE] Thread {thread_id} → {dream_id}",
                    emotion_vector=[coherence, 1 - coherence, 0.0, 0.0],
                    entropy_level=1.0 - coherence,
                    tags=["dream", "tex_dreamstate", "reflection"]
                )
            except Exception as e:
                print(f"⚠️ [ChronoFabric Error] {e}")

            print(f"[DREAM] 🧠 Encoded thread '{thread_id}' → {dream_id}")

            dream_vectors.append({
                "dream_id": dream_id,
                "thread_id": thread_id,
                "vector": vector,
                "timestamp": timestamp,
                "metadata": payload
            })

        return dream_vectors


# === Dev Test ===
if __name__ == "__main__":
    from core_layer.tex_self_reflective_loop import TexSelfReflectiveLoop
    loop = TexSelfReflectiveLoop()
    threads = loop.run_reflection()
    if threads:
        dreamer = DreamVectorAbstraction()
        dreams = dreamer.encode_threads(threads)