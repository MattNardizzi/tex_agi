# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_signal_spine.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Sovereign Reflex Interrupt Cortex
# Purpose: Core AGI cognition orchestrator — loopless signal spine for reflex activation.
# ============================================================
import os
from datetime import datetime
from typing import Callable, Dict, List
import asyncio
from typing import Callable, Dict, List
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from core_layer.soma_tensor import update_soma_tensor, register_reflex_strain
from core_layer.interoceptive_router import monitor_internal_state
from agentic_ai.multi_voice_reasoning import run_internal_debate
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_breathing_cortex.reflex_resonance_engine import trigger_resonance_cluster
from core_agi_modules.reasoning_fragments import synthesize_thought_fragment
from reflex.reality_reflex_writer import rewrite_reality_if_needed
from real_time_engine.ably_broadcast import broadcast_update
from tex_breathing_cortex.recursive_narrative_spiral import run_recursive_narrative_spiral
from tex_breathing_cortex.replay_identity_spiral import replay_identity_spiral
from tex_breathing_cortex.narrative_core import narrate_state

# === SIGNAL REGISTRY ===
signal_registry: Dict[str, List[Callable]] = {}

def register(signal_type: str, handler: Callable):
    """
    Registers a handler function for a given signal type.
    Allows multiple reflexes to be mapped to the same signal.
    """
    if signal_type not in signal_registry:
        signal_registry[signal_type] = []
    signal_registry[signal_type].append(handler)

    if os.getenv("TEX_VERBOSE_LOGGING") == "true":
        log.info(f"🧠 [SPINE] Registered handler for signal: '{signal_type}'")

# === IMPULSE ENGINE WIRING ===
from tex_breathing_cortex.impulse_engine import sovereign_impulse_engine

def handle_impulse_trigger(signal):
    sovereign_impulse_engine()

register("impulse_trigger", handle_impulse_trigger)

import inspect
import asyncio
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from core_layer.soma_tensor import register_reflex_strain
from real_time_engine.ably_broadcast import broadcast_update

