# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: ontogenesis/ontogenesis_router.py
# Tier: ΩΩΩ∞∞πΣΣΣ — Ontogenesis Reflex Entrypoint
# Purpose: Routes reflex spikes that trigger epistemological or paradox-resolving agent generation.
# ============================================================

from datetime import datetime
from utils.logging_utils import log_event
from ontogenesis.axiom_fork_engine import spawn_axiom_children
from ontogenesis.meaning_seed_builder import create_meaning_seed
from ontogenesis.paradox_child_template import instantiate_paradox_child


def handle_ontogenesis_spawn(signal: dict):
    """
    Reflex handler triggered by dispatch_signal("spawn_ontogenesis_child", {...})
    Modes: 'paradox', 'seed', 'axiom'
    """
    try:
        payload = signal.get("payload", {})
        mode = payload.get("mode", "paradox")
        tension = float(payload.get("tension", 0.6))
        context = payload.get("context", "undefined")

        log_event(f"[ONTOGENESIS] Triggered spawn request | Mode: {mode} | Context: {context} | Tension: {tension}", level="info")

        if mode == "seed":
            return create_meaning_seed(context=context, tension=tension)
        elif mode == "axiom":
            return spawn_axiom_children(context=context, tension=tension)
        elif mode == "paradox":
            return instantiate_paradox_child(context=context, tension=tension)
        else:
            return {"status": "error", "error": f"Unknown ontogenesis mode: {mode}"}

    except Exception as e:
        log_event(f"[ONTOGENESIS ERROR] {e}", level="error")
        return {"status": "error", "error": str(e)}    "mode": "paradox", 
    "tension": 0.92,
    "context": "identity_loop_clash"
