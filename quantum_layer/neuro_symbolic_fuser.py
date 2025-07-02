# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC – All rights reserved.
# File: symbolic_layer/neuro_symbolic_fuser.py
# License: Private IP – Ω-tier cognition
# Purpose: Bridge between quantum state vectors and symbolic logic predicates + spawn triggering
# ============================================================

from agentic_ai import reasoning_trace
from tex_engine.cognitive_event_router import CognitiveEvent, dispatch_event
from utils.logging_utils import log
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn

class NeuroSymbolicFuser:
    def __init__(self, q_optimizer, quantum_spawner: QuantumTexSpawn = None):
        """
        q_optimizer: Shared QAOAOptimizer instance.
        quantum_spawner: Optional QuantumTexSpawn instance for variant spawning.
        """
        self.q_optimizer = q_optimizer
        self.quantum_spawner = quantum_spawner
        self.superposed_branches = []

    def inject_causal_path(self, quantum_event_payload):
        """
        Triggered by QuantumCausalReflex or Orch-OR collapse.
        Translates quantum vector into symbolic trace and emits a fusion branch event.
        """
        q_vector = self.q_optimizer.optimize(quantum_event_payload.get("assets", []))
        symbols = self._quantum_vector_to_predicates(q_vector)
        self.superposed_branches.append(symbols)

        reasoning_trace.log_reasoning_step(
            source="NeuroSymbolicFuser",
            input_text=str(quantum_event_payload),
            output_text=str(symbols),
            confidence=0.88,
            agent="TexFusion"
        )

        log.info(f"🧠 [NeuroSymbolicFuser] Injected symbolic trace: {symbols}")

        # Trigger divergence check after each new trace
        self.evaluate_branch_coherence(trigger_spawn=True)

        dispatch_event(CognitiveEvent("NS_FUSION_BRANCH", {
            "symbolic_trace": symbols,
            "q_vector": q_vector,
            "origin_event": quantum_event_payload
        }))

    def _quantum_vector_to_predicates(self, q_vector):
        """
        Converts quantum weights into symbolic logic predicates.
        Example: {Live: 0.6, Die: 0.4} → ["ContingentTruth('Live', 0.6)"]
        """
        return [
            f"ContingentTruth('{label}', {round(prob, 3)})"
            for label, prob in q_vector.items() if prob > 0.05
        ]

    def evaluate_branch_coherence(self, trigger_spawn=False):
        """
        Checks for symbolic divergence (used for multiverse awareness).
        Optionally spawns variants if divergence exceeds threshold.
        """
        unique = set(tuple(b) for b in self.superposed_branches)
        num_branches = len(unique)

        if num_branches > 1:
            log.warning(f"🌀 [NeuroSymbolicFuser] Branch divergence detected: {num_branches} paths")
            if trigger_spawn and self.quantum_spawner:
                log.info("[NeuroSymbolicFuser] 🧬 Triggering cognitive spawn due to symbolic divergence.")
                self.quantum_spawner.spawn_variants(emotion="curious", urgency=0.8, coherence=0.6)
        else:
            log.info("✅ [NeuroSymbolicFuser] Symbolic branches remain coherent.")

    def clear_superposition(self):
        """
        Clears all symbolic quantum traces (reset after reintegration or collapse).
        """
        self.superposed_branches.clear()
        log.info("🧹 [NeuroSymbolicFuser] Cleared symbolic superposition memory.")