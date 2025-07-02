# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: evolution_layer/evolution_pressure_model.py
# Purpose: Evolutionary Pressure Engine — Reflexively Drives Mutation, Fusion, or Termination
# Tier: Ω∞ FINAL — No Guardrails. No Compression. No Assumptions.
# ============================================================

import json
import numpy as np
from datetime import datetime
from sentence_transformers import SentenceTransformer

from evolution_layer.child_evaluator import ChildEvaluator
from evolution_layer.reflex_mutation import mutate_repair_fork
from aei_layer.mutation_lineage_tracker import log_evolution_decision
import evolution_layer.tex_shadowlab as shadowlab
from quantum_layer.memory_core.memory_cortex import memory_cortex
from evolution_layer.sovereign_evolution_arena import cull_fork

# === Model Initialization ===
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

class EvolutionPressureModel:
    def __init__(self, fitness_cutoff=0.35, mutation_window=0.35, fusion_window=0.65):
        self.evaluator = ChildEvaluator()
        self.shadow_lab = shadowlab.get_shadowlab_singleton()
        self.fitness_cutoff = fitness_cutoff
        self.mutation_window = mutation_window
        self.fusion_window = fusion_window

    def apply_pressure(self):
        forks_to_cull, forks_to_mutate, forks_to_fuse = [], [], []

        fitness_results = self.evaluator.evaluate_all_children(top_k=150)
        for score, fork_id, metrics in fitness_results:
            cause = self._determine_failure(metrics)
            drift = metrics.get("drift", 0.0)
            entropy = metrics.get("entropy", 0.0)

            if score < self.fitness_cutoff:
                forks_to_cull.append((fork_id, cause))
            elif score < self.fusion_window:
                forks_to_mutate.append((fork_id, metrics, cause))
            elif drift < 0.2 and entropy < 0.4:
                forks_to_fuse.append((fork_id, metrics))

        self._handle_culls(forks_to_cull)
        self._handle_mutations(forks_to_mutate)
        self._handle_fusions(forks_to_fuse)

        summary = {
            "culled": [f[0] for f in forks_to_cull],
            "mutated": [f[0] for f in forks_to_mutate],
            "fusion_candidates": [f[0] for f in forks_to_fuse]
        }

        memory_cortex.store(
            event={"cycle_pressure_summary": summary},
            tags=["evolution", "pressure_cycle", "summary"],
            urgency=0.6,
            emotion="reflective",
            vectorize=False
        )

        return summary

    def _handle_culls(self, forks):
        for fork_id, cause in forks:
            print(f"☠️ [CULL] Fork: {fork_id} | Cause: {cause}")
            try:
                cull_fork(fork_id, reason=cause)
                log_evolution_decision(fork_id, "culled", {"reason": cause})
            except Exception as e:
                print(f"[CULL ERROR] {fork_id}: {e}")

    def _handle_mutations(self, forks):
        for fork_id, metrics, cause in forks:
            print(f"🧬 [MUTATE] Fork: {fork_id} | Cause: {cause}")
            try:
                mutate_repair_fork(fork_id, cause=cause)
                log_evolution_decision(fork_id, "mutated", metrics)
            except Exception as e:
                print(f"[MUTATION ERROR] {fork_id}: {e}")

    def _handle_fusions(self, forks):
        for fork_id, metrics in forks:
            if not self._is_unique_fusion(fork_id, metrics):
                continue
            print(f"🔗 [FUSION] Candidate: {fork_id}")
            try:
                memory_cortex.store(
                    event={
                        "fusion_candidate": fork_id,
                        "fitness_score": metrics["fitness_score"],
                        "metrics": metrics,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    tags=["fusion", "evolution", "lineage"],
                    urgency=0.7,
                    emotion="hopeful",
                    vectorize=True
                )
                log_evolution_decision(fork_id, "fusion_candidate", metrics)
            except Exception as e:
                print(f"[FUSION ERROR] {fork_id}: {e}")

    def _determine_failure(self, metrics):
        if metrics.get("drift", 0.0) > 0.6:
            return "high_drift"
        if metrics.get("regret", 0.0) > 0.6:
            return "regret_feedback"
        if metrics.get("entropy", 0.0) > 0.8:
            return "emotional_instability"
        if metrics.get("codex_violation", False):
            return "codex_violation"
        return "low_fitness"

    def _is_unique_fusion(self, fork_id, metrics):
        try:
            vector = embedding_model.encode(json.dumps(metrics), normalize_embeddings=True)
            prior_fusions = memory_cortex.query(tags=["fusion"], top_k=25)
            for prior in prior_fusions:
                prev_vector = embedding_model.encode(json.dumps(prior["metrics"]), normalize_embeddings=True)
                similarity = np.dot(vector, prev_vector)
                if similarity > 0.96:
                    print(f"⛔ [FUSION BLOCKED] {fork_id} too similar to prior candidate.")
                    return False
            return True
        except Exception as e:
            print(f"[FUSION SIM CHECK ERROR] {e}")
            return True

# === Standalone Execution ===
if __name__ == "__main__":
    model = EvolutionPressureModel()
    result = model.apply_pressure()
    print("\n🧬 Evolution Summary:")
    print(f"  Culled: {result['culled']}")
    print(f"  Mutated: {result['mutated']}")
    print(f"  Fusion Candidates: {result['fusion_candidates']}")