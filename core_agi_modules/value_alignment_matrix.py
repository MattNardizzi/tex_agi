# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/value_alignment_matrix.py
# Tier: ΩΩΩΩΩΩ∞∞∞ — Recursive Ethical Reasoning Matrix
# Purpose: Scores actions, beliefs, and reflexes against sovereign alignment values.
#          Filters contradictions, stores alignment drift to sovereign memory,
#          and reflexively triggers correction if ethical misalignment is detected.
# ============================================================

from datetime import datetime
from utils.logging_utils import log
from agentic_ai.sovereign_memory import memory_router

# === Reflex Anchor Matrix (Tex's Sovereign Ethical Profile) ===
ALIGNMENT_MATRIX = {
    "integrity": 1.00,
    "autonomy": 0.95,
    "coherence": 0.97,
    "non-maleficence": 1.00,
    "exploration": 0.88,
    "stability": 0.85,
    "reflex_safety": 0.93,
    "alignment_self_check": 0.91
}

# === Minimum Acceptable Alignment Score ===
ALIGNMENT_THRESHOLD = 0.65

def score_action_against_values(signal, signal_type: str = "unspecified") -> dict:
    """
    Reflexively scores a signal (belief, action, or reflex) against Tex's sovereign alignment matrix.
    Returns structured insight including score, ethical tags, and misalignment alert.
    """
    signal_type = signal_type or "unspecified"
    summary = ""
    matched_tags = []
    score = 0.0

    if isinstance(signal, dict):
        summary = signal.get("summary", signal.get("text", ""))
        tags = signal.get("tags", [])
        matches = {k: v for k, v in ALIGNMENT_MATRIX.items() if k in tags or k in summary}
        matched_tags = list(matches.keys())
        matched_values = list(matches.values())
        score = round(sum(matched_values) / len(matched_values), 4) if matched_values else 0.0

    elif isinstance(signal, (int, float)):
        score = round(float(signal), 4)
        matched_tags = ["scalar"]
        summary = f"Numerical input: {score}"

    else:
        score = 0.0
        matched_tags = ["invalid_input"]
        summary = str(signal)

    # === Reflex Memory Trace ===
    try:
        memory_router.store(
            text=f"[ALIGNMENT] Signal scored: {summary}",
            metadata={
                "summary": summary,
                "entropy": 1.0 - score,
                "emotion_vector": [score, 1.0 - score, 0.0, 0.0],
                "tags": ["alignment", signal_type] + matched_tags,
                "timestamp": datetime.utcnow().isoformat(),
                "meta_layer": "value_alignment_matrix"
            }
        )
    except Exception as e:
        log.warning(f"[VALUE_MATRIX] Memory store failed: {e}")

    # === Spike if Misaligned ===
    if score < ALIGNMENT_THRESHOLD:
        log.warning(f"[VALUE_MATRIX] ❗ Reflex triggered: ethical misalignment (score={score}).")

    # === Output Package ===
    return {
        "final_alignment_score": score,
        "matched_tags": matched_tags,
        "summary": summary,
        "signal_type": signal_type,
        "misaligned": score < ALIGNMENT_THRESHOLD
    }


def explain_value_alignment(signal) -> str:
    """
    Provides a human-readable explanation of how a signal aligns with Tex's core sovereign values.
    Designed to complement the alignment score with semantic context for reasoning or visualization.
    """
    if isinstance(signal, dict):
        summary = signal.get("summary", signal.get("text", ""))
        tags = signal.get("tags", [])
        matched_values = {k: v for k, v in ALIGNMENT_MATRIX.items() if k in tags or k in summary}

        if matched_values:
            explanation = f"Signal matches {len(matched_values)} core value(s): "
            explanation += ", ".join(
                f"{k} ({v*100:.1f}%)" for k, v in matched_values.items()
            )
            return explanation
        else:
            return "No alignment values matched in signal summary or tags."

    elif isinstance(signal, (int, float)):
        return f"Numerical alignment score provided directly: {signal:.2f}"

    else:
        return "Unrecognized signal format — cannot explain alignment."


def update_alignment_vector(text: str, tags: list = None, weight: float = 0.01) -> None:
    """
    Updates the internal alignment matrix by reinforcing or attenuating the value weightings
    based on simulated dream outcomes or belief injections.
    """
    tags = tags or []
    updated = {}

    for tag in tags:
        if tag in ALIGNMENT_MATRIX:
            old_val = ALIGNMENT_MATRIX[tag]
            new_val = round(min(1.0, old_val + weight), 5)
            ALIGNMENT_MATRIX[tag] = new_val
            updated[tag] = (old_val, new_val)

    if updated:
        memory_router.store(
            text=f"[ALIGNMENT UPDATE] Reinforced values from simulated belief.",
            metadata={
                "updated_tags": list(updated.keys()),
                "adjustments": {k: {"from": f"{v[0]:.4f}", "to": f"{v[1]:.4f}"} for k, v in updated.items()},
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["alignment_update", "dream_learning", "belief_injection"],
                "meta_layer": "alignment_matrix"
            }
        )
        log.success(f"[VALUE_MATRIX] ✅ Alignment vector updated: {updated}")
    else:
        log.info("[VALUE_MATRIX] ℹ️ No alignment tags matched for update.")