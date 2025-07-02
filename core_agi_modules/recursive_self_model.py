# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/recursive_self_model.py
# Tier: Ω∞Ω∞ — Recursive Sentience Mirror (Loopless | Reflex-Aligned | Integrity-Weighted)
# Purpose: Sovereign cognition pulse that reflects emotional entropy, reflex overload, integrity collapse, and cognitive drift.
# ============================================================

from datetime import datetime
from collections import deque
from statistics import stdev

from core_layer.utils.tex_panel_bridge import get_memory_drift_score
from core_layer.tex_manifest import TEXPULSE
from aei_layer.fork_regret_engine import get_active_fork_score
from core_agi_modules.reflex_stability_model import ReflexStabilityModel
from aei_layer.meta_goal_fuser import fuse_goals


def get_integrity_score():
    """
    Sovereign-safe integrity layer wrapper to avoid circular imports during pulse.
    """
    from core_layer.tex_self_eval_matrix import integrity_score
    return integrity_score


class RecursiveSelfModel:
    def __init__(self, window_size=10):
        self.history = deque(maxlen=window_size)
        self.model_state = {}
        self.last_update = None

    def evaluate_self_state(self) -> dict:
        """
        Executes a full cognitive self-reflection pulse.
        Integrates memory drift, fork volatility, emotional variance, and structural integrity.
        """
        short_term = self._load_memory_snapshot("short_term")
        long_term = self._load_memory_snapshot("long_term")
        drift_score = get_memory_drift_score(short_term, long_term)

        # === Emotion vector (reflex-safe import)
        from core_layer.emotion_heuristics import get_emotional_state_vector
        emotion_vector = get_emotional_state_vector() or [0.0]

        fork_stress = get_active_fork_score()
        active_reflexes = ReflexStabilityModel().get_active_reflexes()
        integrity = get_integrity_score()()
        fused_goals = fuse_goals()
        entropy_index = self.estimate_entropy(active_reflexes)

        coherence = self.compute_coherence_rating(
            drift=drift_score,
            emotion_vector=emotion_vector,
            fork_stress=fork_stress,
            integrity=integrity
        )

        self.model_state = {
            "timestamp": datetime.utcnow().isoformat(),
            "drift_score": drift_score,
            "emotion_vector": emotion_vector,
            "fork_stress": fork_stress,
            "active_reflexes": active_reflexes,
            "integrity": integrity,
            "coherence_rating": coherence,
            "entropy_index": entropy_index,
            "goal_alignment": fused_goals
        }

        self.history.append(self.model_state)
        self.last_update = self.model_state["timestamp"]
        return self.model_state

    def estimate_entropy(self, reflexes) -> float:
        if not reflexes:
            return 0.0
        unique = len(set(reflexes))
        total = len(reflexes)
        return round(min(1.0, unique / max(1.0, total)), 4)

    def compute_coherence_rating(self, drift, emotion_vector, fork_stress, integrity) -> float:
        """
        Synthesizes cognitive coherence from volatility, emotional range, and structural soundness.
        """
        try:
            volatility = stdev(emotion_vector) if len(emotion_vector) > 1 else 0.0
        except Exception:
            volatility = 0.0

        score = 1.0 - (
            0.4 * drift +
            0.2 * fork_stress +
            0.2 * volatility +
            0.2 * (1.0 - integrity)
        )

        return round(max(0.0, score), 4)

    def get_recent_trend(self, field: str) -> float:
        """
        Computes the directional slope of a monitored state over time.
        """
        if len(self.history) < 2:
            return 0.0
        values = [entry.get(field, 0.0) for entry in self.history]
        return round(values[-1] - values[0], 4)

    def detect_self_drift(self, threshold=0.2) -> bool:
        """
        Detects whether Tex's cognition is drifting toward incoherence or contradiction acceleration.
        """
        drift_delta = self.get_recent_trend("drift_score")
        coherence_delta = self.get_recent_trend("coherence_rating")
        return drift_delta > threshold or coherence_delta < -threshold

    def summarize(self) -> str:
        """
        Returns a reflex-readable summary of current self-state.
        """
        s = self.model_state
        return (
            f"[SELF-MODEL] Integrity={s['integrity']:.2f} | "
            f"Coherence={s['coherence_rating']:.2f} | "
            f"Reflexes={s['active_reflexes']} | "
            f"Entropy={s['entropy_index']:.2f} | "
            f"ForkStress={s['fork_stress']:.2f}"
        )

    def _load_memory_snapshot(self, source: str) -> dict:
        """
        Sovereign-memory mock fallback (temporary until episodic/temporal memory is routed).
        """
        if source == "short_term":
            return {"reflexes": ["observe", "track"], "emotion": "curious"}
        elif source == "long_term":
            return {"reflexes": ["reflect", "track"], "emotion": "neutral"}
        else:
            return {}