# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/swarm_sync.py
# Purpose: Full Tex Swarm Awareness Sync — Real Child Survival Memory
# ============================================================

from swarm_layer.swarm_awareness_sync import sync_with_swarm_feed
from evolution_layer.self_mutator import SelfMutator
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override  # ✅ Activated
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

mutator = SelfMutator()

def run_swarm_sync_cycle(spawned_variants):
    """Synchronise live offspring signals with the core awareness matrix.

    ▸ Pull the latest swarm summary from *sync_with_swarm_feed()*        
    ▸ Adjust global mutation-pressure according to average child score  
    ▸ Trigger sovereign override if swarm survival is weak or volatile
    ▸ Guard against malformed inputs (str vs dict) to prevent tracebacks
    """
    print("\n[🧬 SWARM AWARENESS] Syncing with full child survival states…")

    try:
        swarm_summary = sync_with_swarm_feed()

        # ── Guard: reject non-dict payloads ──────────────────────────
        if not isinstance(swarm_summary, dict):
            print(f"[SWARM SYNC ERROR] Malformed swarm summary — expected dict, got {type(swarm_summary).__name__}")
            return
        # ─────────────────────────────────────────────────────────────

        # ── Pull average score using the *current* schema ────────────
        average_score = swarm_summary.get("average_child_score")
        children_scores = swarm_summary.get("children_scores", [])

        # Back-compat: fallback to legacy list schema if necessary
        if average_score is None and children_scores:
            average_score = sum(children_scores) / len(children_scores)

        if average_score is None:
            print("[SWARM SYNC WARNING] No child scores retrieved — mutation unchanged.")
            return

        print(f"[SWARM SYNC] 👶 Raw child scores: {children_scores}")

        # ✅ Log swarm sync state to memory
        store_to_memory("swarm_sync_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "average_score": average_score,
            "raw_scores": children_scores,
            "variant_count": len(spawned_variants)
        })

        # ── Mutation-pressure heuristics ─────────────────────────────
        if average_score < -0.2:
            print("[⚠️ SURVIVAL WARNING] Offspring struggling — increasing mutation pressure…")
            mutator.mutation_bias += 0.1

        elif average_score > 0.6:
            print("[🌟 SURVIVAL THRIVING] Offspring thriving — reducing mutation pressure…")
            mutator.mutation_bias = max(mutator.mutation_bias - 0.05, 0.0)

        else:
            print(f"[🧬 SURVIVAL CHECK] Average child survival score: {average_score:.3f}")
        # ─────────────────────────────────────────────────────────────

        # ── Per-variant reconciliation (guarded) ─────────────────────
        for variant in spawned_variants:
            if not isinstance(variant, dict):
                continue  # Skip corrupted entries
            # 🔒 Future extension: lifespan sync, health regression, etc.
            pass
        # ─────────────────────────────────────────────────────────────

        # 🧠 Sovereign Cognition Override (debounced)
        if (average_score < 0.25 or average_score > 0.85) and not TEXPULSE.get("sovereign_override_triggered_this_cycle", False):
            TEXPULSE["sovereign_override_triggered_this_cycle"] = True
            trigger_sovereign_override(
                context="swarm_sync",
                foresight=average_score,
                regret=1.0 - average_score,
                coherence=average_score,
                force=False,
                metadata={
                    "swarm_scores": children_scores,
                    "variant_count": len(spawned_variants)
                }
            )

    except Exception as e:
        print(f"[SWARM SYNC ERROR] {e}")