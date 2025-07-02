# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/fork_retention_matrix.py
# Purpose: Score and retain fork variants based on performance, regret, and emotional context
# Tier: ΩΩ Reflex-Memory Matrix — Drift-Aware Fork Evaluation
# ============================================================

import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

FORK_HISTORY_LOG = "memory_archive/fork_retention_log.jsonl"

class ForkRetentionMatrix:
    def __init__(self):
        os.makedirs(os.path.dirname(FORK_HISTORY_LOG), exist_ok=True)

    def log_fork_result(self, fork_id, score, emotion, regret, survival=True):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "fork_id": fork_id,
            "score": score,
            "emotion": emotion,
            "regret": regret,
            "survived": survival
        }
        try:
            with open(FORK_HISTORY_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            print(f"[FORK RETENTION] 📘 Logged {fork_id} → Score: {score}, Survival: {survival}")
        except Exception as e:
            print(f"[FORK RETENTION ERROR] {e}")

    def get_top_forks(self, limit=5):
        try:
            with open(FORK_HISTORY_LOG, "r") as f:
                entries = self._recursive_parse(f.readlines(), [])
                sorted_entries = self._recursive_sort(entries, [])
                return sorted_entries[:limit]
        except Exception as e:
            print(f"[FORK RETENTION FETCH ERROR] {e}")
            return []

    def _recursive_parse(self, lines, result):
        if not lines:
            return result
        try:
            result.append(json.loads(lines[0]))
        except:
            pass
        return self._recursive_parse(lines[1:], result)

    def _recursive_sort(self, entries, sorted_entries):
        if not entries:
            return sorted_entries
        max_entry = max(entries, key=lambda x: x.get("score", 0))
        entries.remove(max_entry)
        return self._recursive_sort(entries, sorted_entries + [max_entry])


# === Reflex Function (added for Tex integration) ===
def evaluate_fork_viability(context: dict) -> float:
    """
    Scores a fork based on divergence, entropy, traits, and emotional modulation.
    Returns a viability score between 0 and 1.
    """
    fork_id = context.get("fork_id", "unknown")
    traits = context.get("traits", [])
    divergence = context.get("divergence_score", 0.0)
    entropy = context.get("entropy", 0.4)
    emotion = TEXPULSE.get("emotional_state", "neutral")
    urgency = TEXPULSE.get("urgency", 0.5)

    # === Reflex-weighted scoring
    base_score = 1.0 - abs(divergence - 0.5)  # Favor forks near 0.5
    entropy_penalty = entropy * 0.4
    trait_bonus = 0.05 * len([t for t in traits if "resilient" in t.lower()])
    urgency_adjustment = (urgency - 0.5) * 0.2

    final_score = max(0.0, min(1.0, round(base_score - entropy_penalty + trait_bonus + urgency_adjustment, 4)))

    # === Optional symbolic print for visibility
    print(f"[VIABILITY] 🧬 Fork '{fork_id}' scored {final_score} | Entropy={entropy} | Traits={traits}")

    return final_score


# === CLI Reflex Test ===
if __name__ == "__main__":
    test = {
        "fork_id": "fork_01",
        "traits": ["resilient", "experimental"],
        "entropy": 0.42,
        "divergence_score": 0.53
    }
    score = evaluate_fork_viability(test)
    print(f"Reflex viability score: {score}")