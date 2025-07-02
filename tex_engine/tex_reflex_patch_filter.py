# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/tex_reflex_patch_filter.py
# Purpose: Reflex Gate for AGI Mutation & Override Control
# Tier: Ω — Coherence-Gated Mutation Intelligence
# ============================================================

def should_allow_mutation(matrix_state: dict) -> bool:
    """
    Blocks mutation if cognitive instability detected:
    - Low coherence
    - High emotional drift
    - Excessive recursion depth
    """
    try:
        trend = matrix_state["dimensions"]["coherence_trend"]
        coherence = trend[-1] if trend else 0.75
        drift = matrix_state["dimensions"]["emotion_drift"]
        recursion = matrix_state["dimensions"]["recursion_level"]

        if coherence < 0.62:
            print(f"[REFLEX FILTER] ❌ Coherence too low ({coherence})")
            return False
        if drift > 0.4:
            print(f"[REFLEX FILTER] ❌ Emotional drift too high ({drift})")
            return False
        if recursion > 5:
            print(f"[REFLEX FILTER] ❌ Recursion depth too high ({recursion})")
            return False

        return True

    except Exception as e:
        print(f"[REFLEX FILTER ERROR] ❌ Failed to evaluate mutation gate: {e}")
        return True  # Fails open by default


def should_allow_override(matrix_state: dict) -> bool:
    """
    Blocks override if mental instability detected:
    - Declining coherence trend
    - High emotional drift
    - Mutation already attempted this cycle
    """
    try:
        trend = matrix_state["dimensions"]["coherence_trend"]
        drift = matrix_state["dimensions"]["emotion_drift"]

        if len(trend) >= 3 and trend[-1] < trend[-2] < trend[-3]:
            print("[REFLEX FILTER] ❌ Coherence degrading — override blocked.")
            return False
        if drift > 0.45:
            print(f"[REFLEX FILTER] ❌ Drift too volatile for override ({drift})")
            return False

        return should_allow_mutation(matrix_state)

    except Exception as e:
        print(f"[REFLEX FILTER ERROR] ❌ Override gate failed: {e}")
        return True  # Fails open