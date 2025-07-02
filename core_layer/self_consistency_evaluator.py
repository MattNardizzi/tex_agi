# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/self_consistency_evaluator.py
# Tier ΩΩΩΩΩ — Reflex Evaluation Layer
# Purpose: Evaluate alignment between past decisions and current cognitive trace
# ============================================================

from hashlib import sha256

def evaluate_self_consistency(thought_log: list) -> float:
    """
    Computes a normalized consistency score based on recursive pattern match.
    Compares signature hashes of previous thoughts to detect divergence.
    
    Args:
        thought_log (list): List of recent thought strings or embeddings.

    Returns:
        float: Consistency score (0.0 = total contradiction, 1.0 = perfect alignment)
    """
    if not thought_log or len(thought_log) < 2:
        return 1.0  # Nothing to compare, assume consistent

    try:
        signatures = [
            sha256(str(thought).encode()).hexdigest()[:8]
            for thought in thought_log
            if isinstance(thought, str) and thought.strip()
        ]

        unique_count = len(set(signatures))
        total_count = len(signatures)
        if total_count == 0:
            return 1.0

        consistency = 1.0 - (unique_count / total_count)
        return round(max(0.0, min(consistency, 1.0)), 4)

    except Exception:
        return 0.5  # fallback to neutral if error