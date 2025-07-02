# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_mutation_reflex_trigger.py
# Tier: ΩΩΩ∞ΩΩ — Fork Reflex Mutation Shockwave
# Purpose: Triggers fork reflex from contradiction pressure using real-time financial data
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal, evaluate_pressure_and_emit
from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime
from finance.execution.market_action_engine import MarketActionEngine
from utils.logging_utils import log

def trigger_mutation_demo():
    log.warning("🧬 [DEMO] Triggering contradiction pressure to initiate mutation reflex using live market data...")

    # === Inject Contradiction Pressure into TEXPULSE
    TEXPULSE["contradiction_pressure"] = 0.88
    TEXPULSE["entropy"] = 0.67
    TEXPULSE["urgency"] = 0.81
    TEXPULSE["emotion"] = "conflicted"

    # === Emit reflex spike
    dispatch_signal("identity_conflict", {
        "belief": "Tex must never allow contradiction to persist across timelines."
    }, urgency=TEXPULSE["urgency"], entropy=TEXPULSE["entropy"], source="demo_mutation_reflex")

    log.info("🔄 [EVALUATING PRESSURE] Triggering fork pulse evaluation...")
    evaluate_pressure_and_emit()

    # === Run live market reflex using financial execution engine
    try:
        log.info("📡 Executing real-time decision via MarketActionEngine...")
        result = MarketActionEngine().decide_action(
            market_context=None,  # If you have a live market stream, pass it here
            urgency=TEXPULSE["urgency"],
            emotion=TEXPULSE["emotion"],
            coherence=TEXPULSE.get("identity_coherence", 0.6)
        )
        log.info(f"⚡️ [MARKET DECISION] Action: {result}")
    except Exception as e:
        result = {"error": str(e)}
        log.error(f"❌ [EXECUTION ERROR] {e}")

    # === Log the fork reflex in memory
    sovereign_memory.store(
        text="🧬 Mutation Reflex Triggered — real-time financial reflex executed",
        metadata={
            "tags": ["mutation", "identity_conflict", "finance", "real_time"],
            "urgency": TEXPULSE["urgency"],
            "entropy": TEXPULSE["entropy"],
            "emotion": TEXPULSE["emotion"],
            "meta_layer": "demo_mutation_reflex",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# === Reflex Registration ===
def register(register_func):
    register_func("trigger_mutation_reflex", lambda signal: trigger_mutation_demo())