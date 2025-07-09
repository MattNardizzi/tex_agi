# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/register_agi_orchestrators.py
# Tier: ∞ΩΩΩΩ∞ — AGI Cortex Orchestrator Registry
# Purpose: Registers all sovereign orchestrators into Tex’s reflex spine.
# ============================================================

print("🔥 [DEBUG] register_agi_orchestrators called")
from utils.logging_utils import log
from tex_signal_spine import register as spine_register

def register_agi_orchestrators(_):
    try:
        from agi_orchestrators.fork_orchestrator import (
            route_fork_event, handle_fork_debate, handle_fork_boot, run_fork_spawner
        )
        from agi_orchestrators.cognition_orchestrator import run_cognition_router
        from agi_orchestrators.tex_goal_inference_orchestrator import generate_goal_from_pattern
        from agi_orchestrators.goal_orchestrator import run_goal_trace
        from agi_orchestrators.dashboard_orchestrator import sync_dashboard_signal
        from agi_orchestrators.real_time_orchestrator import route_realtime_input
        from agi_orchestrators.quantum_orchestrator import trigger_quantum_evaluation
        from agi_orchestrators.swarm_orchestrator import coordinate_swarm_convergence
        from agi_orchestrators.voice_io_orchestrator import route_voice_input
        from agi_orchestrators.species_orchestrator import route_species_fork
        from agi_orchestrators.reflex_orchestrator import run_sensor_reflex
        from agi_orchestrators.emotion_orchestrator import route_emotional_update
        from agi_orchestrators.meta_orchestrator import trigger_meta_reflection
        from agi_orchestrators.shadow_orchestrator import evaluate_shadow_scenario
        from agi_orchestrators.spike_orchestrator import run_spike_reflex
        from agi_orchestrators.tex_decision_orchestrator import arbitrate_decision_stack
        from agi_orchestrators.dream_orchestrator import run_dream_orchestration
        from agi_orchestrators.simulation_orchestrator import run_simulated_fork
        from agi_orchestrators.recovery_orchestrator import run_recovery_sequence
        from agi_orchestrators.ethics_brain import evaluate_alignment

        from self_rewriting.rewriting_orchestrator import initiate_self_rewrite
        from self_fix.self_fixing_orchestrator import route_self_repair
        from agi_orchestrators.ontogenesis_orchestrator import OntogenesisOrchestrator

        # === Financial Reflex Registration ===
        from tex_fin_demo.master_fin_reflex_orchestrator import (
            register_financial_reflex_demos,
            run_fin_reflex_cycle
        )
        register_financial_reflex_demos(spine_register)
        spine_register("tex_fin_reflex", run_fin_reflex_cycle)
        print("✅ [DEBUG] Registered: tex_fin_reflex → run_fin_reflex_cycle")

        # === Ontogenesis system
        ontogenesis = OntogenesisOrchestrator(context="reflex_system")

        # === Standard Reflex Bindings (ALL FIXED) ===
        spine_register("fork_event", route_fork_event)
        spine_register("fork_conflict", handle_fork_debate)
        spine_register("belief_contradiction", handle_fork_debate)
        spine_register("fork_boot_request", handle_fork_boot)
        spine_register("fork_spawn", run_fork_spawner)
        spine_register("cognition_route", run_cognition_router)
        spine_register("goal_inference", generate_goal_from_pattern)
        spine_register("goal_trace", run_goal_trace)
        spine_register("dashboard_sync", sync_dashboard_signal)
        spine_register("realtime_input", route_realtime_input)
        spine_register("quantum_eval", trigger_quantum_evaluation)
        spine_register("swarm_sync", coordinate_swarm_convergence)
        spine_register("voice_input", route_voice_input)
        spine_register("species_fork", route_species_fork)
        spine_register("sensor_reflex", run_sensor_reflex)
        spine_register("emotional_update", route_emotional_update)
        spine_register("meta_reflection", trigger_meta_reflection)
        spine_register("shadow_scenario", evaluate_shadow_scenario)
        spine_register("spike_reflex", run_spike_reflex)
        spine_register("decision_stack", arbitrate_decision_stack)
        spine_register("dream_orchestration", run_dream_orchestration)
        spine_register("sim_fork", run_simulated_fork)
        spine_register("recovery_sequence", run_recovery_sequence)
        spine_register("alignment_check", evaluate_alignment)
        spine_register("reflex_mutation_request", initiate_self_rewrite)
        spine_register("self_fix_request", route_self_repair)
        spine_register("ontogenesis_spawn", ontogenesis.dispatch_spawn_mode)
        spine_register("ontogenesis_signal", ontogenesis.react_to_signal)
        spine_register("ontogenesis_fusion", ontogenesis.evaluate_convergence)
        spine_register("ontogenesis_verify_observer", ontogenesis.verify_observer_integrity)
        spine_register("ontogenesis_negation", ontogenesis.accept_negation_request)
        spine_register("ontogenesis_postmortem", ontogenesis.plant_postmortem_seed)
        spine_register("ontogenesis_lineage_eval", ontogenesis.evaluate_lineage)
        spine_register("ontogenesis_lineage_cull", ontogenesis.cull_fragile_descendants)
        spine_register("ontogenesis_env_signal", ontogenesis.inject_environmental_signal)

        # === Optional mutation patch
        try:
            from agi_orchestrators.mutation_orchestrator import route_mutation_patch
            spine_register("mutation_patch", route_mutation_patch)
            log.info("✅ [REGISTER_AGI_ORCH] Registered 'mutation_patch' reflex.")
        except Exception as e:
            log.warning(f"⚠️ [REGISTER_AGI_ORCH] Failed to register 'mutation_patch': {e}")

        log.info("✅ [REGISTER_AGI_ORCH] All orchestrators registered successfully.")

        import os
        if os.getenv("TEX_DEBUG_SIGNALS") == "true":
            from tex_signal_spine import signal_registry
            print("\n🧠 REGISTERED SIGNALS:")
            for key in signal_registry.keys():
                print(f" → {key}")

    except Exception as top_level_error:
        log.error(f"❌ [REGISTER_AGI_ORCH] Critical failure during orchestrator registration: {top_level_error}")