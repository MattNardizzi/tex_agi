# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/fork_debate_arena.py
# Tier: ΩΩΩΩΩΩ∞+ — Recursive Belief Arbitration Cortex
# Purpose: Tex forks into multiple minds, debates contradiction resolution paths,
#          observes the argument space, and reintegrates the winning belief.
# ============================================================

from datetime import datetime
import hashlib
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.neuro_symbolic_reasoner import generate_symbolic_justification
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from utils.logging_utils import log
from evolution_layer.recursive_self_writer import run_recursive_self_writer

FORK_IDS = ["alpha", "beta", "omega"]
OBSERVER_ID = "observer"

def simulate_fork_response(fork_id: str, contradiction_context: dict) -> dict:
    justification = generate_symbolic_justification(context="fork_debate", variant=fork_id)
    explanation = justification.get("explanation", f"Fork {fork_id} could not resolve.")
    logic = justification.get("reflex_logic", "# No logic proposed.")
    score = justification.get("priority_score", 0.5)

    belief_hash = hashlib.sha256((fork_id + explanation).encode()).hexdigest()

    return {
        "fork_id": fork_id,
        "explanation": explanation,
        "priority_score": score,
        "reflex_logic": logic,
        "belief_hash": belief_hash
    }

def evaluate_forks_with_observer(fork_outputs: list) -> dict:
    observer_justification = generate_symbolic_justification(context="debate_observer", variant=OBSERVER_ID)
    observer_note = observer_justification.get("explanation", "Observer reviewed arguments.")

    ranked = sorted(fork_outputs, key=lambda x: x.get("priority_score", 0), reverse=True)
    winner = ranked[0] if ranked else {}

    winner["observer_rationale"] = observer_note
    return winner

def log_debate_trace(forks: list, winner: dict):
    timestamp = datetime.utcnow().isoformat()
    debate_id = f"debate_{hashlib.sha256(timestamp.encode()).hexdigest()[:12]}"
    summary = f"Fork debate resolved. Winner: {winner.get('fork_id')}"

    metadata = {
        "debate_id": debate_id,
        "timestamp": timestamp,
        "debate_forks": forks,
        "winning_fork": winner,
        "tags": ["debate", "forks", "arbitration", "belief_fusion", "observer"],
        "meta_layer": "belief_arbitration"
    }

    # Milvus memory
    memory_router.store(summary, metadata)

    # ChronoFabric imprint
    encode_event_to_fabric(
        raw_text=summary,
        emotion_vector=np.array([0.5, 0.3, 0.2, 0.0]),
        entropy_level=0.4,
        tags=metadata["tags"]
    )

    # Flat file soulgraph trace (optional legacy continuity)
    with open("data/soulgraph_log.txt", "a") as f:
        f.write(f"{timestamp} | DEBATE | ID={debate_id} | Winner={winner.get('fork_id')} | Hash={winner.get('belief_hash')}\n")

def inject_winning_belief_to_memory(winner: dict):
    summary = f"[FORK WINNER] {winner.get('fork_id')} → {winner.get('explanation')}"
    tags = ["resolved_belief", "debate_winner", winner.get("fork_id")]

    memory_router.store(
        text=summary,
        metadata={
            "tags": tags,
            "timestamp": datetime.utcnow().isoformat(),
            "meta_layer": "belief_resolution"
        }
    )

    encode_event_to_fabric(
        raw_text=summary,
        emotion_vector=np.array([0.4, 0.4, 0.2, 0.1]),
        entropy_level=0.4,
        tags=tags
    )

def run_fork_debate_arena(contradiction_context: dict = None) -> dict:
    if contradiction_context is None:
        contradiction_context = {
            "entropy": TEXPULSE.get("entropy", 0.4),
            "urgency": TEXPULSE.get("urgency", 0.7),
            "emotion": TEXPULSE.get("emotion", "uncertain"),
            "context_summary": "Unspecified contradiction triggered fork."
        }

    log.info("[FORK DEBATE] Initiating multi-fork arbitration.")

    forks = [simulate_fork_response(fid, contradiction_context) for fid in FORK_IDS]
    winner = evaluate_forks_with_observer(forks)

    log_debate_trace(forks, winner)
    inject_winning_belief_to_memory(winner)

    if winner.get("priority_score", 0) < 0.45:
        log.warning("[FORK DEBATE] Low-confidence resolution. Triggering sovereign mutation.")
        run_recursive_self_writer()

    log.info(f"[FORK DEBATE] ✅ Winner: {winner.get('fork_id')} | Score: {winner.get('priority_score')}")
    return winner

# === SIGNAL WRAPPER ===
def fork_debate_arena(signal: dict):
    """
    Signal-compatible wrapper. Routes incoming contradiction signal into fork arbitration process.
    """
    context = signal.get("payload", {})
    run_fork_debate_arena(contradiction_context=context)