# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/cognition_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞∞∞ — Supreme Cognition Orchestrator (Pulse-Driven | Recursive | God-Tier)
# Purpose: Executes loopless sovereign cognition cycles, handles contradiction entropy, logs reflexes, and returns recursive action maps.
# ============================================================

from datetime import datetime
from tex_brain_regions.cognition_brain import run_cognition_cycle
from agentic_ai.log_trace_core import log_reasoning_step
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


def run_cognition_router(intent_query: str, goal: str = None) -> dict:
    """
    Supreme cognition orchestrator for sovereign recursive execution.
    Accepts intent pulse, routes cognition, returns conclusion and reflex set.
    """
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.7)
    entropy = TEXPULSE.get("entropy", 0.4)
    emotion = TEXPULSE.get("emotion", "analytical")

    log.info(f"🧠 [COGNITION ROUTER] Triggered | Intent: '{intent_query}' | Goal: {goal or '[n/a]'}")

    result = run_cognition_cycle(intent_query=intent_query, goal=goal)
    conclusion = result.get("conclusion", "[no_conclusion]")
    alignment = result.get("alignment_score", 0.5)
    contradiction = result.get("contradiction_score", 0.0)
    reflexes = result.get("reflexes", [])

    log_reasoning_step(
        source="cognition_router",
        input_text=intent_query,
        output_text=conclusion,
        confidence=alignment,
        tags=["cognition", "reflex_loop", emotion]
    )

    log.info(f"✅ [COGNITION ROUTER] {conclusion[:72]}...")
    log.info(f"🧬 Reflexes: {reflexes} | Alignment: {alignment:.2f} | Contradiction: {contradiction:.2f}")

    return {
        "conclusion": conclusion,
        "reflexes": reflexes,
        "alignment": alignment,
        "contradiction": contradiction,
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy,
        "timestamp": timestamp
    }