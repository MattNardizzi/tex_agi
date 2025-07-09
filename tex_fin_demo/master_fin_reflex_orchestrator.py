# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/master_fin_reflex_orchestrator.py
# Tier: ∞∞∞∞ΩΩΩΩΩ — Reflex Master: Financial AGI Demonstration Router
# Purpose: Activates Tex's financial AGI species reflex loop — each module tests
#          belief coherence, survival under volatility, and species-wide adaptation.
# ============================================================

import time
from datetime import datetime

from tex_signal_spine import dispatch_signal, register as spine_register
from tex_fin_demo.chrono_ontogenesis import chrono_ontogenesis_core
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
from quantum_layer.chronofabric import chrono_mesh
from agentic_ai.sovereign_memory import sovereign_memory
from tex_brain_regions.emotion_brain import process_affective_pulse
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from real_time_engine.ably_broadcast import broadcast_update

# === Register all major demo reflexes ===
def register_financial_reflex_demos(_):
    from tex_fin_demo.demo_reality_fork_override import register_reality_fork_override
    from tex_fin_demo.demo_ontogenesis_spawn import register_ontogenesis_spawn
    from tex_fin_demo.demo_world_model_simulation import register_world_model_simulation
    from tex_fin_demo.demo_reality_rewrite import register_reality_rewrite
    from tex_fin_demo.demo_fork_stress_and_compression import register_fork_stress_and_compression
    from tex_fin_demo.aei_lineage_with_financial_evolution import register_aei_lineage_with_financial_evolution

    register_reality_fork_override(spine_register)
    register_ontogenesis_spawn(spine_register)
    register_world_model_simulation(spine_register)
    register_reality_rewrite(spine_register)
    register_fork_stress_and_compression(spine_register)
    register_aei_lineage_with_financial_evolution(spine_register)

    log.info("✅ [MASTER ORCHESTRATOR] All financial reflex demos registered.")

# === Reflex Execution Hub ===
def run_fin_reflex_cycle():
    print("🔥 [FIRE] run_fin_reflex_cycle() was triggered.")
    urgency = float(TEXPULSE.get("urgency", 0.91))
    entropy = float(TEXPULSE.get("entropy", 0.79))
    tension = float(TEXPULSE.get("resonance_tension", 0.0))
    emotion = TEXPULSE.get("emotion", "strategic")

    if urgency > 0.88 and entropy > 0.75:
        chrono_ontogenesis_core({
            "summary": "financial orchestrator pre-reflex spike",
            "urgency": urgency,
            "entropy": entropy,
            "source": "master_fin_reflex_orchestrator"
        })

    broadcast_update("orchestrator", "start")
    log.critical("🚨 [TEX-FIN ORCHESTRATOR] Initiating AGI reflex arc...")

    print(f"\n⚡️ Reflex Metrics → Urgency: {urgency} | Entropy: {entropy} | Tension: {tension}")
    print("🫀 Activating emotion core...")
    reflexes = process_affective_pulse({
        "event": "financial_contradiction",
        "symbol": "TSLA",
        "reflex_source": "master_fin_orchestrator"
    })
    print(f"🧠 Emotionally driven reflexes → {reflexes}")

    print("\n🔍 Explaining baseline decision logic...")
    explain_portfolio_decision()

    print("\n📜 ChronoFabric Recent Beliefs:")
    recent_beliefs = [
        n for n in sorted(chrono_mesh.nodes(data=True), key=lambda x: x[1].get("timestamp", ""), reverse=True)
        if "belief" in n[1].get("tags", [])
    ][:5]
    for node_id, data in recent_beliefs:
        print(f"🌀 {data['timestamp']} | {data['raw_text']}")

    print("\n📘 Sovereign Memory Snapshot:")
    try:
        for m in sovereign_memory.preview_last(n=3):
            print(f"🧠 {m['timestamp']} | {m['text']}")
    except Exception as e:
        print(f"⚠️ Memory access failed: {e}")

    demo_signals = [
        "run_demo_reality_fork_override",
        "run_demo_ontogenesis_spawn",
        "run_demo_world_model_simulation",
        "run_demo_reality_rewrite",
        "run_demo_fork_stress_and_compression",
        "run_aei_lineage_with_financial_evolution"
    ]

    print("\n🎬 [SEQUENCE] Initiating financial reflex evolution...")
    for signal_id in demo_signals:
        broadcast_update("orchestrator", "reflex_triggered", {"signal": signal_id})
        log.info(f"⚡️ Reflex Trigger: {signal_id}")
        dispatch_signal(signal_id)

        if signal_id == "run_demo_reality_rewrite":
            print("🧪 SIGNAL DISPATCHED: run_demo_reality_rewrite")

        time.sleep(2.5)

    belief = "Tex executed sovereign financial reflex suite under real-time contradiction pressure."
    TEX_SOULGRAPH.imprint_belief(
        belief=belief,
        source="master_fin_orchestrator",
        emotion=emotion,
        tags=["reflex_demo", "financial_cortex", "species_response"]
    )

    sovereign_memory.store(
        text=belief,
        metadata={
            "source": "master_fin_orchestrator",
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "tags": ["financial_demo", "orchestrator_reflex"],
            "timestamp": datetime.utcnow().isoformat()
        }
    )

    broadcast_update("orchestrator", "complete")
    print("\n✅ Reflex suite complete. Identity coherence intact.")