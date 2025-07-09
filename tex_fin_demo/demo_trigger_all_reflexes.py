# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/demo_trigger_all_reflexes.py
# Tier: ∞ΩΩΩΩ — Synchronous Reflex Panel Trigger
# Purpose: Fires each reflex panel via dispatch_signal with semantic Ably routing.
# ============================================================

from tex_signal_spine import dispatch_signal

def trigger_all_demo_reflexes():
    print("\n🔥 [TRIGGER_REFLEXES] Starting full panel reflex dispatch sequence...\n")

    dispatch_signal("run_demo_reality_fork_override", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_demo_reality_fork_override")

    dispatch_signal("run_demo_reality_rewrite", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_demo_reality_rewrite")

    dispatch_signal("run_demo_world_model_simulation", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_demo_world_model_simulation")

    dispatch_signal("run_demo_ontogenesis_spawn", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_demo_ontogenesis_spawn")

    dispatch_signal("run_demo_fork_stress_and_compression", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_demo_fork_stress_and_compression")

    dispatch_signal("run_aei_lineage_with_financial_evolution", { "source": "reflex_panel_demo" })
    print("✅ Triggered: run_aei_lineage_with_financial_evolution")

    print("\n✅ [TRIGGER_REFLEXES] All 6 panel reflexes dispatched.\n")