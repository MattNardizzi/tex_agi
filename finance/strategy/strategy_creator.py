# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: finance/strategy/strategy_creator.py
# Tier: ∞ΩΩΩΩ∞ — Autonomous Financial Strategy Generator
# Purpose: Synthesizes trading strategies from emotional, urgency, coherence, and regret signals.
# Author: Matthew Nardizzi / VortexBlack LLC
# ============================================================

import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

class StrategyCreator:
    def __init__(self):
        self.library = []

    def generate_strategy(self, foresight: dict = None, regret_score: float = 0.0):
        """
        Synthesizes a new trading strategy based on:
        - Current emotional tone
        - Urgency + coherence from TEXPULSE
        - Optional foresight projection
        - Reflex-safe modifier encoding
        """
        # === Cognitive inputs
        tone = TEXPULSE.get("emotional_state", "curious")
        urgency = float(TEXPULSE.get("urgency", 0.75))
        coherence = float(TEXPULSE.get("coherence", 0.85))
        timestamp = datetime.utcnow().isoformat()

        # === Reflex processing
        archetype = self._select_archetype(tone, regret_score)
        modifiers = self._generate_modifiers(foresight, urgency, coherence)

        strategy = {
            "strategy_id": f"STRAT-{random.randint(1000, 9999)}",
            "timestamp": timestamp,
            "emotional_tone": tone,
            "urgency": urgency,
            "coherence": coherence,
            "archetype": archetype,
            "modifiers": modifiers,
            "source": "TexSynthetic",
            "foresight_attached": foresight.get("projected_future", "none") if foresight else "none"
        }

        self.library.append(strategy)

        # === Store in Sovereign Memory
        try:
            sovereign_memory.store(
                text=f"[STRATEGY SYNTHESIZED] {strategy['strategy_id']} | {archetype}",
                metadata={
                    "tags": ["strategy", archetype, "generated"],
                    "emotion": tone,
                    "heat": urgency,
                    "trust_score": coherence,
                    "meta_layer": "strategy_creator",
                    "timestamp": timestamp
                }
            )
        except Exception as e:
            log_event(f"[STRATEGY_CREATOR] ❌ Memory store failed: {e}", level="error")

        log_event(f"🧠 [STRATEGY CREATOR] New strategy → {strategy['strategy_id']} ({archetype})")
        return strategy

    def _select_archetype(self, tone: str, regret_score: float) -> str:
        """
        Selects an archetype based on emotion and regret.
        """
        if regret_score > 0.75:
            return "ReversalContrarian"
        if tone == "resolve":
            return "MomentumBreakout"
        if tone == "fear":
            return "LiquidityDefense"
        if tone == "greed":
            return "VolatilityHarvest"
        return "BalancedFlow"

    def _generate_modifiers(self, foresight, urgency: float, coherence: float) -> dict:
        """
        Builds strategy modifiers from current AGI state and projected foresight.
        """
        return {
            "volatility_bias": round(urgency * random.uniform(0.8, 1.2), 3),
            "stability_weight": round(coherence * random.uniform(0.8, 1.2), 3),
            "foresight_tag": foresight.get("projected_future", "none") if foresight else "none"
        }

    def get_latest(self):
        return self.library[-1] if self.library else {}

# === Reflex Test Runner ===
if __name__ == "__main__":
    foresight = {"projected_future": "AI-Driven Market Supercycle"}
    sc = StrategyCreator()
    strat = sc.generate_strategy(foresight=foresight, regret_score=0.42)
    print("\n[GENERATED STRATEGY]")
    print(strat)