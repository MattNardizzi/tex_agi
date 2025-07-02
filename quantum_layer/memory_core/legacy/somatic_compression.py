# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/somatic_compression.py
# Tier ΩΩΩΩΩΩ — Conceptual Memory Compression + Meaning Entropy Indexing
# Purpose: Converts low-impact episodic memory into structured sovereign concepts
# ============================================================

from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from quantum_layer.memory_core.memory_cortex import MemoryCortex
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from datetime import datetime
import numpy as np
import uuid
import math

class SomaticCompressor:
    def __init__(self, cluster_size=8):
        self.cortex = MemoryCortex()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.cluster_size = cluster_size

    def compress_low_urgency_memories(self, emotion_filter=["neutral", "boredom"], urgency_threshold=0.4):
        memories = self._gather_eligible_memories(emotion_filter, urgency_threshold)
        if not memories:
            return []

        texts = [m["content"] for m in memories]
        vectors = self.model.encode(texts)

        kmeans = KMeans(n_clusters=min(self.cluster_size, len(vectors)), random_state=42)
        labels = kmeans.fit_predict(vectors)

        compressed = []
        for cluster_id in range(max(labels) + 1):
            indices = [i for i, label in enumerate(labels) if label == cluster_id]
            cluster_texts = [texts[i] for i in indices]
            source_ids = [memories[i].get("id", str(uuid.uuid4())) for i in indices]
            average_urgency = np.mean([memories[i].get("urgency", 0.5) for i in indices])
            average_trust = np.mean([memories[i].get("trust_score", 0.75) for i in indices])
            entropy_score = self._calculate_entropy(cluster_texts)

            summary = self._abstract_summary(cluster_texts)
            vector = self.model.encode(summary)
            belief_id = str(uuid.uuid4())

            TEX_SOULGRAPH.imprint_belief(
                belief=summary,
                source="somatic_compression",
                tags=["compressed", f"cluster_{cluster_id}"],
                emotion="neutral",
                trust_score=round(average_trust, 3),
                entropy_score=round(entropy_score, 4),
                timestamp=datetime.utcnow().isoformat(),
                id=belief_id,
                source_trace=source_ids
            )

            compressed.append({
                "id": belief_id,
                "summary": summary,
                "cluster_size": len(cluster_texts),
                "entropy_score": entropy_score,
                "trust_score": round(average_trust, 3),
                "source_ids": source_ids,
                "vector": vector
            })

        return compressed

    def _gather_eligible_memories(self, emotion_filter, urgency_threshold):
        all_entries = self.cortex.short_term_memory.recent(500)
        return [
            m for m in all_entries
            if m.get("emotion") in emotion_filter and m.get("urgency", 0.5) <= urgency_threshold
        ]

    def _abstract_summary(self, texts):
        joined = " ".join(texts)
        return f"Core memory abstraction: {joined[:240]}..."  # Optional: Replace with GPT summarizer

    def _calculate_entropy(self, cluster_texts):
        lengths = [len(t.split()) for t in cluster_texts]
        if not lengths:
            return 0.0
        avg = np.mean(lengths)
        std_dev = np.std(lengths)
        if avg == 0:
            return 0.0
        return round((std_dev / avg) * math.log(len(cluster_texts) + 1), 4)