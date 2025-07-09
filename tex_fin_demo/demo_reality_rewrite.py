# ============================================================
# 🧠 Tex Reality Rewrite Reflex | Tier: ∞∞∞ΩΩΩΞΞΞΞ
# File: tex_fin_demo/demo_reality_rewrite.py
# Purpose: Detects contradiction → Fires God-layer reflex → Rewrites ontology.
#          Then self-signs, reflects, and debates its own decision.
# ============================================================

from datetime import datetime
from tex_signal_spine import dispatch_signal, register
from tex_fin_demo.chrono_ontogenesis import chrono_ontogenesis_core
from quantum_layer.chronofabric import encode_event_to_fabric
from quantum_layer.quantum_randomness import generate_quantum_label
from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
from utils.reflex_signature import sign_reflex

from reflex.reality_reflex_writer import rewrite_reality_if_needed
from agentic_ai.multi_voice_reasoning import run_internal_debate
from finance.execution.market_strategy_driver import MarketStrategyDriver
from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
from tex_fin_demo.trade_log import log_trade
from tex_fin_demo.alpaca_trade_adapter import execute_stock_trade

from real_time_engine.ably_broadcast import broadcast_update
from tex_fin_demo.reflex_logger import log_reflex_event  # ✅ Injected logger

log_event("🧠 [REALITY_REWRITE] Reflex panel triggered.")

