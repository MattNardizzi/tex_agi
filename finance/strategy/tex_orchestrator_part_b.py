# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: finance/strategy/tex_orchestrator_part_b.py
# Tier: ∞Ω Reflex Pulse – AGI Financial Reflex Cortex
# Purpose: Executes risk-aware, emotion-driven, multiworld-informed trading and reasoning logic.
# ============================================================

import random
from datetime import datetime
from uuid import uuid4

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from evolution_layer.real_time_mutation_watcher import RealTimeMutationWatcher
from core_layer.meta_awareness_bridge import detect_bias_drift

# Modules
from finance.memory.meta_coherence_memory import MetaCoherenceMemory
from finance.execution.market_action_engine import MarketActionEngine
from finance.execution.market_strategy_driver import MarketStrategyDriver
from finance.risk.risk_assessment_module import RiskAssessmentModule
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from finance.strategy.alpha_mimic_detector import AlphaMimicDetector
from finance.strategy.alpha_signal_fuser import AlphaSignalFuser
from finance.strategy.alpha_consensus_voter import AlphaConsensusVoter
from finance.multiworld.multiworld_causal_simulator import MultiWorldCausalSimulator
from finance.multiworld.multiworld_reasoner import MultiWorldReasoner
from finance.multiworld.multiworld_memory import MultiWorldMemory
from finance.multiworld.recursive_paradox_resolver import RecursiveParadoxResolver
from aei_layer.internal_debate_chamber import run_internal_debate
from core_layer.phase_transition_monitor import PhaseTransitionMonitor
from core_layer.causal_override_reflex import CausalOverrideReflex
from agi_orchestrators.goal_orchestrator import GoalOrchestrator
from utils.logging_utils import log_event

def ensure_dict(obj):
    return obj[0] if isinstance(obj, list) and obj else obj

