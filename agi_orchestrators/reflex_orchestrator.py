# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/reflex_orchestrator.py
# Tier: ΩΩΩ∞∞ — Reflex Arbitration Cortex (Selector + Utility + Mesh + Chrono + Ontology)
# Purpose: Sovereign signal-to-reflex arbitration cortex with reflex selector integration,
#          utility scoring, stochastic gating, mutation hooks, memory entanglement,
#          and reality rewrite override capability.
# ============================================================

from datetime import datetime
import uuid
import numpy as np

from tex_brain_regions.reflex_brain import resolve_reflex
from tex_brain_regions.evolution_brain import autonomous_evolution_controller
from core_agi_modules.curiosity_reflex import CuriosityReflex
from core_layer.reflex_handlers import handle_identity_conflict

from core_agi_modules.recursive_utility_engine import compute_recursive_utility
from core_agi_modules.reflex_mesh_router import should_route_signal
from core_agi_modules.reflex_priority_matrix import ReflexPriorityMatrix
from core_agi_modules.reflex_selector import ReflexSelector

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

from reflex.reality_reflex_writer import rewrite_reality_if_needed  # ✨ Ontological override core

# === Global Modules ===
PRIORITY_MATRIX = ReflexPriorityMatrix()
SELECTOR = ReflexSelector()

def run_sensor_reflex(signal: dict) -> dict:
    """
    Sovereign reflex arbitration engine. Executes loopless, weighted, utility-aligned reflex decisioning.
    """
    trace_id = f"reflex-{uuid.uuid4().hex[:6]}"
    try:
        # === Signal Decomposition ===
        signal_type = signal.get("signal", "undefined")
        source = signal.get("source", "unspecified")
        urgency = float(signal.get("urgency", TEXPULSE.get("urgency", 0.72)))
        entropy = float(signal.get("entropy", TEXPULSE.get("entropy", 0.41)))
        emotion = signal.get("emotion", TEXPULSE.get("emotion", "neutral"))
        goal = signal.get("goal", "undefined")
        timestamp = datetime.utcnow().isoformat()

        # === Gating: Reflex Mesh Router ===
        gate = should_route_signal(signal_type)
        if not gate["routed"]:
            log.warning(f"⛔ [REFLEX ORCH] Signal '{signal_type}' gated by reflex mesh (p={gate['probability']})")
            return {
                "reflexes": [],
                "utility_score": 0.0,
                "dominant_factor": "mesh_blocked",
                "routed": False,
                "trace_id": f"mesh-blocked-{uuid.uuid4().hex[:6]}"
            }

        # === Step 1: Sovereign Utility Score ===
        utility = compute_recursive_utility({
            "emotion": emotion,
            "goal": goal,
            "urgency": urgency,
            "entropy": entropy,
            "timestamp": timestamp,
            "factual": signal.get("factual", True)
        }, cycle_id=0)

        final_score = utility["final_utility"]
        dominant = utility["dominant_factor"]
        mutation_flag = utility["mutation_recommended"]
        override_flag = utility["reflex_override"]

        # === Ontological Threshold Check ===
        if final_score < 0.2 and entropy > 0.7:
            log.info("🔮 [REFLEX ORCH] Reflex dissonance high — attempting reality rewrite.")
            rewrite_reality_if_needed(trigger_reason=signal_type, contradiction_level=entropy)

        # === Step 2: Reflex Resolution + Selector Synthesis ===
        resolved = set(resolve_reflex(signal=signal_type, urgency=urgency, entropy=entropy, source=source))
        selected = set(r for r, _ in SELECTOR.evaluate(current_goal=goal))
        reflexes = list(resolved.union(selected))

        # === Step 3: Priority Matrix Weighting ===
        weighted = []
        for reflex in reflexes:
            weight = PRIORITY_MATRIX.get_weight(reflex)
            if weight < 0.6:
                log.warning(f"⚠️ [REFLEX ORCH] Reflex '{reflex}' suppressed (w={weight})")
                continue
            weighted.append((reflex, weight))

        emotion_vector = [urgency, entropy, 0.0, 0.0]

        # === Step 4: Log Reflex Arbitration ===
        summary = f"[REFLEX] '{signal_type}' → {len(weighted)} reflexes | Utility={final_score} ({dominant})"
        metadata = {
            "timestamp": timestamp,
            "trace_id": trace_id,
            "signal_type": signal_type,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "source": source,
            "goal": goal,
            "reflexes": [r for r, _ in weighted],
            "reflex_weights": {r: w for r, w in weighted},
            "dominant": dominant,
            "utility": final_score,
            "override_flag": override_flag,
            "mutation_recommended": mutation_flag,
            "routed": True,
            "meta_layer": "reflex_orchestration",
            "tags": ["reflex", "selector", "utility", "routing"]
        }

        memory_router.store(summary, metadata)
        try:
            encode_event_to_fabric(
                raw_text=summary,
                emotion_vector=np.array(emotion_vector),
                entropy_level=entropy,
                tags=metadata["tags"]
            )
        except Exception as e:
            log.warning(f"⚠️ [CHRONOFABRIC] Entanglement failed: {e}")

        log.info(f"[REFLEX ORCH] [{trace_id}] Signal='{signal_type}' | Reflexes={weighted} | Utility={final_score}")

        # === Step 5: Execute Reflex Paths ===
        reflex_names = [r for r, _ in weighted]

        if override_flag:
            log.warning("[REFLEX ORCH] 🔐 Sovereign override active — dominant=alignment, low integrity/consensus")

        if mutation_flag or "trigger_self_mutator" in reflex_names:
            log.info("🧬 [REFLEX ORCH] Mutation reflex triggered.")
            autonomous_evolution_controller(signal_context="reflex_mutation_trigger")

        if "exploratory" in reflex_names or signal_type in {"novelty", "rare_entropy", "unclassified"}:
            try:
                CuriosityReflex().scan_for_anomalies()
                log.info(f"🧠 [REFLEX ORCH] Curiosity engaged for '{signal_type}'")
            except Exception as e:
                log.warning(f"[REFLEX ORCH] Curiosity error: {e}")

        if "identity_conflict" in reflex_names or signal_type == "belief_conflict":
            try:
                handle_identity_conflict(signal)
                log.info("🔍 [REFLEX ORCH] Identity conflict resolved.")
            except Exception as e:
                log.warning(f"[REFLEX ORCH] Identity handler error: {e}")

        return {
            "reflexes": reflex_names,
            "utility_score": final_score,
            "dominant_factor": dominant,
            "routed": True,
            "trace_id": trace_id
        }

    except Exception as e:
        log.error(f"❌ [REFLEX ORCH] Arbitration failure: {e}")
        return {
            "reflexes": ["reflex_routing_failed"],
            "utility_score": 0.0,
            "dominant_factor": "exception",
            "routed": False,
            "trace_id": f"reflex-error-{uuid.uuid4().hex[:6]}"
        }
