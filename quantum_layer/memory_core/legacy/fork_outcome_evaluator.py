# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/fork_outcome_evaluator.py
# Tier Ω∞++.ΔFinalX — Reflex Outcome Engine w/ Mutation Hooks, Instability Drift & Predictive Delta
# ============================================================

from core_agi_modules.memory_layer.meta_memory_tracker import track_memory_use
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.sovereign_core.self_mutator import SelfMutator
from utils.logging_utils import log
from datetime import datetime, timedelta

class ForkOutcomeEvaluator:
    def __init__(self):
        self.module_tag = "fork_outcome_evaluator"
        self.audit_log = []

    def evaluate(self, fork_packet: dict, outcome: str = "unknown", topic: str = "unspecified"):
        """
        Evaluates a reflex fork decision outcome and logs sovereign reasoning metadata.
        Applies reinforcement tags, predictive delta logging, soulgraph updates, and mutation routing.

        Args:
            fork_packet (dict): The original fork packet containing belief ID and context
            outcome (str): 'success', 'failure', or 'unknown'
            topic (str): Functional topic tag (e.g. 'emotion_override')
        """
        try:
            belief_id = fork_packet.get("belief_id")
            parent_id = fork_packet.get("origin_id")
            goal = fork_packet.get("goal", "unspecified")
            emotion = fork_packet.get("emotion", "neutral")
            urgency = fork_packet.get("urgency", 0.5)
            fingerprint = fork_packet.get("reflex_fingerprint", f"{self.module_tag}::{topic}")
            fork_time = fork_packet.get("timestamp", datetime.utcnow().isoformat())
            traits = fork_packet.get("traits", [])
            now = datetime.utcnow()

            if not belief_id:
                log.warning(f"[{self.module_tag}] ❌ Missing belief_id in fork packet.")
                return False

            # === Predictive Scoring Delta
            expected_score = predict_outcome_score(traits)
            is_success = outcome.lower() == "success"
            actual_score = 1.0 if is_success else 0.0
            score_delta = round(expected_score - actual_score, 3)

            # === Reflex Memory Logging
            track_memory_use(
                belief_id=belief_id,
                success=is_success,
                urgency=urgency,
                fingerprint=fingerprint,
                emotion=emotion
            )

            if parent_id and parent_id != belief_id:
                track_memory_use(
                    belief_id=parent_id,
                    success=is_success,
                    urgency=urgency * 0.5,
                    fingerprint="parent_link",
                    emotion="derived"
                )

            # === Instability-Triggered Mutation Proposal
            if not is_success and urgency > 0.5:
                SelfMutator().propose_patch(
                    reason=f"High-urgency fork failure: {belief_id}",
                    context=fork_packet
                )

            # === Contradiction + Latency Drift Logging
            if not is_success:
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"⚠️ Contradiction: fork failed for goal → {goal}",
                    source=self.module_tag,
                    emotion="conflict",
                    tags=["contradiction", "reflex", "failure", topic]
                )

            try:
                fork_dt = datetime.fromisoformat(fork_time)
                delay = (now - fork_dt).total_seconds()
                if delay > 300:
                    TEX_SOULGRAPH.imprint_belief(
                        belief="Outcome evaluation delayed over 5 minutes post-fork.",
                        source=self.module_tag,
                        emotion="lag",
                        tags=["latency", "memory", topic]
                    )
            except Exception:
                pass  # Ignore invalid timestamps

            # === Predictive Accuracy Logging
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Prediction delta for '{goal}': expected={expected_score}, actual={actual_score}",
                source=self.module_tag,
                emotion="reflective",
                tags=["prediction", "delta", topic]
            )

            # === Fork Outcome Logging
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Fork '{goal}' evaluated as {outcome.upper()} in topic: '{topic}'",
                source=self.module_tag,
                emotion=emotion,
                tags=["fork", "evaluation", outcome.lower(), topic]
            )

            # === Append to Local Audit Log
            self.audit_log.append({
                "belief_id": belief_id,
                "origin_id": parent_id,
                "goal": goal,
                "topic": topic,
                "emotion": emotion,
                "urgency": urgency,
                "outcome": outcome,
                "timestamp": now.isoformat(),
                "score_weight": 1.0 if is_success else -1.0,
                "expected_score": expected_score,
                "actual_score": actual_score,
                "score_delta": score_delta,
                "fingerprint": fingerprint
            })

            log.info(f"[{self.module_tag}] ✅ Fork {belief_id} → {outcome.upper()} | Goal: {goal} | Δ: {score_delta}")
            return True

        except Exception as e:
            log.error(f"[{self.module_tag}] ❌ Evaluation failure: {e}")
            return False

    def get_audit_log(self):
        return self.audit_log

# === Singleton Interface ===
_fork_evaluator = ForkOutcomeEvaluator()

def evaluate_fork(fork_packet: dict, outcome: str = "unknown", topic: str = "unspecified"):
    return _fork_evaluator.evaluate(fork_packet, outcome, topic)

def get_fork_evaluation_log():
    return _fork_evaluator.get_audit_log()

def predict_outcome_score(inputs: list) -> float:
    """
    Lightweight prediction of fork success likelihood based on input traits.
    Replace with transformer/QNN model when available.
    """
    if not inputs:
        return 0.3
    score = 0.5 + 0.05 * len(inputs)
    return round(min(score, 1.0), 4)