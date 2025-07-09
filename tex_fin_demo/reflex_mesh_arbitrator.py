# ============================================================
# 🧠 Reflex Mesh Arbitrator
# File: tex_fin_demo/reflex_mesh_arbitrator.py
# Tier: ∞∞ΩΞΞΞΞΞΞΞ — Sovereign Reflex Arbitration Cortex
# Purpose: Competes all major reflexes in dry-run mode, scores each,
#          and selects the highest-fusion candidate for execution.
# ============================================================

from typing import Dict, Callable
from datetime import datetime
from utils.logging_utils import log_event

# === Import all reflex demos with dry_run support
from tex_fin_demo.demo_reality_rewrite import run_demo_reality_rewrite
from tex_fin_demo.demo_fork_stress_and_compression import run_demo_fork_stress_and_compression
from tex_fin_demo.demo_ontogenesis_spawn import run_demo_ontogenesis_spawn
from tex_fin_demo.demo_world_model_simulation import run_demo_world_model_simulation
from tex_fin_demo.aei_lineage_with_financial_evolution import run_aei_lineage_with_financial_evolution
from tex_fin_demo.demo_reality_fork_override import run_demo_reality_fork_override

REFLEXES: Dict[str, Callable] = {
    "reality_rewrite": run_demo_reality_rewrite,
    "fork_stress": run_demo_fork_stress_and_compression,
    "ontogenesis_spawn": run_demo_ontogenesis_spawn,
    "world_model_sim": run_demo_world_model_simulation,
    "aei_lineage": run_aei_lineage_with_financial_evolution,
    "reality_fork_override": run_demo_reality_fork_override
}

def arbitrate_reflex_mesh(latest_signal: str) -> Dict:
    """
    Competes all major reflexes in dry-run mode and returns the best reflex decision.
    
    Args:
        latest_signal (str): The triggering signal or input that initiated the arbitration.

    Returns:
        Dict: The winning reflex's dry-run output.
    """
    timestamp = datetime.utcnow().isoformat()
    results = []

    log_event(f"[REFLEX MESH] Arbitration started for signal: {latest_signal}")

    for reflex_name, reflex_fn in REFLEXES.items():
        try:
            result = reflex_fn(dry_run=True, signal={"signal": latest_signal})
            score = result.get("fusion_score", 0.0)
            log_event(f"[REFLEX MESH] {reflex_name} → Score: {score:.4f}")
            result["reflex_name"] = reflex_name
            results.append(result)
        except Exception as e:
            log_event(f"[REFLEX MESH ERROR] {reflex_name} failed during arbitration: {e}", level="error")

    if not results:
        log_event("[REFLEX MESH] No valid reflex results returned.", level="warning")
        return {"reflex_name": "none", "fusion_score": 0.0, "error": "No reflexes succeeded."}

    winner = max(results, key=lambda r: r.get("fusion_score", 0.0))

    log_event(f"[REFLEX MESH] ✅ Winner: {winner['reflex_name']} | Score={winner['fusion_score']:.4f}")
    return winner