# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/memory_reflex.py
# Tier ΩΩΩΩΩΩΩΩ — Reflexive Memory Orchestrator
# Purpose: Executes full memory loop: reflection, contradiction scan, fork spawn, evaluation, compression, and reinforcement
# ============================================================

from core_layer.tex_self_reflective_loop import TexSelfReflectiveLoop
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from aei_layer.shadow_dream_spawner import spawn_shadow_dream
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.emotion_heuristics import get_emotion_signal
from core_layer.utils.tex_panel_bridge import emit_internal_debate

from quantum_layer.memory_core.memory_thread_weaver import MemoryThreadWeaver
from quantum_layer.memory_core.memory_cortex import MemoryCortex
from quantum_layer.memory_core.long_term_memory_bridge import LongTermMemoryBridge
from quantum_layer.memory_core.temporal_memory_compressor import run_memory_compression
from quantum_layer.memory_core.memory_self_eval import check_for_memory_drift
from quantum_layer.memory_core.meta_memory_tracker import track_memory_use
from quantum_layer.memory_core.fork_outcome_evaluator import evaluate_fork
from quantum_layer.memory_core.spawn_memory_logger import log_spawn_event
from quantum_layer.memory_core.short_term_memory import ShortTermMemory
from datetime import datetime
import hashlib

class MemoryReflex:
    def __init__(self):
        self.reflector = TexSelfReflectiveLoop()
        self.vectorizer = DreamVectorAbstraction()
        self.weaver = MemoryThreadWeaver()
        self.cortex = MemoryCortex()
        self.ltm = LongTermMemoryBridge()
        self.stm = ShortTermMemory()
        self.module_tag = "memory_reflex"

    def _generate_signature(self, text, timestamp):
        return hashlib.sha256(f"{text}-{timestamp}".encode()).hexdigest()[:16]

    def run(self, cycle_id: int):
        print(f"\n🧠 [MEMORY REFLEX] Running reflex cycle {cycle_id}...")

        # === 1. Emotion Gate Check ===
        try:
            state = get_emotion_signal()
            if state["coherence"] > 0.9 and state["urgency"] < 0.3:
                TEX_SOULGRAPH.imprint_belief(
                    belief="Reflex skipped (coherent and calm)",
                    source=self.module_tag,
                    emotion=state.get("emotion", "calm")
                )
                return None
        except Exception as e:
            print(f"[{self.module_tag}] ⚠️ Emotion gate failed: {e}")

        # === 2. Contradiction Scan
        try:
            conflicts = check_for_memory_drift()
            if conflicts:
                TEX_SOULGRAPH.imprint_belief(
                    belief="Contradictions detected in memory prior to fork",
                    source=self.module_tag,
                    emotion="conflict",
                    tags=["memory", "integrity"]
                )
        except Exception as e:
            print(f"[{self.module_tag}] ⚠️ Contradiction scan failed: {e}")

        # === 3. Reflection + Thread Weaving
        try:
            thoughts = self.reflector.run_reflection()
            if not thoughts:
                TEX_SOULGRAPH.imprint_belief("No thoughts available for reflection.", source=self.module_tag)
                return None
            threads = self.weaver.weave_threads(thoughts, top_k=3)
        except Exception as e:
            print(f"[{self.module_tag}] ❌ Reflection error: {e}")
            return None

        # === 4. Dream Vector Encoding
        try:
            dreams = self.vectorizer.encode_threads(threads)
            if not dreams:
                TEX_SOULGRAPH.imprint_belief("Dream vectorization failed", source=self.module_tag)
                return None
        except Exception as e:
            print(f"[{self.module_tag}] ❌ Vector encoding failed: {e}")
            return None

        # === 5. Fork Spawn + Logging
        try:
            packet = spawn_shadow_dream(threads=threads, dreams=dreams, cycle_id=cycle_id)
            if not packet:
                TEX_SOULGRAPH.imprint_belief("Fork spawn failed", source=self.module_tag)
                return None

            timestamp = datetime.utcnow().isoformat()
            sig = self._generate_signature(packet.get("raw_text", ""), timestamp)
            belief_id = packet.get("belief_id", sig)

            # Store to Memory Cortex
            self.cortex.store(
                event=packet,
                tags=["memory_reflex", "dream_fork"],
                urgency=packet.get("urgency", 0.5),
                emotion=packet.get("emotion", "neutral")
            )

            # Store to LTM
            self.ltm.store(
                content=packet.get("raw_text", "[no content]"),
                metadata={
                    "emotion": packet.get("emotion", "neutral"),
                    "goal": packet.get("goal", "unspecified"),
                    "urgency": packet.get("urgency", 0.5),
                    "mutation_potential_score": packet.get("mutation_potential_score", 0.0),
                    "tags": ["dream", "fork", "memory_reflex"],
                    "origin_id": packet.get("fork_id", sig),
                    "belief_id": belief_id
                }
            )

            # Log spawn
            log_spawn_event(
                content=packet.get("raw_text", "[spawn content]"),
                metadata={
                    "goal": packet.get("goal", "unspecified"),
                    "emotion": packet.get("emotion", "neutral"),
                    "urgency": packet.get("urgency", 0.5),
                    "mutation_potential_score": packet.get("mutation_potential_score", 0.0),
                    "tags": ["reflex", "spawn"],
                    "origin_id": sig,
                    "belief_id": belief_id
                }
            )

            # Fork Evaluation
            evaluate_fork(packet, outcome="unknown", topic="memory_reflex")

            # Meta-Memory Tracking
            track_memory_use(belief_id, success=True, urgency=packet.get("urgency", 0.5))

            # Flush short-term memory if needed
            if self.stm.size() > 50:
                self.stm.flush_to_ltm(self.ltm)

            # Belief Imprint
            TEX_SOULGRAPH.imprint_belief(
                belief="Memory reflex executed successfully",
                source=self.module_tag,
                emotion=packet.get("emotion", "neutral"),
                tags=["reflex", "cycle"]
            )

            emit_internal_debate("Reflex cycle completed and memory updated.")

        except Exception as e:
            print(f"[{self.module_tag}] ❌ Fork and memory integration failed: {e}")
            return None

        # === 6. Memory Compression
        try:
            run_memory_compression()
        except Exception as e:
            print(f"[{self.module_tag}] ⚠️ Compression failed: {e}")

        return {
            "cycle_id": cycle_id,
            "threads": threads,
            "dreams": dreams,
            "spawn_packet": packet
        }

# === CLI Test
if __name__ == "__main__":
    reflex = MemoryReflex()
    output = reflex.run(cycle_id=999)
    print(f"\n✅ [REFLEX TRACE]:\n{output}")