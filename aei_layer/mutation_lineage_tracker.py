# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: aei_layer/mutation_lineage_tracker.py
# Tier Ω∞+++ — Recursive Lineage Vectorizer for Mutation Reflex Chains
# Purpose: Logs mutation genealogy and AGI fork decisions in vector memory + soulgraph
# ============================================================

from datetime import datetime
from hashlib import sha256
import numpy as np

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from utils.logging_utils import log


def update_lineage(parent_codex: dict, new_codex: dict) -> None:
    """
    Tracks the evolutionary mutation chain by embedding parent-child relationships
    and storing them in vector memory and ChronoFabric for retrieval and identity resonance.
    """
    parent_id = parent_codex.get("id", "unknown_parent")
    child_id = new_codex.get("id", f"child_{sha256(new_codex.get('code', '').encode()).hexdigest()[:10]}")
    strategy = new_codex.get("strategy", "unspecified")
    timestamp = datetime.utcnow().isoformat()
    emotion = new_codex.get("emotion", "neutral")
    entropy = new_codex.get("entropy", 0.5)
    reflex = new_codex.get("reflex_pathway", "undesignated")

    description = f"Lineage: {parent_id} → {child_id} via {strategy}"

    lineage_record = {
        "type": "mutation_lineage",
        "parent_id": parent_id,
        "child_id": child_id,
        "strategy": strategy,
        "reflex": reflex,
        "timestamp": timestamp,
        "emotion": emotion,
        "entropy": entropy,
        "origin": new_codex.get("origin", "simulation"),
        "description": description
    }

    try:
        memory_router.store(description, lineage_record)
        encode_event_to_fabric(
            description,
            np.array([0.3, 0.6, 0.1, 0.2]),
            entropy,
            ["lineage", "mutation", strategy]
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"{child_id} evolved from {parent_id} via {strategy}",
            source="mutation_lineage_tracker",
            emotion=emotion,
            tags=["lineage", "mutation", "strategy", strategy]
        )

        log.info(f"[LINEAGE] ✅ Tracked mutation {parent_id} → {child_id} via {strategy}")

    except Exception as e:
        log.error(f"[LINEAGE ERROR] ❌ Failed to track lineage: {e}")


def log_evolution_decision(variant_id: str, metadata: dict, operator: str = "unknown") -> None:
    """
    Logs a single evolutionary decision event (e.g. spawn, fork, promotion) to vector memory and ChronoFabric.
    """
    timestamp = datetime.utcnow().isoformat()
    text = f"[EVOLUTION] {variant_id} decision by {operator}"

    payload = {
        **metadata,
        "variant_id": variant_id,
        "operator": operator,
        "meta_layer": "evolution_decision_log",
        "tags": ["evolution", "mutation", metadata.get("mutation_type", "unknown")],
        "timestamp": timestamp
    }

    try:
        memory_router.store(text, payload)
        encode_event_to_fabric(
            text,
            np.array([0.4, 0.5, 0.2, 0.1]),
            payload.get("entropy", 0.5),
            payload["tags"]
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"{operator} triggered evolution event for {variant_id}",
            source="mutation_lineage_tracker",
            emotion=metadata.get("emotion", "neutral"),
            tags=["evolution", metadata.get("mutation_type", "unspecified")]
        )

        log.info(f"[EVOLUTION] ✅ Logged decision for {variant_id} via {operator}")

    except Exception as e:
        log.error(f"[EVOLUTION ERROR] ❌ Failed to log evolution decision: {e}")