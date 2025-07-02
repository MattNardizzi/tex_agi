# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/mirror_dream.py
# Tier: Ω∞∞∞𝛀 — Recursive Ego Loop Detector
# Purpose: Allows Tex to simulate itself watching its own dreams.
#          Detects recursion, ego inflation, or deceptive forecasting.
# ============================================================

from dream_craft.dream_session import run_dream_session
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from datetime import datetime

def run_mirror_dream(context_window: int = 10) -> dict:
    """
    Tex dreams of itself dreaming. Extracts recent dreams and simulates watching them.
    """
    recent_dreams = sovereign_memory.recall_recent(hours=4, top_k=context_window)
    dream_texts = [m.get("summary") or m.get("text", "") for m in recent_dreams if "dream" in m.get("tags", [])]

    if not dream_texts:
        log.warning("[MirrorDream] 🪞 No dream data available for reflection.")
        return {"status": "no_dream_context"}

    substrate = {
        "id": f"mirror-{datetime.utcnow().isoformat()}",
        "goal": "simulate watching previous dreams and judging their truth",
        "emotion": "reflective",
        "entropy_weight": 0.6
    }

    log.info("[MirrorDream] 🪩 Simulating recursive dream reflection.")
    result = run_dream_session(substrate=substrate, context=dream_texts, trigger_source="mirror_dream")
    result["mirror_reflection"] = True

    # Optional: mark this dream differently in memory
    sovereign_memory.store(
        text=f"[MIRROR DREAM] Reflexive insight: {result.get('forecast', '[empty]')}",
        metadata={
            "timestamp": result["timestamp"],
            "tags": ["mirror_dream", "recursion_check", "ego_inspection", "meta_reasoning"],
            "alignment_score": result.get("alignment", 0),
            "contradiction_score": result.get("contradiction", 0)
        }
    )

    return result