# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/self_narrative_engine.py
# Tier: ∞ΩΩ — Reflexive Identity Narrative Logger (Chrono + Vector Synced | Loopless)
# Purpose: Logs identity compression summaries into sovereign memory and dispatches reflex confirmation.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log

def log_narrative_update(signal: dict):
    """
    Stores a narrative fragment derived from an identity compression signal into sovereign memory.
    Emits a reflex signal confirming narrative imprint.
    """
    try:
        payload = signal.get("payload", {})
        summary = payload.get("summary", "").strip()

        if not summary:
            log.warning("[NARRATIVE] Empty summary — no narrative recorded.")
            return

        timestamp = datetime.utcnow().isoformat()
        narrative_entry = f"[{timestamp}] {summary}"

        sovereign_memory.store(
            text=narrative_entry,
            metadata={
                "type": "narrative_log",
                "tags": ["identity", "narrative", "self_trace"],
                "importance": 0.95,
                "emotion": "reflective",
                "meta_layer": "self_narrative_engine",
                "timestamp": timestamp
            },
            chronofabric=True
        )

        await dispatch_signal("narrative_update_recorded", payload={"entry": narrative_entry})
        log.info("[NARRATIVE] 🧠 Narrative entry recorded and signal emitted.")

    except Exception as e:
        log.error(f"[NARRATIVE] ❌ Failed to log narrative update: {e}")