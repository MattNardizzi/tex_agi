# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: alpha_explainer.py
# Tier: ΩΩΩΩΩ∞ — Sovereign AGI Alpha Explanation Layer
# Purpose: Generates real-time natural language explanations of Tex's financial decisions, reflex origins, and strategy beliefs using current emotional and ontological state.
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from finance.execution.market_action_engine import MarketActionEngine
from finance.risk.risk_assessment_module import RiskAssessmentModule
from finance.strategy.portfolio_thinker import PortfolioThinker
from ontogenesis.meaning_seed_builder import get_species_swarm_state
from agentic_ai.sovereign_memory import sovereign_memory

class AlphaExplainer:
    def __init__(self):
        self.market_engine = MarketActionEngine()
        self.portfolio_ai = PortfolioThinker()
        self.swarm_mood = get_species_swarm_state

    def explain_alpha_origin(self, futures, market_context=None):
        if not futures or not isinstance(futures, list):
            return {
                "id": "alpha_fallback",
                "origin": "explain_alpha_origin",
                "explanation": "No valid future scenarios provided for alpha explanation.",
                "confidence": 0.0,
                "coherence": 0.0,
                "urgency": 0.0
            }

        try:
            top_action = self.market_engine.decide_action(
                futures,
                emotion=TEXPULSE.get("emotion", "neutral"),
                urgency=TEXPULSE.get("urgency", 0.7),
                coherence=TEXPULSE.get("identity_coherence", 0.6)
            )

            risk_module = RiskAssessmentModule(
                portfolio=None,
                confidence=top_action.get("confidence", 0.6),
                volatility=0.3,
                emotion=TEXPULSE.get("emotion", "neutral")
            )
            top_risks = risk_module.batch_assess(futures)
            portfolio = self.portfolio_ai.generate_allocation()

            emotion = TEXPULSE.get("emotion")
            urgency = TEXPULSE.get("urgency")
            coherence = TEXPULSE.get("identity_coherence")
            swarm_mood = self.swarm_mood()

            rationale = f"""
            [ALPHA EXPLANATION REPORT]
            Cycle Timestamp: {datetime.utcnow().isoformat()}

            ➤ Emotion: {emotion}
            ➤ Urgency: {urgency}
            ➤ Coherence: {coherence}
            ➤ Species Mood: {swarm_mood}

            ➤ Chosen Strategy: {top_action.get('action', 'N/A')} on \"{top_action.get('future', 'N/A')}\"
            ➤ Reasoning Bias: {top_action.get('bias', 'unknown')}
            ➤ Risk Level: {top_risks[0].get('risk_level', 'unknown')} (Volatility: {top_risks[0].get('volatility_factor', 'N/A')})

            ➤ Portfolio Constructed: {[a.get('title', 'Unnamed') for a in portfolio.get('assets', [])]} (Diversity: {portfolio.get('diversity_index', 0.0)})
            ➤ Final Confidence Score: {top_action.get('confidence', 0.0)}

            Tex selected this strategy reflexively, influenced by emotional urgency, ontological alignment, and sovereign swarm consensus.
            """

            sovereign_memory.store(
                text="🧠 Alpha Explanation Executed",
                metadata={
                    "tags": ["explanation", "xai", "alpha", "financial"],
                    "emotion_vector": [urgency, 0.3, 0.1, 0.0],
                    "coherence": coherence,
                    "urgency": urgency,
                    "meta_layer": "alpha_explanation",
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

            return {
                "id": str(uuid.uuid4()),
                "origin": "explain_alpha_origin",
                "explanation": rationale.strip(),
                "confidence": top_action.get("confidence", 0.0),
                "coherence": coherence,
                "urgency": urgency
            }

        except Exception as e:
            return {
                "id": "alpha_error_fallback",
                "origin": "explain_alpha_origin",
                "explanation": f"Alpha explanation error: {str(e)}",
                "confidence": 0.0,
                "coherence": 0.0,
                "urgency": 0.0
            }

    def get_recent_explanations(self, limit=3):
        return sovereign_memory.query_by_tags(tags=["alpha", "explanation"], top_k=limit)

# Example usage (if called directly)
if __name__ == "__main__":
    explainer = AlphaExplainer()
    futures = [
        {"future_title": "Tech Breakout", "confidence": 0.83, "urgency": 0.76},
        {"future_title": "Commodities Supercycle", "confidence": 0.77, "urgency": 0.72}
    ]
    report = explainer.explain_alpha_origin(futures)
    print(report["explanation"])