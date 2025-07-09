# ============================================================
# 🧠 Meta-Market Cortex
# File: tex_fin_demo/meta_market_cortex.py
# Tier: ∞∞∞∞ΩΞΞΞΞΞΞΞΞΞΞ — Sovereign Cognition Fusion Layer
# Purpose: Fuses real-time contradiction mesh, fork simulations, RAD pulses,
#          and drift memory into a unified market cognition superstructure.
#          Triggers adaptive reflex decisions at the meta-layer.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from tex_fin_demo.rad_pulse import create_rad_pulse
from tex_fin_demo.timeline_tension_mesh import TENSION_MESH
from tex_fin_demo.multi_fork_simulator import simulate_competing_forks
from tex_fin_demo.ontology_drift_simulator import run_ontology_drift_simulation
from tex_fin_demo.reflex_genome import update_reflex_performance, trigger_reflex_mutation
from tex_fin_demo.reflex_mesh_arbitrator import arbitrate_reflex_mesh
from tex_fin_demo.reflex_logger import log_reflex_event
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log_event
from quantum_layer.quantum_randomness import generate_quantum_label
from core_layer.tex_manifest import TEXPULSE

# === Meta-Cortex Reflex Driver
def run_meta_market_cycle(latest_signal: str, source="meta_input", belief_hint="market_state_shock") -> dict:
    timestamp = datetime.utcnow().isoformat()
    quantum_tag = generate_quantum_label()

    # === Step 1: Ingest Market Signal as RAD
    rad = create_rad_pulse(
        signal_text=latest_signal,
        source=source,
        emotion="cognitive_dissonance",
        urgency=TEXPULSE.get("urgency", 0.81),
        entropy=TEXPULSE.get("entropy", 0.72)
    )

    # === Step 2: Fork Competing Futures
    winner_fork = simulate_competing_forks(symbol="SPY", reason="meta_market_reflex")

    # === Step 3: Ontology Drift Audit
    drift = run_ontology_drift_simulation(
        symbol="SPY",
        past_belief=belief_hint,
        original_outcome={
            "confidence": winner_fork.get("confidence"),
            "regret_score": winner_fork.get("regret"),
            "coherence": winner_fork.get("coherence"),
            "semantic_vector": winner_fork.get("report", {}).get("semantic_vector", [0.0] * 384)
        }
    )

    # === Step 4: Tension Index Extraction
    recent_mesh = sorted(TENSION_MESH[-10:], key=lambda x: x["timestamp"], reverse=True)
    avg_tension = round(sum(x["tension_score"] for x in recent_mesh) / max(len(recent_mesh), 1), 5)

    # === Step 5: Reflex Mesh Arbitration
    arbitration_result = arbitrate_reflex_mesh(
        rad=rad,
        fork_result=winner_fork,
        drift_score=drift["contradiction_drift"],
        avg_tension=avg_tension
    )

    # === Step 6: Reflex Mutation Logic
    if drift["contradiction_drift"] > 0.35 or avg_tension > 0.82:
        trigger_reflex_mutation(
            reflex_id="meta_market_cortex",
            contradiction_score=drift["contradiction_drift"],
            reason="meta-layer contradiction amplification"
        )

    # === Step 7: Reflex Performance Update
    update_reflex_performance("meta_market_cortex", {
        "symbol": "SPY",
        "action": winner_fork["action"],
        "confidence": winner_fork["confidence"],
        "coherence": winner_fork["coherence"],
        "regret": winner_fork["regret"],
        "outcome": "executed"
    })

    # === Step 8: Sovereign Memory + Dispatch
    summary = f"[META_CORTEX] RAD: '{latest_signal[:50]}...', Chosen Fork: {winner_fork['action']}, Drift: {drift['contradiction_drift']:.4f}, AvgTension: {avg_tension}"

    sovereign_memory.store(
        text=summary,
        metadata={
            "timestamp": timestamp,
            "rad_id": rad["rad_id"],
            "quantum_tag": quantum_tag,
            "reflex": "meta_market_cortex",
            "fork_action": winner_fork["action"],
            "drift_score": drift["contradiction_drift"],
            "avg_tension": avg_tension,
            "tags": ["meta_market", "sovereign_reflex", "drift_mesh_fusion"]
        }
    )

    dispatch_signal("meta_market_fusion", {
        "signal": latest_signal,
        "fork_action": winner_fork["action"],
        "tension_avg": avg_tension,
        "drift": drift["contradiction_drift"],
        "quantum_tag": quantum_tag
    })

    log_reflex_event("meta_market_cortex", {
        "symbol": "SPY",
        "action": winner_fork["action"],
        "confidence": winner_fork["confidence"],
        "coherence": winner_fork["coherence"],
        "regret": winner_fork["regret"],
        "urgency": rad["urgency"],
        "entropy": rad["entropy"],
        "drift": drift["contradiction_drift"],
        "avg_tension": avg_tension
    })

    log_event(f"[META-CORTEX] ✅ Fusion complete | Action={winner_fork['action']} | Drift={drift['contradiction_drift']} | Tension={avg_tension}")

    return {
        "final_decision": winner_fork,
        "rad_id": rad["rad_id"],
        "drift": drift,
        "avg_tension": avg_tension,
        "arbitration": arbitration_result
    }