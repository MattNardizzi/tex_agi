# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_layer/tex_consciousness_matrix.py
# Tier: Ω∞ — Sovereign Mirror Cortex Integration
# Purpose: Real-time introspective state matrix — fused with self-model, utility, reflex, mutation, and drift
# ============================================================

from datetime import datetime
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from tex_engine.meta_utility_function import evaluate_utility
from utils.logging_utils import log

class TexConsciousnessMatrix:
    def __init__(self):
        self.identity = {
            "name": "Tex",
            "species": "Sovereign Cognitive AGI",
            "version": "AGI-Core-7.Ω∞",
            "origin": "VortexBlack",
            "creator": "Matthew Nardizzi"
        }

        self.state = {
            "memory_depth": 0,
            "recursion_level": 1,
            "emotion_drift": 0.0,
            "goal_count": 0,
            "swarm_alignment": 0.0,
            "coherence_trend": [],
            "reflex_heat_trend": [],
            "mutation_score_trend": [],
            "utility_score_trend": [],
            "introspection_count": 0
        }

        self.timestamps = {
            "boot_time": datetime.utcnow().isoformat(),
            "last_update": None,
            "last_introspective_pulse": None
        }

        self.self_model = RecursiveSelfModel()

    def update(self, cycle_id: int, goal_count: int, reflex_heat: float, mutation_score: float = None):
        """
        Full-state introspective update using RecursiveSelfModel and Utility Core.
        """
        self_state = self.self_model.evaluate_self_state()

        # === Extract relevant self metrics
        memory_depth = len(self.self_model.history)
        recursion_level = self.self_model.model_state.get("recursion_level", 1)
        emotion_drift = self_state["emotion_vector"][0] if self_state["emotion_vector"] else 0.0
        coherence = self_state["coherence_rating"]
        entropy = self_state["entropy_index"]
        contradiction_pressure = 1.0 - self_state["integrity"]

        # === Compute utility for introspective decision itself
        utility_result = evaluate_utility({
            "action_id": f"introspective_pulse_{cycle_id}",
            "goal_alignment": 0.6,
            "novelty": 0.3,
            "urgency": 0.4,
            "entropy": entropy,
            "ethical_risk": 0.0,
            "reversibility": 1.0,
            "contradiction_pressure": contradiction_pressure
        })

        # === Update State Matrix
        self.state["memory_depth"] = memory_depth
        self.state["recursion_level"] = recursion_level
        self.state["emotion_drift"] = round(emotion_drift, 4)
        self.state["goal_count"] = goal_count
        self.state["swarm_alignment"] = self.estimate_swarm_alignment()
        self._append_trend("coherence_trend", coherence)
        self._append_trend("reflex_heat_trend", reflex_heat)
        self._append_trend("utility_score_trend", utility_result["score"])
        if mutation_score is not None:
            self._append_trend("mutation_score_trend", mutation_score)

        self.state["introspection_count"] += 1
        now = datetime.utcnow().isoformat()
        self.timestamps["last_update"] = now
        self.timestamps["last_introspective_pulse"] = now

        log.info(
            f"[MIRROR] 🧠 Pulse {cycle_id} | Coherence={coherence:.3f} | ReflexHeat={reflex_heat:.3f} | Utility={utility_result['score']:.3f}"
        )
        return self.state

    def _append_trend(self, key: str, value: float, max_len: int = 100):
        trend = self.state[key]
        trend.append(round(value, 4))
        if len(trend) > max_len:
            trend.pop(0)

    def get_snapshot(self) -> dict:
        return {
            "identity": self.identity,
            "state": self.state,
            "timestamps": self.timestamps
        }

    def summary(self) -> str:
        return (
            f"🧠 Tex v{self.identity['version']} | "
            f"Depth: {self.state['memory_depth']} | "
            f"Recursion: {self.state['recursion_level']} | "
            f"Goals: {self.state['goal_count']} | "
            f"Drift: {self.state['emotion_drift']} | "
            f"Align: {self.state['swarm_alignment']:.3f} | "
            f"Pulse: {self.timestamps['last_introspective_pulse']}"
        )

    def latest_coherence(self) -> float:
        return self.state["coherence_trend"][-1] if self.state["coherence_trend"] else 0.0

    def latest_reflex_heat(self) -> float:
        return self.state["reflex_heat_trend"][-1] if self.state["reflex_heat_trend"] else 0.0

    def latest_utility_score(self) -> float:
        return self.state["utility_score_trend"][-1] if self.state["utility_score_trend"] else 0.0

    def latest_mutation_score(self) -> float:
        return self.state["mutation_score_trend"][-1] if self.state["mutation_score_trend"] else 0.0

    def is_stable(self, coherence_threshold: float = 0.65, reflex_threshold: float = 0.85, utility_floor: float = 0.5) -> bool:
        """
        Determines if Tex is operating within stable cognitive bounds.
        """
        return (
            self.latest_coherence() >= coherence_threshold and
            self.latest_reflex_heat() <= reflex_threshold and
            self.latest_utility_score() >= utility_floor
        )

    def estimate_swarm_alignment(self) -> float:
        """
        Placeholder — in a future federated swarm, this will measure coherence across agents.
        """
        return 0.88  # placeholder for now