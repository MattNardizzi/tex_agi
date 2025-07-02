# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/codex_mutation_reflex.py
# Tier ΩΩΩ-State FinalX — Sovereign Codex Mutation Reflex Engine with Lineage Logging, Sandbox Evaluation, and Shadow Fork Simulation
# ============================================================

from datetime import datetime
import traceback

from core_layer.tex_manifest import TEXPULSE
from core_layer.tex_self_eval_matrix import integrity_score
from aei_layer.codex_mutation_logger import CodexMutationLogger, log_codex_mutation
from aei_layer.mutation_simulation_engine import simulate_mutation_outcome
from aei_layer.shadow_dream_spawner import spawn_shadow_dream
from sovereign_evolution.sovereign_codex_differ import diff_codex_logic
from sovereign_evolution.patch_governor import propose_patch
from sovereign_evolution.code_patch_logger import log_patch_proposal

# === Sovereign Mutation Reflex ===
def evaluate_codex_mutation():
    try:
        print("\n🧬 [MUTATION REFLEX] Evaluating cognitive drift...")

        # 1. Diff logic from prior codex state
        codex_diff = diff_codex_logic()
        if not codex_diff or codex_diff.get("original") == codex_diff.get("mutated"):
            print("[MUTATION REFLEX] ✅ No meaningful divergence.")
            return

        # 2. Gather sovereign metrics
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.8)
        emotion = TEXPULSE.get("emotional_state", "neutral")
        integrity = integrity_score()
        mutation_strength = round((1.0 - integrity) * urgency * coherence, 4)

        print(f"[MUTATION REFLEX] Drift strength: {mutation_strength:.4f}")
        print(f"[MUTATION REFLEX] Emotion={emotion}, Coherence={coherence}, Urgency={urgency}, Integrity={integrity}")

        # 3. Propose new codex patch
        patch = propose_patch(
            trigger="codex_mutation_reflex",
            context_diff=codex_diff,
            weight=mutation_strength,
            emotion=emotion
        )

        if patch:
            log_patch_proposal(patch)

            # 4. Forecast sandbox outcome
            sandbox_result = simulate_mutation_outcome(trigger_reason="sovereign_cognitive_drift")
            print(f"[MUTATION REFLEX] ⚙ Sandbox forecast: {sandbox_result}")

            if sandbox_result.get("confidence", 0.0) < 0.5:
                print("[MUTATION REFLEX] ⚠ Low-confidence forecast. Spawning shadow fork...")
                spawn_shadow_dream(cycle_id=codex_diff.get("cycle_id", 0))

            # 5. Lineage registration (Codex gene logging)
            CodexMutationLogger().register_gene(
                patch_meta={
                    "module_name": patch.get("target_file"),
                    "description": patch.get("description", "Codex update under drift"),
                    "proposed_by": patch.get("proposed_by", "reflex_core"),
                    "intent_alignment": patch.get("intent_alignment", "adaptive_correction")
                },
                outcome={
                    "timestamp": datetime.utcnow().isoformat(),
                    "decision": patch.get("decision", "pending"),
                    "diagnostics": sandbox_result.get("explanation", ""),
                    "score": sandbox_result.get("confidence", 0.0),
                    "cycle": codex_diff.get("cycle_id", None)
                }
            )

            # 6. Codex mutation insight log
            try:
                log_codex_mutation(
                    cycle=codex_diff.get("cycle_id", 0),
                    original=codex_diff.get("original", "[missing]"),
                    mutated=codex_diff.get("mutated", "[missing]"),
                    trigger={
                        "emotion": emotion,
                        "urgency": urgency,
                        "coherence": coherence,
                        "integrity": integrity,
                        "reason": "sovereign_cognitive_drift"
                    }
                )
                print(f"[MUTATION REFLEX] 📜 Codex mutation insight logged.")
            except Exception as log_err:
                print(f"[MUTATION REFLEX] ⚠ Failed to log mutation insight: {log_err}")

            print("[MUTATION REFLEX] ✅ Mutation registered and lineage recorded.")

    except Exception as e:
        print("[MUTATION REFLEX ERROR]", str(e))
        traceback.print_exc()