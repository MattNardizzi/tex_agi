# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/reflex_panel_controller.py
# Tier: ΩΩΩΩΩΩΩ — Autonomous Reflex Selector
# Purpose: Tex decides which financial reflex to trigger based on internal state.
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from tex_fin_demo.demo_reality_rewrite import run_demo_reality_rewrite
from tex_fin_demo.demo_reality_fork import run_demo_reality_fork
from tex_fin_demo.demo_world_simulation import run_demo_world_simulation
from utils.logging_utils import log

async def trigger_best_reflex():
    urgency = float(TEXPULSE.get("urgency", 0.7))
    entropy = float(TEXPULSE.get("entropy", 0.5))
    contradiction = float(TEXPULSE.get("contradiction_pressure", 0.0))
    coherence = float(TEXPULSE.get("identity_coherence", 1.0))

    try:
        # === Reflex logic thresholds ===
        if contradiction > 0.85:
            log.info(f"⚡ Reflex Trigger: Contradiction={contradiction} → reality_rewrite")
            await run_demo_reality_rewrite()
        elif entropy > 0.75:
            log.info(f"⚡ Reflex Trigger: Entropy={entropy} → world_simulation")
            await run_demo_world_simulation()
        elif urgency > 0.88 or coherence < 0.4:
            log.info(f"⚡ Reflex Trigger: Urgency={urgency}, Coherence={coherence} → reality_fork")
            await run_demo_reality_fork()
        else:
            log.info("🔍 Reflex Trigger: No dominant pressure. No panel activated.")
    except Exception as e:
        log.warning(f"❌ trigger_best_reflex failed: {e}")