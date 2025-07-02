# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: future_layer/future_decision_engine.py
# Tier: ∞ΩΩΩ∞Ω — Tex Strategic Futures Cortex (Loopless, Sovereign Memory-Aware)
# Purpose: Scores future paths using risk, emotion, urgency, memory, and coherence.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from finance.risk.risk_assessment_module import RiskAssessmentModule
from utils.logging_utils import log_event

class FutureDecisionEngine:
    def __init__(self):
        self.risk_assessor = None
        self.last_ranked_futures = []

    def assess_risk(self, portfolio, confidence, volatility, emotion):
        self.risk_assessor = RiskAssessmentModule(
            portfolio=portfolio,
            confidence=confidence,
            volatility=volatility,
            emotion=emotion
        )
        log_event("[RISK ENGINE] Risk assessor initialized.")

    def prioritize_futures(self, futures: list, return_full_list: bool = False):
        if not futures:
            return [] if return_full_list else (None, "No futures provided.")

        if not self.risk_assessor:
            self.assess_risk(
                TEXPULSE.get("portfolio_snapshot", {}),
                TEXPULSE.get("trade_confidence", 0.6),
                TEXPULSE.get("forecast_volatility", 0.3),
                TEXPULSE.get("emotional_state", "neutral")
            )

        # === Risk Assessment
        risk_data = self.risk_assessor.batch_assess(futures)

        # === Recent Memory Context
        recent_memory = sovereign_memory.recall_recent(top_k=25, filters={"tags": ["market", "future", "signal"]})

        # === Score function
        def score_future(future, risk, memory_context):
            title = future.get("future_title", "")
            confidence = future.get("confidence", 0.5)
            volatility = risk.get("volatility_factor", 0.5)
            urgency = TEXPULSE.get("urgency", 0.5)
            coherence = TEXPULSE.get("coherence", 0.5)

            emotion_multiplier = self._emotion_weight(confidence)
            memory_multiplier = self._memory_boost(title, memory_context)
            drift_factor = 1.0 - abs(urgency - coherence)

            raw_score = confidence * (1 - risk["combined_risk_score"])
            return round(raw_score * emotion_multiplier * memory_multiplier * drift_factor, 4)

        # === Score + Sort
        scored = [
            {
                "future": f,
                "risk_assessment": r,
                "priority_score": score_future(f, r, recent_memory)
            }
            for f, r in zip(futures, risk_data)
        ]

        self.last_ranked_futures = sorted(scored, key=lambda x: x["priority_score"], reverse=True)

        if return_full_list:
            return [entry["future"] for entry in self.last_ranked_futures]

        top = self.last_ranked_futures[0] if self.last_ranked_futures else None
        return top, f"Evaluated {len(futures)} futures @ {datetime.utcnow().isoformat()}"

    def decision_summary(self, best_future):
        if not best_future:
            return "⚠️ No dominant future selected."

        f = best_future["future"]
        r = best_future["risk_assessment"]
        return (
            f"📈 Future: {f.get('future_title', 'Unnamed')} | "
            f"Confidence: {f.get('confidence', 'n/a')} | "
            f"Risk: {r.get('risk_level', 'n/a')} | "
            f"Volatility: {r.get('volatility_factor', 'n/a')} | "
            f"Bias: {TEXPULSE.get('emotional_state')} | "
            f"Urgency: {TEXPULSE.get('urgency')} | "
            f"Coherence: {TEXPULSE.get('coherence')}"
        )

    def _emotion_weight(self, confidence):
        mood = TEXPULSE.get("emotional_state", "neutral")
        if mood in ["hopeful", "joy", "greed"]: return 1.2
        if mood in ["fear", "doubt"]: return 0.85
        if mood in ["resolve", "strategic"]: return 1.1
        return 1.0

    def _memory_boost(self, title, memory_snaps):
        if any(title.lower() in str(mem).lower() for mem in memory_snaps):
            return 1.25
        return 1.0

    def get_ranked(self):
        return self.last_ranked_futures


# === Reflex Test ===
if __name__ == "__main__":
    test_futures = [
        {"future_title": "Bond Market Collapse", "confidence": 0.72},
        {"future_title": "AI-Driven Equity Boom", "confidence": 0.88},
        {"future_title": "Currency Crisis in Asia", "confidence": 0.64}
    ]
    snapshot = {"equities": 0.4, "bonds": 0.3, "alts": 0.2, "cash": 0.1}

    tex = FutureDecisionEngine()
    tex.assess_risk(snapshot, 0.75, 0.2, "resolve")
    best, note = tex.prioritize_futures(test_futures)
    print("\n[SUMMARY]", tex.decision_summary(best))