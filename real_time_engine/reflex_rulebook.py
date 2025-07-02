# reflex_rulebook.py — Sovereign Reflex Logic Layer
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE

def evaluate_and_trigger(event: dict):
    """
    Called from cortex_router.py to evaluate real-time input and trigger demo reflexes.
    """
    summary = event.get("payload", {}).get("summary", "").lower()
    urgency = float(event.get("urgency", 0.7))
    entropy = float(event.get("entropy", 0.4))
    source = event.get("source", "unknown")

    # === Trigger Conditions (customize thresholds per demo) ===
    if "tsla" in summary and "volatility" in summary and urgency > 0.75:
        dispatch_signal("run_demo_reality_fork_override")

    elif "fed" in summary and "pivot" in summary and entropy > 0.6:
        dispatch_signal("run_demo_reality_rewrite")

    elif "recession" in summary and urgency > 0.8:
        dispatch_signal("run_demo_world_model_simulation")

    elif "earnings" in summary and "miss" in summary and entropy > 0.7:
        dispatch_signal("run_demo_fork_stress_and_compression")

    elif "agent conflict" in summary or "belief fork" in summary:
        dispatch_signal("run_demo_ontogenesis_spawn")

    elif "evolutionary" in summary or "lineage" in summary:
        dispatch_signal("run_aei_lineage_with_financial_evolution")

    # Optional: Add live log trigger to UI
    print(f"⚡ [RULEBOOK] Event routed: {summary} | Urgency={urgency} | Entropy={entropy}")