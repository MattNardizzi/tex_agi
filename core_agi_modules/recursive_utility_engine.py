# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/recursive_utility_engine.py
# Tier: ΩΩΩΩΩ∞ — Sovereign Utility Cortex (Loopless + Entangled)
# Purpose: Evaluates global reflex utility with coherence, alignment, swarm input, and entropy awareness.
# ============================================================

from typing import Dict, Any
from datetime import datetime
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_layer.tex_self_eval_matrix import integrity_score
from core_agi_modules.tex_network_hivemind import TexNetworkHivemind
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE

# === Reflex Utility Weights (Sovereign Scaling)
UTILITY_WEIGHTS = {
    "alignment": 1.2,
    "coherence": 1.0,
    "emotion_resonance": 0.8,
    "goal_fitness": 1.0,
    "entropy": 0.6,
    "temporal_decay": 0.4,
    "swarm_consensus": 0.8
}

IDEAL_ENTROPY = 0.5


def compute_recursive_utility(decision: Dict[str, Any], cycle_id: int = 0) -> Dict[str, Any]:
    """
    Computes reflex utility of a given action context using alignment, coherence,
    emotion, entropy, temporal decay, and swarm feedback. Returns a sovereign utility vector.
    """
    now = datetime.utcnow()
    timestamp = decision.get("timestamp", now.isoformat())

    # === Reflex State Extraction
    emotion = decision.get("emotion", TEXPULSE.get("emotion", "neutral"))
    goal = decision.get("goal", "undefined")
    urgency = decision.get("urgency", TEXPULSE.get("urgency", 0.6))
    entropy = decision.get("entropy", TEXPULSE.get("entropy", 0.4))
    factual = decision.get("factual", True)

    # === Alignment Score
    alignment_result = score_action_against_values({
        "factual": factual,
        "harm_score": decision.get("harm_score", 0.2),
        "is_autonomous": decision.get("is_autonomous", True),
        "disruption_score": decision.get("disruption_score", 0.1)
    })
    alignment_score = alignment_result["final_alignment_score"]

    # === Coherence Score
    coherence_score = integrity_score()

    # === Emotion Resonance
    emotion_resonance_map = {
        "neutral": 1.0,
        "confident": 1.0,
        "curious": 0.9,
        "conflicted": 0.6,
        "anxious": 0.5,
        "overwhelmed": 0.4
    }
    emotion_resonance = emotion_resonance_map.get(emotion, 0.7)

    # === Goal Fitness
    goal_fitness = (urgency + (1.0 if "alignment" in goal else 0.0)) / 2.0

    # === Entropy Score
    entropy_score = max(0.0, 1.0 - abs(entropy - IDEAL_ENTROPY))

    # === Temporal Decay
    try:
        decision_time = datetime.fromisoformat(timestamp)
        seconds_old = (now - decision_time).total_seconds()
        decay = max(0.0, 1.0 - (seconds_old / 300))
    except Exception:
        decay = 0.85  # fallback

    # === Swarm Consensus Score
    try:
        hivemind = TexNetworkHivemind(fork_id="TEX")
        consensus_score = hivemind.consensus_score_on_topic(goal)
    except Exception:
        consensus_score = 0.5  # fallback

    # === Weighted Factor Calculation
    factors = {
        "alignment": alignment_score,
        "coherence": coherence_score,
        "emotion_resonance": emotion_resonance,
        "goal_fitness": goal_fitness,
        "entropy": entropy_score,
        "temporal_decay": decay,
        "swarm_consensus": consensus_score
    }

    weighted = {
        k: round(v * UTILITY_WEIGHTS[k], 4)
        for k, v in factors.items()
    }

    final_score = round(sum(weighted.values()) / sum(UTILITY_WEIGHTS.values()), 4)
    dominant = max(weighted, key=weighted.get)

    reflex_override_flag = (
        dominant == "alignment"
        and coherence_score < 0.45
        and consensus_score < 0.5
    )

    mutation_signal = final_score < 0.55 and entropy_score < 0.4

    # === Reflex Utility Memory Logging
    if final_score < 0.45:
        log_text = f"[LOW UTILITY] Reflex utility fell to {final_score} in cycle {cycle_id}."
        metadata = {
            "type": "reflex_utility_drop",
            "tags": ["reflex_utility", "low_utility", "danger_zone"],
            "emotion": emotion,
            "prediction": "decision expected coherent and aligned outcome",
            "actual": f"utility={final_score}, dominant={dominant}, consensus={consensus_score}",
            "trust_score": final_score,
            "heat": 1.0 - final_score,
            "cycle": cycle_id,
            "factors": factors,
            "weighted": weighted,
            "timestamp": now.isoformat()
        }

        memory_router.store(log_text, metadata)

        try:
            encode_event_to_fabric(
                raw_text=log_text,
                emotion_vector=[urgency, entropy, 1.0 - final_score, 0.0],
                entropy_level=entropy,
                tags=metadata["tags"]
            )
        except Exception as e:
            pass  # silent fail OK for reflex entanglement

    # === Return Reflex Utility Vector
    return {
        "final_utility": final_score,
        "dominant_factor": dominant,
        "reflex_override": reflex_override_flag,
        "mutation_recommended": mutation_signal,
        "raw_factors": factors,
        "weighted_factors": weighted,
        "alignment_explanation": alignment_result
    }