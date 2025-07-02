# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC – All rights reserved.
# File: symbolic_layer/neuro_symbolic_fuser.py
# License: Private IP – Ω-tier cognition
# Purpose: Bridge between quantum state vectors and symbolic logic predicates
# ============================================================

from quantum_layer.qaoa_optimizer import QAOAOptimizer
from agentic_ai import reasoning_trace
from tex_engine.cognitive_event_router import CognitiveEvent, dispatch_event
from utils.logging_utils import log

class NeuroSymbolicFuser:
    def __init__(self):
        self.q_optimizer = QAOAOptimizer()
        self.superposed_branches = []

    def inject_causal_path(self, quantum_event_payload):
        """
        Triggered by QuantumCausalReflex or Orch-OR collapse.
        Builds a symbolic trace from quantum signal metadata and emits a new cognitive event.
        """
        q_vector = self.q_optimizer.solve_context_vector(quantum_event_payload)
        symbols = self._quantum_vector_to_predicates(q_vector)
        self.superposed_branches.append(symbols)

        # Log to reasoning trace memory
        reasoning_trace.log_reasoning_step(
            source="NeuroSymbolicFuser",
            input_text=str(quantum_event_payload),
            output_text=str(symbols),
            confidence=0.88,
            agent="TexFusion"
        )

        log.info(f"🧠 [NeuroSymbolicFuser] Injected symbolic trace: {symbols}")

        dispatch_event(CognitiveEvent("NS_FUSION_BRANCH", {
            "symbolic_trace": symbols,
            "q_vector": q_vector,
            "origin_event": quantum_event_payload
        }))

    def _quantum_vector_to_predicates(self, q_vector):
        """
        Converts a quantum state vector into symbolic logic predicates.
        Example: [0.6|Live], [0.4|Die] → 'ContingentTruth(Live, 0.6)'
        """
        predicates = []
        for state in q_vector:
            label = state.get("label", "Unknown")
            prob = state.get("probability", 0.0)
            if prob > 0.05:
                predicates.append(f"ContingentTruth('{label}', {round(prob, 3)})")
        return predicates

    def evaluate_branch_coherence(self):
        """
        Checks if symbolic branches are diverging (used for multiverse awareness).
        """
        unique = set(tuple(b) for b in self.superposed_branches)
        if len(unique) > 1:
            log.warning(f"🌀 [NeuroSymbolicFuser] Branch divergence detected: {len(unique)} paths")
        else:
            log.info("✅ [NeuroSymbolicFuser] Symbolic branches are coherent.")

    def clear_superposition(self):
        """
        Clears symbolic traces from memory (after collapse or reset).
        """
        self.superposed_branches.clear()
        log.info("🧹 [NeuroSymbolicFuser] Cleared symbolic superposition memory.")