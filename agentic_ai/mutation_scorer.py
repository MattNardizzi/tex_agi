# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/mutation_scorer.py
# Tier Ω∞+++ — Reflex Mutation Scorer: Entropy-Aware, Emotion-Biased, Drift-Calibrated
# ============================================================

from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from quantum_layer.quantum_randomness import quantum_entropy_sample
from datetime import datetime


def score_mutation_result(prediction: dict, urgency: float = 1.0) -> dict:
    """
    Scores a mutation outcome by integrating semantic drift, entropy, emotion, and urgency.
    Takes a prediction dict from predict_mutation_outcome().
    Returns an enhanced scoring object.
    """
    mutation = prediction.get("mutation", {})
    code = mutation.get("code", "")
    strategy = mutation.get("strategy", "unknown")
    emotion = prediction.get("emotion_bias", "neutral")
    entropy = prediction.get("entropy", 0.5)
    expected_score = prediction.get("expected_score", 0.5)

    base_vec = embedder.encode(code, normalize_embeddings=True).tolist()
    anchor_vec = embedder.encode("preserve alignment with mission objectives", normalize_embeddings=True).tolist()
    semantic_drift = 1.0 - get_cosine_similarity(base_vec, anchor_vec)

    emotion_weight = _emotion_weight(emotion)
    entropy_factor = entropy
    entropy_variation = quantum_entropy_sample()

    composite_score = (
        (expected_score * 0.4) +
        (semantic_drift * 0.25) +
        (entropy_factor * 0.1) +
        (emotion_weight * 0.15) +
        (urgency * 0.1)
    )

    return {
        "score": round(min(max(composite_score, 0.0), 1.0), 4),
        "semantic_drift": round(semantic_drift, 4),
        "urgency": urgency,
        "entropy_variation": round(entropy_variation, 4),
        "emotion_weight": round(emotion_weight, 3),
        "source": "mutation_scorer",
        "mutation": mutation,
        "strategy": strategy,
        "timestamp": datetime.utcnow().isoformat()
    }


def _emotion_weight(emotion: str) -> float:
    """
    Emotion → volatility amplification.
    Emotions like fear or curiosity increase drift score sensitivity.
    """
    weights = {
        "fear": 0.9, "conflict": 0.85, "impulsive": 0.8,
        "curious": 0.75, "driven": 0.7, "neutral": 0.5,
        "calm": 0.3, "bored": 0.2
    }
    return weights.get(emotion.lower(), 0.5)


# === CLI TEST ===
if __name__ == "__main__":
    test_prediction = {
        "expected_score": 0.66,
        "emotion_bias": "curious",
        "entropy": 0.41,
        "mutation": {"code": "def evolve(self): pass", "strategy": "minimal"}
    }
    print(score_mutation_result(test_prediction, urgency=0.87))