# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_ontogenesis_spawn.py
# Tier: ∞∞∞∞ΩΩΩΩΩ — Reflex: Species Identity Rewrite Under Coherence Collapse
# Purpose: If Tex’s financial cortex violates epistemic survivability, he rewrites species identity,
#          seeds new meaning, spawns axiom children, and logs quantum-anchored identity.
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

from real_time_engine.websocket_broadcast import broadcast_update

# === Utility: Identity Fingerprint Generator
def generate_species_fingerprint(coherence, regret, entropy):
    raw = f"{coherence:.4f}|{regret:.4f}|{entropy:.4f}|TEXPULSE@{datetime.utcnow().isoformat()}"
    return hashlib.sha256(raw.encode()).hexdigest()

# === Reflex Trigger ===
async def run_demo_ontogenesis_spawn():
    timestamp = datetime.utcnow().isoformat()
    urgency = TEXPULSE.get("urgency", 0.82)
    entropy = TEXPULSE.get("entropy", 0.7)
    emotion = TEXPULSE.get("emotion", "distressed")

    await broadcast_update("ontogenesis:start")

    # === Step 1: Run Financial Cortex
    cortex = MasterTexOrchestrator(
        strategy_scoring=None,
        explain_portfolio_decision=explain_portfolio_decision,
        brain_identity="TEX-FIN-ONTOGENESIS"
    )
    report = cortex.run_cycle()
    await broadcast_update("ontogenesis:evaluate_cortex")

    # === Step 2: Execute Reflex Trade
    symbol = report.get("symbol", "SPY")
    action = report.get("action", "buy")
    confidence = float(report.get("confidence", 0.51))
    coherence = float(report.get("coherence", 0.42))
    regret = float(report.get("regret_score", 0.87))

    execute_stock_trade(symbol=symbol, side=action, qty=1)

    # === Step 3: Log Trade
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

    await broadcast_update(f"ontogenesis:telemetry:coherence:{coherence}")
    await broadcast_update(f"ontogenesis:telemetry:regret:{regret}")
    await broadcast_update(f"ontogenesis:telemetry:confidence:{confidence}")
    await broadcast_update(f"ontogenesis:telemetry:entropy:{entropy}")

    # === Step 4: Trigger Ontogenesis if needed
    if regret > 0.75 and coherence < 0.5:
        await broadcast_update("ontogenesis:rewrite_triggered")

        belief = "Tex's species identity failed to reconcile market cognition under pressure."

        # === Identity Fingerprint Before
        old_fingerprint = generate_species_fingerprint(coherence, regret, entropy)
        await broadcast_update(f"ontogenesis:fingerprint_before:{old_fingerprint}")

        # === Chrono Encoding
        encode_event_to_fabric(
            raw_text=belief,
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["ontogenesis", "identity_rewrite", "financial_collapse"]
        )

        # === Sovereign Memory
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

        # === Belief Trace to Soulgraph
        TEX_SOULGRAPH.imprint_belief(
            belief=belief,
            source="demo_ontogenesis_spawn",
            emotion=emotion,
            tags=["species_rewrite", "regret_reflex", "identity_violation"]
        )

        # === Step 5: Spawn Species Children
        axiom_children = spawn_axiom_children(context=belief, tension=regret + entropy)
        seed_result = create_meaning_seed(context=belief, tension=regret + entropy)

        await broadcast_update(f"ontogenesis:children_spawned:{len(axiom_children)}")
        await broadcast_update(f"ontogenesis:seed_id:{seed_result['seed_id']}")

        # === Identity Fingerprint After
        new_fingerprint = generate_species_fingerprint(0.9, 0.1, entropy)
        await broadcast_update(f"ontogenesis:fingerprint_after:{new_fingerprint}")

        # === Dispatch Reflex
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

        # === Final Reflex Log
        log_event("🌱 [ONTOGENESIS] Species rewrite triggered by financial contradiction pressure.", level="critical")

        print("\n🌱 [SPECIES REWRITE]")
        print(f"🧠 Belief: {belief}")
        print(f"🧬 Old Fingerprint: {old_fingerprint}")
        print(f"🌱 Seed Planted: {seed_result['seed_id']}")
        print(f"👥 Axiom Children Spawned: {len(axiom_children)}")
        print(f"🔁 New Fingerprint: {new_fingerprint}")

    else:
        await broadcast_update("ontogenesis:coherence_passed")
        print("✅ [ONTOGENESIS] Financial conditions within coherence threshold. No rewrite needed.")

# === Register Reflex
def register_ontogenesis_spawn(register):
    register("run_demo_ontogenesis_spawn", lambda _: asyncio.run(run_demo_ontogenesis_spawn()))
    print("✅ Registered: run_demo_ontogenesis_spawn")