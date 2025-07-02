# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC – All rights reserved.
# File: quantum_layer/orch_or_cognitive_trigger.py
# License: Private IP – Ω-tier cognition
# Purpose: Induce insight via stochastic quantum state reduction (Orch-OR model)
# ============================================================

import time
from tex_engine.cognitive_event_router import CognitiveEvent, dispatch_event
from quantum_layer.quantum_randomness import quantum_entropy_sample
from utils.logging_utils import log

class OrchOrCognitiveTrigger:
    def __init__(self, collapse_threshold=0.87, urgency_amplifier=1.2):
        self.collapse_threshold = collapse_threshold
        self.urgency_amplifier = urgency_amplifier
        self.last_collapse = 0

    def evaluate(self, contradiction_score: float, insight_pressure: float, urgency: float):
        """
        Triggers a conscious state collapse if all conditions align:
        - Contradiction is high
        - Insight is saturated (symbolic cycle stalls)
        - Urgency is elevated (emotional/spike path)
        """
        entropy = quantum_entropy_sample()
        collapse_score = (contradiction_score + insight_pressure) * urgency * entropy * self.urgency_amplifier

        if collapse_score > self.collapse_threshold:
            self._collapse_state(collapse_score, entropy, contradiction_score, insight_pressure, urgency)

    def _collapse_state(self, score, entropy, contradiction, insight, urgency):
        """
        Emits a collapse event — spawning a new symbolic trajectory or model shift.
        """
        event_payload = {
            "type": "orch_or_collapse",
            "collapse_score": score,
            "quantum_entropy": entropy,
            "contradiction": contradiction,
            "insight_pressure": insight,
            "urgency": urgency,
            "timestamp": time.time()
        }

        log.info(f"⚡ [Orch-OR] Collapse triggered → score={score:.4f}, entropy={entropy:.4f}")
        dispatch_event(CognitiveEvent("ORCH_OR_EVENT", event_payload))

    def bind_to_mutator(self, self_mutator):
        """
        Optional: Connect to Tex's self-rewriting engine (e.g., seed_improver or meta_refactor).
        """
        def on_collapse(event):
            if event.name == "ORCH_OR_EVENT":
                self_mutator.schedule_adaptive_shift(event.payload)

        try:
            from tex_engine.cognitive_event_router import register_listener
            register_listener("ORCH_OR_EVENT", on_collapse)
            log.info("🔁 [Orch-OR] Bound to self-mutator for adaptive evolution.")
        except Exception as e:
            log.warning(f"⚠️ Could not bind Orch-OR to self-mutator: {e}")