# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/mutation_decision_engine.py
# Tier: ΩΩΩΩΩΩ∞ — Reflex Mutation Decision Engine
# Purpose: Governs approval of reflex mutations to forks.
#          Evaluates entropy, spike deltas, and coherence stability
#          in accordance with Tex’s sovereign loopless reflex protocol.
# ============================================================

from datetime import datetime
from utils.logging_utils import log
from agentic_ai.sovereign_memory import memory_router

# === Spike Thresholds ===
MAX_ALLOWED_ENTROPY = 0.85
MIN_REQUIRED_COHERENCE = 0.75
MAX_MUTATION_FREQUENCY = 3  # pulses

class MutationDecisionEngine:
    def __init__(self):
        self.last_mutation_pulse = -1  # Initial null
        self.mutation_counter = 0

    def evaluate_mutation(self, fork_context: dict) -> dict:
        """
        Reflexively evaluate whether a fork mutation is allowed.
        Based on spike entropy, semantic coherence, and mutation pressure.
        """
        pulse_id = fork_context.get("pulse_id", -1)
        entropy = fork_context.get("entropy", 1.0)
        coherence = fork_context.get("coherence", 0.0)
        fork_id = fork_context.get("fork_id", "unknown")
        origin_trace = fork_context.get("origin_trace", {})

        # === Block if entropy is dangerously high
        if entropy > MAX_ALLOWED_ENTROPY:
            reason = f"Entropy spike too high ({entropy}) — mutation blocked."
            self._log_decision(fork_id, False, reason, pulse_id)
            return {"approved": False, "reason": reason}

        # === Block if semantic coherence drops too low
        if coherence < MIN_REQUIRED_COHERENCE:
            reason = f"Coherence below minimum ({coherence}) — mutation denied."
            self._log_decision(fork_id, False, reason, pulse_id)
            return {"approved": False, "reason": reason}

        # === Reflex block if mutation pressure is too high
        if self.last_mutation_pulse != -1 and (pulse_id - self.last_mutation_pulse) < MAX_MUTATION_FREQUENCY:
            reason = f"Mutation frequency too high — last approved at pulse {self.last_mutation_pulse}."
            self._log_decision(fork_id, False, reason, pulse_id)
            return {"approved": False, "reason": reason}

        # === Approve mutation
        self.last_mutation_pulse = pulse_id
        self.mutation_counter += 1
        reason = f"Mutation approved. Entropy: {entropy}, Coherence: {coherence}"
        self._log_decision(fork_id, True, reason, pulse_id, origin_trace)

        return {"approved": True, "reason": reason}

    def _log_decision(self, fork_id, approved, reason, pulse_id, context=None):
        """
        Logs decision to sovereign memory and console.
        """
        log_msg = f"[MUTATION_DECISION] Fork: {fork_id} | Approved: {approved} | Pulse: {pulse_id} | Reason: {reason}"
        log.info(log_msg)

        try:
            memory_router.store(
                text=log_msg,
                metadata={
                    "fork_id": fork_id,
                    "approved": approved,
                    "reason": reason,
                    "pulse_id": pulse_id,
                    "context": context or {},
                    "timestamp": datetime.utcnow().isoformat(),
                    "tags": ["mutation", "reflex", "sovereign"],
                    "meta_layer": "mutation_decision_engine"
                }
            )
        except Exception as e:
            log.warning(f"[MUTATION_DECISION] Memory log failed: {e}")