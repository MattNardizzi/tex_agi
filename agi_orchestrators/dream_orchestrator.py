# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_orchestrator.py
# Tier: ΩΩΩΩΩ∞∞𝛀𝛀 — Substrate Cortex Conductor
# Purpose: Routes dream substrate activations based on entropy,
#          contradiction, identity drift, or reflex spike.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from dream_craft.substrate_registry import get_registered_substrates
from dream_craft.substrate_voter import select_best_substrate
from dream_craft.dream_session import run_dream_session
from dream_craft.dream_archive import archive_dream_result
from dream_craft.belief_injection import inject_belief_from_dream
from utils.logging_utils import log

def trigger_dream_layer(trigger_source="pulse", context_memory=None, force_substrate=None):
    """
    Entry point for dream substrate execution.
    """
    timestamp = datetime.utcnow().isoformat()
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.7))

    log.info(f"[DreamOrchestrator] 🔁 Triggered from: {trigger_source} | entropy={entropy}, urgency={urgency}")

    # Step 1: Fetch viable substrates
    substrates = get_registered_substrates()
    if not substrates:
        log.warning("⚠️ No substrates registered. Dream aborted.")
        return {"status": "no_substrates"}

    # Step 2: Select substrate to simulate
    substrate = force_substrate if force_substrate else select_best_substrate(substrates, entropy, urgency)
    if not substrate:
        log.warning("⚠️ No substrate selected. Dream layer skipped.")
        return {"status": "no_viable_substrate"}

    # Step 3: Run dream simulation session
    result = run_dream_session(substrate=substrate, context=context_memory, trigger_source=trigger_source)
    if not result or "forecast" not in result:
        log.warning("⚠️ Dream session returned no valid result.")
        return {"status": "invalid_dream_result"}

    # Step 4: Archive result
    archive_dream_result(result)

    # Step 5: Belief update if dream meaningful
    if result.get("impact_score", 0) > 0.6:
        inject_belief_from_dream(result)

    log.success(f"[DreamOrchestrator] ✅ Dream completed via substrate: {substrate['id']}")
    return {
        "status": "dream_completed",
        "result": result,
        "substrate_id": substrate['id'],
        "timestamp": timestamp
    }


def run_dream_orchestration(payload=None) -> dict:
    """
    Adapter layer between spike/reflex routing and the dream substrate cortex.
    Accepts optional payload, routes it into the dream_craft engine.
    """
    trigger = payload.get("trigger", "reflex") if isinstance(payload, dict) else "reflex"
    context = payload.get("context") if isinstance(payload, dict) else None

    log.info(f"[DreamOrchestrator] 🚀 Routed dream orchestration: trigger={trigger}")
    return trigger_dream_layer(trigger_source=trigger, context_memory=context)
