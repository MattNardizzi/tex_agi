# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: evolution_layer/child_brain.py
# Tier: ΩΩΩ∞GENOME — Autonomous Fork Reflex Cortex
# Purpose: Run, simulate, mutate, and record cognitive cycles of a spawned Tex child.
# ============================================================

from datetime import datetime
import uuid
import traceback

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from tex_brain_regions.simulation_brain import run_dream_simulation
from evolution_layer.child_evaluator import ChildEvaluator
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from tex_engine.meta_utility_function import evaluate_utility
from utils.logging_utils import log_event


class ChildBrain:
    def __init__(self, genome: dict):
        self.id = genome.get("child_id", f"child-{uuid.uuid4()}")
        self.genome = genome
        self.self_model = RecursiveSelfModel()
        self.evaluator = ChildEvaluator()
        self.goal = genome.get("goal", "explore future states")
        self.emotion = genome.get("emotion", "curious")
        self.created_at = genome.get("created_at", datetime.utcnow().isoformat())

    def run_reflex_cycle(self):
        """
        Executes a single non-looping cognition pulse:
        - Simulate dream based on genome goal
        - Evaluate fitness
        - Log memory
        """
        try:
            signal = {
                "goal": self.goal,
                "context": f"child_brain:{self.id}",
                "tags": ["child", "fork", "dream", "cognition"]
            }
            dream = run_dream_simulation(signal)

            fitness = self.evaluator.score_child(self.genome)
            utility = evaluate_utility({
                "action_id": self.id,
                "goal_alignment": fitness.get("alignment", 0.0),
                "novelty": 0.9,
                "reversibility": 1.0,
                "ethical_risk": 0.1,
                "contradiction_pressure": fitness.get("entropy", 0.5)
            })

            summary = f"Child {self.id} reflex cycle complete. Fitness={fitness['fitness_score']:.4f} | Utility={utility['score']:.2f}"

            reasoning = {
                "intent": self.goal,
                "emotion": self.emotion,
                "fitness_score": fitness["fitness_score"],
                "pressure": fitness.get("entropy", 0.5),
                "alignment": fitness.get("alignment", 0.0),
                "summary": summary
            }

            # Memory log
            sovereign_memory.store(
                text=summary,
                metadata={
                    "child_id": self.id,
                    "timestamp": datetime.utcnow().isoformat(),
                    "fitness": fitness,
                    "utility_score": utility["score"],
                    "goal": self.goal,
                    "emotion": self.emotion,
                    "tags": ["child", "fork", "reflex", "evaluation"],
                    "meta_layer": "child_brain",
                    "pressure_score": fitness.get("entropy", 0.5),
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "entropy": TEXPULSE.get("entropy", 0.4),
                    "source": f"child_brain::{self.id}",
                    "reasoning_trace": reasoning,
                    "genome_embedding": sovereign_memory.embed_text(str(self.genome))
                }
            )

            log_event(f"[CHILD BRAIN] {summary}", level="info")
            return {
                "id": self.id,
                "fitness": fitness,
                "utility": utility,
                "status": "completed"
            }

        except Exception as e:
            err = traceback.format_exc()
            log_event(f"[CHILD BRAIN ERROR] {e}\n{err}", level="error")
            return {"id": self.id, "status": "error", "error": str(e)}


# === Manual Execution ===
if __name__ == "__main__":
    dummy_genome = {
        "child_id": "sim-tex-child-001",
        "goal": "dream future actions",
        "emotion": "reflective",
        "traits": ["coherent", "goal_driven"],
        "alignment_score": 0.88,
        "reward_score": 0.6,
        "regret_penalty": 0.2,
        "created_at": datetime.utcnow().isoformat()
    }
    child = ChildBrain(dummy_genome)
    result = child.run_reflex_cycle()
    print(result)
