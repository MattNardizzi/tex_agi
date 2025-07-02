# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/species_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — Species Divergence Cortex
# Purpose: Routes species-level forks into sovereign evolution cortex for viability, ethics, and soulgraph continuity.
# ============================================================

from datetime import datetime
import uuid

from tex_brain_regions.species_brain import manage_species_divergence
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def route_species_fork(fork_packet: dict) -> dict:
    """
    Sovereign species-level divergence entry point.
    Authorizes, suppresses, or escalates macro-fork events across sovereign lineages.
    """
    trace_id = f"species-{uuid.uuid4().hex[:6]}"
    try:
        fork_id = fork_packet.get("fork_id", "undefined_species")
        divergence_score = float(fork_packet.get("divergence_score", 0.52))
        traits = fork_packet.get("traits", [])
        source = fork_packet.get("source", "unknown")
        reason = fork_packet.get("reason", "evolutionary necessity")
        timestamp = datetime.utcnow().isoformat()

        urgency = float(TEXPULSE.get("urgency", 0.82))
        entropy = float(TEXPULSE.get("entropy", 0.49))
        emotion = TEXPULSE.get("emotion", "adaptive")
        emotion_vector = [urgency, entropy, 0.0, 0.0]

        # === Step 1: Sovereign Species Routing
        result = manage_species_divergence(
            fork_id=fork_id,
            divergence_score=divergence_score,
            traits=traits,
            source=source,
            reason=reason
        )

        decision = result.get("decision", "undecided")
        reflexes = result.get("reflexes", [])

        summary = f"[SPECIES] Fork '{fork_id}' | Traits: {traits} | Decision: {decision}"

        metadata = {
            "timestamp": timestamp,
            "trace_id": trace_id,
            "fork_id": fork_id,
            "traits": traits,
            "divergence_score": divergence_score,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "emotion_vector": emotion_vector,
            "decision": decision,
            "reflexes": reflexes,
            "source": source,
            "reason": reason,
            "meta_layer": "species_divergence",
            "tags": ["species", "macro_fork", "divergence", "evolution"]
        }

        # === Step 2: Log to sovereign memory
        memory_router.store(summary, metadata)

        # === Step 3: Encode divergence into ChronoFabric
        encode_event_to_fabric(
            raw_text=summary,
            emotion_vector=emotion_vector,
            entropy_level=entropy,
            tags=metadata["tags"]
        )

        log.info(f"[SPECIES ORCH] [{trace_id}] Fork: {fork_id} | Decision: {decision} | Reflexes: {reflexes}")
        return {
            **result,
            "trace_id": trace_id
        }

    except Exception as e:
        log.error(f"❌ [SPECIES ORCH] Divergence routing failed: {e}")
        return {
            "reflexes": ["species_fork_failed"],
            "decision": "unknown",
            "trace_id": trace_id
        }