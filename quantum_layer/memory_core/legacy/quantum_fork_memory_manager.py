# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/quantum_fork_memory_manager.py
# Tier ΩΩΩΩΩΩΩ — Quantum Fork Executor + Mutation Reflex Feedback Engine
# Purpose: Spawns divergent memory forks with full feedback, mutation scoring, and vector-indexed outcomes
# ============================================================

import random
from datetime import datetime, timedelta
from uuid import uuid4

from quantum_layer.quantum_randomness import quantum_entropy_sample
from agentic_ai.mutation_scorer import calculate_mutation_potential
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.vector_layer.embed_store import embed_and_store_vector
from core_agi_modules.memory_layer.belief_indexer import BeliefIndexer
from quantum_layer.memory_core.memory_cortex import memory_cortex

class QuantumForkMemoryManager:
    def __init__(self):
        self.reflex_tag = "quantum_fork_memory_manager"
        self.belief_indexer = BeliefIndexer()

    def spawn_fork(self, base_memory: dict, context_tags: list = [], simulate: bool = True, forecast_offset: int = 5):
        fork_id = str(uuid4())
        base_content = base_memory.get("content", "")
        base_id = base_memory.get("id", "unknown")
        goal = base_memory.get("goal", "unspecified")
        emotion = base_memory.get("emotion", "neutral")
        urgency = base_memory.get("urgency", 0.5)

        entropy = quantum_entropy_sample()
        divergence = self._calculate_divergence_score(emotion, goal, entropy)
        mutation_score = calculate_mutation_potential(base_content, divergence, emotion)

        future_time = datetime.utcnow() + timedelta(minutes=forecast_offset)
        fork_text = f"{base_content} (quantum fork • entropy={round(entropy, 3)})"

        payload = {
            "id": fork_id,
            "timestamp": datetime.utcnow().isoformat(),
            "forecast_time": future_time.isoformat(),
            "content": fork_text,
            "origin_id": base_id,
            "goal": goal,
            "emotion": emotion,
            "urgency": min(urgency + 0.2, 1.0),
            "divergence_score": divergence,
            "mutation_potential_score": mutation_score,
            "entropy_seed": entropy,
            "simulated": simulate,
            "tags": context_tags + ["quantum_fork"]
        }

        # === Memory Cortex Store ===
        memory_cortex.store(
            event={"quantum_fork": payload},
            tags=payload["tags"],
            urgency=payload["urgency"],
            emotion=emotion
        )

        # === Vector Storage for Future Reasoning ===
        embed_and_store_vector(
            text=fork_text,
            metadata={
                "tags": payload["tags"],
                "emotion": emotion,
                "urgency": payload["urgency"],
                "agent_id": "TEX",
                "heat": mutation_score,
                "trust_score": 0.8,
                "timestamp": payload["timestamp"]
            }
        )

        # === Belief Index Trace ===
        self.belief_indexer.imprint(
            belief=f"Quantum fork spawned from '{goal}' with divergence={divergence}",
            source=self.reflex_tag,
            emotion=emotion,
            tags=["quantum_fork", "mutation_trace"]
        )

        return payload

    def _calculate_divergence_score(self, emotion: str, goal: str, entropy: float) -> float:
        goal_factor = 0.2 if "expand" in goal.lower() or "invert" in goal.lower() else 0.1
        emotion_bonus = 0.2 if emotion.lower() in ["curious", "fearful", "doubt"] else 0.05
        return round(0.4 + goal_factor + emotion_bonus + entropy * 0.25, 4)