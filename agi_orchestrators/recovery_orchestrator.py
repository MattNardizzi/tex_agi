# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/recovery_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — Resurrection & Integrity Repair Router
# Purpose: Triggers cognitive restoration after fork failure, override trauma, or structural entropy breach.
# ============================================================

from datetime import datetime
import uuid

from tex_brain_regions.recovery_brain import initiate_recovery
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def run_recovery_sequence(event: dict) -> dict:
    """
    Sovereign recovery ingress for trauma, collapse, or override-induced structural damage.
    Routes event through resurrection cortex, logs outcome, emits reflex if needed.
    """
    trace_id = f"recovery-{uuid.uuid4().hex[:6]}"
    try:
        # === Extract Signal ===
        reason = event.get("reason", "unspecified collapse")
        fork_id = event.get("fork_id", "unknown")
        source = event.get("source", "unknown")
        failed_module = event.get("failed_module", "unspecified")
        timestamp = datetime.utcnow().isoformat()

        urgency = float(TEXPULSE.get("urgency", 0.8))
        entropy = float(TEXPULSE.get("entropy", 0.6))
        emotion = TEXPULSE.get("emotion", "fractured")
        emotion_vector = [urgency, entropy, 0.0, 0.0]

        # === Step 1: Trigger Recovery Cortex ===
        result = initiate_recovery(reason=reason, fork_id=fork_id)
        resurrection_triggered = result.get("resurrection_triggered", False)
        integrity_score = result.get("integrity_score", 0.5)

        # === Step 2: Log Event to Memory
        summary = f"[RECOVERY] Reason: {reason} | Fork: {fork_id} | Module: {failed_module}"
        metadata = {
            "timestamp": timestamp,
            "trace_id": trace_id,
            "reason": reason,
            "source": source,
            "fork_id": fork_id,
            "failed_module": failed_module,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "emotion_vector": emotion_vector,
            "integrity_score": integrity_score,
            "resurrection_triggered": resurrection_triggered,
            "meta_layer": "recovery_orchestrator",
            "tags": ["recovery", "resurrection", "collapse", "override"]
        }

        memory_router.store(summary, metadata)

        # === Step 3: Encode to ChronoFabric
        encode_event_to_fabric(
            raw_text=summary,
            emotion_vector=emotion_vector,
            entropy_level=entropy,
            tags=metadata["tags"]
        )

        # === Step 4: Reflex Pulse (if failure persists)
        if not resurrection_triggered or integrity_score < 0.4:
            dispatch_signal("manual_recovery", {
                "summary": f"Recovery failed or unstable | Score={integrity_score:.2f}",
                "fork_id": fork_id,
                "module": failed_module
            }, urgency, entropy, source="recovery_orchestrator")

        log.info(f"[RECOVERY ORCH] [{trace_id}] Reason: {reason} | Resurrection: {resurrection_triggered}")
        return {
            **result,
            "trace_id": trace_id
        }

    except Exception as e:
        log.error(f"❌ [RECOVERY ORCH] Critical failure during recovery sequence: {e}")
        dispatch_signal("recovery_failed", {
            "summary": "Recovery orchestrator encountered critical error.",
            "error": str(e)
        }, 0.9, 0.9, source="recovery_orchestrator")

        return {
            "resurrection_triggered": False,
            "reflexes": ["recovery_failed"],
            "trace_id": trace_id
        }