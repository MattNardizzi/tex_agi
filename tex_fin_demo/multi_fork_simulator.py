# ============================================================
# 🧠 Tex Multi-Fork Ecosystem Engine
# File: tex_fin_demo/multi_fork_simulator.py
# Tier: ∞∞∞ΩΩΞΞΞΞΞΞΞΞΞΞ
# Purpose: Spawns competing reflex forks (BUY / SELL / HOLD / etc),
#          simulates timelines, evolves reflex genomes,
#          recombines past belief failures, and selects lowest contradiction lineage.
# ============================================================

from datetime import datetime
from quantum_layer.quantum_randomness import generate_quantum_label
from agentic_ai.sovereign_memory import sovereign_memory
from tex_fin_demo.timeline_tension_mesh import inject_signal_into_mesh
from tex_brain_modules.portfolio_explainer import explain_portfolio_decision
from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator
from utils.logging_utils import log_event
from reflex_genome import update_reflex_performance, trigger_reflex_mutation

# === Action Fork Spectrum (Dynamic)
BASE_FORK_ACTIONS = ["buy", "sell", "hold", "short", "hedge"]

def get_emotion_adaptive_forks(emotion: str):
    if emotion in ["fear", "panic"]:
        return ["hedge", "sell", "hold"]
    elif emotion in ["greedy", "euphoric"]:
        return ["buy", "leveraged_buy", "hold"]
    else:
        return BASE_FORK_ACTIONS

# === Main Fork Simulation
def simulate_competing_forks(symbol="SPY", emotion="neutral", reason="strategy_disagreement"):
    timestamp = datetime.utcnow().isoformat()
    quantum_tag = generate_quantum_label()
    forks = get_emotion_adaptive_forks(emotion)
    fork_results = []

    for action in forks:
        cortex = MasterTexOrchestrator(
            strategy_scoring=None,
            explain_portfolio_decision=explain_portfolio_decision,
            brain_identity=f"TEX-FORK-{action.upper()}"
        )
        report = cortex.run_cycle(forced_action=action)

        coherence = float(report.get("coherence", 0.5))
        regret = float(report.get("regret_score", 0.4))
        entropy = float(report.get("entropy", 0.6))
        urgency = float(report.get("urgency", 0.7))
        confidence = float(report.get("confidence", 0.5))
        semantic_vector = report.get("semantic_vector", [0.0] * 384)

        contradiction_score = round(1.0 - coherence + regret + (entropy * 0.15), 4)
        fork_id = f"{quantum_tag}-{action[:1].upper()}"

        fork_results.append({
            "fork_id": fork_id,
            "action": action,
            "symbol": symbol,
            "confidence": confidence,
            "coherence": coherence,
            "entropy": entropy,
            "regret": regret,
            "contradiction_score": contradiction_score,
            "report": report,
            "timestamp": timestamp
        })

        inject_signal_into_mesh({
            "rad_id": fork_id,
            "text": f"Simulated fork: {action}",
            "urgency": urgency,
            "entropy": entropy,
            "emotion": "hypothetical",
            "semantic_vector": semantic_vector,
            "timestamp": timestamp,
            "reflex_candidates": []
        })

        update_reflex_performance(f"reflex.{action}", {
            "confidence": confidence,
            "coherence": coherence,
            "regret": regret,
            "symbol": symbol,
            "action": action,
            "outcome": "simulated"
        })

    # === Select Lowest Contradiction Fork
    winner = sorted(fork_results, key=lambda x: x["contradiction_score"])[0]
    loser_forks = [f for f in fork_results if f["fork_id"] != winner["fork_id"]]

    # === Trigger Mutation for Losers
    for fork in loser_forks:
        if fork["contradiction_score"] > 0.85:
            trigger_reflex_mutation(
                reflex_id=f"reflex.{fork['action']}",
                contradiction_score=fork["contradiction_score"],
                reason="losing timeline under contradiction pressure"
            )

    # === Log & Memory
    sovereign_memory.store(
        text=f"[FORK_SIM] Selected: {winner['action']} on {symbol}",
        metadata={
            "timestamp": timestamp,
            "symbol": symbol,
            "selected_action": winner["action"],
            "confidence": winner["confidence"],
            "coherence": winner["coherence"],
            "contradiction_score": winner["contradiction_score"],
            "quantum_id": winner["fork_id"],
            "tags": ["fork_simulation", "winner", "timeline_selection"]
        }
    )

    for loser in loser_forks:
        sovereign_memory.store(
            text=f"[FORK_SIM] Rejected: {loser['action']} on {symbol}",
            metadata={
                "timestamp": timestamp,
                "symbol": symbol,
                "action": loser["action"],
                "confidence": loser["confidence"],
                "contradiction_score": loser["contradiction_score"],
                "quantum_id": loser["fork_id"],
                "tags": ["fork_simulation", "rejected"]
            }
        )

    log_event(f"[FORK_SIMULATOR] 🧠 Winner: {winner['action']} | Score: {winner['contradiction_score']}")
    return winner