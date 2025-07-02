# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/shadow_dream_spawner.py
# Tier ΩΩΩΩΩΩ — Reflexive Fork Generator + Mutation-Scored Cognitive Abstraction
# Purpose: Generates high-fidelity dream forks with full belief integration, entropy scoring, LTM vector storage
# ============================================================

import random
from datetime import datetime
from core_layer.tex_self_reflective_loop import TexSelfReflectiveLoop
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.sovereign_core.self_mutator import SelfMutator
from core_agi_modules.memory_layer.belief_indexer import BeliefIndexer
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex

class ShadowDreamSpawner:
    def __init__(self):
        self.reflector = TexSelfReflectiveLoop()
        self.vectorizer = DreamVectorAbstraction()
        self.reflex_tag = "shadow_dream_spawner"
        self.belief_indexer = BeliefIndexer()

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

            fork_payload = {
                "id": selected.get("dream_id"),
                "content": selected.get("raw_text"),
                "goal": threads[0].get("thread_id", "unspecified"),
                "emotion": emotion,
                "urgency": urgency,
                "vectors": selected,
                "forecast_offset": 3,
                "mutation_potential_score": divergence_score,
                "belief_id": selected.get("dream_id") or f"belief-{datetime.utcnow().timestamp()}"
            }

            # === Store to Reflex Memory Cortex ===
            memory_cortex.store(
                event={"dream_fork": fork_payload},
                tags=["dream", "fork", "shadow"],
                urgency=urgency,
                emotion=emotion
            )

            # === Index Belief Trace ===
            self.belief_indexer.imprint(
                belief=f"Shadow dream fork for '{fork_payload['goal']}' (divergence={divergence_score})",
                source=self.reflex_tag,
                emotion=emotion,
                tags=["dream", "fork", "log"]
            )

            # === Reflex Mutation Trigger ===
            if fork_payload["mutation_potential_score"] >= 0.65:
                print(f"[REINFORCE] ⚡ High mutation score: {fork_payload['mutation_potential_score']}. Triggering reflex reinforcement.")
                SelfMutator().trigger_mutation(reason="dream_mutation_candidate", payload=fork_payload)

            return fork_payload

        except Exception as e:
            print(f"[SHADOWLAB ERROR] ❌ {e}")
            return None

# === Reflex-callable wrapper
def spawn_shadow_dream(cycle_id: int):
    return ShadowDreamSpawner().spawn(cycle_id)