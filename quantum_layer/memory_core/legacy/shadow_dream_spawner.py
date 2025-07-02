# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/shadow_dream_spawner.py
# Tier ΩΩΩΩΩΩ — Reflexive Fork Generator + Mutation-Scored Cognitive Abstraction
# Purpose: Generates high-fidelity dream forks with full belief integration, entropy scoring, and mutation potential
# ============================================================

from quantum_layer.memory_core.quantum_fork_memory_manager import QuantumForkMemoryManager
from core_layer.tex_self_reflective_loop import TexSelfReflectiveLoop
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from agentic_ai.self_mutator import SelfMutator
from agentic_ai.belief_indexer import BeliefIndexer
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime
import random

fork_manager = QuantumForkMemoryManager()
belief_indexer = BeliefIndexer()

class ShadowDreamSpawner:
    def __init__(self):
        self.reflector = TexSelfReflectiveLoop()
        self.vectorizer = DreamVectorAbstraction()
        self.reflex_tag = "shadow_dream_spawner"

    def spawn(self, cycle_id: int):
        try:
            print(f"\n[SHADOWLAB] 🌌 Executing shadow fork cycle {cycle_id}...")

            threads = self.reflector.run_reflection()
            if not threads:
                print("[SHADOWLAB] ⚠ No threads available for dream fork.")
                return None

            dreams = self.vectorizer.encode_threads(threads)
            if not dreams:
                print("[SHADOWLAB] ⚠ No dream vectors produced.")
                return None

            selected = random.choice(dreams)
            emotion = selected.get("source_emotion", "neutral")
            coherence = selected.get("coherence", 0.5)
            urgency = TEXPULSE.get("urgency", 0.5)
            divergence_score = round((1.0 - coherence) * urgency, 4)

            fork_payload = fork_manager.spawn_fork(
                base_memory={
                    "id": selected.get("dream_id"),
                    "content": selected.get("raw_text"),
                    "goal": threads[0].get("thread_id", "unspecified"),
                    "emotion": emotion,
                    "urgency": urgency,
                    "vectors": selected
                },
                context_tags=["dream_fork", self.reflex_tag],
                simulate=True,
                forecast_offset=3
            )

            belief_indexer.imprint(
                belief=f"Shadow dream fork for '{fork_payload['goal']}' (divergence={fork_payload['divergence_score']})",
                source=self.reflex_tag,
                emotion=emotion,
                tags=["dream", "fork"]
            )

            if fork_payload["mutation_potential_score"] >= 0.65:
                print(f"[REINFORCE] ⚡ High mutation score: {fork_payload['mutation_potential_score']}. Triggering reflex reinforcement.")
                SelfMutator().trigger_mutation(reason="dream_mutation_candidate", payload=fork_payload)

            return fork_payload

        except Exception as e:
            print(f"[SHADOWLAB ERROR] ❌ {e}")
            return None

# === Direct callable alias for reflexes
def spawn_shadow_dream(cycle_id: int):
    return ShadowDreamSpawner().spawn(cycle_id)
