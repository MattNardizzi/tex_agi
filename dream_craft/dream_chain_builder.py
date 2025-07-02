# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_chain_builder.py
# Tier: ΩΩΩ∞∞∞ — Recursive Forecast Architect
# Purpose: Builds recursive chains of dreams using substrate mutation,
#          simulating long-horizon futures and divergent forks.
# ============================================================

from dream_craft.dream_session import run_dream_session
from dream_craft.dream_mutator import mutate_substrate
from dream_craft.dream_archive import archive_dream_result
from dream_craft.belief_injection import inject_belief_from_dream
from utils.logging_utils import log

def build_dream_chain(initial_substrate: dict, depth: int = 3, context: list = None) -> list:
    """
    Runs a recursive dream simulation chain by evolving the substrate at each stage.
    """
    current_substrate = initial_substrate
    chain_results = []

    log.info(f"[DreamChainBuilder] 🔁 Starting dream chain with depth: {depth}")

    for step in range(depth):
        result = run_dream_session(substrate=current_substrate, context=context, trigger_source=f"chain_step_{step}")
        if not result or "forecast" not in result:
            log.warning(f"[DreamChainBuilder] ⚠️ Step {step} failed. Halting chain.")
            break

        archive_dream_result(result)

        if result.get("impact_score", 0.7) > 0.65:
            inject_belief_from_dream(result)

        chain_results.append(result)
        current_substrate = mutate_substrate(current_substrate, result)

    log.success(f"[DreamChainBuilder] ✅ Dream chain completed with {len(chain_results)} stages.")
    return chain_results