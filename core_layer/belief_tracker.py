# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/belief_tracker.py
# Tier: ∞ΩΩΩ — Reflex Belief Imprint Cortex (Chrono + Vector Synced)
# Purpose: Logs introspective belief pattern updates into sovereign memory.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime

def store_belief(signal: dict) -> None:
    """
    Extracts belief reflection from signal and stores a reflex-safe belief trace in memory.
    """
    try:
        payload = signal.get("payload", {})
        pattern = payload.get("pattern", "")
        if not pattern:
            return

        belief = f"I have been thinking in the pattern: {pattern}"
        timestamp = datetime.utcnow().isoformat()

        sovereign_memory.store(
            text=belief,
            metadata={
                "type": "belief_update",
                "tags": ["belief", "pattern", "introspection"],
                "emotion": "introspective",
                "importance": 0.85,
                "urgency": 0.5,
                "entropy": 0.35,
                "meta_layer": "belief_tracker",
                "timestamp": timestamp
            }
        )

    except Exception as e:
        print(f"[BELIEF TRACKER ERROR] Failed to store belief: {e}")