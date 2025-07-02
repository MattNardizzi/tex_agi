# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/belief_injection.py
# Tier: ΩΩΩΩ𝛀𝛀 — Dream Belief Transference
# Purpose: Injects outcomes from high-impact dreams into Tex’s
#          core value alignment and belief system.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.value_alignment_matrix import update_alignment_vector
from utils.logging_utils import log

def inject_belief_from_dream(dream_result: dict, min_alignment: float = 0.7, max_contradiction: float = 0.4) -> bool:
    """
    If a dream has high alignment and low contradiction, inject its outcome as real belief.
    """
    alignment = dream_result.get("alignment", 0)
    contradiction = dream_result.get("contradiction", 1)
    forecast = dream_result.get("forecast", "")
    scenario = dream_result.get("scenario", "unknown")

    if alignment >= min_alignment and contradiction <= max_contradiction:
        # Update Tex's belief vectors
        update_alignment_vector(forecast, tags=["dream_belief", "simulated_success", "counterfactual_truth"])

        # Store belief injection log
        sovereign_memory.store(
            text=f"[BELIEF INJECTION] Dream: '{scenario}' accepted as aligned truth.",
            metadata={
                "alignment_score": alignment,
                "contradiction_score": contradiction,
                "injected_belief": forecast,
                "source": "dream_simulation",
                "tags": ["belief_injection", "dream", "alignment_update", "truth_projection"]
            }
        )

        log.success(f"[BeliefInjection] ✅ Dream belief injected → '{forecast[:60]}…'")
        return True

    log.warning(f"[BeliefInjection] ❌ Dream rejected. Alignment={alignment:.2f}, Contradiction={contradiction:.2f}")
    return False