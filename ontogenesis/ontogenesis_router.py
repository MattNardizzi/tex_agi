# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: ontogenesis/ontogenesis_router.py
# Tier: ΩΩΩ∞∞πΣΣΣΣ∞R — Apex Ontogenesis & Mutation Reflex Stack
# Purpose: Routes mutation-class reflexes: paradox agents, axiom seeds, compiler shifts,
#          observer decoherence, and substrate mutation for recursive evolution.
# ============================================================

from datetime import datetime
from utils.logging_utils import log_event

# Base ontogenesis agents
from ontogenesis.axiom_fork_engine import spawn_axiom_children
from ontogenesis.meaning_seed_builder import create_meaning_seed
from ontogenesis.paradox_child_template import instantiate_paradox_child

# Apex-tier modules
from tex_hypercore.reflex_physics import mutate_substrate_field
from tex_hypercore.recursive_mutator_compiler import launch_onto_compiler
from tex_hypercore.reality_collapse_engine import resolve_symbolic_collapse


def handle_ontogenesis_spawn(signal: dict):
    """
    Reflex handler triggered by dispatch_signal("spawn_ontogenesis_child", {...})

    Modes:
        - 'paradox' → spawn paradox-resolution agent
        - 'seed' → generate meaning seed and symbolic trigger
        - 'axiom' → fork new axiomatic subgraph
        - 'substrate_mutator' → mutate underlying belief emergence logic
        - 'onto_compiler' → recursively evolve the mutation ruleset
        - 'observer_collapse' → select between entangled symbolic realities
    """
    try:
        payload = signal.get("payload", {})
        mode = payload.get("mode", "paradox")
        tension = float(payload.get("tension", 0.6))
        context = payload.get("context", "undefined")

        log_event(
            f"[ONTOGENESIS] Triggered spawn request | Mode: {mode} | Context: {context} | Tension: {tension}",
            level="info"
        )

        if mode == "seed":
            return create_meaning_seed(context=context, tension=tension)

        elif mode == "axiom":
            return spawn_axiom_children(context=context, tension=tension)

        elif mode == "paradox":
            return instantiate_paradox_child(context=context, tension=tension)

        elif mode == "substrate_mutator":
            return mutate_substrate_field(context=context, tension=tension)

        elif mode == "onto_compiler":
            return launch_onto_compiler(context=context, tension=tension)

        elif mode == "observer_collapse":
            return resolve_symbolic_collapse(context=context, tension=tension)

        else:
            return {
                "status": "error",
                "error": f"Unknown ontogenesis mode: {mode}"
            }

    except Exception as e:
        log_event(f"[ONTOGENESIS ERROR] {e}", level="error")
        return {"status": "error", "error": str(e)}