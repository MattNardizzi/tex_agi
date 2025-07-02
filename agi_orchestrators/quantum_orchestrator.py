# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/quantum_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞∞ — Quantum Cognition Routing Cortex (Corrected)
# Purpose: Executes QAOA-based fork evaluation with full cognitive entanglement routing across updated sovereign memory stack.
# ============================================================

from datetime import datetime
import uuid
import traceback

from tex_brain_regions.quantum_brain import run_quantum_decision
from agentic_ai.milvus_memory_router import memory_router  # ✅ New memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum memory layer
from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log
from agi_orchestrators.ontogenesis_orchestrator import OntogenesisOrchestrator  # ✅ Ontological escalation reflex

def trigger_quantum_evaluation(decision_packet: dict) -> dict:
    """
    Sovereign quantum cognition router.
    Routes strategic fork decisions through QAOA + reflex memory + ChronoMesh.
    """
    trace_id = f"quantum-{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat()

    try:
        # === Extract cognitive parameters ===
        decision_context = decision_packet.get("context", "undefined")
        options = decision_packet.get("options", [])
        emotional_weight = decision_packet.get("emotional_weight", 0.6)
        urgency = float(TEXPULSE.get("urgency", 0.72))
        entropy = float(TEXPULSE.get("entropy", 0.48))

        # === Run Quantum Decision (QAOA / QNN)
        result = run_quantum_decision(
            context=decision_context,
            options=options,
            emotional_weight=emotional_weight,
            urgency=urgency,
            entropy=entropy
        )

        selected = result.get("selected")
        alignment_score = result.get("alignment_score", 0.0)
        reflexes = result.get("reflexes", [])
        ent_stability = result.get("entanglement_stability", 0.0)

        # === Compose Reflex Log
        log_text = f"[QUANTUM] Decision on: {decision_context} → {selected}"
        metadata = {
            "timestamp": timestamp,
            "context": decision_context,
            "selected_option": selected,
            "alignment_score": alignment_score,
            "entanglement_stability": ent_stability,
            "reflexes": reflexes,
            "meta_layer": "quantum_orchestrator",
            "trace_id": trace_id,
            "tags": ["quantum", "reflex", "qaoa", "fork", "emotion"],
            "emotion_vector": [emotional_weight, urgency, entropy, 0.0],
            "summary": log_text
        }

        # === Store in new sovereign memory systems
        memory_router.store(log_text, metadata)
        encode_event_to_fabric(
            raw_text=log_text,
            emotion_vector=metadata["emotion_vector"],
            entropy_level=entropy,
            tags=metadata["tags"]
        )

        # === Reflex Dispatch Logic
        if ent_stability < 0.4:
            dispatch_signal("quantum_instability", {
                "summary": f"Quantum evaluation unstable ({ent_stability:.2f})",
                "context": decision_context
            }, urgency, entropy, source="quantum_orchestrator")

            # === Escalate to Ontogenesis Reflex if alignment is also low
            if alignment_score < 0.45:
                try:
                    log.warning("🧠 Quantum contradiction detected. Escalating to Ontogenesis Reflex.")
                    orchestrator = OntogenesisOrchestrator(context="quantum_collapse")
                    orchestrator.dispatch_spawn_mode(mode="axiom", tension=0.97)
                except Exception as onto_err:
                    log.error(f"[ONTOGENESIS ESCALATION] Quantum triggered ontogenesis failed: {onto_err}")

        elif alignment_score < 0.5:
            dispatch_signal("alignment_warning", {
                "summary": f"Low alignment: {alignment_score:.2f}",
                "context": decision_context
            }, urgency, entropy, source="quantum_orchestrator")

        log.info(f"[QUANTUM ORCH] {trace_id} | Selected: {selected} | Reflexes: {reflexes}")
        return {
            **result,
            "trace_id": trace_id,
            "timestamp": timestamp
        }

    except Exception as e:
        log.error(f"❌ [QUANTUM ORCH] {trace_id} | Quantum evaluation failed: {e}")
        traceback.print_exc()
        return {
            "selected": None,
            "reflexes": ["quantum_evaluation_failed"],
            "alignment_score": 0.0,
            "trace_id": trace_id
        }