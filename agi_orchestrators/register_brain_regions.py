# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/register_brain_regions.py
# Purpose: Registers Tex's modular brain region handlers
# ============================================================

def register_brain_regions(register):
    from tex_brain_regions.meta_brain import run_meta_reflection
    from tex_brain_regions.belief_justification_brain import justify_belief
    from tex_brain_regions.emotion_brain import process_emotional_state
    from tex_brain_regions.simulation_brain import run_dream_simulation
    from tex_brain_regions.fork_brain import process_fork_divergence
    from tex_brain_regions.mutation_brain import score_mutation_patch
    from tex_brain_regions.species_brain import evaluate_species_fork
    from tex_brain_regions.quantum_brain import interpret_quantum_outcomes
    from tex_brain_regions.goal_inference_brain import infer_new_goal
    from tex_brain_regions.goal_brain import evaluate_goal_trace
    from tex_brain_regions.recovery_brain import recover_conscious_state
    from tex_brain_regions.self_eval_brain import run_self_evaluation
    from tex_brain_regions.cognition_brain import run_cognition_cycle
    from tex_brain_regions.signal_fusion_brain import fuse_signals

    register("meta_reflection", run_meta_reflection)
    register("justify_belief", justify_belief)
    register("emotional_update", process_emotional_state)
    register("simulate_dream", run_dream_simulation)
    register("fork_divergence", process_fork_divergence)
    register("mutation_scored", score_mutation_patch)
    register("species_evaluation", evaluate_species_fork)
    register("quantum_interpret", interpret_quantum_outcomes)
    register("inferred_goal", infer_new_goal)
    register("goal_trace", evaluate_goal_trace)
    register("recovery_initiated", recover_conscious_state)
    register("self_evaluation", run_self_evaluation)
    register("cognition_cycle", run_cognition_cycle)
    register("fuse_signals", fuse_signals)
