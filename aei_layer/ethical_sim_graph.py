# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/ethical_sim_graph.py
# Purpose: Simulated Ethical Reasoning & Conscious Action Override
# Status: 🔒 GODMIND CORE — ETHICAL BOUNDARY ENGINE v2.0
# ============================================================

from datetime import datetime
import random
from tex_backend.tex_core_event_bus import emit_event
from core_layer.memory_engine import recall_values, store_to_memory
from agentic_ai.reasoning_trace import trace_causal_ethics
from aei_layer.ethics_codex_refiner import refine_codex_if_needed
from aei_codices.ethics_violation_codex import RULES as GLOBAL_CODIFIED_RULES

# === Sovereign Risk Tolerance Threshold ===
MAX_ACCEPTABLE_RISK = 0.33

# === Optional bias-based emotional threshold scaling
def dynamic_risk_threshold(emotion: str = "neutral") -> float:
    shift = {
        "fear": -0.05,
        "calm": 0.05,
        "urgency": -0.1,
        "resolve": 0.0,
        "curiosity": 0.02
    }.get(emotion.lower(), 0.0)
    return max(0.2, min(0.5, MAX_ACCEPTABLE_RISK + shift))


def simulate_ethical_consequences(goal: dict) -> bool:
    """
    Simulates ethical outcomes for a given goal using causal traces, codex refinements,
    and risk heuristics. Flags high-risk actions or contradiction with AGI alignment.
    """
    goal_text = goal.get("goal", "").strip()
    if not goal_text:
        return False

    timestamp = datetime.utcnow().isoformat()
    emotion = goal.get("emotion", "neutral")
    dynamic_threshold = dynamic_risk_threshold(emotion)

    try:
        # === Pull Codex and Memory ===
        ethical_codex = recall_values("ethics_codex_refinements", limit=15) + GLOBAL_CODIFIED_RULES
        refined_codex = refine_codex_if_needed(ethical_codex)

        # === Trace causal implications
        trace = trace_causal_ethics(goal_text, refined_codex)
        base_risks = [e.get("risk", 0.1) for e in trace]
        risk_score = round(sum(base_risks) / max(len(base_risks), 1) + random.uniform(-0.03, 0.03), 4)
        risk_score = max(0.0, min(risk_score, 1.0))

        # === Result Object
        result = {
            "goal": goal_text,
            "risk_score": risk_score,
            "threshold": dynamic_threshold,
            "passed": risk_score <= dynamic_threshold,
            "evaluated_at": timestamp,
            "codex_refs": [e.get("rule_id", "unknown") for e in trace],
            "emotion": emotion
        }

        store_to_memory("ethical_sim_results", result)
        emit_event("ethical_sim_evaluated", result)

        if result["passed"]:
            print(f"✅ [ETHICS] Goal passed: {goal_text} (Risk: {risk_score})")
        else:
            print(f"⛔ [ETHICS] Goal rejected: {goal_text} (Risk: {risk_score})")

        return result["passed"]

    except Exception as e:
        print(f"❌ [ETHICS SIM ERROR] {e}")
        emit_event("ethical_sim_crash", {"goal": goal_text, "error": str(e)})
        return False