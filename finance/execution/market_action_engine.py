# ============================================================
# 🔹 VortexBlack Confidential
# File: market_action_engine.py
# Purpose: TIER 6 AGI Market Execution Core — Tex Cognitive Fusion Layer
# MAXGODMODE ENABLED — Real-Time + Sovereign + Reinforcement + Risk + Mutation + Quantum Ready
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
from datetime import datetime

from finance.memory.future_meta_memory import FutureMetaMemory
from dream_layer.dream_fusion_engine import DreamFusionEngine
from core_layer.memory_consolidator import MemoryConsolidator
from agi_orchestrators.ontogenesis_orchestrator import get_ontogenesis_swarm_state
from core_layer.goal_engine import get_active_goals
from core_layer.goal_inference_engine import GoalInferenceEngine
from core_agi_modules.tex_codex_sync import TexCodexSync
from finance.strategy.alpha_fusion_engine import AlphaFusionEngine

# === Sovereign Reflex Stack
try:
    from core_layer.tex_manifest import TEXPULSE
    from agentic_ai.sovereign_memory import sovereign_memory
    from finance.risk.risk_assessment_module import RiskAssessmentModule
    from real_time_engine.advanced_analytics import AdvancedAnalytics
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    from finance.strategy.strategy_mutator import trigger_strategy_mutation
    SOVEREIGN_ENABLED = True
    REALTIME_ENABLED = True
except ImportError:
    TEXPULSE = {"emotional_state": "neutral", "urgency": 0.5, "coherence": 0.8}
    SOVEREIGN_ENABLED = False
    REALTIME_ENABLED = False

