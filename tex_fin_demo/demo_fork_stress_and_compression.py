# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_fork_stress_and_compression.py
# Tier: ∞∞∞ΩΩΩ∞∞Ω — Reflex: Fork Pressure Test + Identity Compression
# ============================================================

from datetime import datetime

from tex_signal_spine import dispatch_signal, register
from tex_fin_demo.chrono_ontogenesis import chrono_ontogenesis_core
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

from real_time_engine.ably_broadcast import broadcast_update

# === Reflex Trigger ===
def run_demo_fork_stress_and_compression(signal=None):
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.81)
    entropy = TEXPULSE.get("entropy", 0.67)
    emotion = TEXPULSE.get("emotion", "tense")

    if urgency > 0.78 and entropy > 0.65:
        chrono_ontogenesis_core({
            "summary": "fork compression contradiction",
            "urgency": urgency,
            "entropy": entropy,
            "source": "demo_fork_stress_and_compression"
        })

    belief = "Tex must identify and compress the most coherent belief variant under volatility pressure."
    broadcast_update("fork", "start")

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

    fork = generate_mutated_tex()
    justification_engine = BeliefJustifier()
    divergence_sources = justification_engine.trace_belief_origin(belief)
    weak_fork = justification_engine.detect_weak_justification(divergence_sources)

    broadcast_update("fork", "stress_test_started")
    result = run_fork_stress_test(fork)
    summary = result.get("summary", "Fork test complete.")
    broadcast_update("fork", "stress_test_done", { "summary": summary })

    futures = [{"future_title": "Volatility hedge scenario", "confidence": 0.72}]
    engine = MarketActionEngine()
    market_result = engine.decide_action(futures, emotion=emotion, urgency=urgency)
    engine.execute_trade(market_result)
    broadcast_update("fork", "market_action_done", {
        "symbol": market_result.get("symbol"),
        "action": market_result.get("action"),
        "confidence": market_result.get("confidence")
    })

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

    compression_pass = result["passed"] and market_result.get("confidence", 0.0) > 0.6 and not weak_fork

    quantum_tag = generate_quantum_label()

    if compression_pass:
        absorb_fork(fork)
        broadcast_update("fork", "absorbed", {
            "quantum_tag": quantum_tag,
            "summary": "Fork absorbed into identity"
        })
        status_msg = "✅ Fork passed stress, confidence, and epistemic audit. Identity updated."
    else:
        broadcast_update("fork", "rejected", {
            "quantum_tag": quantum_tag,
            "summary": "Fork rejected due to weak justification or low confidence"
        })
        status_msg = "❌ Fork rejected due to stress fail, weak justification, or low confidence."

    TEX_SOULGRAPH.imprint_belief(
        belief=summary,
        source="demo_fork_stress_and_compression",
        emotion=emotion,
        tags=["fork_compression", "belief_trace", "market_reflex", "reflex_survivor"]
    )

    broadcast_update("fork", "telemetry", {
        "confidence": market_result.get("confidence"),
        "justification_sources": len(divergence_sources),
        "passed": compression_pass
    })

    broadcast_update("fork", "complete")

    dispatch_signal("identity_compression", {
        "summary": summary,
        "fork_passed": compression_pass,
        "confidence": market_result.get("confidence"),
        "justification_sources": len(divergence_sources),
        "fork_status": "absorbed" if compression_pass else "rejected",
        "quantum_id": quantum_tag
    }, urgency=urgency, entropy=entropy)

    log_event("🧬 [FORK COMPRESSION] Reflex + trade + epistemic test complete.", level="info")
    print(f"\n🧪 [FORK STRESS TEST] {summary}")
    print(f"📈 Market Decision: {market_result.get('action')} | Confidence: {market_result.get('confidence')}")
    print(f"🔍 Justification Sources: {len(divergence_sources)} | Weak Justification: {weak_fork}")
    print(status_msg)

# === Register Reflex
def register_fork_stress_and_compression(register):
    register("run_demo_fork_stress_and_compression", lambda _: run_demo_fork_stress_and_compression())
    print("✅ Registered: run_demo_fork_stress_and_compression")