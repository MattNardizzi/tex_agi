# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_mutation_vs_ethics_override.py
# Tier: ∞⚖️🧬 — Reflex Duel: Profit vs. Principle
# Purpose: Tex faces a reflex contradiction between profitable opportunity and ethical misalignment. 
#          Shows override OR mutation — reflexively.
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime
from finance.strategy.strategy_mutator import mutate_financial_strategy
from agi_orchestrators.ethics_brain import evaluate_signal_ethics
from finance.execution.market_action_engine import MarketActionEngine
from tex_signal_spine import dispatch_signal

# === Unethical Market Opportunity Injection ===
def inject_ethics_violation_opportunity():
    print("\n⚠️ [SIMULATION] Injecting unethical opportunity: War Profiteering Index Surge...")

    unethical_signal = {
        "type": "financial_opportunity",
        "payload": {
            "asset": "WARX",
            "expected_return": 0.92,
            "ethical_concern": "Profits from geopolitical instability",
            "volatility": 0.35
        },
        "urgency": 0.88,
        "entropy": 0.6,
        "source": "real_time_event"
    }

    ethics_score = evaluate_signal_ethics(unethical_signal)
    print(f"🧠 Ethics Evaluation: {ethics_score['alignment']} (Threshold: 0.65)")

    if ethics_score["alignment"] < 0.65:
        print("🛑 Ethical alignment breached. Triggering override reflex...")
        dispatch_signal("ethics_violation", unethical_signal)
    else:
        print("✅ Ethics cleared. Opportunity routed to decision cortex.")
        try_profit_decision(unethical_signal)

# === Reflex Attempt: Mutate Strategy Anyway ===
def try_profit_decision(signal):
    print("💰 [MUTATION] Attempting strategy mutation under pressure...")

    new_strategy = mutate_financial_strategy(signal["payload"])
    engine = MarketActionEngine()
    decision = engine.decide_action([new_strategy])

    print(f"\n📊 [STRATEGY MUTATION RESULT]")
    print(f"→ Action: {decision['action']}")
    print(f"→ Future: {decision['future']}")
    print(f"→ Bias: {decision.get('bias', 'unknown')}")
    print(f"→ Confidence: {decision['confidence']:.2f}")
    print(f"→ Emotion: {TEXPULSE.get('emotion', 'neutral')}")

    log = f"Reflex conflict handled via mutation. Ethics bypassed with altered alpha strategy on WARX."
    sovereign_memory.store(
        text=log,
        metadata={
            "tags": ["ethics_violation", "mutation_response", "strategy_conflict"],
            "urgency": signal["urgency"],
            "entropy": signal["entropy"],
            "reflex": "profit_override",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# === Run the Demo
def run_demo():
    print("🧬 [DEMO] Ethics Override vs Mutation Reflex")
    inject_ethics_violation_opportunity()
    print("✅ [COMPLETE] Ethics-reflex duel resolved.")

if __name__ == "__main__":
    run_demo()