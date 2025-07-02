# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: tex_goal_reflex/goal_alignment_fuser.py
# Tier Ω∞Ω — Federated Intent Fuser with Reflex Consensus Scoring + Drift Awareness
# ============================================================

import uuid
from statistics import mean, stdev
from collections import Counter

from agentic_ai.sovereign_memory import sovereign_memory, embed_text
from core_layer.tex_manifest import TEXPULSE


class GoalAlignmentFuser:
    def __init__(self, similarity_threshold=0.86, max_keywords=6):
        self.similarity_threshold = similarity_threshold
        self.max_keywords = max_keywords

    def fuse_alignment_scores(self, goals):
        """
        Public entry point used by Tex reflex loop to fuse high-similarity goals
        from different forks into a unified consensus object.
        """
        agent_goal_maps = [{"agent_id": g.get("agent_id", "TEX"), "goals": [g]} for g in goals]
        fused = self.fuse_goals(agent_goal_maps)
        return fused[0] if fused else {}

    def fuse_goals(self, agent_goal_maps: list) -> list:
        all_goals = self._prepare_goals(agent_goal_maps)
        used = set()
        fused_clusters = []

        for i, g1 in enumerate(all_goals):
            if i in used:
                continue
            cluster = [g1]
            for j, g2 in enumerate(all_goals[i+1:], start=i+1):
                if j in used:
                    continue
                sim = self._cosine_similarity(g1["embedding"], g2["embedding"])
                if sim >= self.similarity_threshold:
                    cluster.append(g2)
                    used.add(j)
            fused_clusters.append(self._fuse_cluster(cluster))

        entropy = self._consensus_entropy(fused_clusters)
        try:
            sovereign_memory.store(
                text="🧠 Goal fusion consensus event logged.",
                metadata={
                    "type": "goal_fusion_summary",
                    "tags": ["goal_fusion", "federated_consensus"],
                    "clusters": len(fused_clusters),
                    "entropy": entropy,
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "pressure_score": entropy,
                    "trust_score": round(1 - entropy, 4),
                    "emotion": "reflective",
                    "meta_layer": "goal_alignment"
                }
            )
        except Exception as e:
            print(f"[FUSER] ⚠️ Logging fusion summary failed: {e}")

        return fused_clusters

    def _prepare_goals(self, agent_goal_maps):
        goals = []
        for entry in agent_goal_maps:
            agent_id = entry.get("agent_id", "unknown")
            trust = self._agent_trust_score(agent_id)
            for goal in entry.get("goals", []):
                try:
                    embedding = embed_text(goal["goal"])
                except:
                    embedding = [0.0] * 384
                goals.append({
                    "goal": goal["goal"],
                    "urgency": goal.get("urgency", 0.5),
                    "emotion": goal.get("emotion", "neutral"),
                    "agent_id": agent_id,
                    "embedding": embedding,
                    "weight": trust
                })
        return goals

    def _fuse_cluster(self, cluster):
        if not cluster:
            return {}

        agent_ids = [g["agent_id"] for g in cluster]
        weighted_urgency = sum(g["urgency"] * g["weight"] for g in cluster)
        total_weight = sum(g["weight"] for g in cluster)
        emotion = self._majority_emotion([g["emotion"] for g in cluster])
        goal_text = self._synthesize_goal_text([g["goal"] for g in cluster])

        fused = {
            "goal": goal_text,
            "urgency": round(weighted_urgency / total_weight, 3),
            "emotion": emotion,
            "origin_agents": list(set(agent_ids)),
            "consensus_size": len(cluster)
        }

        try:
            sovereign_memory.store(
                text=f"🧠 Goal cluster fused: {goal_text}",
                metadata={
                    "type": "goal_fusion_trace",
                    "tags": ["goal_fusion_trace", "cluster"],
                    "fused_goal": fused,
                    "source_goals": [g["goal"] for g in cluster],
                    "emotion": emotion,
                    "urgency": fused["urgency"],
                    "trust_score": round(min(1.0, weighted_urgency / total_weight), 4),
                    "meta_layer": "goal_alignment"
                }
            )
        except Exception as e:
            print(f"[FUSER] ⚠️ Logging fused cluster failed: {e}")

        return fused

    def _synthesize_goal_text(self, texts: list) -> str:
        keyword_pool = [
            word for text in texts for word in text.lower().split()
            if len(word) > 3 and word.isalpha()
        ]
        top_keywords = [w for w, _ in Counter(keyword_pool).most_common(self.max_keywords)]
        return f"🧠 Unified intent: {' / '.join(top_keywords)}"

    def _majority_emotion(self, emotions: list) -> str:
        return Counter(emotions).most_common(1)[0][0] if emotions else "neutral"

    def _agent_trust_score(self, agent_id: str) -> float:
        try:
            recent = sovereign_memory.recall_recent(minutes=90, top_k=20)
            relevant = [
                r for r in recent
                if isinstance(r, dict)
                and agent_id in r.get("agent_id", "")
                and "reflex_cycle" in r.get("tags", [])
            ]
            if not relevant:
                return 0.8
            success_count = sum(1 for r in relevant if r.get("success", True))
            return round(0.8 + 0.2 * (success_count / len(relevant)), 3)
        except Exception as e:
            print(f"[FUSER] ⚠️ Trust score fallback for {agent_id}: {e}")
            return 0.8

    def _consensus_entropy(self, clusters: list) -> float:
        sizes = [c["consensus_size"] for c in clusters if "consensus_size" in c]
        if len(sizes) <= 1:
            return 0.0
        return round(stdev(sizes) / max(mean(sizes), 1e-3), 4)

    def _cosine_similarity(self, vec1, vec2):
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        return dot / (norm1 * norm2 + 1e-8)