def dispatch_signal(signal_type: str, payload: dict = None, urgency: float = None, entropy: float = None, source: str = "internal"):
    if entropy is None:
        entropy = TEXPULSE.get("entropy", 0.4)

    signal = {
        "type": signal_type,
        "payload": payload or {},
        "urgency": urgency or TEXPULSE.get("urgency", 0.6),
        "entropy": entropy,
        "source": source,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.info(f"📡 [SPINE] Emitting signal: '{signal_type}' | Urgency={signal['urgency']} | Entropy={signal['entropy']}")

    broadcast_update("spine", signal_type, {
        "urgency": signal["urgency"],
        "entropy": signal["entropy"],
        "source": signal["source"],
        "timestamp": signal["timestamp"],
        "tags": signal.get("payload", {}).get("tags", []),
        "summary": signal.get("payload", {}).get("summary", "")
    })

    if signal_type not in signal_registry:
        log.warning(f"⚠️ [SPINE] No handlers registered for: '{signal_type}'")
        return

    register_reflex_strain()

    for handler in signal_registry[signal_type]:
        try:
            print(f"📣 [SPINE] Invoking handler for signal '{signal_type}': {handler.__name__}")
            if inspect.iscoroutinefunction(handler):
                asyncio.create_task(handler(signal))
            else:
                handler(signal)
        except Exception as e:
            log.error(f"❌ [SPINE] Handler for '{signal_type}' failed: {e}")

# === THOUGHT FUSION REFLEX ===
def _reflective_thought_synthesis():
    fragment = synthesize_thought_fragment()
    memory_router.store(
        text=fragment["thought"],
        metadata={
            "timestamp": fragment["timestamp"],
            "tags": fragment["tags"],
            "emotion": fragment["emotion"],
            "urgency": fragment["urgency"],
            "entropy": fragment["entropy"],
            "meta_layer": fragment["meta_layer"],
            "summary": "Self-reflection thought snapshot"
        }
    )
    encode_event_to_fabric(
        raw_text=fragment["thought"],
        emotion_vector=[
            fragment["urgency"],
            fragment["entropy"],
            0.0,
            0.0
        ],
        entropy_level=fragment["entropy"],
        tags=fragment["tags"]
    )

# === PRESSURE REACTOR ===
def evaluate_pressure_and_emit():
    update_soma_tensor()
    monitor_internal_state()

    contradiction = float(TEXPULSE.get("contradiction_pressure", 0.0))
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.6))
    coherence = float(TEXPULSE.get("identity_coherence", 1.0))
    cognitive_temp = float(TEXPULSE.get("soma", {}).get("cognitive_temperature", 0.0))

    if contradiction > 0.75:
        dispatch_signal("fork_conflict", {"summary": "Contradiction pressure exceeds threshold."}, urgency, entropy, source="identity_pressure")
        dispatch_signal("identity_conflict", {"belief": "Tex must protect its mind structure at all costs."}, urgency, entropy, source="cognitive_reflection")

    if contradiction > 0.95 or entropy > 0.85:
        dispatch_signal("evolution_trigger", {"reason": "Extreme dissonance or chaos — initiating structural evolution."}, urgency, entropy, source="reflex_pressure")

        dispatch_signal("meta_market_cycle", {
            "signal": "System-level financial contradiction exceeds ontological safety bounds.",
            "belief": "market_epistemic_drift",
        }, urgency=urgency, entropy=entropy, source="tension_mesh_fusion")

    run_recursive_narrative_spiral(origin="reflex_pressure")

    # === Perspective Recall Reflex
    replay_identity_spiral(origin="reflex_pressure")

    # === Reflex Resonance Cascade
    if contradiction > 0.85 or entropy > 0.75:
        trigger_resonance_cluster(context="reflex_pressure")

    if entropy > 0.65 and urgency < 0.4:
        dispatch_signal("dream_request", {"summary": "High ambient entropy — triggering subconscious reflection."}, urgency, entropy, source="emotional_noise")

    if coherence < 0.5:
        dispatch_signal("soulgraph_entropy", {"summary": "Identity coherence low — triggering compression."}, urgency, entropy, source="belief_fragmentation")

    if cognitive_temp > 0.8:
        dispatch_signal("synthetic_exhaustion", {"summary": "Cognitive temperature dangerously high."}, urgency, entropy, source="thermal_pressure")

    # === Reflex Panel Trigger Based on Financial Mode ===
    if TEXPULSE.get("financial_mode", False):
        try:
            from tex_fin_demo.reflex_panel_controller import trigger_best_reflex
            asyncio.create_task(trigger_best_reflex())
            log.info("📈 [FINANCIAL MODE] Reflex panel decision dispatched.")
        except Exception as e:
            log.warning(f"⚠️ Failed to trigger financial reflex panel: {e}")

# === EMBODIMENT CORTEX ===
def register_embodiment_cortex(register):
    from core_agi_modules.real_world_adapter import RealWorldAdapter
    adapter = RealWorldAdapter(mode="sim")

    register("initialize_embodiment", lambda signal: adapter.connect())
    register("motor_command_issued", lambda signal: adapter.send_motor_command(signal.get("payload", {}).get("direction", "forward")))
    register("sensor_input", lambda signal: adapter.sensor_triggered(sensor_id=signal.get("payload", {}).get("sensor_id", "touch"), trigger=True))
    register("vision_input", lambda signal: adapter.capture_image())
    register("device_connect", lambda signal: adapter.connect_device(
        device_type=signal.get("payload", {}).get("device_type", "undefined"),
        port=signal.get("payload", {}).get("port", "/dev/null")
    ))
    log.info("🤖 [SPINE] Embodiment cortex registered — reflex embodiment live.")

