# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/tex_master_orchestrator.py
# Purpose: Master controller to execute Part A + B of Tex AGI Brain
# Tier: ΩΩ — Financial Cortex Reflex Driver
# ============================================================

from finance.strategy.tex_execution_hub import TexExecutionHub  # optional
from finance.strategy.tex_orchestrator_part_a import FinanceOrchestrator as OrchestratorPartA
from finance.strategy.tex_orchestrator_part_b import FinanceOrchestrator as OrchestratorPartB


class MasterTexOrchestrator:
    def __init__(self, strategy_scoring, explain_portfolio_decision, brain_identity=None):
        self.last_future_report = {}

        # === Trait Injection ===
        self.identity = brain_identity or "TEX-FIN"
        self.strategy_scoring = strategy_scoring
        self.explain_portfolio_decision = explain_portfolio_decision

        # === Part A: Foresight & Alpha Cortex ===
        self.part_a = OrchestratorPartA(
            strategy_scoring=self.strategy_scoring
        )

        # === Part B: Reflex + Execution Cortex ===
        self.part_b = OrchestratorPartB(
            explain_portfolio_decision=self.explain_portfolio_decision,
            strategy_scoring=self.strategy_scoring
        )

        # Bind B’s reflex into A (loopless slot injection)
        self.part_a.run_cycle_part_b = self.part_b.run_cycle_part_b.__get__(self.part_a)

        # === Optional Hub ===
        self.hub = TexExecutionHub(
            strategy_scoring=self.strategy_scoring
        )

    def run_cycle(self):
        # === Part A: Generate strategy & projection
        part_a_output, alpha, foresight, portfolio, ranked, futures = self.part_a.run_cycle_part_a()

        # === Part B: Evaluate risk + reflex + voting
        part_b_output = self.part_b.run_cycle_part_b(alpha, foresight, portfolio, ranked, futures)

        # === Hub: Tactical feedback layer
        hub_output = self.hub.evaluate_reinforcements(alpha, foresight, portfolio, ranked)

        # === Final Fusion Report
        full_report = {
            **part_a_output,
            **part_b_output,
            "hub_result": hub_output,
            "cycle_brain_id": self.identity,
            "cycle_timestamp": datetime.utcnow().isoformat()
        }

        self.last_future_report = full_report
        return full_report


# === Local Reflex Test ===
if __name__ == "__main__":
    from datetime import datetime
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