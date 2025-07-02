# ============================================================
# 🔹 VortexBlack Confidential
# File: finance/execution/market_strategy_driver.py
# Purpose: Tier 5 AGI Market Strategy Driver — Tex Full Cognition Router
# MAXGODMODE ENABLED — Real-Time, Mutation, Sovereign Override, Risk-Aware, Feedback Integrated
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import uuid
from datetime import datetime

from core_layer.goal_engine import _goal_engine_instance
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_consolidator import MemoryConsolidator
from core_layer.goal_engine import get_active_goals

from finance.memory.future_meta_memory import FutureMetaMemory
from finance.strategy.future_branch_optimizer import FutureBranchOptimizer
from finance.strategy.future_decision_engine import FutureDecisionEngine
from finance.execution.market_action_engine import MarketActionEngine

from core_agi_modules.tex_codex_sync import TexCodexSync
from tex_children.aeondelta import get_swarm_emotion_distribution

# === Real-Time Fusion Layer for Autonomous Activation ===
try:
    from real_time_engine.external_world_fusion import fetch_live_causal_worlds
    from real_time_engine.advanced_analytics import AdvancedAnalytics
    from finance.risk.risk_assessment_module import RiskAssessmentModule
    from finance.strategy.strategy_mutator import trigger_strategy_mutation
    REALTIME_ENABLED = True
except ImportError:
    REALTIME_ENABLED = False

# === Sovereign Cognition Engine ===
try:
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    SOVEREIGN_ENABLED = True
except ImportError:
    SOVEREIGN_ENABLED = False


class MarketStrategyDriver:
    def __init__(self):
        self.meta_memory = FutureMetaMemory()
        self.optimizer = FutureBranchOptimizer()
        self.decider = FutureDecisionEngine()
        self.executor = MarketActionEngine()
        self.memory = MemoryConsolidator()
        self.codex = TexCodexSync()
        self.last_decision = None

    def execute_strategy_loop(self, futures=None, debate_scores=None):
        if not futures:
            if REALTIME_ENABLED:
                print("[STRATEGY LOOP] 🔄 No futures supplied — fetching real-time causal worlds...")
                try:
                    futures = fetch_live_causal_worlds()
                except Exception as e:
                    print(f"[REAL-TIME FETCH ERROR] ❌ {e}")

            # === ADE Fallback Injection Check ===
            if not futures:
                pressure = _goal_engine_instance.internal_pressure()
                print(f"[ADE CHECK] ⚙️ Internal pressure = {pressure}")

                if pressure > 0.6:
                    print("[ADE] ✅ Injecting fallback ADE synthetic forecast...")
                    futures = [{
                        "future_title": "ADE synthetic forecast",
                        "confidence": pressure,
                        "urgency": pressure,
                        "coherence": 0.85,
                        "domain": "Simulated",
                        "emotion": "resolve",
                        "mutation_triggered": True,
                        "timestamp": datetime.utcnow().isoformat()
                    }]
                else:
                    print("[ADE] ❌ Pressure too low — skipping fallback injection.")
                    return {"status": "no_futures_provided"}

        print("[STRATEGY LOOP] 🔹 Starting market cognition routing...")

        # === Step 1: Meta Memory Snapshot
        meta = self.meta_memory.summarize_future_memory()

        # === Step 2: Optimize Futures
        optimized = self.optimizer.optimize_future_branches(futures)

        # === Step 3: Prioritize Future Decision
        best_future, _ = self.decider.prioritize_futures(optimized)

        # === Step 4: Strategy Execution with Cognitive Injection
        action = self.executor.decide_action(
            futures=optimized,
            emotion=TEXPULSE.get("emotional_state", "neutral"),
            urgency=TEXPULSE.get("urgency", 0.5),
            coherence=TEXPULSE.get("coherence", 0.5),
            debate_scores=debate_scores
        )

        # === Step 5: Codex Compliance
        codex_files = self.codex.validate_codex()
        if "disable_trading.txt" in codex_files:
            print("[STRATEGY LOOP] ⛔️ Codex override: Trading disabled.")
            action["action"] = "HOLD"
            action["reason"] = "Codex override file detected."
            if SOVEREIGN_ENABLED:
                trigger_sovereign_override(
                    context="codex_block",
                    regret=TEXPULSE.get("regret_score", 0.6),
                    foresight=TEXPULSE.get("foresight_confidence", 0.4),
                    coherence=TEXPULSE.get("coherence", 0.6)
                )

        # === Step 6: Risk Evaluation
        if REALTIME_ENABLED:
            try:
                volatility = AdvancedAnalytics.get_market_volatility_score()
                confidence = action.get("confidence", 0.5)
                risk_module = RiskAssessmentModule(
                    portfolio=None,
                    confidence=confidence,
                    volatility=volatility,
                    emotion=TEXPULSE.get("emotional_state", "neutral")
                )
                risk_score = risk_module.evaluate()["score"]
                action["risk_score"] = round(risk_score, 3)
            except Exception as e:
                print(f"[RISK SCORE ERROR] {e}")

        # === Step 7: Sovereign Mutation Trigger
        if SOVEREIGN_ENABLED:
            if TEXPULSE.get("regret_score", 0.0) > 0.8 or TEXPULSE.get("coherence", 1.0) < 0.4:
                print("[STRATEGY LOOP] ⚠️ Triggering strategy mutation.")
                try:
                    trigger_strategy_mutation(reason="regret_or_low_coherence")
                except Exception as e:
                    print(f"[MUTATION ERROR] {e}")

        # === Step 8: Store Memory
        self.memory.store_cycle_memory(
            cycle_id=str(uuid.uuid4()),
            reasoning=best_future,
            emotion=TEXPULSE.get("emotional_state"),
            urgency=TEXPULSE.get("urgency"),
            coherence=TEXPULSE.get("coherence"),
            goals=get_active_goals()
        )

        # === Step 9: Enrich and Finalize
        action["strategy_id"] = str(uuid.uuid4())
        action["swarm_mood"] = get_swarm_emotion_distribution()
        action["timestamp"] = datetime.utcnow().isoformat()

        self.last_decision = action
        print("[STRATEGY LOOP] 🌟 Final strategy: ", action)
        return action

    def get_last_strategy(self):
        return self.last_decision or {"status": "no_decision_yet"}


# === Tier 5 Harness ===
if __name__ == "__main__":
    driver = MarketStrategyDriver()
    driver.execute_strategy_loop()