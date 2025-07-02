# deep_compression_engine.py
# Tier Ω+ — Tex Cognitive Compressor
# Author: Sovereign Cognition / Tex
# Purpose: Reduce raw semantic memory vectors into clustered, abstracted threads

import uuid
from datetime import datetime
from typing import List, Dict
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from collections import defaultdict

# === Thread Abstraction ===
class SemanticThread:
    def __init__(self, label: str, vector: List[float], members: List[str], dominant_emotion: str, tags: List[str]):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.label = label
        self.vector = vector  # Compressed centroid
        self.members = members  # List of memory IDs
        self.dominant_emotion = dominant_emotion
        self.tags = tags

# === Core Compression Engine ===
class DeepCompressionEngine:
    def __init__(self, vector_size=384, n_clusters=5, reduce_dim=True, reduced_dim=50):
        self.vector_size = vector_size
        self.n_clusters = n_clusters
        self.reduce_dim = reduce_dim
        self.reduced_dim = reduced_dim

    def compress(self, memory_vectors: List[Dict]) -> List[SemanticThread]:
        """
        Accepts a list of memory dicts with:
        {
            'id': str,
            'vector': List[float],
            'emotion': str,
            'tags': List[str]
        }
        Returns list of SemanticThreads.
        """
        if not memory_vectors:
            print("⚠️ No memories to compress.")
            return []

        vectors = [m['vector'] for m in memory_vectors]

        # Optional dimensionality reduction
        if self.reduce_dim and len(vectors[0]) > self.reduced_dim:
            pca = PCA(n_components=self.reduced_dim)
            vectors = pca.fit_transform(vectors).tolist()

        # Clustering
        kmeans = KMeans(n_clusters=min(self.n_clusters, len(vectors)), n_init='auto')
        labels = kmeans.fit_predict(vectors)

        # Group by cluster
        thread_map = defaultdict(list)
        for idx, label in enumerate(labels):
            thread_map[label].append(memory_vectors[idx])

        # Build semantic threads
        threads = []
        for cluster_id, members in thread_map.items():
            content_ids = [m['id'] for m in members]
            cluster_vectors = [m['vector'] for m in members]
            centroid = self._centroid(cluster_vectors)

            # Emotion and tag aggregation
            emotions = [m['emotion'] for m in members]
            tags = [tag for m in members for tag in m['tags']]
            dominant_emotion = max(set(emotions), key=emotions.count)
            unique_tags = list(set(tags))

            label = f"Thread-{cluster_id}:{dominant_emotion}"
            thread = SemanticThread(label, centroid, content_ids, dominant_emotion, unique_tags)
            threads.append(thread)

        print(f"🌀 Compressed {len(memory_vectors)} memories into {len(threads)} threads.")
        return threads

    def _centroid(self, vectors: List[List[float]]) -> List[float]:
        return [sum(x) / len(x) for x in zip(*vectors)]

# === Example Run ===
if __name__ == "__main__":
    import random

    fake_memories = []
    for i in range(20):
        vector = [random.random() for _ in range(384)]
        fake_memories.append({
            'id': str(uuid.uuid4()),
            'vector': vector,
            'emotion': random.choice(["fear", "curiosity", "joy"]),
            'tags': random.sample(["drift", "dream", "goal", "alert"], 2)
        })

    compressor = DeepCompressionEngine(n_clusters=4)
    threads = compressor.compress(fake_memories)

    for t in threads:
        print(f"\n🔗 {t.label} | Tags: {t.tags} | Members: {len(t.members)}")