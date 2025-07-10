# ============================================================
# 🧠 Tex Master Reflex Orchestrator | Tier: ∞∞∞ΩΞΣΩ
# File: finance/strategy/tex_master_orchestrator.py
# Purpose: Executes full AGI loop — Strategy Cortex (Part A) → Reflex Cortex (Part B) → Hub Reinforcement
# ============================================================

from datetime import datetime
from uuid import uuid4

from agentic_ai.sovereign_memory import sovereign_memory
from finance.strategy.tex_orchestrator_part_a import FinanceOrchestrator as OrchestratorPartA
from finance.strategy.tex_orchestrator_part_b import FinanceOrchestrator as OrchestratorPartB
from finance.strategy.tex_execution_hub import TexExecutionHub  # Optional layer

class MasterTexOrchestrator:
    def __init__(self, strategy_scoring, explain_portfolio_decision, brain_identity=None):
        self.identity = brain_identity or "TEX-FINANCE"
        self.strategy_scoring = strategy_scoring
        self.explain_portfolio_decision = explain_portfolio_decision
        self.last_future_report = {}

        # === Cortex A: Strategy + Foresight + Portfolio Thinking
        self.part_a = OrchestratorPartA(strategy_scoring=self.strategy_scoring)

        # === Cortex B: Reflex Reasoning + Risk + Override
        self.part_b = OrchestratorPartB(
            explain_portfolio_decision=self.explain_portfolio_decision,
            strategy_scoring=self.strategy_scoring
        )

        # Inject Part B reflex into Part A (loopless continuity)
        self.part_a.run_cycle_part_b = self.part_b.run_cycle_part_b.__get__(self.part_a)

        # === Optional Hub: Reinforcement Reasoner
        self.hub = TexExecutionHub(strategy_scoring=self.strategy_scoring)

    def run_cycle(self, forced_action=None):
        cycle_tag = uuid4().hex
        cycle_timestamp = datetime.utcnow().isoformat()

        # === Run Part A: Generate alpha, foresight, portfolio, futures
        part_a = self.part_a.run_cycle()
        alpha = part_a["strategy"]
        foresight = part_a["foresight"]
        portfolio = part_a["portfolio"]
        futures = part_a["futures"]
        score = part_a["score"]
        ranked = [{"strategy": alpha, "score": score}]  # Compatibility stub

        # === Run Part B: Execution, Reflex Logic, Overrides
        part_b = self.part_b.run_cycle_part_b(
            alpha=alpha,
            foresight=foresight,
            portfolio=portfolio,
            ranked=ranked,
            futures=futures
        )

        # === Hub Layer: Tactical Reinforcement & Fine-Tuning
        hub = self.hub.evaluate_reinforcements(
            alpha=alpha,
            foresight=foresight,
            portfolio=portfolio,
            ranked=ranked
        )

        # === Final Memory Fusion
        full_report = {
            **part_a,
            **part_b,
            "hub_result": hub,
            "cycle_brain_id": self.identity,
            "cycle_timestamp": cycle_timestamp
        }

        self.last_future_report = full_report

        # === Reflex Memory Injection
        sovereign_memory.store(
            text="🧠 [MASTER CYCLE COMPLETE] Full orchestration of strategy + reflex.",
            metadata={
                "intent": "master_strategy_cycle",
                "meta_layer": "tex_master_orchestrator",
                "tags": ["master_cycle", "fusion", "reflex", "alpha", "finance"],
                "cycle_id": cycle_tag,
                "timestamp": cycle_timestamp,
                "identity": self.identity,
                "strategy_id": alpha.get("strategy_id"),
                "quantum_tag": full_report.get("quantum_tag")
            }
        )

        return full_report


# === Reflex Test Entry ===
if __name__ == "__main__":
    from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
    from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator

    print("\n🔁 [TEST MODE] Launching Tex Financial Cortex Reflex...\n")

    cortex = MasterTexOrchestrator(
        strategy_scoring=StrategyVariantSimulator(),
        explain_portfolio_decision=explain_portfolio_decision,
        brain_identity="ReflexTestCore"
    )

    result = cortex.run_cycle()
    for key, value in result.items():
        print(f"\n=== {key.upper()} ===\n{value}")