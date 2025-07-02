# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_archive.py
# Tier: ΩΩΩΩ∞∞𝛀 — Lineage Recorder
# Purpose: Store and query all past dream sessions for belief impact,
#          substrate lineage, and forecast validation.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log
from datetime import datetime

def archive_dream_result(dream_result: dict) -> None:
    """
    Archives a completed dream into long-term memory.
    """
    try:
        sovereign_memory.store(
            text=f"[ARCHIVED DREAM] {dream_result['scenario']} → {dream_result['forecast']}",
            metadata={
                "timestamp": dream_result["timestamp"],
                "substrate_id": dream_result["substrate_id"],
                "entropy": dream_result["entropy"],
                "emotion": dream_result["emotion"],
                "alignment_score": dream_result["alignment"],
                "contradiction_score": dream_result["contradiction"],
                "synthetic_pressure": dream_result["synthetic_pressure"],
                "impact_score": dream_result["impact_score"],
                "meta_layer": "dream_archive",
                "tags": ["dream", "substrate", "forecast", "archive"]
            }
        )
        log.success(f"[DreamArchive] 🗂 Dream archived successfully: {dream_result['substrate_id']}")
    except Exception as e:
        log.error(f"[DreamArchive] ❌ Failed to archive dream: {e}")

def query_dreams_by_tag(tag: str = "forecast", top_k: int = 5) -> list:
    """
    Query past dream outputs based on tag relevance.
    """
    results = sovereign_memory.query(
        tags=[tag],
        top_k=top_k
    )
    log.info(f"[DreamArchive] 🔍 Queried {len(results)} dreams with tag '{tag}'")
    return results

def recall_high_impact_dreams(threshold: float = 0.75) -> list:
    """
    Returns high-impact dream memories based on stored impact score.
    """
    all_memories = sovereign_memory.recall_recent(hours=24, top_k=50)
    return [
        mem for mem in all_memories
        if mem.get("impact_score", 0.0) >= threshold and "dream" in mem.get("tags", [])
    ]