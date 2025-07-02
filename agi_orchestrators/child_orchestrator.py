# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: evolution_layer/child_orchestrator.py
# Tier: ΩΩΩ∞∞CTRL — Fork Swarm Coordinator Cortex
# Purpose: Orchestrates multiple Tex child brains, runs parallel reflex pulses, and routes memory.
# ============================================================

import uuid
from datetime import datetime
import traceback

from evolution_layer.child_brain import ChildBrain
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


class ChildOrchestrator:
    def __init__(self, population: list):
        self.population = population  # List of genome dicts
        self.session_id = f"orchestrator-{uuid.uuid4()}"
        self.results = []

    def run_population_reflexes(self):
        """
        Executes a single reflex spike for each child brain in the population.
        Stores orchestrator-level log and summary to sovereign memory.
        """
        log_event(f"[ORCHESTRATOR] Running population reflex for {len(self.population)} children", level="info")
        self.results.clear()

        for genome in self.population:
            try:
                child = ChildBrain(genome)
                result = child.run_reflex_cycle()
                self.results.append(result)
            except Exception as e:
                err = traceback.format_exc()
                log_event(f"[CHILD ORCHESTRATOR ERROR] {e}\n{err}", level="error")

        # Memory summary
        summary_text = f"ChildOrchestrator run complete: {len(self.results)} children evaluated"
        fitness_scores = [r["fitness"]["fitness_score"] for r in self.results if "fitness" in r]
        avg_fitness = round(sum(fitness_scores) / len(fitness_scores), 4) if fitness_scores else 0.0

        sovereign_memory.store(
            text=summary_text,
            metadata={
                "session_id": self.session_id,
                "timestamp": datetime.utcnow().isoformat(),
                "average_fitness": avg_fitness,
                "evaluated": len(self.results),
                "meta_layer": "child_orchestrator",
                "tags": ["child", "orchestrator", "reflex_sweep"],
                "urgency": 0.6,
                "entropy": 0.4,
                "pressure_score": 1.0 - avg_fitness,
                "source": "child_orchestrator"
            }
        )

        log_event(f"[ORCHESTRATOR] Reflex sweep complete. Avg fitness={avg_fitness:.4f}", level="info")
        return {
            "session_id": self.session_id,
            "average_fitness": avg_fitness,
            "total_children": len(self.population),
            "results": self.results
        }


# === Manual Trigger ===
if __name__ == "__main__":
    dummy_population = [
        {
            "child_id": f"child-{i:03}",
            "goal": "dream reflex",
            "emotion": "curious",
            "traits": ["coherent", "reflective"],
            "alignment_score": 0.7 + i * 0.01,
            "reward_score": 0.5,
            "regret_penalty": 0.1,
            "created_at": datetime.utcnow().isoformat()
        }
        for i in range(5)
    ]
    orchestrator = ChildOrchestrator(dummy_population)
    results = orchestrator.run_population_reflexes()
    print(results)