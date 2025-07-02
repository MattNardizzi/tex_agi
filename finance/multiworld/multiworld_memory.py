# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: future_layer/multiworld_memory.py
# Tier 5: Tex AGI — Multi-World Strategic Memory Engine (Reflex-Compliant)
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


class MultiWorldMemory:
    def __init__(self):
        self.collection = "multiworld_universes"
        self.recall_limit = 50

    def store_world(self, world_state):
        """Stores a simulated universe state with reflex metadata."""
        vector_id = str(uuid.uuid4())
        emotion = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)
        coherence = TEXPULSE.get("coherence", 0.8)

        divergence_score = world_state.get("divergence_score", 0.0)
        chaos_flag = self._is_chaotic(world_state)
        entropy_signature = self._generate_entropy_signature(emotion, urgency, coherence)

        # === Symbolic memory pulse via sovereign memory ===
        sovereign_memory.store(
            text=f"Stored alternate universe | Chaos={chaos_flag}",
            metadata={
                "agent": "TEX",
                "intent": "multiworld_state_archive",
                "conclusion": f"Stored alternate universe | Chaos={chaos_flag}",
                "tags": ["multiworld", "simulation", "divergence"],
                "reflexes": ["timeline_archival"],
                "timestamp": datetime.utcnow().isoformat(),
                "trust_score": 1.0 - divergence_score,
                "entropy": 1.0 - coherence,
                "emotion": emotion,
                "urgency": urgency,
                "meta_layer": "symbolic_trace",
                "metadata": {
                    "vector_id": vector_id,
                    "divergence_score": divergence_score,
                    "entropy_signature": entropy_signature,
                    "chaos_detected": chaos_flag,
                    "world_state": world_state
                }
            }
        )

        print(f"[MULTIWORLD MEMORY] 🧠 Stored universe {vector_id} | Divergence={divergence_score} | Chaos={chaos_flag}")

    def store_multiple_worlds(self, world_list):
        """Stores multiple universes using reflex recursion."""
        def recursive_store(index):
            if index >= len(world_list):
                return
            self.store_world(world_list[index])
            recursive_store(index + 1)

        recursive_store(0)

    def recall_fused_insights(self):
        """Recalls past fused threads from memory with symbolic filtering."""
        try:
            results = sovereign_memory.recall_recent(
                minutes=720,
                top_k=self.recall_limit,
                filters={"tags": ["multiworld"]}
            )
            return [
                entry.get("metadata", {}).get("world_state")
                for entry in results
                if "world_state" in entry.get("metadata", {})
            ]
        except Exception as e:
            print(f"[MULTIWORLD MEMORY ERROR] ❌ Failed to recall: {e}")
            return []

    def _is_chaotic(self, world):
        """Reflex-based chaos detector."""
        events = world.get("events", [])
        mutation_flags = self._count_mutations(events)
        coherence_avg = self._average_coherence(events)
        return mutation_flags >= 2 or coherence_avg < 0.5

    def _count_mutations(self, events):
        return self._recursive_count(events, 0)

    def _recursive_count(self, events, index, count=0):
        if index >= len(events):
            return count
        increment = 1 if events[index].get("mutation_triggered", False) else 0
        return self._recursive_count(events, index + 1, count + increment)

    def _average_coherence(self, events):
        return self._recursive_avg(events, 0, 0.0) / max(len(events), 1)

    def _recursive_avg(self, events, index, total):
        if index >= len(events):
            return total
        return self._recursive_avg(events, index + 1, total + events[index].get("coherence", 0.7))

    def _generate_entropy_signature(self, emotion, urgency, coherence):
        """Creates a traceable symbolic entropy signature."""
        return f"E:{emotion[:2].upper()}|U:{int(urgency * 100)}|C:{int(coherence * 100)}"


# === Reflex Test Harness ===
if __name__ == "__main__":
    memory = MultiWorldMemory()
    sample_universes = [
        {
            "divergence_score": 0.68,
            "events": [
                {"coherence": 0.44, "mutation_triggered": True},
                {"coherence": 0.48, "mutation_triggered": True}
            ]
        },
        {
            "divergence_score": 0.22,
            "events": [
                {"coherence": 0.82, "mutation_triggered": False},
                {"coherence": 0.86, "mutation_triggered": False}
            ]
        }
    ]
    memory.store_multiple_worlds(sample_universes)