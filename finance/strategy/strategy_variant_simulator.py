# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: finance/strategy/strategy_variant_simulator.py
# Purpose: Simulate parallel strategy variants + rank for execution (Reflex-Compliant)
# ============================================================

import random
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory


class StrategyVariantSimulator:
    def __init__(self, num_variants=5):
        self.num_variants = num_variants

    def simulate_variants(self, futures, foresight_confidence):
        """
        Recursively simulate N strategy variants based on incoming futures.
        """
        return self._simulate_recursive([], 0, futures, foresight_confidence)

    def _simulate_recursive(self, variants, index, futures, foresight_confidence):
        if index >= self.num_variants:
            return variants

        variant = {
            "id": f"variant_{index+1}",
            "allocation": self._random_portfolio(futures),
            "coherence": round(random.uniform(0.5, 1.0), 3),
            "volatility": round(random.uniform(0.1, 0.5), 3),
            "confidence": foresight_confidence + random.uniform(-0.1, 0.1),
            "regret": round(random.uniform(0.0, 1.0), 3)
        }

        return self._simulate_recursive(variants + [variant], index + 1, futures, foresight_confidence)

    def rank_variants(self, variants):
        """
        Rank variants by regret, coherence, and confidence — log top pick to symbolic memory.
        """
        def recursive_sort(vs):
            if len(vs) <= 1:
                return vs
            pivot = vs[0]
            lesser = [v for v in vs[1:] if self._score_variant(v) < self._score_variant(pivot)]
            greater = [v for v in vs[1:] if self._score_variant(v) >= self._score_variant(pivot)]
            return recursive_sort(lesser) + [pivot] + recursive_sort(greater)

        ranked = recursive_sort(variants)
        top = ranked[0]

        sovereign_memory.store(
            text=f"Selected {top['id']} for deployment",
            metadata={
                "agent": "TEX",
                "intent": "top_strategy_variant_selected",
                "conclusion": f"Selected {top['id']} for deployment",
                "tags": ["strategy", "variant", "ranking"],
                "timestamp": datetime.utcnow().isoformat(),
                "reflexes": ["variant_evaluation"],
                "trust_score": top["confidence"],
                "urgency": 0.6,
                "entropy": 1.0 - top["coherence"],
                "meta_layer": "symbolic_trace",
                "metadata": {
                    "variant": top
                }
            }
        )

        return top

    def _score_variant(self, variant):
        """
        Lower score = better (sorted by regret, then coherence, then confidence).
        """
        return (variant["regret"], -variant["coherence"], -variant["confidence"])

    def _random_portfolio(self, futures):
        """
        Reflex-safe portfolio constructor using bounded randomness.
        """
        return random.sample(futures, min(3, len(futures)))