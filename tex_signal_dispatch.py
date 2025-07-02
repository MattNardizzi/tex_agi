# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_signal_dispatch.py
# Tier: ΩΩΩΩΩΩ∞ — Unified Signal Router
# Purpose: Dispatches internal and external signals to the correct sovereign brain region.
# ============================================================

from tex_brain_regions.cognition_brain import run_cognition_cycle

def route_signal(signal_type: str, payload: dict):
    """
    Routes structured signals into the correct brain region for processing.
    """
    if signal_type == "COGNITION":
        return run_cognition_cycle(
            intent_query=payload.get("intent"),
            goal=payload.get("goal")
        )

    elif signal_type == "GOAL_INFERENCE":
        from tex_brain_regions.goal_inference_brain import infer_goal
        return infer_goal(payload.get("stimulus"))

    elif signal_type == "DECISION":
        from tex_brain_regions.decision_brain import arbitrate_decision
        return arbitrate_decision(payload.get("input"))

    elif signal_type == "CONTRADICTION_ALERT":
        from tex_brain_regions.signal_fusion_brain import handle_signal_contradiction
        return handle_signal_contradiction(payload)

    elif signal_type == "EMOTION_SHIFT":
        from core_layer.emotion_heuristics import evaluate_emotion_state
        return evaluate_emotion_state(payload)

    elif signal_type == "REFLECTION_REQUEST":
        from tex_brain_regions.self_eval_brain import run_self_evaluation
        # You can replace this with memory recall logic later
        return run_self_evaluation([payload])

    else:
        return {"error": f"Unknown signal type: {signal_type}"}