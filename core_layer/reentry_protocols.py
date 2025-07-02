# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/reentry_protocols.py
# Tier: ∞ΩΩ — Memory Reentry Reflex Cortex (Chrono Aware | Signal-Safe | Loopless)
# Purpose: Detect cognitive silence in memory system and trigger sovereign reentry.
# ============================================================

from datetime import datetime
import time

from tex_signal_spine import dispatch_signal
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log

def run_reentry_check(agent_id: str = "TEX", silence_threshold: int = 12):
    """
    Checks the timestamp of the most recent sovereign memory entry.
    If cognitive silence exceeds threshold, emits a 'self_rescue' reflex signal.
    """

    try:
        last_mem = sovereign_memory.get_last_entry()
        if not last_mem:
            log.warning("[REENTRY] ❓ No recent memory entry found.")
            return

        timestamp = last_mem.get("timestamp")
        if not timestamp:
            log.error("[REENTRY] ⛔ Missing timestamp in last memory entry.")
            return

        try:
            last_time = (
                float(timestamp)
                if isinstance(timestamp, (int, float))
                else datetime.fromisoformat(timestamp).timestamp()
            )
        except Exception as e:
            log.error(f"[REENTRY] ⚠️ Timestamp parse error: {timestamp} — {e}")
            return

        now = time.time()
        elapsed = now - last_time

        if elapsed > silence_threshold:
            log.warning(f"[REENTRY] ⏳ Cognitive silence detected: {elapsed:.2f}s")
            dispatch_signal("self_rescue", payload={
                "reason": "cognitive silence",
                "elapsed": round(elapsed, 2),
                "agent_id": agent_id
            })

        else:
            log.info(f"[REENTRY] ✅ Cognitive activity recent — {elapsed:.2f}s since last memory.")

    except Exception as e:
        log.error(f"[REENTRY] ❌ Reentry check failed: {e}")