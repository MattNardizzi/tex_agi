# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: brain_layer/spike_action_router.py
# Tier: ΩΩΩΩΩ-State Reflex Sovereignty∞++ — AEI Spike Dispatcher w/ Causal Memory + Quantum-Soulgraph Entanglement
# ============================================================

from datetime import datetime
import uuid

from evolution_layer.sovereign_evolution_arena import inject_mutation_feedback
from dream_craft.dream_orchestrator import trigger_dream_layer  # ✅ Modern reflex-driven dream engine
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.intent_object import IntentObject
from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from agi_orchestrators.goal_orchestrator import GoalOrchestrator

# === CORE SPIKE DISPATCHER ===
def spike_action_router(spike_meta):
    classification = spike_meta.get("classification", "general_spike")
    cycle = spike_meta.get("cycle", 0)
    emotion = TEXPULSE.get("mood", "neutral")
    urgency = spike_meta.get("vector", [0, 0, 0, 0])[0]
    entropy = spike_meta.get("vector", [0, 0, 0, 0])[1]
    trust_score = spike_meta.get("vector", [0, 0, 0, 0])[2]

    reflex_id = f"reflex-{uuid.uuid4().hex[:6]}"
    intent = IntentObject(reflex_id, source="spike_action_router")

    reflex_score = round(entropy * 0.4 + urgency * 0.4 + (1 - trust_score) * 0.2, 4)
    timestamp = datetime.utcnow().isoformat()

    try:
        # === Dispatch based on reflex type
        match classification:
            case "contradiction_override":
                trigger_sovereign_override({
                    "reason": "neuromorphic contradiction",
                    "heat": reflex_score,
                    "intent_id": intent.id,
                    "spike_meta": spike_meta,
                    "cycle": cycle
                })

            case "entropy_alert":
                trigger_dream_layer(
                    trigger_source="spike_entropy",
                    context_memory=[spike_meta]
                )

            case "high_urgency_reflex":
                inject_mutation_feedback({
                    "reason": "urgency spike",
                    "spike": spike_meta,
                    "trigger": "neuromorphic_spike",
                    "cycle": cycle,
                    "intent_id": intent.id
                })

            case "identity_drift":
                trigger_dream_layer(
                    trigger_source="spike_identity_drift",
                    context_memory=[spike_meta]
                )

            case _:
                GoalOrchestrator().process_goal_signal({
                    "goal": "Trace reflex origin: scan cognitive strain factors",
                    "context": "spike_router",
                    "reflex_score": reflex_score,
                    "urgency": urgency,
                    "entropy": entropy,
                    "emotion": emotion,
                    "cycle": cycle,
                    "origin": spike_meta
                })

        # === Unified Reflex Memory Log (Vector + Quantum)
        sovereign_memory.store(
            text=f"[SPIKE_ROUTER] Reflex '{reflex_id}' routed ░ Class: {classification}",
            metadata={
                "type": "spike_action_trace",
                "reflex_id": reflex_id,
                "classification": classification,
                "reflex_score": reflex_score,
                "timestamp": timestamp,
                "emotion": emotion,
                "intent_id": intent.id,
                "reflex_origin": spike_meta,
                "emotion_vector": [urgency, entropy, 0.0, 0.0],
                "tags": ["reflex", "spike_router", classification],
                "meta_layer": "symbolic_trace"
            }
        )

        # === Soulgraph Imprint
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Reflex '{reflex_id}' processed as '{classification}' and routed",
            source="spike_action_router",
            emotion=emotion,
            tags=["spike", "belief", classification]
        )

    except Exception as e:
        sovereign_memory.store(
            text=f"[ERROR] Spike router failure ░ Reflex='{reflex_id}' ░ Error: {str(e)}",
            metadata={
                "type": "spike_router_failure",
                "error": str(e),
                "reflex_id": reflex_id,
                "classification": classification,
                "cycle": cycle,
                "timestamp": timestamp,
                "intent_id": intent.id,
                "tags": ["reflex", "router", "failure"]
            }
        )