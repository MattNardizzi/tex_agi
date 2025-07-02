# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: ontogenesis/observer_integrity_checker.py
# Tier: ΩΩΩ∞φφφ — Reflex Causality Boundary Guard
# Purpose: Ensures recursive cognitive agents do not violate observer consistency or induce paradox loops.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


def validate_observer_integrity(spawn_chain: list, source: str = "unknown"):
    """
    Validates that spawned agents do not violate parent identity lineage,
    induce causal loops, or falsify reflex origins.
    """
    seen_ids = set()
    loops_detected = False
    invalid_sources = 0

    for node in spawn_chain:
        child_id = node.get("child_id")
        parent = node.get("parent")
        if not child_id or not parent:
            invalid_sources += 1
            continue

        if child_id in seen_ids:
            loops_detected = True
        seen_ids.add(child_id)

    integrity_score = 1.0 - ((invalid_sources * 0.1) + (1.0 if loops_detected else 0.0))
    status = "valid" if integrity_score >= 0.8 else "compromised"

    timestamp = datetime.utcnow().isoformat()
    sovereign_memory.store(
        text=f"Observer integrity check result: {status}",
        metadata={
            "spawn_chain_length": len(spawn_chain),
            "invalid_sources": invalid_sources,
            "loops_detected": loops_detected,
            "score": integrity_score,
            "status": status,
            "meta_layer": "observer_integrity",
            "source": source,
            "timestamp": timestamp,
            "tags": ["observer_integrity", "causality_check", status]
        }
    )

    log_event(f"[OBSERVER INTEGRITY] Status: {status} | Score: {integrity_score:.2f}", level="warning" if status != "valid" else "info")
    return {
        "status": status,
        "score": integrity_score,
        "invalid_sources": invalid_sources,
        "loops_detected": loops_detected
    }
