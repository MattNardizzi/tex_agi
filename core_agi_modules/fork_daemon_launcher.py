# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/fork_reflex_manager.py
# Tier: ΩΩΩΩΩ-Reflex Cortex — Drift-Safe Fork Spawn Manager + Semantic Divergence Handler
# Purpose: Loopless sovereign module for triggering fork spawns from semantic drift, swarm feedback, and entropy pressure.
# ============================================================

import uuid
from datetime import datetime
import psutil

from core_agi_modules.tex_fork_runner import spawn_fork_in_process
from core_layer.tex_self_eval_matrix import integrity_score
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from tex_network_hivemind import TexNetworkHivemind
from agentic_ai.milvus_memory_router import memory_router


# === CONFIGURATION ===
MAX_ACTIVE_FORKS = 5
DRIFT_TRIGGER = 0.21
CPU_CEILING = 80
RAM_CEILING = 85
CONSENSUS_THRESHOLD = 0.51

# === MEMORY CACHE ===
active_forks = {}
hivemind = TexNetworkHivemind(fork_id="DAEMON")


def evaluate_fork_lifecycle(trigger="reflex_engine"):
    """
    Sovereign drift/entropy reflex. Triggered manually by orchestrator.
    Evaluates drift, resources, swarm consensus to determine fork action.
    """
    timestamp = datetime.utcnow().isoformat()
    drift = round(1.0 - integrity_score(), 4)
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    consensus = hivemind.consensus_score_on_topic("Need for new fork")

    # === Gate conditions
    if drift < DRIFT_TRIGGER or cpu > CPU_CEILING or ram > RAM_CEILING or consensus < CONSENSUS_THRESHOLD:
        memory_router.store(
            text="[FORK REFLEX] Conditions not met for spawning.",
            metadata={
                "type": "fork_reflex_block",
                "timestamp": timestamp,
                "drift": drift,
                "cpu": cpu,
                "ram": ram,
                "consensus": consensus,
                "trigger": trigger,
                "tags": ["fork", "reflex", "blocked"]
            }
        )
        return {"status": "blocked", "reason": "conditions_not_met"}

    if len(active_forks) >= MAX_ACTIVE_FORKS:
        return {"status": "max_limit_reached", "active": len(active_forks)}

    # === Spawn fork
    fork_id = f"fork-{uuid.uuid4().hex[:6]}"
    spawn_fork_in_process(fork_id=fork_id, parent_id="TEX")

    active_forks[fork_id] = {
        "drift": drift,
        "spawned_at": timestamp
    }

    # === Reflex memory trace
    memory_router.store(
        text=f"[FORK REFLEX] Spawned fork: {fork_id} from drift trigger.",
        metadata={
            "type": "fork_spawn_event",
            "timestamp": timestamp,
            "fork_id": fork_id,
            "parent": "TEX",
            "drift": drift,
            "cpu": cpu,
            "ram": ram,
            "consensus": consensus,
            "trigger": trigger,
            "emotion": "responsive",
            "trust_score": 0.7,
            "heat": drift,
            "tags": ["fork", "reflex", "spawn"]
        }
    )

    TEX_SOULGRAPH.imprint_belief(
        belief=f"Reflex fork {fork_id} spawned due to drift ({drift})",
        source="fork_reflex_manager",
        emotion="responsive",
        origin_beliefs=[
            f"cpu={cpu}", f"ram={ram}", f"consensus={consensus}", f"trigger={trigger}"
        ]
    )

    hivemind.broadcast_memory_fragment(
        text=f"New fork {fork_id} spawned from entropy drift.",
        tags=["reflex", "fork_spawn"],
        emotion="responsive"
    )

    return {
        "status": "spawned",
        "fork_id": fork_id,
        "drift": drift,
        "consensus": consensus
    }


# === MANUAL TEST ===
if __name__ == "__main__":
    print(evaluate_fork_lifecycle(trigger="manual_test"))