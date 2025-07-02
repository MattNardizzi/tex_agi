# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/strategy_scoring.py
# Purpose: Tier 6 — Synthetic Strategy Evaluator + Pruner
# ============================================================

import random
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory

class StrategyScorer:
    def __init__(self):
        self.history = []

    def evaluate(self, strategy, regret_score=0.0, forecast_confidence=0.5):
        """
        Reflex: Scores a synthetic strategy and stores symbolic trace.
        Considers regret, coherence, urgency, and projected volatility impact.
        """
        tone = strategy.get("emotional_tone", "neutral")
        urgency = strategy.get("urgency", 0.7)
        coherence = strategy.get("coherence", 0.8)

        # Modifiers
        volatility_bias = strategy["modifiers"].get("volatility_bias", 1.0)
        stability_weight = strategy["modifiers"].get("stability_weight", 1.0)

        # === Dynamic impact score ===
        impact_score = round(
            (1 - regret_score) * coherence * stability_weight * forecast_confidence -
            (urgency * volatility_bias * 0.3),
            3
        )

        timestamp = datetime.utcnow().isoformat()
        strategy_id = strategy.get("id", f"STRAT-{random.randint(1000, 9999)}")

        strategy_record = {
            "id": strategy_id,
            "timestamp": timestamp,
            "score": impact_score,
            "reasoning": {
                "regret": regret_score,
                "confidence": forecast_confidence,
                "coherence": coherence,
                "tone": tone,
                "urgency": urgency
            }
        }

        self.history.append(strategy_record)

        # === Symbolic trace pulse (via sovereign_memory)
        sovereign_memory.store(
            text=f"Score {impact_score} for {strategy_id}",
            metadata={
                "agent": "TEX",
                "intent": "strategy_scoring",
                "conclusion": f"Score {impact_score} for {strategy_id}",
                "alignment_score": impact_score,
                "emotion": tone,
                "urgency": urgency,
                "reflexes": [
                    "strategy_evaluation",
                    "strategy_pruning" if impact_score < 0.2 else "strategy_retention"
                ],
                "tags": strategy.get("tags", []) + ["synthetic_strategy"],
                "trust_score": 0.7 + (coherence * 0.3),
                "contradiction_score": regret_score,
                "justification": (
                    f"Regret={regret_score}, Coherence={coherence}, "
                    f"Confidence={forecast_confidence}, Bias={volatility_bias}"
                ),
                "rewrite_patch": None,
                "meta_layer": "symbolic_trace"
            }
        )

        # Reflex output
        if impact_score < 0.2:
            print(f"[STRATEGY PRUNE] 🪓 Strategy {strategy_id} marked for pruning (score: {impact_score})")
        else:
            print(f"[STRATEGY SCORE] ✅ Strategy {strategy_id} scored: {impact_score}")

        return impact_score