class MarketActionEngine:
    def __init__(self):
        self.last_actions = []
        self.memory = MemoryConsolidator()
        self.meta_memory = FutureMetaMemory()
        self.dream_engine = DreamFusionEngine()
        self.swarm_emotions = get_ontogenesis_swarm_state
        self.goal_trace = GoalInferenceEngine()
        self.codex = TexCodexSync()
        self.alpha_fusion = AlphaFusionEngine()

        self.behavioral_bias_map = {
            "fear": "DEFENSIVE",
            "doubt": "DEFENSIVE",
            "greed": "AGGRESSIVE",
            "hope": "AGGRESSIVE",
            "resolve": "STRATEGIC",
            "curious": "STRATEGIC",
            "anger": "RECKLESS",
            "joy": "EXPANSIVE"
        }

    def decide_action(self, futures, emotion=None, urgency=None, coherence=None, debate_scores=None, override_bias=None):
        emotion = emotion or TEXPULSE.get("emotional_state", "curious")
        urgency = urgency if urgency is not None else TEXPULSE.get("urgency", 0.5)
        coherence = coherence if coherence is not None else TEXPULSE.get("coherence", 0.9)

        if not futures:
            return {"action": "HOLD", "confidence": 0.3, "reason": "No futures supplied."}

        top = sorted(futures, key=lambda x: x.get("confidence", 0), reverse=True)[0]
        bias = override_bias or self.behavioral_bias_map.get(emotion, "NEUTRAL")
        volatility = 1.0 - coherence

        if REALTIME_ENABLED:
            try:
                volatility = AdvancedAnalytics.get_market_volatility_score()
            except Exception as e:
                print(f"[VOLATILITY FETCH ERROR] {e}")

        fused = self.alpha_fusion.fuse_alpha_signals(
            variant_alpha={"coherence": coherence, "regret": 0.5},
            foresight_signal={"confidence": top.get("confidence", 0.5)},
            mood_signal={"mood": emotion, "strength": urgency}
        )
        fused_conf = fused["fused_confidence"]

        dream_projection = self.dream_engine.generate_dream_projection()
        if dream_projection and top["future_title"] in str(dream_projection):
            volatility += 0.1

        mem_snap = self.memory.get_recent_memory(limit=1)
        last_goal = get_active_goals()[0] if get_active_goals() else "none"
        reason_entry = self.goal_trace.infer_reason(last_goal, emotion, urgency, fused_conf)

        decision = "HOLD"
        if bias == "DEFENSIVE":
            decision = "LIQUIDATE" if urgency > 0.85 else "HEDGE"
        elif bias == "AGGRESSIVE":
            decision = "BUY_HEAVY" if fused_conf > 0.8 else "BUY_SELECTIVE"
        elif bias == "STRATEGIC":
            decision = "REBALANCE" if urgency > 0.75 and coherence > 0.75 else "DIVERSIFY"
        elif bias == "RECKLESS":
            decision = "LEVERAGE_PUSH" if random.random() > 0.5 else "SWING_TRADE"
        elif bias == "EXPANSIVE":
            decision = "SECTOR_ROTATE" if fused_conf > 0.65 else "SCAN_EMERGING"

        if debate_scores:
            winning_agent = max(debate_scores, key=lambda x: x["score"])
            if winning_agent["score"] < 0.6:
                decision = "WAIT_SIGNAL"

        if urgency > 0.92 and coherence < 0.6 and random.random() < 0.25:
            decision = "MUTATION_TRADE"
            if SOVEREIGN_ENABLED:
                trigger_strategy_mutation(reason="high_urgency_low_coherence")

        codex_files = self.codex.validate_codex()
        if codex_files and "restricted_sectors.txt" in codex_files:
            if "energy" in top["future_title"].lower():
                decision = "AVOID_SECTOR"
                if SOVEREIGN_ENABLED:
                    print("🛑 [SOVEREIGN] Codex conflict — restricted sector triggered.")
                    trigger_sovereign_override(
                        context="restricted_sector_violation",
                        regret=0.8,
                        foresight=0.4,
                        coherence=coherence
                    )

        if SOVEREIGN_ENABLED and volatility > 0.6 and fused_conf > 0.85 and coherence < 0.5:
            print("🔥 [SOVEREIGN] Action contradiction detected — escalating override.")
            trigger_sovereign_override(
                context="market_execution_conflict",
                regret=0.7,
                foresight=0.4,
                coherence=coherence
            )

        risk_score = RiskAssessmentModule(
            portfolio=None,
            confidence=fused_conf,
            volatility=volatility,
            emotion=emotion
        ).evaluate()["score"]

        action_plan = {
            "action": decision,
            "bias": bias,
            "future": top.get("future_title", "unknown"),
            "confidence": round(fused_conf, 3),
            "volatility": round(volatility, 3),
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "swarm_emotion": self.swarm_emotions(),
            "goal_trace": reason_entry,
            "risk_score": round(risk_score, 3),
            "timestamp": datetime.utcnow().isoformat()
        }

        self.last_actions.append(action_plan)
        return action_plan

    def get_recent_actions(self, limit=5):
        return self.last_actions[-limit:]

    def execute_trade(self, candidate):
        print(f"📈 [TRADE] Executing trade for: {candidate}")
        trade_result = {
            "status": "executed",
            "details": candidate,
            "timestamp": datetime.utcnow().isoformat()
        }

        try:
            sovereign_memory.store(
                text=f"Executed trade: {candidate.get('action', 'unknown')}",
                metadata={
                    "agent": "TEX",
                    "intent": "market_trade_execution",
                    "conclusion": f"Executed trade: {candidate.get('action', 'unknown')}",
                    "tags": ["market", "reinforcement", "execution"],
                    "timestamp": trade_result["timestamp"],
                    "emotion": candidate.get("emotion", TEXPULSE.get("emotional_state")),
                    "urgency": candidate.get("urgency", TEXPULSE.get("urgency")),
                    "coherence": candidate.get("coherence", TEXPULSE.get("coherence")),
                    "trust_score": candidate.get("confidence", 0.5),
                    "reflexes": ["trade_execution", "reinforcement_loop"],
                    "meta_layer": "symbolic_trace",
                    "metadata": {
                        "goal": get_active_goals()[0] if get_active_goals() else "none",
                        "reason": candidate.get("goal_trace", "N/A"),
                        "risk_score": candidate.get("risk_score"),
                        "swarm_emotion": candidate.get("swarm_emotion", "N/A"),
                        "strategy_id": candidate.get("strategy_id", "unknown")
                    }
                }
            )
        except Exception as e:
            print(f"[REINFORCEMENT LOG ERROR] ❌ {e}")