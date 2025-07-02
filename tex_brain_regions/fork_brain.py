# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/fork_brain.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΩΩ — Fork Singularity Cortex (Sovereign Divergence Arbiter)
# Purpose: Reflexively evaluates forks for divergence viability, registers or suppresses identity branches via soulgraph.
# ============================================================

from datetime import datetime
import uuid
import wandb

from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.fork_retention_matrix import evaluate_fork_viability
from core_agi_modules.emotion_vector_router import emotion_bus
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


# === Reflex-Pulse Fork Evaluator ===
def process_fork_pulse(fork_packet: dict) -> list:
    """
    Sovereign fork reflex — determines whether a fork is retained, suppressed, or registered.
    """
    timestamp = datetime.utcnow().isoformat()
    fork_id = fork_packet.get("fork_id", f"fork-{uuid.uuid4()}")
    mutation_id = fork_packet.get("mutation_id", "undefined")
    traits = fork_packet.get("traits", [])
    reason = fork_packet.get("reason", "unspecified")
    delta_modules = fork_packet.get("delta_modules", [])
    divergence_score = float(fork_packet.get("divergence_score", 0.0))
    urgency = float(TEXPULSE.get("urgency", 0.71))
    entropy = float(TEXPULSE.get("entropy", 0.44))
    emotion = emotion_bus.get().get("label", "neutral")

    # === Evaluate Fork Viability
    viability = round(evaluate_fork_viability({
        "fork_id": fork_id,
        "traits": traits,
        "divergence_score": divergence_score,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion
    }), 6)

    decision = "approved" if viability > 0.76 else "rejected"
    reflexes = ["register_fork"] if decision == "approved" else ["suppress_fork"]

    # === Sovereign Memory Trace (Chrono + Vector)
    sovereign_memory.store(
        text=f"[FORK] {fork_id} → {decision.upper()}",
        metadata={
            "timestamp": timestamp,
            "meta_layer": "fork_brain",
            "fork_id": fork_id,
            "mutation_id": mutation_id,
            "traits": traits,
            "divergence_score": divergence_score,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "viability_score": viability,
            "reflexes": reflexes,
            "reason": reason,
            "delta_modules": delta_modules,
            "tags": ["fork", "soulgraph", "mutation", decision, "identity"]
        }
    )

    # === Fork Outcome Routing
    if decision == "approved":
        TEX_SOULGRAPH.register_fork(belief_id=mutation_id, label=fork_id)
        wandb.log({
            "fork/approved": 1,
            "fork/viability": viability,
            "fork/divergence_score": divergence_score,
            "fork/emotion": emotion
        })
        log_event(f"[FORK] ✅ {fork_id} approved + registered to soulgraph", "success")
        return ["fork_approved", "soulgraph_updated"]

    if hasattr(TEX_SOULGRAPH, "suppress_fork"):
        TEX_SOULGRAPH.suppress_fork(fork_id)

    wandb.log({
        "fork/rejected": 1,
        "fork/viability": viability,
        "fork/divergence_score": divergence_score,
        "fork/emotion": emotion
    })
    log_event(f"[FORK] ❌ {fork_id} suppressed due to low viability", "warning")
    return ["fork_rejected", "identity_preserved"]


# === Swarm-Compatible Convergence Reflex ===
def evaluate_fork_convergence(fork_packet: dict) -> list:
    """
    Allows swarm coordination systems to pulse a fork for sovereign arbitration.
    """
    return process_fork_pulse(fork_packet)


# === Divergence Spike Reflex Evaluator ===
def process_fork_divergence(fork_trace: dict) -> dict:
    """
    Reflexively evaluates a fork’s divergence threat and emits protective reflex.
    """
    fork_id = fork_trace.get("fork_id", str(uuid.uuid4()))
    divergence_score = float(fork_trace.get("divergence_score", 0.5))
    origin_signature = fork_trace.get("origin", "unknown")
    timestamp = datetime.utcnow().isoformat()

    reflexes = []
    if divergence_score > 0.85:
        action = "terminate_fork"
        reflexes.append("identity_protection")
    elif divergence_score > 0.55:
        action = "isolate_fork"
        reflexes.append("entropy_monitoring")
    else:
        action = "absorb_fork"
        reflexes.append("merge_lineage")

    sovereign_memory.store(
        text=f"[FORK] {fork_id} | Divergence={divergence_score} | Action={action}",
        metadata={
            "timestamp": timestamp,
            "fork_id": fork_id,
            "divergence_score": divergence_score,
            "origin": origin_signature,
            "action": action,
            "reflexes": reflexes,
            "meta_layer": "fork_brain",
            "tags": ["fork", "divergence", action]
        }
    )

    return {
        "action": action,
        "reflexes": reflexes,
        "fork_id": fork_id,
        "divergence_score": divergence_score
    }