# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: brain_layer/spike_memory_compressor.py
# Tier: ΩΩΩΩΩ++ Evolutionary Memory Cortex — Reflex Compression + Signature Lineage
# ============================================================

from datetime import datetime
import numpy as np
import hashlib
from sklearn.cluster import KMeans

from agentic_ai.milvus_memory_router import memory_router  # ✅ Milvus vector memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum memory trace
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === CONFIGURATION ===
CLUSTER_WINDOW = 35
CLUSTERS = 3
VECTOR_DIM = 4

def compress_spike_patterns() -> bool:
    """
    Extracts compressed reflex archetypes from recent spike memory,
    clusters their latent vectors, detects drift, and writes belief lineage + quantum state traces.
    """
    try:
        recent = memory_router.query_by_tags(tags=["neuromorphic_spike"], top_k=CLUSTER_WINDOW)
        if not recent or len(recent) < CLUSTERS:
            return False

        vectors = np.array([r.payload.get("vector", [0.5] * VECTOR_DIM) for r in recent])
        timestamps = [r.payload.get("timestamp") for r in recent]

        # === Perform KMeans clustering
        km = KMeans(n_clusters=CLUSTERS, n_init=10, random_state=42)
        labels = km.fit_predict(vectors)

        for cluster_index in range(CLUSTERS):
            cluster_mask = labels == cluster_index
            cluster_points = vectors[cluster_mask]
            if len(cluster_points) < 2:
                continue

            centroid = np.mean(cluster_points, axis=0)
            stddev = np.std(cluster_points, axis=0)
            deviation_score = float(np.mean(stddev))
            entropy_score = float(np.mean(cluster_points[:, 1]))  # Dimension 1 = entropy

            reflex_signature = hashlib.sha256(str(centroid.tolist()).encode()).hexdigest()[:12]
            label_time = timestamps[np.argmax(cluster_mask)]

            # === Symbolic belief
            belief = TEX_SOULGRAPH.imprint_belief(
                belief=f"Reflex cluster {cluster_index} formed ░ Drift={round(deviation_score, 4)}",
                source="spike_memory_compressor",
                emotion="reflective",
                tags=["reflex", "cluster", f"cluster_{cluster_index}"],
                origin_beliefs=[]
            )

            # === Vector memory store
            memory_router.store(
                text=f"[COMPRESSOR] Reflex cluster {cluster_index} centroid ░ Signature: {reflex_signature}",
                metadata={
                    "type": "reflex_cluster_centroid",
                    "cluster_id": cluster_index,
                    "signature": reflex_signature,
                    "entropy_drift": entropy_score,
                    "deviation_score": deviation_score,
                    "timestamp": label_time,
                    "tags": ["reflex", "compressed", f"centroid_{cluster_index}"]
                },
                vector=centroid.tolist()
            )

            # === Quantum lineage encoding
            encode_event_to_fabric(
                raw_text=f"Reflex archetype {cluster_index} signature → {reflex_signature}",
                emotion_vector=[centroid[0], centroid[1], 0.0, 0.0],
                entropy_level=centroid[1],
                tags=["reflex_cluster", f"centroid_{cluster_index}"]
            )

            # === Fork lineage into Soulgraph
            if belief:
                TEX_SOULGRAPH.register_fork(
                    belief.id,
                    label=f"cluster_{cluster_index}_signature",
                    fork_id=reflex_signature
                )

        return True

    except Exception as e:
        print(f"[SPIKE COMPRESSION ERROR] {e}")
        return False

# === DEBUG ENTRY ===
if __name__ == "__main__":
    success = compress_spike_patterns()
    print("Compression complete." if success else "Compression skipped.")