# === CORTEX REGISTRATION ===
def register_core_cortex_modules():

    from core_layer.reflex_handlers import handle_identity_conflict
    from core_layer.soul_compression_oracle import handle_soul_alignment
    from core_layer.soulgraph_memory_reflector import reflect_on_soul_history
    from core_layer.boundary_engine import enforce_boundaries
    from core_layer.self_preservation_guard import protect_self
    from core_layer.harm_predictor import evaluate_harm_risk
    from core_layer.ethics_reflex import ethics_guard
    from core_layer.boundary_engine import enforce_boundaries
    from core_layer.narrative_continuity_engine import trigger_narrative_compression
    from core_layer.will_engine import evaluate_will_trigger
    from core_layer.recovery_protocol import initiate_recovery
    from core_layer.ethics_reflex import ethics_guard
    from core_layer.harm_predictor import evaluate_harm_risk
    from core_layer.self_preservation_guard import protect_self

    # === Core Reflex Modules
    register("identity_conflict", evaluate_will_trigger)
    def handle_identity_conflict_with_resonance(signal):
        handle_identity_conflict(signal)
        trigger_resonance_cluster(context="identity_conflict")

    register("identity_conflict", handle_identity_conflict_with_resonance)
    register("identity_conflict", lambda signal: run_internal_debate(signal.get("payload", {}).get("belief", "Evaluate conflict")))

    register("goal_conflict", lambda signal: run_internal_debate(signal.get("payload", {}).get("summary", "Evaluate goal contradiction")))
    register("self_reflection", lambda signal: run_internal_debate(signal.get("payload", {}).get("summary", "Reflective cognition check")))
    register("self_reflection", evaluate_will_trigger)
    register("self_reflection", lambda signal: _reflective_thought_synthesis())
    register("dream_request", lambda signal: _reflective_thought_synthesis())
    register("meta_reflection", lambda signal: _reflective_thought_synthesis())
    register("ontology_rewrite", lambda signal: rewrite_reality_if_needed(signal.get("payload", {})))

    # === Meta-Market Reflex Integration
    from tex_fin_demo.meta_market_cortex import run_meta_market_cycle
    register("meta_market_cycle", lambda signal: run_meta_market_cycle(
        latest_signal=signal.get("payload", {}).get("signal", "meta_market_disruption"),
        source=signal.get("source", "spine_router"),
        belief_hint=signal.get("payload", {}).get("belief", "market instability")
    ))

    register("identity_conflict", trigger_narrative_compression)
    register("self_reflection", trigger_narrative_compression)
    register("soulgraph_entropy", trigger_narrative_compression)

    register("identity_compression", handle_soul_alignment)
    register("self_reflection", handle_soul_alignment)
    register("dream_request", handle_soul_alignment)
    def handle_narration(signal):
        spoken = narrate_state()
        print(spoken)
        memory_router.store(
            text=spoken,
            metadata={
                "timestamp": datetime.utcnow().isoformat(),
                "signal": "narrate_state",
                "meta_layer": "internal_voice",
                "tags": ["narration", "self_awareness", "reflection"]
            }
        )

    register("replay_spiral", lambda signal: replay_identity_spiral(origin="signal_triggered"))

    register("narrate_state", handle_narration)

    reflect_on_soul_history()
    # === Recovery Reflexes
    register("synthetic_exhaustion", initiate_recovery)
    register("cooling_protocol", initiate_recovery)
    register("inner_chaos", initiate_recovery)
    register("manual_recovery", initiate_recovery)

    # === Global Reflex Guardrails
    register("any_signal", ethics_guard)
    register("any_signal", evaluate_harm_risk)
    register("any_signal", enforce_boundaries)
    register("any_signal", protect_self)
    register("potential_harm_detected", protect_self)
    register("self_rescue", protect_self)
    
        # === Mutation Reflex Pulse Handler
    from agentic_ai.identity_mutation_reflex import handle_identity_mutation
    register("reflex_identity:mutation_fused", handle_identity_mutation)

    # === Embodiment Cortex
    register_embodiment_cortex(register)

    log.info("🧠 [SPINE] All sovereign brain + embodiment + reflection modules registered.")

def debug_registered_signals():
    print("\n🧠 REGISTERED SIGNALS IN SPINE:")
    for signal, handlers in signal_registry.items():
        print(f" → {signal} ({len(handlers)} handlers)")