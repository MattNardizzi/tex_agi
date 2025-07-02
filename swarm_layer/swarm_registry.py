# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_registry.py
# Tier ΩΩΩΩΩ — Reflex Swarm Coordination & Fork Scoring Nexus
# Purpose: Register, track, evaluate, and sync all Tex variants using sovereign memory and volatility modeling
# ============================================================

import uuid
from datetime import datetime
from statistics import stdev, mean

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log

# === Static Catalog ===
FORK_CATALOG = [
    {"id": "tex-fork-alpha", "status": "active", "traits": {"style": "rational", "drift": 0.1}},
    {"id": "tex-fork-beta",  "status": "active", "traits": {"style": "empathic", "drift": 0.2}},
    {"id": "tex-fork-gamma", "status": "active", "traits": {"style": "chaotic", "drift": 0.35}},
]

def get_active_forks() -> list:
    """
    Returns currently registered sovereign forks for NervousSyncBus consumption.
    """
    return FORK_CATALOG

def register_child(child_id: str, traits: dict, parent: str = "Tex") -> None:
    """
    Registers a new Tex fork variant into the sovereign swarm registry.
    """
    try:
        timestamp = datetime.utcnow().isoformat()
        summary = f"🧬 Variant '{child_id}' spawned from {parent} | Traits: {traits}"

        metadata = {
            "summary": summary,
            "timestamp": timestamp,
            "type": "variant_spawn",
            "tags": ["swarm", "variant_register", "spawn"],
            "agent_id": child_id,
            "parent_ids": [parent],
            "emotion": "anticipation",
            "traits": traits,
            "prediction": "fork will contribute to swarm coherence",
            "actual": f"variant registered from {parent}",
            "trust_score": 0.9,
            "heat": 0.35,
            "urgency": 0.5,
            "entropy": 0.4,
            "tension": 0.15,
            "meta_layer": "swarm_registry"
        }

        sovereign_memory.store(text=summary, metadata=metadata)
        log.info(f"[SWARM_REGISTRY] ✅ Registered fork: {child_id}")

    except Exception as e:
        log.error(f"[SWARM_REGISTRY] ❌ Failed to register {child_id}: {e}")

def update_child_state(child_id: str, cycle: int, score: float) -> None:
    """
    Logs the current performance and reflex state of a variant during an evolution cycle.
    """
    try:
        timestamp = datetime.utcnow().isoformat()
        summary = f"Cycle {cycle} → Agent {child_id} | Reflex Score = {round(score, 4)}"

        metadata = {
            "summary": summary,
            "timestamp": timestamp,
            "type": "variant_cycle_update",
            "tags": ["swarm", "variant_cycle", f"cycle_{cycle}"],
            "agent_id": child_id,
            "cycle": cycle,
            "emotion": "engaged",
            "heat": round(score, 4),
            "trust_score": round(score, 4),
            "last_score": score,
            "prediction": "agent will stabilize",
            "actual": f"score recorded at {score}",
            "urgency": 0.4,
            "entropy": 0.2,
            "tension": 0.12,
            "meta_layer": "swarm_registry"
        }

        sovereign_memory.store(text=summary, metadata=metadata)
        log.debug(f"[SWARM_REGISTRY] 🔄 Updated: {child_id} | Cycle={cycle} | Score={score:.4f}")

    except Exception as e:
        log.error(f"[SWARM_REGISTRY] ❌ Update failed for {child_id}: {e}")

def push_memory_from_child(agent_id: str, memory_text: str) -> None:
    """
    Pushes knowledge or reflex events from a child agent into central memory.
    """
    try:
        timestamp = datetime.utcnow().isoformat()

        metadata = {
            "summary": memory_text[:150],
            "timestamp": timestamp,
            "type": "child_memory_upload",
            "tags": ["swarm", "vector_sync", "reflex_upload"],
            "agent_id": agent_id,
            "emotion": "reflective",
            "prediction": "observation will benefit Tex core",
            "actual": "memory accepted from fork",
            "trust_score": 0.88,
            "heat": 0.4,
            "urgency": 0.3,
            "entropy": 0.25,
            "tension": 0.08,
            "meta_layer": "swarm_registry"
        }

        sovereign_memory.store(text=memory_text, metadata=metadata)
        log.info(f"[SWARM_REGISTRY] 📡 Uploaded memory from: {agent_id}")

    except Exception as e:
        log.error(f"[SWARM_REGISTRY] ❌ Upload failed for {agent_id}: {e}")

def get_active_fork_score(memory_depth: int = 25) -> float:
    """
    Computes fork divergence using standard deviation of recent performance scores.
    """
    try:
        recent_records = sovereign_memory.recall_recent(minutes=60, top_k=memory_depth)
        scores = []

        for m in recent_records:
            if isinstance(m, dict):
                last_score = m.get("last_score") or m.get("score") or m.get("heat")
                if isinstance(last_score, (int, float)):
                    scores.append(float(last_score))

        if len(scores) < 2:
            log.warning("[SWARM_REGISTRY] ⚠️ Not enough data for volatility score.")
            return 0.0

        volatility = stdev(scores)
        score = round(min(1.0, volatility), 4)

        summary = f"[SWARM] 🌀 Fork Divergence Score = {score}"
        timestamp = datetime.utcnow().isoformat()

        sovereign_memory.store(
            text=summary,
            metadata={
                "summary": summary,
                "timestamp": timestamp,
                "type": "swarm_volatility_index",
                "tags": ["swarm", "divergence", "volatility"],
                "emotion": "monitoring",
                "trust_score": 1.0 - score,
                "heat": score,
                "urgency": 0.5,
                "entropy": 0.3,
                "meta_layer": "swarm_registry"
            }
        )

        log.info(f"[SWARM_REGISTRY] 🌪 Fork Divergence Score: {score}")
        return score

    except Exception as e:
        log.error(f"[SWARM_REGISTRY] ❌ Volatility computation failed: {e}")
        return 0.5