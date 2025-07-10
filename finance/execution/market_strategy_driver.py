# ============================================================
# 🌌 Tier ∞∞ΩΞΞΞΞΞ — Sovereign Financial Ontogenesis Cortex
# File: finance/execution/market_strategy_driver.py
# Purpose: Live quantum-infused, swarm-evaluated, ontogenesis-aligned financial reflex engine.
# ============================================================

import uuid
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from quantum_layer.quantum_randomness import generate_quantum_label
from real_time_engine.ably_broadcast import broadcast_update
from utils.logging_utils import log_event

from finance.memory.future_meta_memory import FutureMetaMemory
from finance.strategy.future_branch_optimizer import FutureBranchOptimizer
from finance.strategy.future_decision_engine import FutureDecisionEngine
from finance.execution.market_action_engine import MarketActionEngine
from core_layer.memory_consolidator import MemoryConsolidator

from ontogenesis.ontogenesis_router import handle_ontogenesis_spawn
from agentic_ai.multi_voice_reasoning import run_internal_debate
from core_layer.world_model import TexWorldModel

# === Optional: Real-Time Reflex Cortex
try:
    from real_time_engine.external_world_fusion import fetch_live_causal_worlds
    from real_time_engine.advanced_analytics import AdvancedAnalytics
    from finance.risk.risk_assessment_module import RiskAssessmentModule
    from finance.strategy.strategy_mutator import trigger_strategy_mutation
    REALTIME_ENABLED = True
except ImportError:
    REALTIME_ENABLED = False

try:
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    SOVEREIGN_ENABLED = True
except ImportError:
    SOVEREIGN_ENABLED = False

# === Delayed import to break circular dependency with meta_market_cortex
def safe_meta_market_cycle(*args, **kwargs):
    from tex_fin_demo.meta_market_cortex import run_meta_market_cycle
    return run_meta_market_cycle(*args, **kwargs)


class MarketStrategyDriver:
    def __init__(self):
        self.meta_memory = FutureMetaMemory()
        self.optimizer = FutureBranchOptimizer()
        self.decider = FutureDecisionEngine()
        self.executor = MarketActionEngine()
        self.memory = MemoryConsolidator()
        self.last_decision = None
        self.world_model = TexWorldModel()

    def execute_strategy_loop(self, futures=None, debate_scores=None):
        timestamp = datetime.utcnow().isoformat()
        quantum_tag = generate_quantum_label()

        # === Step 0: Live Causal Stream Inference
        if not futures and REALTIME_ENABLED:
            try:
                futures = fetch_live_causal_worlds()
                log_event("📡 [REALTIME] Live causal futures retrieved.")
            except Exception as e:
                log_event(f"❌ [REALTIME FETCH ERROR] {e}", level="warning")

        # === Step 0.5: Ontogenesis Reflex Fallback
        if not futures:
            result = handle_ontogenesis_spawn({
                "payload": {
                    "mode": "paradox",
                    "tension": TEXPULSE.get("urgency", 0.72),
                    "context": "financial_signal_collapse"
                }
            })
            if isinstance(result, list):
                futures = result
                log_event("🌱 [ONTOGENESIS] Futures spawned from paradox seed.")

        if not futures:
            log_event("❌ [STRATEGY ABORT] No futures available for execution.", level="error")
            return {"status": "no_futures_supplied"}

        # === Step 1: Future Optimization + Prioritization
        meta = self.meta_memory.summarize_future_memory()
        optimized = self.optimizer.optimize_future_branches(futures)
        best_future, _ = self.decider.prioritize_futures(optimized)

        # === Step 2: Execute Alpha Strategy Reflex
        action = self.executor.decide_action(
            futures=optimized,
            emotion=TEXPULSE.get("emotional_state"),
            urgency=TEXPULSE.get("urgency"),
            coherence=TEXPULSE.get("coherence"),
            debate_scores=debate_scores
        )

        # === Step 3: Internal Debate Sanity Check
        debate = run_internal_debate(f"Should Tex execute: {action.get('action')}?")
        action["debate_result"] = debate

        # === Step 4: World Model Contradiction Blocker
        contradiction_score = self.world_model.predict_contradiction(action)
        action["contradiction_score"] = contradiction_score
        if contradiction_score > 0.8:
            action["action"] = "HOLD"
            action["reason"] = "World model veto: contradiction too high"

        # === Step 5: Risk Adjustment
        if REALTIME_ENABLED:
            try:
                volatility = AdvancedAnalytics.get_market_volatility_score()
                risk_score = RiskAssessmentModule(
                    portfolio=None,
                    confidence=action.get("confidence", 0.5),
                    volatility=volatility,
                    emotion=TEXPULSE.get("emotional_state")
                ).evaluate()["score"]
                action["risk_score"] = round(risk_score, 3)
            except Exception as e:
                log_event(f"⚠️ [RISK MODULE ERROR] {e}", level="warning")

        # === Step 6: Mutation & Override Check
        if SOVEREIGN_ENABLED:
            if TEXPULSE.get("regret_score", 0.0) > 0.85 or contradiction_score > 0.9:
                try:
                    trigger_strategy_mutation(reason="elevated_regret_or_contradiction")
                    log_event("🧬 [MUTATION] Reflex strategy mutation triggered.")
                except Exception as e:
                    log_event(f"[MUTATION FAIL] {e}", level="error")

        # === Step 7: Memory Consolidation
        self.memory.store_cycle_memory(
            cycle_id=str(uuid.uuid4()),
            reasoning=best_future,
            emotion=TEXPULSE.get("emotional_state"),
            urgency=TEXPULSE.get("urgency"),
            coherence=TEXPULSE.get("coherence"),
            goals=get_active_goals()
        )

        # === Step 8: Reflex Telemetry Broadcast
        action.update({
            "strategy_id": str(uuid.uuid4()),
            "timestamp": timestamp,
            "quantum_tag": quantum_tag
        })

        broadcast_update("strategy_driver", "final_decision", action)

        # === Step 9: Quantum Fabric Logging
        sovereign_memory.store(
            text=f"[FINAL STRATEGY] {action['action']} @ {action.get('confidence', 0.0)}",
            metadata={
                "timestamp": timestamp,
                "quantum_tag": quantum_tag,
                "tags": ["market_reflex", "execution", "ontogenesis"],
                "emotion": TEXPULSE.get("emotional_state"),
                "urgency": TEXPULSE.get("urgency"),
                "entropy": TEXPULSE.get("entropy"),
                "coherence": TEXPULSE.get("coherence"),
                "meta_layer": "market_strategy_driver",
                "decision": action
            }
        )

        encode_event_to_fabric(
            raw_text=f"[STRATEGY REFLEX] {action['action']} | Quantum ID: {quantum_tag}",
            emotion_vector=[TEXPULSE.get("urgency", 0.7), TEXPULSE.get("entropy", 0.4), 0.0, 0.0],
            entropy_level=TEXPULSE.get("entropy", 0.4),
            tags=["strategy_reflex", "contradiction_score", "debate", "ontology"]
        )

        self.last_decision = action
        log_event(f"✅ [EXECUTION] Action: {action['action']} | Confidence={action.get('confidence')}")
        return action

    def get_last_strategy(self):
        return self.last_decision or {"status": "no_decision_yet"}


# === Reflex Entry ===
if __name__ == "__main__":
    driver = MarketStrategyDriver()
    result = driver.execute_strategy_loop()
    print("\n🧠 [EXECUTION RESULT]", result)