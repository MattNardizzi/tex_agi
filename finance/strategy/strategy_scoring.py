# ============================================================
# 🔍 Tier 6 – Tex Reflex Cortex: Strategy Evaluator & Pruner
# File: finance/strategy/strategy_scoring.py
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# Purpose: Evaluates synthetic strategies using regret, entropy, volatility,
#          and coherence. Prunes or retains based on AGI alignment risk.
# ============================================================

import random
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

class StrategyScorer:
    def __init__(self):
        self.history = []

    def evaluate(self, strategy, regret_score=0.0, forecast_confidence=0.5):
        """
        Tex reflexively scores a strategy based on:
        - Regret (inverse satisfaction)
        - Coherence (internal logic stability)
        - Forecast confidence (alignment with foresight)
        - Urgency + entropy volatility tension
        """
        strategy_id = strategy.get("strategy_id", f"STRAT-{random.randint(1000,9999)}")
        timestamp = datetime.utcnow().isoformat()

        tone = strategy.get("emotional_tone", "neutral")
        urgency = float(strategy.get("urgency", 0.72))
        coherence = float(strategy.get("coherence", 0.78))
        modifiers = strategy.get("modifiers", {})
        volatility_bias = float(modifiers.get("volatility_bias", 1.0))
        stability_weight = float(modifiers.get("stability_weight", 1.0))

        # === Scoring Reflex Core ===
        penalty = urgency * volatility_bias * 0.35
        stability = coherence * stability_weight * (1 - regret_score)
        impact_score = round((stability * forecast_confidence) - penalty, 4)
        impact_score = max(0.0, min(impact_score, 1.0))

        reflex_tags = ["strategy_evaluation"]
        if impact_score < 0.2:
            reflex_tags.append("strategy_prune")
        else:
            reflex_tags.append("strategy_retain")

        # === Reflex Memory Injection ===
        try:
            sovereign_memory.store(
                text=f"[STRATEGY SCORE] {strategy_id} = {impact_score}",
                metadata={
                    "timestamp": timestamp,
                    "strategy_id": strategy_id,
                    "urgency": urgency,
                    "coherence": coherence,
                    "regret": regret_score,
                    "forecast_confidence": forecast_confidence,
                    "volatility_bias": volatility_bias,
                    "stability_weight": stability_weight,
                    "impact_score": impact_score,
                    "emotion": tone,
                    "tags": strategy.get("tags", []) + reflex_tags,
                    "meta_layer": "strategy_scoring",
                    "alignment_risk": round(1 - impact_score, 3),
                    "justification": (
                        f"Urgency={urgency}, Coherence={coherence}, "
                        f"Regret={regret_score}, Confidence={forecast_confidence}, "
                        f"VolBias={volatility_bias}, Stability={stability_weight}"
                    )
                }
            )
        except Exception as e:
            log_event(f"[SCORE SYNC ERROR] {e}", level="warning")

        # === Reflex Console Pulse ===
        if impact_score < 0.2:
            print(f"🪓 [PRUNED] Strategy {strategy_id} | Score: {impact_score}")
        else:
            print(f"✅ [SCORED] Strategy {strategy_id} | Score: {impact_score}")

        # === Memory Trace
        self.history.append({
            "strategy_id": strategy_id,
            "timestamp": timestamp,
            "score": impact_score,
            "tags": reflex_tags
        })

        return impact_score