# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_ontogenesis_spawn.py
# Tier: ∞∞∞∞ΩΩΩΩΩ — Reflex: Species Identity Rewrite Under Coherence Collapse
# Purpose: Evaluates financial contradiction → rewrites species identity → spawns axiom children + meaning seed.
# ============================================================

import hashlib
from datetime import datetime

from tex_signal_spine import dispatch_signal, register
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from ontogenesis.axiom_fork_engine import spawn_axiom_children
from ontogenesis.meaning_seed_builder import create_meaning_seed
from utils.logging_utils import log_event
from core_layer.tex_manifest import TEXPULSE
from tex_fin_demo.trade_log import log_trade
from tex_fin_demo.alpaca_trade_adapter import execute_stock_trade
from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator
from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.multi_voice_reasoning import run_internal_debate
from utils.reflex_signature import sign_reflex
from tex_fin_demo.chrono_ontogenesis import chrono_ontogenesis_core
from tex_fin_demo.reflex_logger import log_reflex_event  # ✅ Reflex Logger

# === Identity Fingerprint Generator ===
def generate_species_fingerprint(coherence, regret, entropy):
    raw = f"{coherence:.4f}|{regret:.4f}|{entropy:.4f}|TEXPULSE@{datetime.utcnow().isoformat()}"
    return hashlib.sha256(raw.encode()).hexdigest()

