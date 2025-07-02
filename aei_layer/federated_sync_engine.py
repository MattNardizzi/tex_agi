# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: aei_layer/federated_sync_engine.py
# Tier: ΩΩΩΩΩ∞ — Final Sovereign Federated Reflex Sync Cortex
# ============================================================

from datetime import datetime
from collections import defaultdict
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router
from agentic_ai.milvus_memory_router import embed_text
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from swarm_layer.federated_tex import push_insight, register_child_agent
from agentic_ai.multi_voice_reasoning import run_internal_vote
from utils.logging_utils import log

SYNC_TAG = "federated_sync_vector"
SYNC_FIELDS = ["short_term_memory", "emotion_state", "goal_trace", "reflex_handoff_state"]
TRUST_THRESHOLD = 0.6
TOP_K_AGENTS = 50
DRIFT_DECAY = 0.92


class FederatedSyncEngine:
    def __init__(self, agent_id: str = None):
        self.agent_id = agent_id or TEXPULSE.get("agent_id", "Tex")
        self.trust_scores = TEXPULSE.get("federated_trust_scores", {})
        self.variant_id = TEXPULSE.get("variant_id", "none")
        self.ancestor_id = TEXPULSE.get("ancestor_id", "root")
        self.agent_profiles = TEXPULSE.get("federated_profiles", {})
        register_child_agent(agent_id=self.agent_id, traits=TEXPULSE.get("traits", ["sovereign"]))

    def dynamic_threshold_for(self, agent_id: str) -> float:
        profile = self.agent_profiles.get(agent_id, {})
        forgiveness = float(profile.get("drift_forgiveness", 0.3))
        return max(0.1, min(forgiveness, 1.0))

    def compute_drift(self, local: dict, remote: dict) -> float:
        try:
            v1 = embed_text(str(local))
            v2 = embed_text(str(remote))
            cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            return round(1.0 - cos_sim, 4)
        except Exception as e:
            log.warning(f"[FED_SYNC] Drift computation failed: {e}")
            return 1.0

    def pull_remote_vectors(self) -> list:
        return memory_router.query_by_tags(tags=[SYNC_TAG], top_k=TOP_K_AGENTS)

    def broadcast_memory_vector(self, vector_payload: dict):
        vector_payload["agent"] = self.agent_id
        vector_payload["variant_id"] = self.variant_id
        vector_payload["timestamp"] = datetime.utcnow().isoformat()

        memory_router.store(
            text=f"[FED_SYNC] Broadcasted sync vector for agent: {self.agent_id}",
            metadata={
                "type": "federated_sync_vector",
                "agent_id": self.agent_id,
                "variant_id": self.variant_id,
                "tags": [SYNC_TAG],
                "vector_payload": vector_payload,
                "timestamp": vector_payload["timestamp"]
            }
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Agent '{self.agent_id}' pushed sync vector to swarm.",
            source="federated_sync_engine",
            emotion="collaborative",
            tags=["federated", "sync", "vector"]
        )

        push_insight(self.agent_id, "memory_vector_broadcast", confidence=1.0)
        return vector_payload

    def sync_inbound_vectors(self) -> dict:
        results = self.pull_remote_vectors()
        local_vector = TEXPULSE.get("short_term_memory_snapshot", {})
        drift_map = {}
        merged_state = defaultdict(list)

        for r in results:
            payload = r.get("entity", r)
            sender = payload.get("agent", "unknown")
            if sender == self.agent_id:
                continue

            trust = float(self.trust_scores.get(sender, 0.5))
            if trust < TRUST_THRESHOLD:
                continue

            if payload.get("variant_id") == self.ancestor_id:
                log.warning(f"[FED_SYNC] 🧬 Loop block: ancestor vector from {sender}")
                continue

            drift = self.compute_drift(local_vector, payload.get("short_term_memory", {}))
            threshold = self.dynamic_threshold_for(sender)
            drift_map[sender] = drift

            if drift > threshold:
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Semantic drift detected from {sender} ░ Δ={drift}",
                    source="federated_sync_engine",
                    emotion="unease",
                    tags=["drift", "federated", "sync"]
                )

            for field in SYNC_FIELDS:
                if field in payload:
                    merged_state[field].append(payload[field])

        # Symbolically commit merges
        for field, values in merged_state.items():
            for value in values:
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Merged '{field}' from remote agent input.",
                    source="federated_sync_engine",
                    emotion="reflective",
                    tags=["federated", "merge", field]
                )

        return {
            "merged": dict(merged_state),
            "drift_matrix": drift_map
        }

    def sync_cycle(self):
        log.info("[FED_SYNC] 🔁 Starting federated sync cycle...")
        result = self.sync_inbound_vectors()
        return result["drift_matrix"]