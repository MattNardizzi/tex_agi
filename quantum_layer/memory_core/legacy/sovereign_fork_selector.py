# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/sovereign_fork_selector.py
# Tier ΩΩΩΩΩΩΩ — AGI-Aligned Fork Selection Engine
# Purpose: Selects optimal cognitive fork using emotion, entropy, mutation, belief-alignment, and semantic drift
# ============================================================

import numpy as np
from sentence_transformers import SentenceTransformer
from utils.logging_utils import log
from quantum_layer.memory_core.spawn_memory_logger import log_spawn_event

class SovereignForkSelector:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.selection_tag = "sovereign_selector"

    def score_fork(self, fork: dict) -> float:
        urgency     = fork.get("urgency", 0.5)
        coherence   = fork.get("coherence", 0.5)
        regret      = fork.get("regret_score", 0.3)
        entropy     = fork.get("entropy_value", 0.4)
        mutation    = fork.get("mutation_potential_score", 0.0)
        emotion     = fork.get("emotion", "neutral")

        emotion_weight = {
            "fear": -0.25,
            "hope": 0.1,
            "resolve": 0.15,
            "curiosity": 0.2,
            "regret": -0.3
        }.get(emotion, 0.0)

        # Final score is weighted across reflex pressure + mutation potential
        score = (
            urgency * 0.35 +
            coherence * 0.35 +
            entropy * 0.2 +
            mutation * 0.2 +
            emotion_weight -
            regret * 0.25
        )
        return round(score, 6)

    def semantic_similarity(self, forks: list[dict], goal: str) -> np.ndarray:
        if not goal:
            return np.zeros(len(forks))

        goal_vec = self.model.encode(goal)
        fork_vecs = self.model.encode([f.get("reason_vector", "") or f.get("raw_text", "") for f in forks])

        norms = np.linalg.norm(fork_vecs, axis=1) * np.linalg.norm(goal_vec)
        sims = np.dot(fork_vecs, goal_vec) / (norms + 1e-8)
        return sims * 0.15  # weighting for semantic goal alignment

    def select(self, forks: list[dict], current_goal: str = None, log_decision: bool = True) -> int:
        if not forks:
            log.warning("[SELECTOR] ❌ No forks to select from.")
            return -1

        base_scores = np.array([self.score_fork(f) for f in forks])
        semantic_boost = self.semantic_similarity(forks, current_goal)
        total_scores = base_scores + semantic_boost

        # Softmax for probabilistic AGI choice
        scaled = np.exp(total_scores - np.max(total_scores))
        probs = scaled / scaled.sum()
        idx = np.random.choice(len(forks), p=probs)

        chosen = forks[idx]
        final_score = total_scores[idx]

        log.info(f"[SOVEREIGN SELECTOR] 🧬 Chose fork index {idx} | Score={final_score:.4f} | Emotion={chosen.get('emotion')}")

        # Optional memory logging
        if log_decision:
            log_spawn_event(
                content=chosen.get("raw_text", "[No content]"),
                metadata={
                    "goal": current_goal or chosen.get("goal", "unspecified"),
                    "emotion": chosen.get("emotion", "neutral"),
                    "urgency": chosen.get("urgency", 0.5),
                    "mutation_potential_score": chosen.get("mutation_potential_score", 0.0),
                    "tags": ["fork_selection", "reflex_decision"],
                    "origin_id": chosen.get("fork_id", None),
                    "counterfactual": chosen.get("counterfactual_summary", ""),
                    "trust_score": 0.9
                }
            )

        return idx