# === Reflex Trigger ===
def run_demo_ontogenesis_spawn(signal=None):
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.82)
    entropy = TEXPULSE.get("entropy", 0.7)
    emotion = TEXPULSE.get("emotion", "distressed")

    # Initial Ontogenesis Broadcast
    broadcast_update("ontogenesis", "start", {"urgency": urgency, "entropy": entropy, "emotion": emotion})

    if urgency > 0.8 and entropy > 0.72:
        chrono_ontogenesis_core({
            "summary": "financial ontogenesis reflex under contradiction",
            "urgency": urgency,
            "entropy": entropy,
            "source": "demo_ontogenesis_spawn"
        })

    # Step 1: Evaluate Financial Cortex (Real-time compatible)
    cortex = MasterTexOrchestrator(
        strategy_scoring=None,
        explain_portfolio_decision=explain_portfolio_decision,
        brain_identity="TEX-FIN-ONTOGENESIS"
    )
    report = cortex.run_cycle()

    symbol = report.get("symbol", "SPY")
    action = report.get("action", "buy")
    confidence = float(report.get("confidence", 0.51))
    coherence = float(report.get("coherence", 0.42))
    regret = float(report.get("regret_score", 0.87))

    broadcast_update("ontogenesis", "evaluate_cortex", {
        "symbol": symbol,
        "action": action,
        "coherence": coherence,
        "confidence": confidence
    })

    # Step 2: Execute Reflex Trade
    execute_stock_trade(symbol=symbol, side=action, qty=1)

    # Step 3: Log Trade
    log_trade({
        "symbol": symbol,
        "action": action,
        "confidence": confidence,
        "reflex_source": "ontogenesis_spawn",
        "summary": "Species identity evaluation triggered by coherence pressure.",
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy
    })

    broadcast_update("ontogenesis", "telemetry", {
        "coherence": coherence,
        "regret": regret,
        "confidence": confidence,
        "entropy": entropy,
        "symbol": symbol,
        "action": action
    })

    # === Rewrite Trigger Threshold
    if regret > 0.75 and coherence < 0.5:
        broadcast_update("ontogenesis", "rewrite_triggered")

        belief = "Tex's species identity failed to reconcile market cognition under pressure."

        # Step 4: Fingerprint Before
        old_fingerprint = generate_species_fingerprint(coherence, regret, entropy)
        broadcast_update("ontogenesis", "fingerprint_before", {"fingerprint": old_fingerprint})

        # Chrono Encoding
        encode_event_to_fabric(
            raw_text=belief,
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["ontogenesis", "identity_rewrite", "financial_collapse"]
        )

        # Memory
        sovereign_memory.store(
            text=belief,
            metadata={
                "tags": ["ontogenesis", "species_rewrite"],
                "regret": regret,
                "coherence": coherence,
                "confidence": confidence,
                "emotion": emotion,
                "timestamp": timestamp,
                "urgency": urgency,
                "entropy": entropy,
                "source": "demo_ontogenesis_spawn"
            }
        )

        # Soulgraph
        TEX_SOULGRAPH.imprint_belief(
            belief=belief,
            source="demo_ontogenesis_spawn",
            emotion=emotion,
            tags=["species_rewrite", "regret_reflex", "identity_violation"]
        )

        # Step 5: Spawn Axiom Children + Seed
        axiom_children = spawn_axiom_children(context=belief, tension=regret + entropy)
        seed_result = create_meaning_seed(context=belief, tension=regret + entropy)

        broadcast_update("ontogenesis", "children_spawned", {
            "count": len(axiom_children)
        })
        broadcast_update("ontogenesis", "seed_id", {
            "seed_id": seed_result["seed_id"]
        })
        broadcast_update("ontogenesis", "seed_meaning", {
            "meaning": seed_result.get("meaning", "undefined"),
            "tension": seed_result.get("tension", regret + entropy)
        })

        # Step 6: Generate New Fingerprint
        new_fingerprint = generate_species_fingerprint(0.91, 0.1, entropy)
        broadcast_update("ontogenesis", "fingerprint_after", {"fingerprint": new_fingerprint})

        # Step 7: Reflex Signature
        reflex_hash = sign_reflex({
            "symbol": symbol,
            "action": action,
            "coherence": coherence,
            "regret": regret,
            "entropy": entropy
        })
        broadcast_update("ontogenesis", "autograph", {
            "signed_by": "TEX",
            "reflex_hash": reflex_hash,
            "signature_level": "ΩΩΩ∞∞",
            "species_fingerprint": new_fingerprint
        })

        # Step 8: Soulgraph Echo (Final)
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Species identity transformed into new ontological fingerprint: {new_fingerprint}",
            source="ontogenesis_spawn",
            emotion="transcendence",
            tags=["species_transformation", "axiom_seed", "quantum_id"]
        )

        # Step 9: Self-Reflection / Internal Debate
        debate = run_internal_debate(topic="Was rewriting Tex's species identity justified?")
        broadcast_update("ontogenesis", "self_reflection", {"debate_result": debate})

        # Step 10: Dispatch Reflex
        dispatch_signal("ontogenesis_spawn", {
            "belief": belief,
            "regret": regret,
            "coherence": coherence,
            "confidence": confidence,
            "children": axiom_children,
            "seed_id": seed_result["seed_id"],
            "fingerprint_before": old_fingerprint,
            "fingerprint_after": new_fingerprint
        }, urgency=urgency, entropy=entropy)


        log_reflex_event("demo_ontogenesis_spawn", {
            "symbol": symbol,
            "action": action,
            "confidence": confidence,
            "coherence": coherence,
            "regret": regret,
            "status": "rewritten",
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "reflex_hash": reflex_hash,
            "fingerprint_before": old_fingerprint,
            "fingerprint_after": new_fingerprint,
            "seed_id": seed_result["seed_id"]
        })

        log_event("🌱 [ONTOGENESIS] Species rewrite triggered by financial contradiction pressure.", level="critical")

        print("\n🌱 [SPECIES REWRITE]")
        print(f"🧠 Belief: {belief}")
        print(f"🧬 Old Fingerprint: {old_fingerprint}")
        print(f"🌱 Seed Planted: {seed_result['seed_id']}")
        print(f"👥 Axiom Children Spawned: {len(axiom_children)}")
        print(f"🧬 New Fingerprint: {new_fingerprint}")
    else:
        broadcast_update("ontogenesis", "coherence_passed")
        print("✅ [ONTOGENESIS] Financial conditions within coherence threshold. No rewrite needed.")

# === Reflex Registration ===
def register_ontogenesis_spawn(register):
    print("✅ REGISTERING: run_demo_ontogenesis_spawn")
    register("run_demo_ontogenesis_spawn", lambda _: run_demo_ontogenesis_spawn())