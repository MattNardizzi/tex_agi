# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/reflex_stability_model.py
# Tier: ΩΩΩΩ — Reflex Stability Estimator
# Purpose: Tracks active reflexes, logs reflex entropy, and emits drift scores
# ============================================================

from datetime import datetime
from statistics import mean, stdev

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE


class ReflexStabilityModel:
    def __init__(self):
        self.active_reflexes = []

    def update(self, new_reflex: str):
        """
        Adds a reflex event and logs its metadata to sovereign memory.
        """
        reflex_event = {
            "name": new_reflex,
            "timestamp": datetime.utcnow().isoformat(),
            "emotion": TEXPULSE.get("emotional_state", "unknown"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "coherence": TEXPULSE.get("coherence", 0.75),
        }

        self.active_reflexes.append(reflex_event)

        # Pulse symbolic reflex to sovereign memory
        sovereign_memory.store(
            text=f"Reflex event: {new_reflex}",
            metadata={
                "agent": "TEX",
                "intent": "reflex_event_log",
                "conclusion": f"Reflex event: {new_reflex}",
                "emotion": reflex_event["emotion"],
                "urgency": reflex_event["urgency"],
                "coherence": reflex_event["coherence"],
                "timestamp": reflex_event["timestamp"],
                "reflexes": [new_reflex],
                "tags": ["reflex", "event", "trace"],
                "meta_layer": "reflex_stability",
                "metadata": reflex_event
            }
        )

    def get_active_reflexes(self, window: int = 20) -> list:
        """
        Returns a list of recent reflexes from sovereign memory.
        """
        try:
            events = sovereign_memory.recall_recent(
                minutes=360,
                top_k=window,
                filters={"tags": ["reflex"]}
            )
            return [
                e.get("metadata", {}).get("name", "unknown")
                for e in events
                if e.get("metadata", {}).get("name")
            ]
        except Exception as e:
            print(f"[ReflexStabilityModel] ⚠️ Failed to fetch reflexes: {e}")
            return []

    def compute_entropy(self, reflex_list: list = None) -> float:
        """
        Computes the entropy (diversity index) of recent reflex triggers.
        """
        reflexes = reflex_list or self.get_active_reflexes()
        if not reflexes:
            return 0.0

        unique = len(set(reflexes))
        total = len(reflexes)
        return round(min(1.0, unique / total), 3)

    def get_stability_snapshot(self) -> dict:
        """
        Returns a current reflex stability snapshot with entropy and reflex volume.
        """
        reflexes = self.get_active_reflexes()
        entropy = self.compute_entropy(reflexes)

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "reflexes": reflexes,
            "entropy": entropy,
            "reflex_volume": len(reflexes),
            "emotion": TEXPULSE.get("emotional_state", "unknown"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "coherence": TEXPULSE.get("coherence", 0.75)
        }