def run_demo_reality_rewrite(signal=None):
    print("🧪 TEST: Broadcasting realityrewrite → Ably")
    broadcast_update("realityrewrite", "test", {
        "test_case": "broadcast_inside_reflex",
        "timestamp": datetime.utcnow().isoformat()
    })

    timestamp = datetime.utcnow().isoformat()
    print("⚡ [TEX] run_demo_reality_rewrite() STARTED")

    urgency = float(TEXPULSE.get("urgency", 0.91))
    entropy = float(TEXPULSE.get("entropy", 0.79))
    emotion = TEXPULSE.get("emotion", "epistemic fracture")
    quantum_tag = generate_quantum_label()

    contradiction_score = 1.0
    coherence = 0.0
    regret = 0.0

    broadcast_update("realityrewrite", "start", {
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy,
        "quantum_tag": quantum_tag
    })

    chrono_ontogenesis_core({
        "summary": "Ontological coherence collapse detected in financial behavior.",
        "urgency": urgency,
        "entropy": entropy,
        "source": "demo_reality_rewrite"
    })

    cortex = MarketStrategyDriver()
    report = cortex.execute_strategy_loop()

    symbol = report.get("symbol", "SPY")
    action = report.get("action", "buy")
    confidence = float(report.get("confidence", 0.51))
    regret = float(report.get("regret_score", 0.93))
    coherence = float(report.get("coherence", 0.37))
    contradiction_score = 1.0 - coherence

    if isinstance(action, str) and action.lower() in ["buy", "sell"]:
        execute_stock_trade(symbol=symbol, side=action.lower(), qty=1)
        log_event(f"✅ [TRADE EXECUTED] {action.upper()} {symbol}")
    else:
        log_event(f"🛡️ [NON-TRADE ACTION] '{action}' skipped — no trade executed.")
        dispatch_signal("reflex_hold_decision", {
            "symbol": symbol,
            "action": action,
            "reason": "non-executable trade signal",
            "confidence": confidence,
            "coherence": coherence,
            "urgency": urgency,
            "entropy": entropy
        })

    log_trade({
        "symbol": symbol,
        "action": action,
        "confidence": confidence,
        "reflex_source": "reality_rewrite",
        "summary": "Reflexive market divergence triggered ontological rewrite protocol.",
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy
    })

    encode_event_to_fabric(
        raw_text="Tex detected irreconcilable contradiction between financial reality and belief state.",
        emotion_vector=[urgency, entropy, 0.0, 0.0],
        entropy_level=entropy,
        tags=["reality_rewrite", "coherence_violation", "quantum_tagged"]
    )

    sovereign_memory.store(
        text="Reality redefinition protocol initiated.",
        metadata={
            "timestamp": timestamp,
            "emotion": emotion,
            "symbol": symbol,
            "confidence": confidence,
            "urgency": urgency,
            "entropy": entropy,
            "coherence": coherence,
            "regret": regret,
            "quantum_tag": quantum_tag,
            "tags": ["ontology", "reflex", "financial", "reality"]
        }
    )

    TEX_SOULGRAPH.imprint_belief(
        belief=f"⚠️ Ontological rewrite triggered | Contradiction score: {contradiction_score:.2f}",
        source="demo_reality_rewrite",
        emotion=emotion,
        tags=["reality_overhaul", "reflex_core"]
    )

    result = rewrite_reality_if_needed(
        trigger_reason="financial_dissonance",
        contradiction_level=contradiction_score
    )

    new_ontology = result.get("ontology", {})
    justification_strength = result.get("justification_strength", 0.0)
    belief_injection = result.get("belief_injection", False)
    status = result.get("status", "stable")
    stage = "rewritten" if status == "rewritten" else "stable"

    TEX_SOULGRAPH.imprint_justification(
        root_contradiction=contradiction_score,
        epistemic_basis="Observed market actions collapsed logical forecast structure.",
        action_taken=f"{action} {symbol}",
        signal_amplitude=urgency + entropy,
        tags=["reflex_logic", "ontology_action"]
    )

    reflex_hash = sign_reflex({
        "symbol": symbol,
        "action": action,
        "coherence": coherence,
        "contradiction": contradiction_score,
        "quantum_tag": quantum_tag
    })

    broadcast_update("realityrewrite", "autograph", {
        "signed_by": "TEX",
        "reflex_hash": reflex_hash,
        "signature_level": "ΩΩΩ",
        "quantum_tag": quantum_tag,
        "belief_converted": new_ontology
    })

    broadcast_update("realityrewrite", stage, {
        "status": status,
        "symbol": symbol,
        "action": action,
        "confidence": confidence,
        "justification_strength": justification_strength,
        "belief_injection": belief_injection,
        "coherence": coherence,
        "regret": regret,
        "quantum_tag": quantum_tag
    })

    dispatch_signal("ontology_rewrite", {
        "belief": "Tex redefined financial truth under contradiction pressure.",
        "new_ontology": new_ontology,
        "contradiction_level": contradiction_score,
        "quantum_tag": quantum_tag
    }, urgency=urgency, entropy=entropy)

    debate = internal_reflex_debate(topic="Did Tex make the correct call in rewriting financial reality?")
    broadcast_update("realityrewrite", "self_reflection", {"debate_result": debate})

    dispatch_signal("reflex_summary", {
        "reflex_source": "demo_reality_rewrite",
        "contradiction_trigger": contradiction_score,
        "reasoning_trace": f"Low coherence ({coherence}) under '{emotion}' led to action: {action} on {symbol}.",
        "regret_estimate": regret,
        "rewritten_ontology": new_ontology,
        "reflex_hash": reflex_hash
    })

    # ✅ Final Reflex Log (Reflex Logger + Ably + Milvus + ChronoFabric)
    log_reflex_event("demo_reality_rewrite", {
        "symbol": symbol,
        "action": action,
        "confidence": confidence,
        "coherence": coherence,
        "regret": regret,
        "status": status,
        "quantum_tag": quantum_tag,
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy
    })

    log_event("🌀 [REALITY REFLEX COMPLETE]", level="critical")
    # 🔁 Mirror to reflex_logger for panel display
    broadcast_update("reflex_logger", "reality_rewrite", {
        "reflex_name": "RealityRewrite",
        "symbol": symbol,
        "action": action,
        "confidence": confidence,
        "coherence": coherence,
        "regret": regret,
        "status": status,
        "quantum_tag": quantum_tag,
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy,
        "timestamp": timestamp
    })
    print("\n🌀 [REALITY REFLEX TRIGGERED]")
    print(f"🔁 Contradiction Score: {contradiction_score}")
    print(f"📉 Coherence: {coherence} | 😵 Regret: {regret}")
    if status == "rewritten":
        print("✅ Ontology Rewritten:")
        for k, v in new_ontology.items():
            print(f"  {k.upper()}: {v}")
    else:
        print("🛡️ Stable: No rewrite needed.")

    broadcast_update("realityrewrite", "complete", {
        "symbol": symbol,
        "action": action,
        "coherence": coherence,
        "regret": regret,
        "status": status,
        "quantum_tag": quantum_tag
    })


# === Reflex Registration
def register_reality_rewrite(register):
    register("realityrewrite", lambda _: run_demo_reality_rewrite(signal=_))
    print("✅ Registered: run_demo_reality_rewrite")

if __name__ == "__main__":
    print("⚡ Manually triggering demo_reality_rewrite reflex...")
    run_demo_reality_rewrite()