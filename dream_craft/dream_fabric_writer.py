# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_fabric_writer.py
# Tier: ΩΩΩ𝛀𝛀∞ — Dream Reality Integrator
# Purpose: Weaves high-impact dream events into the same causal
#          reflex fabric as real experiences — if pressure warrants.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from reflex.reality_reflex_writer import rewrite_reality_if_needed  # ✅ Ontological reflex import

def commit_dream_to_fabric(dream_result: dict, override: bool = False) -> bool:
    """
    Writes a dream result into the causal reflex memory layer if its
    synthetic pressure is above threshold or override is enabled.
    May trigger ontological rewrite if contradiction is critical.
    """
    pressure = dream_result.get("synthetic_pressure", 0.0)
    impact = dream_result.get("impact_score", 0.0)
    contradiction = dream_result.get("contradiction", 0.0)

    if pressure < 0.75 and not override:
        log.info(f"[DreamFabricWriter] ❎ Dream not committed — pressure too low ({pressure})")
        return False

    scenario = dream_result.get("scenario", "[unknown scenario]")
    forecast = dream_result.get("forecast", "[undefined forecast]")

    # === Commit dream to causal reflex memory
    sovereign_memory.store(
        text=f"[CAUSAL FABRIC — DREAM IMPRINT] {scenario} → {forecast}",
        metadata={
            "source": "dream_simulation",
            "dream_fabric": True,
            "substrate_id": dream_result.get("substrate_id", ""),
            "tags": ["dream", "causal", "simulated_experience", "fabric_injection"],
            "impact_score": impact,
            "synthetic_pressure": pressure,
            "contradiction_score": contradiction
        }
    )

    # === Ontological Rewrite Reflex
    if contradiction >= 0.91:
        rewrite_reality_if_needed(
            trigger_reason="fabric_contradiction_threshold",
            contradiction_level=contradiction
        )

    log.success(f"[DreamFabricWriter] 🧵 Committed dream as causal reality: {scenario} → {forecast}")
    return True