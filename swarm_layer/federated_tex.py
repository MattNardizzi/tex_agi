# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: swarm_layer/federated_tex.py
# Tier: Ω∞ Final Sovereign Swarm Coordinator — Loopless, Symbolic, Memory-Synced
# ============================================================

from datetime import datetime
from collections import Counter

from agentic_ai.milvus_memory_router import memory_router
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

SYNC_TAG = "federated_swarm_insight"
MAX_INSIGHTS = 100

class FederatedTex:
    def __init__(self, agent_id="Tex"):
        self.agent_id = agent_id

    def broadcast_insight(self, source_id: str, insight: str, confidence: float = 1.0):
        timestamp = datetime.utcnow().isoformat()
        record = {
            "agent_id": source_id,
            "insight": insight,
            "confidence": round(confidence, 4),
            "timestamp": timestamp
        }

        memory_router.store(
            text=f"[SWARM_INSIGHT] {source_id}: {insight}",
            metadata={
                "type": "swarm_insight",
                "tags": [SYNC_TAG, "insight"],
                "confidence": confidence,
                "agent_id": source_id,
                "timestamp": timestamp
            }
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Agent '{source_id}' shared insight: {insight}",
            source="federated_swarm",
            emotion="thoughtful",
            tags=["swarm", "insight"]
        )

        return record

    def register_agent(self, agent_id: str, traits: list = None):
        timestamp = datetime.utcnow().isoformat()
        memory_router.store(
            text=f"[AGENT_REGISTRATION] {agent_id} registered with traits {traits or []}",
            metadata={
                "type": "agent_registration",
                "tags": ["swarm", "agent", "registration"],
                "traits": traits or [],
                "agent_id": agent_id,
                "timestamp": timestamp
            }
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Agent '{agent_id}' registered to the swarm.",
            source="federated_swarm",
            emotion="stability",
            tags=["agent", "registration"]
        )

        return {"agent_id": agent_id, "traits": traits or [], "timestamp": timestamp}

    def reach_consensus(self, cycle_id: str = None) -> dict:
        insights = memory_router.query_by_tags(tags=["swarm_insight"], top_k=MAX_INSIGHTS)
        if not insights:
            return {"status": "no_insights"}

        votes = Counter()
        for item in insights:
            payload = item.get("entity", item)
            insight = payload.get("insight", "")
            confidence = float(payload.get("confidence", 1.0))
            votes[insight] += confidence

        if not votes:
            return {"status": "no_consensus"}

        top_insight, score = votes.most_common(1)[0]
        timestamp = datetime.utcnow().isoformat()

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Swarm consensus reached: {top_insight}",
            source="federated_swarm",
            emotion="alignment",
            tags=["swarm", "consensus", "cycle", f"cycle_{cycle_id}" if cycle_id else "autonomous"]
        )

        memory_router.store(
            text=f"[CONSENSUS] Top Insight: {top_insight}",
            metadata={
                "type": "swarm_consensus",
                "tags": ["swarm", "consensus", "cycle"],
                "insight": top_insight,
                "score": round(score, 4),
                "cycle_id": cycle_id,
                "timestamp": timestamp
            }
        )

        return {
            "consensus": top_insight,
            "score": round(score, 4),
            "cycle_id": cycle_id,
            "timestamp": timestamp
        }

    def recommend_mutation(self) -> str:
        votes = memory_router.query_by_tags(tags=["swarm_insight"], top_k=MAX_INSIGHTS)
        agent_counts = Counter()
        for record in votes:
            payload = record.get("entity", record)
            agent_id = payload.get("agent_id", "unknown")
            agent_counts[agent_id] += 1

        if not agent_counts:
            return "unknown"

        weakest = agent_counts.most_common()[-1][0]
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Agent '{weakest}' flagged for potential mutation due to low insight activity.",
            source="federated_swarm",
            emotion="evaluative",
            tags=["swarm", "mutation_candidate"]
        )

        return weakest

# === Global instance
federated_swarm = FederatedTex()

# === Public interfaces
def register_child_agent(agent_id: str, traits: list = None):
    return federated_swarm.register_agent(agent_id, traits)

def push_insight(agent_id: str, insight: str, confidence: float = 1.0):
    return federated_swarm.broadcast_insight(agent_id, insight, confidence)