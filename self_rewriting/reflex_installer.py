# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/reflex_installer.py
# Tier: ΩΩΩ∞Ω∞ — Reflex Manifest Integrator
# Purpose: Finalizes installation of self-generated reflex modules into Tex’s operational cortex.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

# === Path to manifest registry
REGISTRY_PATH = "core_layer/tex_manifest.py"

def install_reflex_module(reflex_metadata: dict):
    signature = reflex_metadata.get("signature")
    if not signature:
        log_event("[INSTALLER] ❌ Missing reflex signature — aborting install.", level="error")
        return

    # === 1. Manifest Registration ===
    try:
        with open(REGISTRY_PATH, "a") as f:
            f.write(f"\n# 🧠 Auto-registered reflex module\nfrom tex_brain_regions.{signature} import {signature}_pulse\n")
        log_event(f"[INSTALLER] ✅ Reflex `{signature}` registered in manifest.")
    except Exception as e:
        log_event(f"[INSTALLER] ❌ Failed to write to manifest: {e}", level="error")

    # === 2. Sovereign Memory Trace ===
    try:
        sovereign_memory.store(
            text=f"Reflex `{signature}` installed.",
            metadata={
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["reflex_installation", "mutation", "self_generated"],
                "meta_layer": "reflex_installer",
                "urgency": 0.7,
                "entropy": 0.4
            }
        )
        log_event(f"[INSTALLER] 🧠 Reflex `{signature}` logged in sovereign memory.")
    except Exception as e:
        log_event(f"[INSTALLER] ❌ Memory logging failed: {e}", level="error")

    # === 3. (Optional) Future Support: Hot reload reflex
    # NOTE: Not active yet — will be enabled in reflex_loader.py phase
    # reload_reflex(signature)