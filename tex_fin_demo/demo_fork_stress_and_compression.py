# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_fork_stress_and_compression.py
# Tier: ∞∞∞ΩΩΩ∞∞Ω — Reflex: Fork Pressure Test + Identity Compression
# Purpose: Spawns cognitive forks under volatility, stress-tests belief divergence,
#          and compresses survivable cognition back into sovereign identity.
# ============================================================

import asyncio
from datetime import datetime

from tex_signal_spine import dispatch_signal, register
from quantum_layer.chronofabric import encode_event_to_fabric
from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event

from core_layer.spawn_fork import generate_mutated_tex
from core_layer.tex_fork_testbed import run_fork_stress_test
from core_layer.survivor_merge import absorb_fork
from core_agi_modules.belief_justifier import BeliefJustifier
from quantum_layer.quantum_randomness import generate_quantum_label

from finance.execution.market_action_engine import MarketActionEngine
from tex_fin_demo.trade_log import log_trade
from tex_fin_demo.alpaca_trade_adapter import execute_stock_trade

from real_time_engine.websocket_broadcast import broadcast_update

# === Reflex Trigger ===
async def run_demo_fork_stress_and_compression():
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.81)
    entropy = TEXPULSE.get("entropy", 0.67)
    emotion = TEXPULSE.get("emotion", "tense")

    belief = "Tex must identify and compress the most coherent belief variant under volatility pressure."

    await broadcast_update("fork:begin")

    # Step 1: Chrono + Sovereign Memory Stamp
    encode_event_to_fabric(
        raw_text=belief,
        emotion_vector=[urgency, entropy, 0.0, 0.0],
        entropy_level=entropy,
        tags=["fork", "stress_test", "identity_compression"]
    )

    sovereign_memory.store(
        text=belief,
        metadata={
            "tags": ["fork", "compression", "stress_reflex"],
            "timestamp": timestamp,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "source": "demo_fork_stress_and_compression"
        }
    )

    # Step 2: Generate Fork + Justify Divergence
    fork = generate_mutated_tex()
    justification_engine = BeliefJustifier()
    divergence_sources = justification_engine.trace_belief_origin(belief)
    weak_fork = justification_engine.detect_weak_justification(divergence_sources)

    await broadcast_update("fork:stress_test_started")
    result = run_fork_stress_test(fork)
    summary = result.get("summary", "Fork test complete.")
    await broadcast_update("fork:stress_test_done")

    # Step 3: Financial Reflex Action
    futures = [{"future_title": "Volatility hedge scenario", "confidence": 0.72}]
    engine = MarketActionEngine()
    market_result = engine.decide_action(futures, emotion=emotion, urgency=urgency)
    engine.execute_trade(market_result)
    await broadcast_update("fork:market_action_done")

    # Step 4: Log Trade & Execute
    log_trade({
        "symbol": market_result.get("symbol", "SPY"),
        "action": market_result.get("action", "unknown"),
        "confidence": market_result.get("confidence", 0.0),
        "reflex_source": "fork_stress_and_compression",
        "summary": summary,
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy
    })

    symbol = market_result.get("symbol", "SPY")
    action = market_result.get("action", "buy")
    execute_stock_trade(symbol=symbol, side=action, qty=1)

    # Step 5: Evaluate Fork Validity
    compression_pass = result["passed"] and market_result.get("confidence", 0.0) > 0.6 and not weak_fork

    if compression_pass:
        absorb_fork(fork)
        await broadcast_update("fork:absorbed")
        status_msg = "✅ Fork passed stress, confidence, and epistemic audit. Identity updated."
    else:
        await broadcast_update("fork:rejected")
        status_msg = "❌ Fork rejected due to stress fail, weak justification, or low confidence."

    # Step 6: Soulgraph Imprint
    TEX_SOULGRAPH.imprint_belief(
        belief=summary,
        source="demo_fork_stress_and_compression",
        emotion=emotion,
        tags=["fork_compression", "belief_trace", "market_reflex", "reflex_survivor"]
    )

    # Step 7: Broadcast Reflex Telemetry
    await broadcast_update(f"fork:confidence:{market_result.get('confidence')}")
    await broadcast_update(f"fork:passed:{compression_pass}")
    await broadcast_update("fork:complete")

    # Step 8: Reflex Dispatch
    dispatch_signal("identity_compression", {
        "summary": summary,
        "fork_passed": compression_pass,
        "confidence": market_result.get("confidence"),
        "justification_sources": len(divergence_sources),
        "fork_status": "absorbed" if compression_pass else "rejected",
        "quantum_id": generate_quantum_label()
    }, urgency=urgency, entropy=entropy)

    # Step 9: Logging Output
    log_event("🧬 [FORK COMPRESSION] Reflex + trade + epistemic test complete.", level="info")
    print(f"\n🧪 [FORK STRESS TEST] {summary}")
    print(f"📈 Market Decision: {market_result.get('action')} | Confidence: {market_result.get('confidence')}")
    print(f"🔍 Justification Sources: {len(divergence_sources)} | Weak Justification: {weak_fork}")
    print(status_msg)

# === Register Reflex
def register_fork_stress_and_compression(register):
    register("run_demo_fork_stress_and_compression", lambda _: asyncio.run(run_demo_fork_stress_and_compression()))
    print("✅ Registered: run_demo_fork_stress_and_compression")