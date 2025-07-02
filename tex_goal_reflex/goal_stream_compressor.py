# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_stream_compressor.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Prunes, merges, and compresses redundant or decaying goals in active stack
# ============================================================

import uuid
from datetime import datetime, timedelta

from core_layer.tex_manifest import TEXPULSE
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.quantum_randomness import QuantumRandomness

class GoalStreamCompressor:
    def __init__(self):
        self.vectorizer = DreamVectorAbstraction()
        self.qrng = QuantumRandomness()
        policy = TEXPULSE.get("compression_policy", {})
        self.similarity_threshold = policy.get("similarity_threshold", 0.88)
        self.stale_age_seconds = policy.get("stale_threshold_sec", 3600)
        self.utility_floor = policy.get("utility_floor", 0.3)
        self.cluster_collapse_threshold = policy.get("cluster_collapse_count", 3)

    def compress(self, goal_stack):
        """
        Compresses a goal stack by removing stale goals and merging high-similarity duplicates.
        """
        compressed = []
        removed = []
        seen_vectors = []
        goal_clusters = {}
        compression_id = f"compress_{uuid.uuid4().hex[:10]}"

        for goal in goal_stack:
            if self._is_stale(goal):
                removed.append({"goal": goal, "reason": "stale"})
                continue

            g_vec = self.vectorizer.vectorize(goal["goal"])
            best_sim = 0
            match_index = -1

            for i, existing_vec in enumerate(seen_vectors):
                sim = 1 - self.vectorizer.cosine_distance(g_vec, existing_vec)
                if sim > self.similarity_threshold:
                    best_sim = sim
                    match_index = i
                    break

            if match_index >= 0:
                cluster_key = hash(str(seen_vectors[match_index]))
                goal_clusters.setdefault(cluster_key, []).append(goal)
                removed.append({"goal": goal, "reason": f"duplicate (similarity={best_sim:.2f})"})
            else:
                seen_vectors.append(g_vec)
                compressed.append(goal)

        # Optional: collapse clusters into meta-goals
        for cluster in goal_clusters.values():
            if len(cluster) >= self.cluster_collapse_threshold:
                entropy = self.qrng.get_entropy()
                representative = max(cluster, key=lambda x: x.get("utility", 0))
                representative["merged_from"] = len(cluster)
                representative["entropy"] = entropy
                representative["note"] = "meta-goal collapsed from cluster"
                compressed.append(representative)

        memory_cortex.store(
            event={
                "compression_id": compression_id,
                "compression_result": {
                    "original_count": len(goal_stack),
                    "compressed_count": len(compressed),
                    "removed": removed,
                    "clusters_merged": len(goal_clusters)
                }
            },
            tags=["goal_stream", "compression"],
            urgency=0.4,
            emotion="neutral"
        )

        return compressed

    def _is_stale(self, goal):
        try:
            timestamp = datetime.fromisoformat(goal.get("timestamp"))
            age = datetime.utcnow() - timestamp
            if age.total_seconds() > self.stale_age_seconds and goal.get("utility", 0.0) < self.utility_floor:
                return True
        except:
            return False
        return False