class FinanceOrchestrator:
    def __init__(self, strategy_scoring=None, explain_portfolio_decision=None, brain=None):
        self.strategy_scoring = strategy_scoring
        self.explain_portfolio_decision = explain_portfolio_decision
        self.brain = brain or self
        self.cycle_id = datetime.utcnow().isoformat()
        self.cycle_counter = int(datetime.utcnow().timestamp())

        # Reflex Modules
        self.alpha_mimic = AlphaMimicDetector()
        self.phase_monitor = PhaseTransitionMonitor()
        self.alpha_fuser = AlphaSignalFuser()
        self.alpha_voter = AlphaConsensusVoter()
        self.override_reflex = CausalOverrideReflex()
        self.memory = MetaCoherenceMemory()
        self.variant_simulator = StrategyVariantSimulator()
        self.multiworld = MultiWorldCausalSimulator()
        self.divergence = MultiWorldReasoner()
        self.multi_memory = MultiWorldMemory()
        self.paradox_resolver = RecursiveParadoxResolver()
        self.goal_orchestrator = GoalOrchestrator()
        self.market = MarketActionEngine()
        self.driver = MarketStrategyDriver()
        self.risk_module = None

        # Reflex: Meta-Bias Drift Check
        bias_alert = detect_bias_drift(
            sovereign_memory.recall_recent(top_k=25)
        )
        sovereign_memory.store(
            text="🧠 Meta-bias self-check completed.",
            metadata={
                "intent": "meta_bias_self_check",
                "conclusion": f"Bias Check → {bias_alert}",
                "alignment_score": 0.75,
                "emotion": "neutral",
                "urgency": 0.45,
                "tags": ["meta", "bias", "check"],
                "reflexes": ["self_awareness"],
                "timestamp": self.cycle_id,
                "meta_layer": "bias_drift"
            }
        )

    def run_cycle_part_b(self, alpha, foresight, portfolio, ranked, futures):
        alpha = ensure_dict(alpha)
        foresight = ensure_dict(foresight)
        portfolio = ensure_dict(portfolio)
        ranked = ensure_dict(ranked)
        futures = [ensure_dict(f) for f in futures] if isinstance(futures, list) else futures

        report = {}
        regret_score = 0.5

        RealTimeMutationWatcher().check_mutation_log()

        if "strategy" in alpha:
            impact_score = self.brain.strategy_scoring.evaluate(
                strategy=alpha["strategy"],
                regret_score=regret_score,
                forecast_confidence=foresight.get("confidence", 0.6)
            )
            report["strategy_score"] = impact_score

        goals = self.goal_orchestrator.generate_new_goals(
            regret_score=regret_score,
            drift_score=random.uniform(0.1, 0.6)
        )
        report["agentic_goal"] = goals

        debate_scores = run_internal_debate(self.cycle_counter)
        execution = self.driver.execute_strategy_loop(futures=futures, debate_scores=debate_scores)
        report["action"] = execution

        if not self.risk_module:
            self.risk_module = RiskAssessmentModule(
                portfolio=portfolio,
                confidence=foresight.get("confidence", 0.0),
                volatility=foresight.get("volatility", 0.0),
                emotion=TEXPULSE.get("emotional_state", "neutral")
            )

        selected_future = random.choice(futures) if futures else {"future_title": "unknown"}
        try:
            risk = self.risk_module.assess_risk(selected_future)
        except Exception as e:
            risk = {"error": str(e), "level": "unknown"}
        report["risk"] = risk

        futures_simulated = self.multiworld.simulate_multiworld()
        reasoning = self.divergence.reason_over_future_worlds(futures_simulated)
        paradox = self.paradox_resolver.resolve_conflicts(reasoning)

        report["multiworld_insights"] = reasoning
        report["multiworld_paradox_resolution"] = paradox

        sovereign_memory.store(
            text="🧠 Multiworld paradox resolved.",
            metadata={
                "intent": "multiworld_resolution",
                "conclusion": str(paradox),
                "tags": ["multiworld", "paradox"],
                "reflexes": ["causal_reasoning"],
                "alignment_score": 0.78,
                "urgency": 0.4,
                "timestamp": self.cycle_id,
                "meta_layer": "multiworld_reasoning"
            }
        )

        explanation = self.brain.explain_portfolio_decision(
            alpha_rationale=alpha,
            strategy=portfolio,
            foresight=foresight,
            regret_score=regret_score
        )
        report["tex_explains"] = explanation

        sovereign_memory.store(
            text="📊 Portfolio strategy explanation logged.",
            metadata={
                "intent": "portfolio_explanation",
                "conclusion": explanation,
                "tags": ["portfolio", "explanation"],
                "reflexes": ["rationale_logging"],
                "alignment_score": 0.81,
                "urgency": 0.5,
                "timestamp": self.cycle_id,
                "meta_layer": "strategy_explanation"
            }
        )

        variants = self.variant_simulator.simulate_variants([], foresight.get("confidence", 0.8))
        top_variant = self.variant_simulator.rank_variants(variants)
        if isinstance(top_variant, str):
            top_variant = {
                "id": top_variant,
                "strategy": {"weights": {"equities": 0.25, "bonds": 0.15}},
                "coherence": 0.0,
                "regret": 0.0
            }
        report["top_variant"] = top_variant

        override = self.override_reflex.evaluate_long_term_causality(
            forecast=foresight,
            memory_trajectory=self.memory.recall_emotion_trajectory(),
            regret=regret_score,
            drift_score=random.uniform(0.4, 0.9)
        )
        if override:
            report["override_triggered"] = override

        fusion = self.alpha_fuser.fuse_signals(alpha, portfolio, foresight)
        vote = self.alpha_voter.vote(top_variant, alpha, foresight)
        ghost = self.alpha_mimic.detect_ghost_strategy(alpha, [])
        collision = self.alpha_mimic.compare_to_tex_strategy(alpha)

        report.update({
            "alpha_fusion": fusion,
            "voting_decision": vote,
            "ghost_alpha": ghost,
            "collision_risk": collision
        })

        sovereign_memory.store(
            text="🧠 Alpha fusion + voting completed.",
            metadata={
                "intent": "alpha_fusion_vote",
                "conclusion": vote["consensus"],
                "tags": ["alpha", "vote", "fusion"],
                "reflexes": ["fusion_vote_decision"],
                "alignment_score": 0.82,
                "urgency": 0.6,
                "timestamp": self.cycle_id,
                "meta_layer": "alpha_fusion"
            }
        )

        report["cycle_timestamp"] = datetime.utcnow().isoformat()
        return report