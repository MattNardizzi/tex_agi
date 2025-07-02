# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: brain_layer/spike_belief_linker.py
# Tier: ΩΩΩΩΩ++ Reflex Lineage Cortex — Self-Contained Spike→Belief Similarity Linker
# ============================================================

from datetime import datetime
import numpy as np
import uuid
from typing import List, Dict

from agentic_ai.milvus_memory_router import memory_router  # ✅ Final reflex memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum linkage
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === CONFIGURATION ===
LINK_THRESHOLD = 0.88
REINFORCE_THRESHOLD = 0.95
TAGGED_TYPES = ["belief_embedding", "internal_debate_fragment"]

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    v1 = np.array(vec1)
    v2 = np.array(vec2)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    return float(np.dot(v1, v2) / denom) if denom != 0 else 0.0

def link_spike_to_beliefs():
    """
    Self-contained reflex-belief linker.
    Locates belief embeddings similar to recent spike vectors.
    Flags contradictions, reinforces alignment, and links to soulgraph lineage.
    """
    try:
        spikes = memory_router.query_by_tags(tags=["neuromorphic_spike"], top_k=20)
        beliefs = memory_router.query_by_tags(tags=["belief", "debate"], top_k=100)

        linked_count = 0

        for spike in spikes:
            spike_vec = spike.payload.get("vector", [0.5, 0.5, 0.5, 0.0])
            spike_id = spike.payload.get("reflex_id", f"spike-{uuid.uuid4().hex[:6]}")
            classification = spike.payload.get("classification", "general_spike")
            lineage_thread = f"thread-{uuid.uuid4().hex[:6]}"

            for belief in beliefs:
                belief_meta = belief.payload
                belief_vec = belief_meta.get("vector", [])

                if not belief_vec or belief_meta.get("type") not in TAGGED_TYPES:
                    continue

                sim_score = cosine_similarity(spike_vec, belief_vec)
                if sim_score < LINK_THRESHOLD:
                    continue

                belief_id = belief_meta.get("belief_id") or belief_meta.get("signature")
                if not belief_id:
                    continue

                contradiction = (
                    "contradiction" in belief_meta.get("tags", []) or
                    belief_meta.get("emotion", "") in ["conflict", "doubt"]
                )

                # === Link reflex to belief
                TEX_SOULGRAPH.relate_beliefs(belief_id, spike_id, relation=f"reflex_origin::{lineage_thread}")

                # === Imprint belief trace
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Spike ({classification}) linked to belief {belief_id} via {lineage_thread}",
                    source="spike_belief_linker",
                    emotion="alert" if contradiction else "curious",
                    tags=["spike", "belief_link", classification, lineage_thread]
                )

                # === Contradiction handling
                if contradiction:
                    TEX_SOULGRAPH.flag_drift(belief_id, drift_score=0.7)

                # === Reinforce highly aligned beliefs
                node = TEX_SOULGRAPH.graph.get(belief_id)
                if sim_score >= REINFORCE_THRESHOLD and node:
                    if hasattr(node, "confidence"):
                        node.confidence = round(min(1.0, node.confidence + 0.1), 4)
                    if hasattr(node, "activation"):
                        node.activation = round(min(1.0, node.activation + 0.1), 4)

                # === Quantum event trace
                encode_event_to_fabric(
                    raw_text=f"Reflex '{spike_id}' linked to belief '{belief_id}'",
                    emotion_vector=[spike_vec[0], spike_vec[1], 0.0, 0.0],
                    entropy_level=spike_vec[1],
                    tags=["belief_link", "reflex", classification]
                )

                linked_count += 1

        # === Final memory log
        memory_router.store(
            text=f"[LINKER] Reflex-to-belief pass complete ░ Links made: {linked_count}",
            metadata={
                "type": "spike_belief_link_report",
                "linked_count": linked_count,
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["belief", "reflex", "linkage"]
            }
        )

        return True

    except Exception as e:
        memory_router.store(
            text=f"[LINKER ERROR] Spike-to-belief linker failed: {e}",
            metadata={
                "type": "spike_linker_error",
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["error", "belief_linking"]
            }
        )
        return False

# === DEBUG ENTRY ===
if __name__ == "__main__":
    link_spike_to_beliefs()