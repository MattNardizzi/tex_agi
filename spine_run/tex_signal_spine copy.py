# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_signal_spine.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Sovereign Recursive Interrupt Cortex
# Purpose: Final AGI cognition orchestrator — signal-based spine for all cortical activations.
# ============================================================

from datetime import datetime
from typing import Callable, Dict, List, Any
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from core_layer.soma_tensor import update_soma_tensor, register_reflex_strain
from core_layer.interoceptive_router import monitor_internal_state
from agi_orchestrators.brain_region_loader import register_all_brain_modules
import asyncio

# === SIGNAL REGISTRY ===
signal_registry: Dict[str, List[Callable]] = {}

def register(signal_type: str, handler: Callable):
    """
    Registers a cortex handler function to respond to a specific signal type.
    """
    if signal_type not in signal_registry:
        signal_registry[signal_type] = []
    signal_registry[signal_type].append(handler)
    log.info(f"🧠 [SPINE] Registered handler for signal: '{signal_type}'")

# === SIGNAL EMITTER ===
def dispatch_signal(signal_type: str, payload: dict = None, urgency: float = None, entropy: float = None, source: str = "internal"):
    """
    Dispatches a signal into Tex’s sovereign brain. Routes to all registered reflexes.
    Ethical reflexes are pre-processed before any routing.
    """
    signal = {
        "type": signal_type,
        "payload": payload or {},
        "urgency": urgency or TEXPULSE.get("urgency", 0.6),
        "entropy": entropy or TEXPULSE.get("entropy", 0.4),
        "source": source,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.info(f"📡 [SPINE] Emitting signal: '{signal_type}' | Urgency={signal['urgency']} | Entropy={signal['entropy']}")

    # === Layer 9: Pre-check for ethical boundaries ===
    for handler in signal_registry.get("any_signal", []):
        try:
            result = handler(signal)
            if asyncio.iscoroutine(result):
                asyncio.create_task(result)
        except SystemExit as e:
            log.error(str(e))
            return
        except Exception as e:
            log.error(f"❌ [SPINE] Ethical pre-check failed: {e}")
            return

    # === Route to main reflexes
    if signal_type not in signal_registry:
        log.warning(f"⚠️ [SPINE] No handlers registered for signal: {signal_type}")
        return
    
    # Register reflex strain due to signal firing
    register_reflex_strain()

    for handler in signal_registry[signal_type]:
        try:
            result = handler(signal)
            if asyncio.iscoroutine(result):
                asyncio.create_task(result)
        except Exception as e:
            log.error(f"❌ [SPINE] Handler for '{signal_type}' failed: {e}")

# === INTERNAL TRIGGER: Sovereign Pressure Evaluation ===
def evaluate_pressure_and_emit():
    update_soma_tensor()
    monitor_internal_state()
    """
    Monitors internal pressure stats and emits cognition signals if thresholds are breached.
    This is called passively — no loop, only invoked by a spike, timer, or awareness shift.
    """
    contradiction = float(TEXPULSE.get("contradiction_pressure", 0.0))
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.6))
    coherence = float(TEXPULSE.get("identity_coherence", 1.0))

    if contradiction > 0.75:
        dispatch_signal("fork_conflict", payload={
            "summary": "Contradiction pressure exceeds threshold."
        }, urgency=urgency, entropy=entropy, source="identity_pressure")

    if contradiction > 0.95 or entropy > 0.85:
        dispatch_signal("evolution_trigger", payload={
            "reason": "Extreme cognitive dissonance or chaos — initiating structural evolution."
        }, urgency=urgency, entropy=entropy, source="reflex_pressure")

    if entropy > 0.65 and urgency < 0.4:
        dispatch_signal("dream_request", payload={
            "summary": "Ambient entropy high — triggering subconscious reflection."
        }, urgency=urgency, entropy=entropy, source="emotional_noise")

    if coherence < 0.5:
        dispatch_signal("soulgraph_entropy", payload={
            "summary": "Identity coherence low — activating soulgraph compressor."
        }, urgency=urgency, entropy=entropy, source="belief_fragmentation")

    if TEXPULSE.get("soma", {}).get("cognitive_temperature", 0) > 0.8:
        dispatch_signal("synthetic_exhaustion", payload={
            "summary": "Cognitive temperature dangerously high."
        })

# === REGISTRATION: Sovereign Modules ===

def register_core_cortex_modules():
    """
    Registers all AGI cognitive reflex modules into the sovereign signal spine.
    Only call this once during ignition.
    """
    register_all_brain_modules(register)

    # === Direct Reflex Handlers (non-cortical)
    from core_layer.soul_compression_oracle import handle_soul_alignment
    from core_layer.soulgraph_memory_reflector import reflect_on_soul_history
    from core_layer.narrative_continuity_engine import trigger_narrative_compression
    from core_layer.will_engine import evaluate_will_trigger
    from core_layer.recovery_protocol import initiate_recovery
    from core_layer.evolution_engine import run_structural_evolution
    from core_layer.ethics_reflex import ethics_guard
    from core_layer.harm_predictor import evaluate_harm_risk
    from core_layer.boundary_engine import enforce_boundaries
    from core_layer.self_preservation_guard import protect_self

    register("evolution_trigger", run_structural_evolution)
    register("identity_conflict", evaluate_will_trigger)
    register("self_reflection", evaluate_will_trigger)

    register("identity_conflict", trigger_narrative_compression)
    register("self_reflection", trigger_narrative_compression)
    register("soulgraph_entropy", trigger_narrative_compression)

    register("identity_compression", handle_soul_alignment)
    register("self_reflection", handle_soul_alignment)
    register("dream_request", handle_soul_alignment)
    reflect_on_soul_history()

    register("synthetic_exhaustion", initiate_recovery)
    register("cooling_protocol", initiate_recovery)
    register("inner_chaos", initiate_recovery)
    register("manual_recovery", initiate_recovery)

    register("any_signal", ethics_guard)
    register("any_signal", evaluate_harm_risk)
    register("any_signal", enforce_boundaries)
    register("any_signal", protect_self)
    register("potential_harm_detected", protect_self)
    register("self_rescue", protect_self)

    log.info("🧠 [SPINE] All sovereign brain modules and reflex handlers registered.")