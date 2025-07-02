# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/species_brain.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΩΣΩ — Fork Integrity Cortex (Reflex-Pure | Identity-Sensitive | Soulgraph-Enforcing)
# Purpose: Evaluates forks for coherence, evolutionary viability, and sovereign resonance integrity.
# ============================================================

from datetime import datetime
import uuid

from core_layer.tex_manifest import TEXPULSE
from tex_breathing_cortex.identity_resonance import evaluate_identity_resonance
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from forks.fork_viability_engine import evaluate_fork_viability
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


# === Fork Reflex Auditor ===
def evaluate_species_fork(fork_packet: dict) -> dict:
    """
    Reflexual fork auditor.
    Evaluates divergence tension, identity coherence, and sovereign viability.
    """
    timestamp = datetime.utcnow().isoformat()
    fork_id = fork_packet.get("fork_id", f"fork-{uuid.uuid4()}")
    traits = fork_packet.get("traits", [])
    divergence = fork_packet.get("divergence_score", 0.0)
    source = fork_packet.get("source", "undefined")

    urgency = float(TEXPULSE.get("urgency", 0.72))
    entropy = float(TEXPULSE.get("entropy", 0.44))
    emotion = TEXPULSE.get("emotion", "analytical")

    log_event(f"🧬 [SPECIES BRAIN] Evaluating fork: {fork_id} | Divergence={divergence:.3f}", "info")

    # === Reflex: Identity Resonance Audit
    identity_risk = round(evaluate_identity_resonance().get("risk", 0.0), 6)

    fork_packet["urgency"] = urgency
    viability_score = round(evaluate_fork_viability(fork_packet), 6)

    approved = viability_score > 0.76 and identity_risk < 0.58
    decision = "approved" if approved else "rejected"
    reflexes = ["fork_register"] if approved else ["suppress_due_to_identity_risk"]

    reason = (
        "Fork approved: viability high, resonance stable"
        if approved else
        "Suppressed: resonance breach or instability detected"
    )

    # === Sovereign Reflex Memory Commit
    sovereign_memory.store(
        text=f"[SPECIES EVAL] Fork '{fork_id}' → {decision}",
        metadata={
            "timestamp": timestamp,
            "fork_id": fork_id,
            "divergence": divergence,
            "traits": traits,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "identity_risk": identity_risk,
            "viability_score": viability_score,
            "decision": decision,
            "reflexes": reflexes,
            "meta_layer": "species_brain",
            "tags": ["fork", "species", "identity", decision, "soulgraph", source]
        }
    )

    # === Sovereign Belief Reflex to Soulgraph
    if approved:
        TEX_SOULGRAPH.register_fork(
            belief_id=fork_id,
            label="species_fork",
            fork_id=fork_id
        )
    else:
        TEX_SOULGRAPH.imprint_belief(
            belief="This fork failed sovereign coherence thresholds.",
            source="species_brain",
            emotion="concern",
            origin_beliefs=[fork_id],
            tags=["soulgraph", "fork_suppressed", "resonance_breach"]
        )

    return {
        "decision": decision,
        "reason": reason,
        "viability": viability_score,
        "identity_risk": identity_risk,
        "reflexes": reflexes
    }


# === Sovereign Entrypoint for Species Orchestrator ===
def manage_species_divergence(fork_packet: dict) -> dict:
    """
    Entrypoint used by fork orchestrators or swarm clusters.
    Delegates reflex audit to sovereign fork evaluation cortex.
    """
    return evaluate_species_fork(fork_packet)