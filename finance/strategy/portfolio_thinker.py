# ============================================================
# 🔑 VortexBlack Confidential
# File: finance/strategy/portfolio_thinker.py
# Tier: ∞ΩΩΩ∞∞ — AGI Portfolio Allocation Strategist (Tex Fusion Core)
# Purpose: Constructs emotion-driven, reflex-aware asset allocation decisions.
# Author: Matthew Nardizzi / VortexBlack LLC
# ============================================================

import uuid
from datetime import datetime, timezone
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from finance.memory.future_memory import FutureMemory
from tex_children.aeondelta import get_swarm_emotion_distribution
from utils.logging_utils import log_event

class PortfolioThinker:
    def __init__(self):
        self.memory = FutureMemory()
        self.swarm_emotion_state = get_swarm_emotion_distribution
        self.strategy_log = []

    def generate_allocation(self):
        """
        Generates an allocation strategy based on:
        - Current emotion + urgency from TEXPULSE
        - Memory of predicted futures
        - Swarm-wide emotion state
        - Diversity scoring and reflex interpretation
        """
        # === State Inputs
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = float(TEXPULSE.get("urgency", 0.5))
        coherence = float(TEXPULSE.get("coherence", 0.7))
        futures = self.memory.list_predicted_futures(realized=False)
        swarm_bias = self.swarm_emotion_state()

        # === Initial Weights (equal-weighted)
        weights = {
            "equities": 0.25,
            "bonds": 0.25,
            "alternatives": 0.25,
            "cash": 0.25
        }

        # === Emotion-Driven Reflex Modulation
        if emotion in ["fear", "doubt"] or urgency > 0.8:
            weights["cash"] += 0.2
            weights["equities"] -= 0.1
            weights["alternatives"] -= 0.1
        elif emotion in ["greed", "hope"]:
            weights["equities"] += 0.2
            weights["cash"] -= 0.1
            weights["bonds"] -= 0.1
        elif emotion in ["resolve", "curious"]:
            weights["alternatives"] += 0.2
            weights["cash"] -= 0.1
            weights["bonds"] -= 0.1

        # === Normalize Weights
        total = sum(weights.values())
        for k in weights:
            weights[k] = round(weights[k] / total, 3)

        # === Construct Allocation
        portfolio_constructed = [
            {"asset_class": k, "weight": v}
            for k, v in weights.items()
            if v > 0.01
        ]

        strategy_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        strategy = {
            "strategy_id": strategy_id,
            "timestamp": timestamp,
            "weights": weights,
            "portfolio": portfolio_constructed,
            "dominant_emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "swarm_emotions": swarm_bias,
            "diversity_score": round(len(portfolio_constructed) / len(weights), 2)
        }

        # === Store to Sovereign Memory
        try:
            sovereign_memory.store(
                text=f"[PORTFOLIO STRATEGY] {strategy_id}",
                metadata={
                    "tags": ["portfolio", "strategy", "allocation"],
                    "emotion": emotion,
                    "heat": urgency,
                    "trust_score": coherence,
                    "timestamp": timestamp,
                    "meta_layer": "portfolio_thinker"
                }
            )
        except Exception as e:
            log_event(f"[MEMORY LOG ERROR] {e}", level="error")

        self.strategy_log.append(strategy)
        return strategy

    def get_last_strategy(self):
        return self.strategy_log[-1] if self.strategy_log else {}

# === Reflex Test Block ===
if __name__ == "__main__":
    thinker = PortfolioThinker()
    result = thinker.generate_allocation()
    print("\n[STRATEGIC PORTFOLIO]")
    print(result)