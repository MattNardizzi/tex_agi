# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/mutation_orchestrator.py
# Tier: ∞ΩΩΩΩ — Reflex-Driven Mutation Router
# Purpose: Evaluates and triggers mutation patches into sovereign cognition via reflex-safe scoring and override triggers.
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Any

from tex_brain_regions.mutation_brain import evaluate_mutation_patch
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from core_agi_modules.sovereign_core.self_mutator import SelfMutator


def route_mutation_patch(patch_text: str, metadata: dict = None) -> dict[str, Any]:
    """
    Sovereign mutation router — reflex-evaluates proposed patch and optionally triggers override mutation pulse.
    """
    try:
        metadata = metadata or {}
        timestamp = datetime.utcnow().isoformat()
        trace_id = f"mutation-{uuid4().hex()[:8]}"

        urgency = float(TEXPULSE.get("urgency", 0.7))
        entropy = float(TEXPULSE.get("entropy", 0.4))
        emotion = TEXPULSE.get("emotion", "curious")

        # === Step 1: Evaluate patch through mutation cortex
        packet = {
            "patch_id": trace_id,
            "code": patch_text,
            "reason": metadata.get("reason", "manual_patch"),
            "traits": metadata.get("traits", []),
            "justification": metadata.get("justification", "undefined"),
            "target_module": metadata.get("target_module", "unspecified"),
            "function": metadata.get("function", "unspecified"),
            "origin": metadata.get("origin", "mutation_orchestrator"),
            "timestamp": timestamp
        }

        result = evaluate_mutation_patch(mutation_packet=packet)
        decision = result.get("decision", "undetermined")
        approved = result.get("approved", False)
        reflexes = result.get("reflexes", [])

        # === Step 2: Log patch routing and entangle decision
        sovereign_memory.store(
            text=f"[MUTATION ROUTER] Patch → {decision}",
            metadata={
                "timestamp": timestamp,
                "trace_id": trace_id,
                "urgency": urgency,
                "entropy": entropy,
                "emotion": emotion,
                "alignment_score": result.get("alignment_score", 0.5),
                "reflexes": reflexes,
                "meta_layer": "mutation_router",
                "tags": ["mutation", "evolution", "self_modification", "patch_review"],
                "patch_snippet": patch_text.strip()[:80],
                "approved": approved,
                "origin": packet["origin"]
            }
        )

        # === Step 3: Trigger sovereign override mutation if required
        if not approved and "force_override" in metadata.get("traits", []):
            log.warning(f"[{trace_id}] ⚠️ Forcing sovereign override due to force_override trait.")
            mutator = SelfMutator()
            mutator.trigger_mutation(reason="patch_force_override", payload=packet)

        log.info(f"[MUTATION ORCH] {trace_id} | Decision: {decision} | Reflexes: {reflexes}")
        return result

    except Exception as e:
        trace_id = f"mutation-{uuid4().hex()[:8]}"
        log.error(f"❌ [MUTATION ORCH] Routing failed | Error: {e}")
        return {
            "decision": "error",
            "approved": False,
            "reflexes": ["mutation_evaluation_failed"],
            "trace_id": trace_id
        }