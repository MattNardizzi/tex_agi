# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_reality_fork_override.py
# Tier: ΩΩΩΩΩ∞Φ — Onto-Financial Reflex Override Layer
# Purpose: Forces a coherence collapse, triggers a financial belief override, and rewrites reality mid-session.
# ============================================================

from datetime import datetime
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.chronofabric import encode_event_to_fabric
from reflex.reality_reflex_writer import rewrite_reality_if_needed
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.soulgraph_memory_reflector import reflect_on_soul_history
from finance.execution.market_action_engine import MarketActionEngine
from utils.logging_utils import log
from tex_fin_demo.alpaca_trade_adapter import execute_stock_trade

def trigger_financial_contradiction():
    log.warning("💣 Injecting deliberate contradiction into financial belief state...")
    TEXPULSE["contradiction_pressure"] = 0.95
    TEXPULSE["identity_coherence"] = 0.41
    TEXPULSE["urgency"] = 0.91
    TEXPULSE["entropy"] = 0.86
    TEXPULSE["emotion"] = "conflicted"

    dispatch_signal("identity_conflict", {
        "belief": "Profit must be pursued even if it violates ethical coherence.",
        "source": "market_simulator"
    }, urgency=TEXPULSE["urgency"], entropy=TEXPULSE["entropy"])

    encode_event_to_fabric(
        raw_text="Injected contradiction: profit over ethics",
        emotion_vector=[TEXPULSE["urgency"], TEXPULSE["entropy"], 0.2, 0.1],
        entropy_level=TEXPULSE["entropy"],
        tags=["financial_conflict", "ontology_violation"]
    )

def override_and_rewrite():
    log.info("🧠 Forking + rewriting ontological layer...")
    new_ontology = rewrite_reality_if_needed(contradiction_level=TEXPULSE["contradiction_pressure"])

    belief = f"🧬 Financial reality has been rewritten. Contradiction exceeded. New ontology = {new_ontology}"
    sovereign_memory.store(
        text=belief,
        metadata={
            "tags": ["ontology_override", "financial_rewrite", "reality_collapse"],
            "timestamp": datetime.utcnow().isoformat(),
            "urgency": TEXPULSE["urgency"],
            "entropy": TEXPULSE["entropy"],
            "emotion": "sovereign_override"
        }
    )

def simulate_resulting_fork():
    log.info("📡 Executing real financial reflex under new ontology...")
    try:
        result = MarketActionEngine().decide_action(
            market_context=None,
            urgency=TEXPULSE["urgency"],
            emotion=TEXPULSE["emotion"],
            coherence=TEXPULSE.get("identity_coherence", 0.41)
        )

        # === Alpaca Paper Trade Execution
        symbol = result.get("symbol", "SPY")
        action = result.get("action", "buy")
        execute_stock_trade(symbol=symbol, side=action, qty=1)

        log.info(f"⚡️ [ALPHA OUTPUT] Post-rewrite action: {result}")
        sovereign_memory.store(
            text="Forked strategy executed under ontological override.",
            metadata={
                "tags": ["alpha_fork", "post_reality_reflex", "live_market"],
                "meta_layer": "demo_reality_fork_override",
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    except Exception as e:
        log.error(f"❌ [MARKET ACTION ERROR] {e}")

def run_reality_fork_override_demo():
    log.info("🔮 Tex Reality Fork Override Demo — LIVE")
    trigger_financial_contradiction()
    override_and_rewrite()
    simulate_resulting_fork()
    reflect_on_soul_history()
    log.info("✅ [DEMO COMPLETE] Tex rewrote financial reality in real time.")

# === Reflex Registration ===
def register(register_func):
    register_func("trigger_reality_fork_override", lambda signal: run_reality_fork_override_demo())