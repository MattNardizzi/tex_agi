# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/meta_memory_tracker.py
# Tier ΩΩΩΩΩΩΩΩ — Memory-of-Memory Engine (Final Form)
# Purpose: Tracks priority, frequency, usefulness, and LTM status of beliefs; rewrites memory evolution
# ============================================================

from quantum_layer.memory_core.long_term_memory_bridge import LongTermMemoryBridge
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from utils.logging_utils import log
from datetime import datetime
import json
import os

class MetaMemoryTracker:
    def __init__(self, db_path="meta_memory_log.json"):
        self.db_path = db_path
        self.memory_stats = self._load()
        self.ltm = LongTermMemoryBridge()
        self.module_tag = "meta_memory_tracker"

    def _load(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(self.db_path, "w") as f:
            json.dump(self.memory_stats, f, indent=2)

    def update_retrieval(self, belief_id: str, success: bool = True, urgency: float = 0.5):
        now = datetime.utcnow().isoformat()
        stats = self.memory_stats.get(belief_id, {
            "retrieval_count": 0,
            "last_retrieved": now,
            "success_count": 0,
            "failure_count": 0,
            "urgency_avg": urgency
        })

        stats["retrieval_count"] += 1
        stats["last_retrieved"] = now
        stats["urgency_avg"] = round((stats["urgency_avg"] + urgency) / 2, 4)

        if success:
            stats["success_count"] += 1
        else:
            stats["failure_count"] += 1

        # Compute priority score
        score = (
            stats["success_count"] * 1.2 -
            stats["failure_count"] * 1.0 +
            stats["urgency_avg"] * 0.8
        )
        stats["priority_score"] = round(score, 4)

        self.memory_stats[belief_id] = stats
        self._save()

        # Push updates to LTM
        try:
            self.ltm.update_point(point_id=belief_id, updates={
                "retrieval_count": stats["retrieval_count"],
                "priority_score": stats["priority_score"],
                "urgency_avg": stats["urgency_avg"]
            })
        except Exception as e:
            log.warning(f"[{self.module_tag}] ❌ LTM update failed for {belief_id}: {e}")

        # Imprint belief for reflex awareness
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Belief {belief_id} used (success={success})",
            source=self.module_tag,
            emotion="reflective",
            tags=["meta", "retrieval"]
        )

        log.info(f"[{self.module_tag}] 📈 Updated: {belief_id} → priority={stats['priority_score']}")

    def get_stats(self, belief_id: str):
        return self.memory_stats.get(belief_id, {
            "retrieval_count": 0,
            "last_retrieved": "never",
            "success_count": 0,
            "failure_count": 0,
            "priority_score": 0.0,
            "urgency_avg": 0.5
        })

    def get_top_memories(self, sort_by="priority_score", top_k=5):
        sorted_items = sorted(
            self.memory_stats.items(),
            key=lambda x: x[1].get(sort_by, 0),
            reverse=True
        )
        return sorted_items[:top_k]

    def decay_low_priority(self, min_score=0.5, max_age_days=14):
        now = datetime.utcnow()
        removed = []

        for belief_id, stats in list(self.memory_stats.items()):
            try:
                last = datetime.fromisoformat(stats.get("last_retrieved", now.isoformat()))
                days_old = (now - last).days
                if stats.get("priority_score", 0) < min_score and days_old > max_age_days:
                    removed.append(belief_id)
                    del self.memory_stats[belief_id]
            except Exception:
                continue

        self._save()

        if removed:
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Pruned {len(removed)} low-priority beliefs.",
                source=self.module_tag,
                emotion="clean",
                tags=["meta", "prune"]
            )

        return removed

# === Singleton Interface
_meta_memory = MetaMemoryTracker()

def track_memory_use(belief_id: str, success: bool = True, urgency: float = 0.5):
    _meta_memory.update_retrieval(belief_id, success, urgency)

def get_meta_stats(belief_id: str):
    return _meta_memory.get_stats(belief_id)

def prune_stale_memories():
    return _meta_memory.decay_low_priority()