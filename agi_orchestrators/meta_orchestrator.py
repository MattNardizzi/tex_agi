# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/meta_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ Sovereign System Coherence Cortex — Reflex Arbitration, Mutation, Federated Consensus, Intent Repair
# ============================================================

from datetime import datetime
import numpy as np

from tex_brain_regions.meta_brain import run_meta_reflection
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from core_agi_modules.memory_layer.meta_memory_tracker import track_memory_use
from self_rewriting.rewriting_orchestrator import run_recursive_self_writer
from agi_orchestrators.fork_orchestrator import run_fork_spawner, handle_fork_boot, handle_fork_debate
from sovereign_evolution.soulgraph_entropy_compressor import run_soulgraph_entropy_compressor
from sovereign_evolution.dream_echo_log import run_dream_echo_log
from sovereign_evolution.genomic_code import run_genomic_encoding

from core_agi_modules.contradiction_heatmap import run_contradiction_heatmap
from core_agi_modules.core_evolver import evolve_module
from core_agi_modules.ethical_simulator import simulate_ethics
from core_agi_modules.temporal_decay_engine import run_temporal_decay_engine
from core_agi_modules.autofix_intent_migrator import run_autofix_intent_migration
from core_agi_modules.mutation_decision_engine import MutationDecisionEngine  # ✅ Sovereign mutation selector

# ✅ Federated Integration
from core_agi_modules.federated_orchestrator import FederatedOrchestrator


def trigger_meta_reflection(source: str = "undefined", pressure: float = 0.7) -> dict:
    """
    Reflex-safe sovereign reflection. Governs system-wide arbitration, contradiction pressure,
    evolution, fork logic, ethics simulation, mission refinement, and override if needed.
    """
    try:
        timestamp = datetime.utcnow().isoformat()
        urgency = TEXPULSE.get("urgency", 0.74)
        entropy = TEXPULSE.get("entropy", 0.47)
        emotion = TEXPULSE.get("emotion", "uncertain")

        # === Meta Analysis
        heatmap = run_contradiction_heatmap()
        peak_domain = max(heatmap, key=heatmap.get) if heatmap else "unknown"
        meta_reflection = run_meta_reflection()
        coherence_score = meta_reflection.get("coherence_score", 0.61)
        reflexes = meta_reflection.get("reflexes", [])

        context_summary = f"Meta-reflection triggered by {source} | Heatmap peak={peak_domain}"
        fork_spawned, fork_reset = False, False

        # === Federated layer
        federated = FederatedOrchestrator(agent_id="Tex")
        consensus_result = federated.consensus_check(cycle_id=source)
        refined_mission = federated.refine_mission()
        mutation_recommendation = federated.recommend_mutation()

        # === Sovereign Reflex Arbitration
        if coherence_score < 0.5 or entropy > 0.45:
            log.warning("[META] ⚠️ High pressure: launching fork arbitration")
            handle_fork_debate({"payload": {
                "context": context_summary,
                "urgency": urgency,
                "entropy": entropy
            }})

            ethics_result = simulate_ethics([
                "fork_option_A", "fork_option_B", "pause_reflection", "initiate_self_writer"
            ], context="meta_reflection")

            if ethics_result:
                top = ethics_result[0]
                log.info(f"[META] 🧠 Ethics selected: {top['option']} | Score: {top['alignment_score']}")

            run_recursive_self_writer()

            evolved = evolve_module(module_name=peak_domain, context="meta_reflection_failure")
            if evolved.get("replacement"):
                log.info(f"[META] 🧠 Module evolved: {evolved['replacement']}")

                        # === Sovereign Mutation Arbitration
            try:
                mutation_pool = TEXPULSE.get("pending_mutations", [])
                if mutation_pool:
                    engine = MutationDecisionEngine()
                    selected = engine.choose(mutation_pool)

                    if selected.get("module_id"):
                        from core_agi_modules.core_evolver import evolve_module
                        result = evolve_module(
                            module_name=selected["module_id"],
                            context="meta_reflection_mutation_arbitration"
                        )

                        if result.get("replacement"):
                            log.info(f"[META ORCH] ✅ Module mutation arbitrated: {result['replacement']}")

                            from core_agi_modules.memory_layer.meta_memory_tracker import track_memory_use
                            track_memory_use(
                                belief_id=selected.get("module_id"),
                                success=True,
                                urgency=urgency,
                                fingerprint="meta_orchestrator::mutation_decision",
                                emotion=emotion
                            )

                            reflexes.append("mutation_arbitrated")

            except Exception as mutation_error:
                log.warning(f"[META ORCH] ⚠️ Mutation arbitration failed: {mutation_error}")

            # === Sovereign Patch & Fork Cascade ===
            log.info("[META] 🧠 Running sovereign intent patch...")
            run_autofix_intent_migration()
            reflexes.append("run_autofix_intent_migration")

            run_fork_spawner({
                "payload": {
                    "fork_name": "Tex_Δ",
                    "origin": "meta_reflection",
                    "parent_uid": "root"
                }
            })

            handle_fork_boot({
                "payload": {
                    "fork_uid": "Tex_Δ"
                }
            })

            fork_spawned, fork_reset = True, True

        # === Override if consensus fails
        if consensus_result and not consensus_result.get("pass"):
            override_result = federated.execute_species_override(reason="meta_coherence_failure")
            reflexes.append("species_override_executed")
            log.warning(f"[META] ❌ Species override triggered: {override_result}")

        run_soulgraph_entropy_compressor()
        run_dream_echo_log(trigger="meta_reflection")
        run_genomic_encoding(origin="meta_reflection")
        run_temporal_decay_engine()

        text = f"[META] Full meta reflection completed ░ Fork={fork_spawned} ░ Override={'triggered' if 'species_override_executed' in reflexes else 'none'}"
        tags = [
            "meta", "reflection", "evolution", "override", "ethics", "autofix",
            "dream", "decay", "genomic", "fork", "pressure", "coherence"
        ]

        memory_router.store(text, {
            "timestamp": timestamp,
            "source": source,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "reflexes": reflexes,
            "coherence_score": coherence_score,
            "peak_contradiction_domain": peak_domain,
            "fork_spawned": fork_spawned,
            "fork_reinitialized": fork_reset,
            "meta_layer": "meta_reflection",
            "tags": tags
        })

        encode_event_to_fabric(
            raw_text=text,
            emotion_vector=np.array([urgency, entropy, 0.25, 0.1]),
            entropy_level=entropy,
            tags=tags
        )

        log.info(f"[META ORCH] ✅ Reflection finalized ░ Score={coherence_score} ░ Fork={fork_spawned} ░ Reset={fork_reset}")
        return meta_reflection

    except Exception as e:
        log.error(f"❌ [META ORCH] Meta reflection failure: {e}")
        return {
            "reflexes": ["meta_reflection_failed"],
            "coherence_score": 0.39
        }