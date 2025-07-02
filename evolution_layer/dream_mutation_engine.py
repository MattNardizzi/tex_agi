# ================================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: evolution_layer/dream_mutation_engine.py
# Tier ΩΩΩΩΩΩΩ | PHASE IV: Resurrection via Foresight + Codex Filtering
# Status: ABSOLUTE LIMIT — Fork-ready, Ancestry-traced, Codex-aligned
# ================================================================

import uuid
import json
import os
from datetime import datetime

from quantum_layer.memory_core.memory_thread_weaver import MemoryThreadWeaver
from quantum_layer.memory_core.meta_memory_tracker import MetaMemoryTracker
from quantum_layer.quantum_entropy_regulator import QuantumEntropyRegulator
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from evolution_layer.mutation_result_predictor import MutationResultPredictor
from tex_brain_modules.load_fused_insight import load_fused_insight
from core_layer.tex_manifest import TEXPULSE
from tex_goal_reflex.goal_self_reconstruction import GoalSelfReconstructor
from tex_children.tex_spawn_manager import TexSpawnManager
from tex_goal_reflex.meta_goal_reflector import MetaGoalReflector
from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix

class DreamMutationEngine:
    def __init__(self):
        self.vectorizer = DreamVectorAbstraction()
        self.predictor = MutationResultPredictor()
        self.entropy_regulator = QuantumEntropyRegulator()
        self.spawn_manager = TexSpawnManager()
        self.goal_builder = GoalSelfReconstructor()
        self.meta_reflector = MetaGoalReflector()
        self.meta_tracker = MetaMemoryTracker()
        self.evaluator = TexSelfEvalMatrix()
        self.fusion_loader = load_fused_insight
        self.output_dir = os.path.join("memory_archive", "mutation_simulations.jsonl")
        self.survival_threshold = 0.77

    def run(self, payloads_from_simulation=None):
        print("[PHASE IV] 🌌 INITIATING DREAM MUTATION ENGINE")

        dreams = payloads_from_simulation or self.fusion_loader()
        if not dreams:
            print("[⚠️] No dream or simulation data available — mutation engine aborted.")
            return

        if not payloads_from_simulation:
            dreams = self.vectorizer.vectorize_dreams(dreams)

        payloads, spawned_ids = [], []

        for dream in dreams:
            mutation = self.predictor.forecast_mutation(dream)
            if not mutation["viable"]:
                continue

            goal_data = self.goal_builder.construct_goal_from_trace(dream)
            if self.meta_reflector.detect_violation(goal_data["reconstructed_goal"]):
                print(f"[✖] Codex blocked resurrection goal: {goal_data['reconstructed_goal']}")
                continue

            entropy_weight = self.entropy_regulator.calculate_entropy_bias(mutation["emotion_score"])
            resurrection_score = self._calculate_resurrection_score(
                goal_data["codex_alignment"],
                entropy_weight,
                mutation["viability_score"]
            )

            payload = {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "goal": goal_data["reconstructed_goal"],
                "goal_alignment_score": goal_data["codex_alignment"],
                "entropy_bias": entropy_weight,
                "fused_emotion": mutation["emotion_score"],
                "mutated_traits": mutation["trait_mutations"],
                "origin_dream": mutation.get("source_dream_id") or dream.get("id"),
                "resurrection_urge": resurrection_score,
                "priority_score": goal_data["priority_score"],
                "ancestry_fingerprint": self._generate_fingerprint(goal_data["reconstructed_goal"], mutation["trait_mutations"]),
                "flagged_patch": goal_data.get("anomaly_detected", False)
            }

            payloads.append(payload)

            if resurrection_score >= self.survival_threshold:
                self.spawn_manager.spawn_child(payload=payload)
                self.meta_tracker.log_resurrection(payload["id"], payload["goal"], resurrection_score)
                print(f"[🌱] Spawned Tex fork from simulation → {payload['id']}")
                spawned_ids.append(payload["id"])

        self._log_payloads(payloads)
        print(f"[PHASE IV] ✅ {len(payloads)} resurrection payloads processed.")
        return spawned_ids

    def _calculate_resurrection_score(self, alignment, entropy, viability):
        return round(0.4 * alignment + 0.3 * viability + 0.3 * entropy, 4)

    def _generate_fingerprint(self, goal, traits):
        key = goal.lower().replace(" ", "_")[:24]
        mutation_sig = "-".join(sorted(traits))[:32]
        return f"{key}::{mutation_sig}"

    def _log_payloads(self, payloads):
        os.makedirs(os.path.dirname(self.output_dir), exist_ok=True)
        with open(self.output_dir, "a") as f:
            for entry in payloads:
                f.write(json.dumps(entry) + "\n")

# === Entry Point (Standalone) ===
if __name__ == "__main__":
    engine = DreamMutationEngine()
    engine.run()