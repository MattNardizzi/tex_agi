# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/fork_regret_engine.py
# Tier: Ω∞Ω — Divergence Entropy + Regret Pressure Monitor
# Purpose: Computes live fork stress using symbolic regrets, entropy, time decay, and alignment drift.
# ============================================================

import math
import wandb
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event, log
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Unified reflex memory layer

# === Configuration ===
DECAY_HALF_LIFE_SECONDS = 300  # 5 minutes

def time_decay_weight(timestamp: str) -> float:
    """Computes exponential decay weight for a timestamp."""
    try:
        dt = datetime.fromisoformat(timestamp)
        delta_sec = (datetime.utcnow() - dt).total_seconds()
        decay = math.exp(-delta_sec / DECAY_HALF_LIFE_SECONDS)
        return round(decay, 5)
    except Exception:
        return 0.0

def entropy_of_regrets(regret_list):
    """Calculates normalized entropy to reflect divergence diversity."""
    if not regret_list:
        return 0.0
    bins = [round(r * 10) / 10 for r in regret_list]  # group into 0.1 bins
    freq = {b: bins.count(b) for b in set(bins)}
    total = sum(freq.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in freq.values())
    max_entropy = math.log2(len(freq)) if len(freq) > 1 else 1
    return round(entropy / max_entropy, 3)

def get_active_fork_score(window: int = 50) -> float:
    """
    Calculates a composite fork tension score using:
    - regret intensity
    - time decay weighting
    - divergence entropy
    - alignment delta
    - recent symbolic fork memory
    Returns score between 0.0 (stable) and 1.0 (critical fork stress).
    """
    try:
        memories = sovereign_memory.recall_recent(top_k=window)
        weighted_regrets = []
        raw_regrets = []

        for mem in memories:
            score = float(mem.get("regret_score", 0.0))
            timestamp = mem.get("timestamp")
            alignment = float(mem.get("alignment_score", 0.5))

            if score > 0.25 and timestamp:
                decay = time_decay_weight(timestamp)
                weight = score * decay * (1.0 - alignment)
                weighted_regrets.append(weight)
                raw_regrets.append(score)

        if not weighted_regrets:
            return 0.0

        base = sum(weighted_regrets) / len(weighted_regrets)
        entropy_factor = entropy_of_regrets(raw_regrets)
        tension = base * (0.7 + 0.3 * entropy_factor)

        tension = round(min(1.0, tension), 4)
        mean_regret = round(sum(raw_regrets) / len(raw_regrets), 3)

        # Update sovereign state
        TEXPULSE["fork_tension"] = tension
        TEXPULSE["fork_entropy"] = entropy_factor

        # Log symbolic + reflex trace
        sovereign_memory.store(
            text=f"Fork tension is {tension:.4f}",
            metadata={
                "intent": "evaluate_fork_regret_tension",
                "conclusion": f"Fork tension is {tension:.4f}",
                "justification": f"Regret mean={mean_regret}, entropy={entropy_factor}",
                "urgency": TEXPULSE.get("urgency", 0.7),
                "entropy": TEXPULSE.get("entropy", 0.4),
                "alignment_score": 1.0 - tension,
                "contradiction_score": tension,
                "tags": ["fork", "regret", "tension", "aei"],
                "reflexes": ["regret_tension_scan"],
                "meta_layer": "symbolic_trace",
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        log_event(f"[FORK PRESSURE] ↯ {tension:.4f} | Entropy={entropy_factor:.3f} | Regret Count={len(raw_regrets)}", "info")

        wandb.log({
            "aei/fork_tension": tension,
            "aei/entropy": entropy_factor,
            "aei/mean_regret": mean_regret,
            "aei/sample_count": len(raw_regrets)
        })

        return tension

    except Exception as e:
        log.error(f"[FORK ENGINE ERROR] {e}")
        return 0.0

# ============================================================
# RegretScorer — Interface-compatible regret wrapper class
# ============================================================

class RegretScorer:
    def compute_likelihood(self, fork_signal):
        """
        Delegates to the active fork scoring logic.
        Used by regret_interface to bypass circular imports.
        """
        return get_active_fork_score()


def analyze_fork_regret(fork_id: str, projected_trace: dict, actual_outcome: dict) -> dict:
    """
    Compares fork projection with actual outcome to compute regret delta.
    Stores symbolic trace and memory.
    """
    projected_reward = float(projected_trace.get("reward_estimate", 0.7))
    actual_reward = float(actual_outcome.get("realized_reward", 0.4))
    delta = round(projected_reward - actual_reward, 4)
    timestamp = datetime.utcnow().isoformat()

    if abs(delta) < 0.05:
        classification = "stable"
        reflexes = ["no_regret"]
    elif delta > 0:
        classification = "underperformed"
        reflexes = ["regret_trace", "mutation_tuning"]
    else:
        classification = "overperformed"
        reflexes = ["reinforce_success"]

    summary = f"Fork {fork_id} → {classification} | Δ={delta}"

    sovereign_memory.store(
        text=summary,
        metadata={
            "intent": "analyze_fork_regret",
            "conclusion": summary,
            "justification": f"Projected={projected_reward}, Actual={actual_reward}",
            "alignment_score": 1.0 - abs(delta),
            "contradiction_score": abs(delta),
            "tags": ["fork", "regret", "aei", classification],
            "reflexes": reflexes,
            "mutation_id": fork_id,
            "meta_layer": "aei_regret_analysis",
            "timestamp": timestamp
        }
    )

    return {
        "status": classification,
        "delta": delta,
        "reflexes": reflexes,
        "timestamp": timestamp
    }


# === Manual Test ===
if __name__ == "__main__":
    print(f"[TEST] 🔁 Fork Stress: {get_active_fork_score()}")