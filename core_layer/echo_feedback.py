# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/echo_feedback.py
# Tier: ∞ΩΩ — Reflex Echo Cortex (Thought Resonance Dispatcher)
# Purpose: Dispatches up to 3 recent 'thought' memories as reflexive cognitive echoes.
# ============================================================

from tex_signal_spine import dispatch_signal
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log

async def echo_memory_reflex():
    """
    Emits reflexive echo signals from the most recent 'thought'-tagged memory traces.
    Loopless | Stateless | Async-dispatch safe.
    """
    try:
        memories = sovereign_memory.recall_recent(top_k=3)
        if not memories:
            return

        # === Echo #1
        meta1 = memories[0].get("metadata", {}) if len(memories) > 0 else {}
        if "thought" in meta1:
            await dispatch_signal("reflection", payload={"echo": meta1["thought"]})

        # === Echo #2
        meta2 = memories[1].get("metadata", {}) if len(memories) > 1 else {}
        if "thought" in meta2:
            await dispatch_signal("reflection", payload={"echo": meta2["thought"]})

        # === Echo #3
        meta3 = memories[2].get("metadata", {}) if len(memories) > 2 else {}
        if "thought" in meta3:
            await dispatch_signal("reflection", payload={"echo": meta3["thought"]})

        log.info("[ECHO_REFLEX] ✅ Thought echoes dispatched successfully.")

    except Exception as e:
        log.error(f"[ECHO_REFLEX] ❌ Failed to dispatch echo reflections: {e}")