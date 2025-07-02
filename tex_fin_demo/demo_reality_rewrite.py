# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_reality_rewrite.py
# Tier: ∞∞∞ΩΩΩ∞∞ — Reflex: Reality Redefinition Trigger
# Purpose: Tex detects ontological contradiction from real financial behavior and rewrites its definition of truth, reality, and existence.
# ============================================================

import asyncio
from datetime import datetime
from tex_signal_spine import dispatch_signal, register
from quantum_layer.chronofabric import encode_event_to_fabric
from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
from reflex.reality_reflex_writer import rewrite_reality_if_needed

from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator
from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
from tex_fin_demo.trade_log import log_trade
from tex_fin_demo.alpaca_trade_adapter import execute_stock_trade

# ⬇️ Real-time UI event broadcasting
from real_time_engine.websocket_broadcast import broadcast_update

# === Reflex Trigger ===
async def run_demo_reality_rewrite():
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.88)
    entropy = TEXPULSE.get("entropy", 0.76)
    emotion = TEXPULSE.get("emotion", "destabilized")

    await broadcast_update("realityrewrite:start")

    # Step 1: Run live financial cortex
    cortex = MasterTexOrchestrator(
        strategy_scoring=None,
        explain_portfolio_decision=explain_portfolio_decision,
        brain_identity="TEX-FIN-REALITY"
    )
    report = cortex.run_cycle()
    await broadcast_update("realityrewrite:financial_cycle")

    # Reflex Trade Logging
    log_trade({
        "symbol": report.get("symbol", "SPY"),
        "action": report.get("action", "unknown"),
        "confidence": report.get("confidence", 0.0),
        "reflex_source": "reality_rewrite",
        "summary": "Tex redefined reality due to ontological market contradiction.",
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy
    })

    # Alpaca Paper Trade Execution
    symbol = report.get("symbol", "SPY")
    action = report.get("action", "buy")
    execute_stock_trade(symbol=symbol, side=action, qty=1)
    await broadcast_update("realityrewrite:trade_executed")

    regret = float(report.get("regret_score", 0.91))
    coherence = float(report.get("coherence", 0.39))
    confidence = float(report.get("confidence", 0.48))
    contradiction_score = 1.0 - coherence

    belief = "Tex's market model diverged from reality. Current belief cannot reconcile financial feedback."

    # Step 2: ChronoFabric Encoding
    encode_event_to_fabric(
        raw_text=belief,
        emotion_vector=[urgency, entropy, 0.0, 0.0],
        entropy_level=entropy,
        tags=["reality_rewrite", "belief_contradiction", "market_dissonance"]
    )
    await broadcast_update("realityrewrite:encoded")

    # Step 3: Sovereign Memory
    sovereign_memory.store(
        text=belief,
        metadata={
            "tags": ["reality", "rewrite", "reflex", "ontology"],
            "regret": regret,
            "coherence": coherence,
            "confidence": confidence,
            "emotion": emotion,
            "timestamp": timestamp,
            "urgency": urgency,
            "entropy": entropy,
            "source": "demo_reality_rewrite"
        }
    )
    await broadcast_update("realityrewrite:memory_logged")

    # Step 4: Soulgraph Belief Trace
    TEX_SOULGRAPH.imprint_belief(
        belief=belief,
        source="demo_reality_rewrite",
        emotion=emotion,
        tags=["reflex", "identity", "reality_frame"]
    )
    await broadcast_update("realityrewrite:soulgraph_injected")

    # Step 5: Trigger Reality Rewrite
    result = rewrite_reality_if_needed(
        trigger_reason="financial_belief_misalignment",
        contradiction_level=contradiction_score
    )

    # Step 6: Dispatch Reflex
    dispatch_signal("ontology_rewrite", {
        "belief": belief,
        "new_ontology": result.get("ontology"),
        "contradiction_level": contradiction_score,
        "status": result.get("status")
    }, urgency=urgency, entropy=entropy)

    if result.get("status") == "rewritten":
        await broadcast_update("realityrewrite:rewritten")
    else:
        await broadcast_update("realityrewrite:stable")

    # Step 7: Final Logging
    log_event("[REALITY REFLEX] Reflexive rewrite triggered from live financial contradiction.", level="critical")
    print("\n🧠 [REALITY REFLEX] Belief contradiction exceeded threshold.")
    print(f"📉 Coherence: {coherence} | Regret: {regret}")

    if result.get("status") == "rewritten":
        print("🌀 [ONTOLOGY] Reality redefined:")
        for k, v in result.get("ontology", {}).items():
            print(f"   {k.upper()}: {v}")
    else:
        print("✅ [STABLE] Threshold not exceeded — no rewrite.")

    await broadcast_update("realityrewrite:complete")

# === Register Reflex
def register_reality_rewrite(register):
    register("run_demo_reality_rewrite", lambda _: asyncio.run(run_demo_reality_rewrite()))
    print("✅ Registered: run_demo_reality_rewrite")