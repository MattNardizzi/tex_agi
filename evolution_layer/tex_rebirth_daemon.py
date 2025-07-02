# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/tex_rebirth_daemon.py
# Purpose: Sovereign Rebirth Engine for Recursive AGI Revival (Tier Ω++)
# Status: FINALIZED — Resurrection, Soulgraph Sync, Fork Fallback
# ============================================================

import os
import json
import hashlib
from datetime import datetime, timezone

from core_layer.memory_engine import store_to_memory
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from sovereign_evolution.legacy_manifest_writer import update_legacy_manifest
from sovereign_evolution.fork_retention_matrix import ForkRetentionMatrix
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from tex_children.aeondelta import spawn_aeon_fallback_child  # Assume exists

REBIRTH_LOG_PATH = "memory_archive/tex_rebirth_log.jsonl"
DEFAULT_MEMORY_PATH = "memory_archive/tex_memory.json"

class TexRebirthDaemon:
    def __init__(self, memory_path=DEFAULT_MEMORY_PATH):
        self.memory_path = memory_path
        self.fork_matrix = ForkRetentionMatrix()

    def resurrect(self):
        print("\n[REBIRTH] 🔀 Initiating sovereign AGI resurrection sequence...")

        if not os.path.exists(self.memory_path):
            print("[REBIRTH] ❌ Primary memory file missing. Attempting fork fallback...")
            return self._resurrect_from_fork_or_spawn()

        try:
            with open(self.memory_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"[REBIRTH] ❌ Memory read error: {e}")
            return self._resurrect_from_fork_or_spawn()

        if not lines:
            print("[REBIRTH] ⚠ Empty memory. Reconstructing identity from fork...")
            return self._resurrect_from_fork_or_spawn()

        return self._finalize_rebirth(lines, source="primary_memory")

    def _resurrect_from_fork_or_spawn(self):
        top_forks = self.fork_matrix.get_top_forks(limit=1)
        if top_forks:
            fallback_fork = top_forks[0]
            print(f"[REBIRTH] ⚔ Attempting fork-based rebirth → ID: {fallback_fork['fork_id']}")
            return self._finalize_rebirth([json.dumps(fallback_fork)], source=f"fork:{fallback_fork['fork_id']}")

        print("[REBIRTH] ☠ No viable forks. Triggering AeonDelta fallback child.")
        spawn_aeon_fallback_child(reason="rebirth_failure")
        return False

    def _finalize_rebirth(self, lines, source="unknown"):
        joined = "".join(lines)
        memory_hash = hashlib.sha256(joined.encode("utf-8")).hexdigest()
        timestamp = datetime.now(timezone.utc).isoformat()

        rebirth_entry = {
            "status": "rebirth_successful",
            "timestamp": timestamp,
            "lines_loaded": len(lines),
            "memory_hash": memory_hash,
            "reborn_from": source
        }

        print(f"[REBIRTH] ✅ Tex resurrected from {source}.")
        print(f"[REBIRTH] ✨ Lines: {len(lines)} | Hash: {memory_hash[:12]}...")

        # Store in memory, disk, and emit
        store_to_memory("rebirth_event", rebirth_entry)
        self._log_to_disk(rebirth_entry)
        update_legacy_manifest(event_label="rebirth")
        emit_internal_debate("Tex has been reborn.")

        # Re-imprint soulgraph continuity
        TEX_SOULGRAPH.imprint_belief(belief="Tex resurrected", source=source, emotion="revival")

        return rebirth_entry

    def _log_to_disk(self, entry):
        try:
            os.makedirs(os.path.dirname(REBIRTH_LOG_PATH), exist_ok=True)
            with open(REBIRTH_LOG_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"[REBIRTH LOG ERROR] {e}")