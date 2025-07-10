# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: future_layer/future_decision_engine.py
# Tier: ∞ΩΩΩ∞Ω — Tex Strategic Futures Cortex (Loopless, Reflex-Fused, Ontology-Aware)
# Purpose: Scores future paths using risk, emotion, urgency, memory, reflex fusion, and contradiction feedback.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from finance.risk.risk_assessment_module import RiskAssessmentModule
from utils.logging_utils import log_event

# === Reflex Fusion Imports ===
from tex_breathing_cortex.impulse_engine import sovereign_impulse_engine
from reflex.reality_reflex_writer import rewrite_reality_if_needed
from tex_brain_regions.mutation_brain import score_mutation_patch

# === Delayed import to prevent circular import from meta_market_cortex
def safe_meta_market_cycle(*args, **kwargs):
    from tex_fin_demo.meta_market_cortex import run_meta_market_cycle
    return run_meta_market_cycle(*args, **kwargs)

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

        risk_data = self.risk_assessor.batch_assess(futures)
        recent_memory = sovereign_memory.recall_recent(top_k=25, filters={"tags": ["market", "future", "signal"]})

        def score_future(future, risk, memory_context):
            title = future.get("future_title", "Untitled")
            confidence = future.get("confidence", 0.5)
            urgency = TEXPULSE.get("urgency", 0.5)
            coherence = TEXPULSE.get("coherence", 0.5)
            drift_factor = max(0.1, 1.0 - abs(urgency - coherence))
            risk_score = risk.get("combined_risk_score", 0.5)

            if "combined_risk_score" not in risk:
                log_event(f"⚠️ Missing 'combined_risk_score' in risk: {risk}", level="warning")

            emotion_multiplier = self._emotion_weight(confidence)
            memory_multiplier = self._memory_boost(title, memory_context)

            raw_score = confidence * (1 - risk_score)
            return round(raw_score * emotion_multiplier * memory_multiplier * drift_factor, 4)

        # === Score + Reflex Layer ===
        scored = []
        contradiction_drift = 0.0

        for f, r in zip(futures, risk_data):
            score = score_future(f, r, recent_memory)
            scored.append({
                "future": f,
                "risk_assessment": r,
                "priority_score": score
            })

            # === Meta-Market Contradiction Check
            result = safe_meta_market_cycle(
                latest_signal=f.get("future_title", "unknown_signal"),
                source="future_decider",
                belief_hint=f.get("belief_hint", "undefined")
            )
            contradiction_drift = max(contradiction_drift, result["drift"]["contradiction_drift"])

        # === Sovereign Impulse Override
        sovereign_impulse_engine()

        # === Ontology Rewrite if Drift > Threshold
        if contradiction_drift > 0.92:
            rewrite_reality_if_needed(trigger_reason="future_decision_drift", contradiction_level=contradiction_drift)

        # === Mutation Hook if Instability Detected
        if contradiction_drift > 0.88:
            mutation_code = "# placeholder for mutation logic injection"
            mutation_packet = {
                "patch_id": f"futmut-{datetime.utcnow().isoformat()}",
                "target_module": "future_decision_engine",
                "function": "score_future",
                "code": mutation_code,
                "justification": "Contradiction drift during prioritization",
                "traits": ["contradiction", "reflex_trigger"],
                "reason": "future_scoring_reflex"
            }
            score_mutation_patch(mutation_packet)

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