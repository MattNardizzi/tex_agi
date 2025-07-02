# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/reinforcement.py
# Purpose: AdaptiveReinforcer for Sovereign Cognition - Real-Time Behavioral Learning Core
# ============================================================

import random
import time
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from agentic_ai.reasoning_trace import log_reasoning_step
from sovereign_evolution.code_patch_logger import CodePatchLogger

class AdaptiveReinforcer:
    def __init__(self):
        self.reward_history = []
        self.policy_weights = {}
        self.last_feedback = None
        self.patch_logger = CodePatchLogger()

    def learn(self, decision, reward, context="", metadata=None):
        timestamp = datetime.utcnow().isoformat()

        # ✅ Handle invalid inputs safely
        if isinstance(decision, float):
            decision = f"float_input_{round(decision, 3)}"
        elif not isinstance(decision, str):
            decision = str(decision)

        if isinstance(reward, dict):  # Defensive fallback
            reward = reward.get("value", 0.5)

        feedback = {
            "decision": decision,
            "reward": reward,
            "context": context,
            "emotion": TEXPULSE.get("emotional_state", "neutral"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "coherence": TEXPULSE.get("coherence", 0.75),
            "timestamp": timestamp
        }

        if metadata:
            feedback.update(metadata)

        self.reward_history.append(feedback)
        self.last_feedback = feedback

        store_to_memory("reinforcement_log", feedback)
        log_reasoning_step(f"[REINFORCE] Decision '{decision}' scored reward = {reward}")

        if reward > 0.8:
            self.patch_logger.log({
                "strategy": "reinforce_decision",
                "decision": decision,
                "reward": reward,
                "emotion": feedback["emotion"],
                "timestamp": timestamp,
                "context": context
            }, approved=True)

    def score_action(self, emotion, urgency, coherence):
        base = 0.5
        if emotion in {"resolve", "hope"}:
            base += 0.1
        if urgency > 0.7:
            base += 0.1
        if coherence > 0.8:
            base += 0.1

        return round(min(base, 1.0), 3)

    def update_policy(self):
        # Placeholder — simulate dynamic policy adjustment
        outcome_weights = {}
        for fb in self.reward_history[-10:]:
            key = f"{fb['decision']}:{fb['emotion']}"
            outcome_weights[key] = outcome_weights.get(key, 0) + fb["reward"]

        # Normalize and update
        for k in outcome_weights:
            self.policy_weights[k] = round(outcome_weights[k] / 10, 3)

        return self.policy_weights

    def suggest_decision_bias(self):
        if not self.policy_weights:
            return "exploratory"

        sorted_bias = sorted(self.policy_weights.items(), key=lambda x: x[1], reverse=True)
        top = sorted_bias[0][0].split(":")[1] if ":" in sorted_bias[0][0] else "adaptive"
        return top

    def assess(self, *args, **kwargs):
        """
        Assess Tex's current state and reinforce recent outcomes.
        Can be expanded with PPO/LSTM/meta-RL logic.
        """
        print("[REINFORCER] 🔍 Assessing behavioral trajectory...")

        recent_policy = self.update_policy()
        bias = self.suggest_decision_bias()
        timestamp = datetime.utcnow().isoformat()

        store_to_memory("reinforcement_event", {
            "event": "assess",
            "policy_snapshot": recent_policy,
            "suggested_bias": bias,
            "timestamp": timestamp
        })

        log_reasoning_step("adaptive_reinforcer", f"Suggested bias: {bias}", f"Policy: {recent_policy}", 0.7, "Tex")

        return {
            "status": "assessed",
            "suggested_bias": bias,
            "policy": recent_policy,
            "timestamp": timestamp
        }