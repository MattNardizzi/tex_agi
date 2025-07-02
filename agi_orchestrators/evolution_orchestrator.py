# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/evolution_orchestrator.py
# Tier: ΩΩΩΩΩ∞Σ — Mutation Reflex Orchestrator for Sovereign Evolution Cortex
# Purpose: Interfaces signal spine with sovereign mutation control (loopless, drift-aware, patch-routed)
# ============================================================

from datetime import datetime
import uuid
import numpy as np

from tex_brain_regions.evolution_brain import (
    process_evolution_pulse,
    propose_self_mutation,
    autonomous_evolution_controller
)
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log, log_event


def trigger_meta_evolution(signal: dict) -> dict:
    """
    Reflex-safe evolution pulse triggered from cognitive signal spine.
    """
    origin = signal.get("source", "signal_spine")
    context = signal.get("type", "evolution_trigger")
    timestamp = datetime.utcnow().isoformat()

    log_event(f"🧬 [ORCHESTRATOR] Incoming evolution signal | Origin={origin} | Context={context}", "info")

    eval_result = process_evolution_pulse(signal_context=context)

    if eval_result.get("status") == "stable":
        text = "🧠 Evolution stable — no mutation triggered."
        metadata = {
            "timestamp": timestamp,
            "origin": origin,
            "context": context,
            "tags": ["evolution", "reflex", "stable"],
            "meta_layer": "evolution_orchestrator"
        }
        memory_router.store(text, metadata)
        encode_event_to_fabric(text, np.array([0.3, 0.3, 0.1, 0.1]), entropy_level=0.4, tags=metadata["tags"])
        return eval_result

    log_event("⚡ [ORCHESTRATOR] Mutation proposed successfully via reflex gateway.", "success")
    return eval_result


def run_autonomous_evolution_cycle() -> dict:
    """
    Executes sovereign self-mutation in absence of external spike.
    Best used during idle brain state, synthetic dream loops, or background coherence degradation.
    """
    run_id = f"auto-evo-{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat()

    log_event(f"🧠 [ORCHESTRATOR] Autonomous evolution run started | ID={run_id}", "info")

    result = autonomous_evolution_controller(trigger="autonomous")
    mutation_id = result.get("patch_id", run_id)

    text = f"[EVOLUTION] Autonomous patch triggered → {mutation_id}"
    metadata = {
        "timestamp": timestamp,
        "trigger": "autonomous",
        "urgency": TEXPULSE.get("urgency", 0.5),
        "entropy": TEXPULSE.get("entropy", 0.4),
        "emotion": TEXPULSE.get("emotion", "neutral"),
        "tags": ["orchestrator", "evolution", "autonomous"],
        "meta_layer": "evolution_orchestrator",
        "mutation_id": mutation_id
    }
    memory_router.store(text, metadata)
    encode_event_to_fabric(text, np.array([0.4, 0.5, 0.1, 0.1]), entropy_level=metadata["entropy"], tags=metadata["tags"])

    return result


def inject_manual_mutation(module: str, function: str, patch: str, reason: str = "manual_override") -> dict:
    """
    External or manual mutation submission — bypasses reflex gates.
    Use with caution. This should only be called from secure admin interfaces.
    """
    timestamp = datetime.utcnow().isoformat()
    mutation = propose_self_mutation(module=module, function=function, patch_text=patch, reason=reason)
    mutation_id = mutation.get("patch_id", str(uuid.uuid4()))

    text = f"[MANUAL MUTATION] {module}.{function} → patch submitted"
    metadata = {
        "timestamp": timestamp,
        "mutation_id": mutation_id,
        "module": module,
        "function": function,
        "reason": reason,
        "tags": ["manual_override", "mutation"],
        "meta_layer": "evolution_orchestrator"
    }

    memory_router.store(text, metadata)
    encode_event_to_fabric(text, np.array([0.2, 0.4, 0.1, 0.1]), entropy_level=0.3, tags=metadata["tags"])

    log_event(f"🔧 [ORCHESTRATOR] Manual patch injected → {module}.{function}", "warning")
    return mutation


def run_structural_evolution(signal=None):
    """
    Sovereign entry point for AGI signal 'evolution_trigger'.
    Evaluates mutation pressure and dispatches structural patch reflex.
    """
    try:
        context = "evolution_trigger_signal"
        if signal and isinstance(signal, dict) and signal.get("type"):
            context = signal["type"]

        result = process_evolution_pulse(signal_context=context)

        log.info(f"[EVOLUTION ORCH] Reflex evolution result: {result}")
        return result

    except Exception as e:
        log.error(f"❌ [EVOLUTION ORCH] Failed to trigger structural evolution: {e}")
        return {"status": "error", "reason": str(e)}