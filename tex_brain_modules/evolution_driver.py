# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/evolution_driver.py
# Purpose: Sovereign Cognition Lifecycle Controller — Tex AEI Evolution Godmode
# ============================================================

import json
import uuid
import time
import random
from datetime import datetime, timezone

from evolution_layer.sovereign_evolution_arena import SovereignEvolutionArena
from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix
from aei_layer.mutation_lineage_tracker import log_mutation_lineage
from agentic_ai.qdrant_vector_memory import store_vector_to_qdrant
from swarm_layer.federated_tex import push_insight
from core_layer.meta_coherence_loop import MetaCoherenceLoop
from core_layer.memory_engine import store_to_memory

# ✅ NEW: AEI modules
from aei_layer.mutation_result_predictor import MutationResultPredictor
from aei_layer.evolutionary_mission_sequencer import EvolutionaryMissionSequencer
from aei_layer.genome_archiver import GenomeArchiver
from aei_layer.mutation_mission_driver import MutationMissionDriver
from aei_layer.adaptive_pressure_mapper import map_mutation_pressure
from aei_layer.heritable_memory_transcriber import extract_heritable_traits

# Global Genome Drift Archive
DRIFT_HISTORY = []
CHAMPION_HISTORY = []
SEQUENCER = EvolutionaryMissionSequencer()
ARCHIVER = GenomeArchiver()
MUTATION_DRIVER = MutationMissionDriver()

# ============================================================
# LAYER 1: Sovereign Evolution Loop
# ============================================================
def run_sovereign_evolution_loop(cycle_number):
    print("\n🌌 [SOVEREIGN AEI] Beginning full evolution cycle...")
    arena = SovereignEvolutionArena(num_variants=7, max_cycles=3)
    survivors = arena.run_cycle()
    top = max(survivors, key=lambda x: x[1])
    CHAMPION_HISTORY.append(top)
    log_champion(top, cycle_number)
    analyze_drift(top[2])
    return top

# ============================================================
# LAYER 2: Genome Drift Analysis
# ============================================================
def analyze_drift(current_genome):
    if not DRIFT_HISTORY:
        DRIFT_HISTORY.append(current_genome)
        return

    last = DRIFT_HISTORY[-1]
    drift_score = sum(
        abs(current_genome[k] - last.get(k, 0))
        for k in current_genome
        if isinstance(current_genome[k], (int, float))
    )
    DRIFT_HISTORY.append(current_genome)

    if drift_score < 0.05:
        print("[🧬 LOW DRIFT] Injecting novelty into future generations...")
    elif drift_score > 0.3:
        print("[⚠️ HIGH DRIFT] Mutation regime unstable. Reinforcing core logic filters...")

# ============================================================
# LAYER 3: Meta-Reasoning Over Evolution
# ============================================================
def enforce_mutation_theory_of_mind(champion):
    loop = MetaCoherenceLoop()
    thought = f"Why did agent {champion[0]} outperform all others?"
    loop.log_thought(thought)
    contradiction = loop._is_contradictory(thought)
    if contradiction:
        print(f"[⛔ CONTRADICTION] Detected contradiction in evolution logic: {thought}")
    else:
        print(f"[✅ METACO] No contradiction in winner rationale: {thought}")

# ============================================================
# Memory + Mutation Injection
# ============================================================
def log_champion(champ, cycle):
    variant_id, score, genome = champ
    payload = {
        "champion_id": variant_id,
        "score": score,
        "genome": genome,
        "cycle": cycle,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tag": "SOEVL"
    }

    store_vector_to_qdrant(variant_id, score, metadata=payload)
    log_mutation_lineage(variant_id, payload)

    # ✅ Fixed: archive now passes all required args in correct order
    ARCHIVER.archive(
        variant_id=variant_id,
        genome=genome,
        score=score,
        cycle=cycle,
        hash_id=None,
        meta={"tag": "SOEVL", "source": "evolution_driver"}
    )

    with open("memory_archive/sovereign_champion.json", "w") as f:
        json.dump(payload, f)

    push_insight("tex", f"[🏆 SOVEREIGN CHAMPION] ID: {variant_id} | Score: {score:.4f}")

# ============================================================
# Unified Evolution Executor (Replaces old patch loop)
# ============================================================
def evaluate_thought_cycle(cycle_number, emotion, urgency, coherence, last_memory):
    total_similarity = 1.0  # ✅ ensures it's always defined
    champion = run_sovereign_evolution_loop(cycle_number)
    if not champion or len(champion) < 3:
        print("[⚠️ EVALUATION ERROR] Champion result malformed.")
        return {}, total_similarity, 0.0, None

    enforce_mutation_theory_of_mind(champion)

    # ✅ Predict future viability of champion genome
    predictor = MutationResultPredictor()
    predicted_success = predictor.predict(champion[2])
    print(f"[PREDICTOR] 🔮 Estimated mutation confidence: {predicted_success:.3f}")

    store_to_memory("predicted_mutation_scores", {
        "cycle": cycle_number,
        "champion_id": champion[0],
        "predicted_score": predicted_success,
        "actual_score": champion[1],
        "timestamp": datetime.utcnow().isoformat()
    })

    # ✅ Mission + Memory + Pressure fusion
    mission = SEQUENCER.propose_next_mission({
        "cycle": cycle_number,
        "emotion": emotion,
        "urgency": urgency,
        "coherence": coherence
    })

    heritable = extract_heritable_traits()
    pressure = map_mutation_pressure()
    MUTATION_DRIVER.inject_guidance(mission, heritable, pressure)

    total_similarity = 1.0

    return {
        "strategy": "sovereign_evolution_loop",
        "champion_id": champion[0],
        "genome": champion[2],
        "score": champion[1],
        "predicted_score": predicted_success,
        "mission_goal": mission.get("fused_goal", "none"),
        "cycle": cycle_number
    }, total_similarity, champion[1], champion

# ============================================================
# Optional: Reinforce Mutation Bias Heuristics
# ============================================================
def adjust_mutation_pressure(average_child_score):
    legacy_adjust(average_child_score)
    if average_child_score > 0.85:
        print("[💡 METAEVOLVE] Tex mutation bias will enter curiosity mode next cycle.")
    elif average_child_score < 0.2:
        print("[🔁 REINFORCE] Tex mutation bias tightening toward goal coherence.")