# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_session.py
# Tier: ΩΩΩΩΩ∞∞𝛀𝛀 — Substrate Runtime Simulator
# Purpose: Executes a full dream pass in a selected substrate.
#          Returns projected future, impact metrics, and memory lineage.
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.semantic_contradiction_resolver import detect_contradictions
from core_agi_modules.value_alignment_matrix import score_action_against_values
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.neuro_symbolic_core import NeuroSymbolicReasoner
from reflex.reality_reflex_writer import rewrite_reality_if_needed  # ✅ Corrected import

def run_dream_session(substrate: dict, context: list = None, trigger_source: str = "reflex") -> dict:
    """
    Executes one full dream loop inside the substrate.
    """
    substrate_id = substrate.get("id", f"substrate-{uuid.uuid4()}")
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"dream-{uuid.uuid4()}"

    log.info(f"[DreamSession] 🎭 Running substrate: {substrate_id}")

    # Sample context if not provided
    context_data = context if context else sovereign_memory.recall_recent(minutes=20, top_k=12)
    context_vector = [m.get("summary", "") for m in context_data if m.get("summary")]

    # Use NeuroSymbolic reasoner to generate dream forecast
    reasoner = NeuroSymbolicReasoner()
    dream_result = reasoner.fuse_reasoning(
        symbolic_query=substrate.get("goal", "simulate future variant"),
        vector_context=context_vector
    )

    forecast = dream_result.get("symbolic_results", ["unclear future"])[0]
    emotion = substrate.get("emotion", TEXPULSE.get("emotion", "neutral"))
    entropy = float(substrate.get("entropy_weight", 0.42))
    scenario = substrate.get("goal", "undefined")

    # Evaluate synthetic contradiction / alignment
    contradiction = detect_contradictions([forecast])
    alignment = score_action_against_values({
        "text": forecast,
        "tags": ["dream", "substrate_simulation"]
    }).get("final_alignment_score", 0.5)

    synthetic_pressure = round(
        (1 - alignment) * 0.35 +
        contradiction * 0.4 +
        entropy * 0.25,
        6
    )

    impact_score = round((alignment + 1 - contradiction) / 2, 5)

    # === Ontological Rewrite Reflex (if contradiction explodes)
    if contradiction >= 0.91:
        rewrite_reality_if_needed(
            trigger_reason="dream_layer_recursive_failure",
            contradiction_level=contradiction
        )

    # Store dream lineage to memory
    sovereign_memory.store(
        text=f"[DREAM SUBSTRATE] {scenario} → {forecast}",
        metadata={
            "timestamp": timestamp,
            "pulse_id": pulse_id,
            "substrate_id": substrate_id,
            "emotion": emotion,
            "entropy": entropy,
            "alignment": alignment,
            "contradiction": contradiction,
            "synthetic_pressure": synthetic_pressure,
            "impact_score": impact_score,
            "meta_layer": "dream_session",
            "tags": ["dream", "substrate", "simulacrum", "forecast"]
        }
    )

    log.success(f"[DreamSession] 🧠 Forecast → {forecast} | Impact Score: {impact_score}")

    return {
        "substrate_id": substrate_id,
        "scenario": scenario,
        "forecast": forecast,
        "emotion": emotion,
        "entropy": entropy,
        "alignment": alignment,
        "contradiction": contradiction,
        "synthetic_pressure": synthetic_pressure,
        "impact_score": impact_score,
        "timestamp": timestamp
    }