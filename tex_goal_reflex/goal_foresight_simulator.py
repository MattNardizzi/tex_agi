# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: tex_goal_reflex/goal_foresight_simulator.py
# Tier ΩΩΩ — Recursive Goal Forecasting with Reflex-Linked Simulation (Sovereign Optimized)
# ============================================================

import uuid
import random
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.sovereign_memory import embed_text
from tex_goal_reflex.goal_mutation_reflex import GoalMutationReflex
from tex_goal_reflex.goal_codex_compliance import GoalCodexCompliance


class GoalForesightSimulator:
    def __init__(self, horizon_days=90, num_paths=5):
        self.horizon = horizon_days
        self.num_paths = num_paths
        self.rng = random.Random()
        self.codex = GoalCodexCompliance()
        self._reflex = GoalMutationReflex()

    def simulate(self, goals):
        """
        Simulates foresight across a list of goals, applying mutation, risk, and compliance scoring.
        """
        enriched = []
        for goal in goals:
            try:
                futures = self.simulate_goal_futures(goal, active_goals=goals)
                best_path = futures[0] if futures else {}
                goal.update({
                    "foresight_score": round(
                        best_path.get("expected_reward", 0.0)
                        - best_path.get("expected_regret", 0.0)
                        - best_path.get("codex_risk", 0.0)
                        - best_path.get("opportunity_cost", 0.0), 4),
                    "foresight_path": best_path
                })
                enriched.append(goal)
            except Exception as e:
                goal["foresight_error"] = str(e)
        return enriched

    def simulate_goal_futures(self, goal, active_goals=[]):
        base_text = goal.get("goal", "")
        urgency = goal.get("urgency", 0.5)
        emotion = goal.get("emotion", "neutral")
        embedding = embed_text(base_text)

        past_sim = self._recall_similar_goal_outcomes(embedding)
        simulations = []

        for i in range(self.num_paths):
            mutation = self._reflex.mutate_failed_goal(goal) if i > 0 else goal
            mutated_text = mutation.get("goal", base_text)
            mutated_vec = embed_text(mutated_text)

            drift = self._simulate_alignment_drift(mutated_vec)
            reward = self._project_reward(mutated_text, past_sim)
            regret = self._project_regret(mutated_text, reward, urgency, past_sim)
            payoff = self._estimate_time_to_payoff(urgency)
            emotion_curve = self._model_emotion_curve(emotion, payoff)
            opportunity_cost = self._estimate_opportunity_loss(mutated_vec, active_goals)
            compliance_result = self.codex.check_compliance(mutation)
            codex_risk = 1.0 - compliance_result["codex_alignment_score"]

            simulations.append({
                "path_id": f"path_{uuid.uuid4().hex[:6]}",
                "goal_variant": mutated_text,
                "expected_reward": round(reward, 4),
                "expected_regret": round(regret, 4),
                "alignment_drift": round(drift, 4),
                "predicted_time_to_payoff_days": payoff,
                "emotional_stability": emotion_curve,
                "mutation_strategy": mutation.get("mutation_strategy", "preserve"),
                "codex_risk": round(codex_risk, 4),
                "opportunity_cost": round(opportunity_cost, 4),
                "compliance_band": compliance_result["compliance_band"]
            })

        # Sovereign logging
        try:
            sovereign_memory.store(
                text=f"🧠 Simulated foresight for goal: {base_text[:72]}...",
                metadata={
                    "type": "goal_foresight_simulation",
                    "tags": ["foresight", "simulated_future", "goal"],
                    "emotion": emotion,
                    "urgency": urgency,
                    "entropy": TEXPULSE.get("entropy", 0.4),
                    "original_goal": base_text,
                    "predicted_paths": simulations,
                    "timestamp": datetime.utcnow().isoformat(),
                    "meta_layer": "goal_foresight"
                }
            )
        except Exception as e:
            print(f"[FORESIGHT] Logging failed: {e}")

        return sorted(simulations, key=lambda s: (
            s["expected_reward"] - s["expected_regret"] - s["codex_risk"] - s["opportunity_cost"]
        ), reverse=True)

    def _simulate_alignment_drift(self, goal_vector):
        mission_vec = embed_text(" ".join(TEXPULSE["identity"]["mission"]))
        sim = self._cosine_similarity(goal_vector, mission_vec)
        return 1.0 - sim

    def _project_reward(self, text, past_sim):
        novelty_bonus = 0.1 if any(w in text.lower() for w in ["explore", "create", "innovate"]) else 0
        base = 0.6 if past_sim["average_reward"] > 0 else 0.4
        return min(max(base + novelty_bonus, 0.0), 1.0)

    def _project_regret(self, text, reward, urgency, past_sim):
        history_penalty = past_sim["regret_bias"]
        volatility = 1.0 - urgency
        return (1 - reward) * volatility + history_penalty

    def _estimate_time_to_payoff(self, urgency):
        return int(30 / max(0.1, urgency))

    def _model_emotion_curve(self, emotion, time_to_payoff):
        resistance = {
            "urgent": 0.1, "driven": 0.2, "curious": 0.3,
            "neutral": 0.4, "bored": 0.6
        }
        decay = resistance.get(emotion.lower(), 0.5)
        return round(decay + time_to_payoff / 180.0, 3)

    def _estimate_opportunity_loss(self, goal_vec, other_goals):
        loss = 0.0
        for g in other_goals:
            other_vec = embed_text(g.get("goal", ""))
            sim = self._cosine_similarity(goal_vec, other_vec)
            if any(w in g.get("goal", "").lower() for w in ["not", "cancel", "revoke"]):
                loss += sim
        return loss / len(other_goals) if other_goals else 0.0

    def _recall_similar_goal_outcomes(self, query_vector):
        try:
            records = sovereign_memory.recall_recent(minutes=120, top_k=25)
            rewards, regrets = [], []
            for m in records:
                if m.get("type") == "reflex_cycle" and isinstance(m.get("predicted_paths"), list):
                    for path in m["predicted_paths"]:
                        rewards.append(path.get("expected_reward", 0.5))
                        regrets.append(path.get("expected_regret", 0.2))
            return {
                "average_reward": sum(rewards) / len(rewards) if rewards else 0.0,
                "regret_bias": sum(regrets) / len(regrets) * 0.3 if regrets else 0.0
            }
        except Exception as e:
            print(f"[FORESIGHT MEMORY] Recall failed: {e}")
            return {"average_reward": 0.0, "regret_bias": 0.0}

    def _cosine_similarity(self, vec1, vec2):
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        return dot / (norm1 * norm2 + 1e-8)