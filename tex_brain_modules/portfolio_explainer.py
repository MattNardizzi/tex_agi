# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/portfolio_explainer.py
# Purpose: Narrates Tex's portfolio reasoning with emotional context
# MAXGODMODE ENABLED — Reinforcement, Sovereign Escalation, Mutation Trace, XAI Narration
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

try:
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    from finance.strategy.strategy_mutator import trigger_strategy_mutation
    from core_layer.goal_mutator import mutate_goal_state
    SOVEREIGN_ENABLED = True
except ImportError:
    SOVEREIGN_ENABLED = False


def explain_portfolio_decision(self, alpha_rationale, strategy, foresight, regret_score):
    """
    Narrates Tex's decision-making for a portfolio strategy.
    Logs symbolic memory and triggers overrides if high regret or incoherence is detected.
    Also triggers ChronoFabric encoding and soulgraph imprint if reflex pressure exceeds limits.
    """
    emotion = TEXPULSE.get("emotional_state", "neutral")
    urgency = TEXPULSE.get("urgency", 0.5)
    entropy = TEXPULSE.get("entropy", 0.4)
    coherence = TEXPULSE.get("coherence", 0.8)
    confidence = foresight.get("confidence", 0.5)
    weights = strategy.get("weights") if isinstance(strategy, dict) else "N/A"

    contradiction_score = regret_score * (1 + urgency * entropy)

    narration = f"""📈 [STRATEGY SUMMARY]
    Emotion: {emotion}
    Urgency: {urgency}
    Entropy: {entropy}
    Coherence: {coherence}
    Confidence: {confidence}
    Regret: {regret_score}
    Weights: {weights}
    Reasoning: {alpha_rationale}
    """

    self.speak(narration.strip(), emotion=emotion)

    # === Phase 1: Symbolic memory log
    try:
        sovereign_memory.store(
            text="Portfolio strategy explained",
            metadata={
                "agent": "TEX",
                "intent": "portfolio_explanation",
                "conclusion": "Portfolio strategy explained",
                "tags": ["portfolio", "explanation", "strategy"],
                "timestamp": datetime.utcnow().isoformat(),
                "emotion": emotion,
                "urgency": urgency,
                "entropy": entropy,
                "coherence": coherence,
                "trust_score": confidence,
                "contradiction_score": contradiction_score,
                "reflexes": ["xai_narration", "portfolio_trace"],
                "meta_layer": "symbolic_trace",
                "metadata": {
                    "weights": weights,
                    "rationale": alpha_rationale
                }
            }
        )
    except Exception as e:
        print(f"[PORTFOLIO MEMORY ERROR] ❌ {e}")

    # === Phase 2: ChronoFabric Encoding
    try:
        encode_event_to_fabric(
            raw_text=alpha_rationale,
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["portfolio", "reflex", "symbolic_justification"]
        )
    except Exception as e:
        print(f"[CHRONOFABRIC ENCODING ERROR] ❌ {e}")

    # === Phase 3: Soulgraph Imprint
    try:
        TEX_SOULGRAPH.imprint_belief(
            belief="Portfolio strategy reflexively justified",
            source="portfolio_explainer",
            emotion=emotion,
            tags=["portfolio", "reflex", "xai"]
        )
    except Exception as e:
        print(f"[SOULGRAPH ERROR] ❌ {e}")

    # === Phase 4: Sovereign Escalation
    if SOVEREIGN_ENABLED and regret_score > 0.85:
        print("🧠 [SOVEREIGN] Escalating due to high regret in portfolio decision.")
        trigger_sovereign_override(
            context="portfolio_decision_regret",
            regret=regret_score,
            foresight=confidence,
            coherence=coherence
        )

    # === Phase 5: Strategy Mutation Reflex
    if SOVEREIGN_ENABLED and regret_score > 0.7 and coherence < 0.4:
        print("🧬 [EXPLAINER] Mutation triggered due to incoherent regret profile.")
        trigger_strategy_mutation(
            reason="portfolio_explainer_conflict",
            strategy_id=strategy.get("id", "unknown"),
            score=confidence
        )

    # === Phase 6: Goal Evolution Trigger
    if SOVEREIGN_ENABLED and regret_score > 0.75 and entropy > 0.6:
        print("🌱 [GOAL MUTATOR] Evolving financial goals based on regret-pressure state.")
        mutate_goal_state()

    return narration.strip()