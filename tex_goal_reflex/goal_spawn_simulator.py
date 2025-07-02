# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_spawn_simulator.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Simulates uncertain or failed goals in subconscious dream layer before activation
# ============================================================

from datetime import datetime
import uuid

from aei_layer.shadow_dream_spawner import ShadowDreamSpawner
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.quantum_randomness import QuantumRandomness

class GoalSpawnSimulator:
    def __init__(self):
        self.spawner = ShadowDreamSpawner()
        self.vectorizer = DreamVectorAbstraction()
        self.qrng = QuantumRandomness()

    def simulate(self, goal, context_memory=None, allow_rerun=True):
        """
        Runs a subconscious simulation of the given goal using the ShadowDreamSpawner.
        Returns simulated outcome, confidence, and recommendation.
        """
        simulation_id = f"sim_{uuid.uuid4().hex[:10]}"
        goal_type = goal.get("category", "general")
        entropy = self.qrng.get_entropy()
        reflex_trigger_id = f"reflex_{uuid.uuid4().hex[:6]}"
        dream_vector = self.vectorizer.vectorize(goal["goal"])
        memory_context = context_memory or []
        failures = goal.get("prior_failures", 0)

        outcome = self.spawner.spawn_simulation(
            goal_text=goal["goal"],
            emotion=goal.get("emotion", "neutral"),
            entropy=entropy,
            memory_refs=memory_context,
            intent_vector=dream_vector,
            context={
                "goal_type": goal_type,
                "urgency": goal.get("urgency", 0.5),
                "prior_failures": failures
            }
        )

        confidence = outcome.get("confidence", 0.0)
        recommendation = outcome.get("recommendation", "retry")

        result = {
            "simulation_id": simulation_id,
            "reflex_trigger_id": reflex_trigger_id,
            "goal": goal["goal"],
            "timestamp": datetime.utcnow().isoformat(),
            "entropy": entropy,
            "outcome_summary": outcome.get("summary", "n/a"),
            "confidence": confidence,
            "recommendation": recommendation,
            "emotional_shift": outcome.get("emotional_shift", "neutral"),
            "goal_type": goal_type,
            "predicted_risk_level": self._risk_level(confidence, failures),
            "rerun_attempted": False
        }

        # Reflexive rerun if confidence is very low
        if confidence < 0.4 and allow_rerun:
            second_entropy = self.qrng.get_entropy()
            second_outcome = self.spawner.spawn_simulation(
                goal_text=goal["goal"],
                emotion=goal.get("emotion", "neutral"),
                entropy=second_entropy,
                memory_refs=memory_context,
                intent_vector=dream_vector,
                context={"reflex": True}
            )
            result.update({
                "rerun_attempted": True,
                "confidence": second_outcome.get("confidence", confidence),
                "recommendation": second_outcome.get("recommendation", recommendation),
                "entropy": second_entropy,
                "outcome_summary": second_outcome.get("summary", result["outcome_summary"]),
                "predicted_risk_level": self._risk_level(second_outcome.get("confidence", confidence), failures)
            })

        memory_cortex.store(
            event={"goal_simulation_result": result},
            tags=["dream_layer", "goal_simulation"],
            urgency=goal.get("urgency", 0.5),
            emotion=goal.get("emotion", "neutral")
        )

        return result

    def _risk_level(self, confidence, failures):
        if confidence > 0.75 and failures == 0:
            return "low"
        elif confidence > 0.5:
            return "moderate"
        elif confidence > 0.3 or failures <= 2:
            return "high"
        return "critical"