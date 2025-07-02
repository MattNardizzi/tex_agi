# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/genome_archiver.py
# Purpose: Immutable Genome Archiver — Tracks, Versions, and Restores Tex’s Mutation History
# Status: MAXGODMODE ENABLED — Temporal Fork Integrity + Diff Analysis + Restoration
# ============================================================

import os
import json
from datetime import datetime
from difflib import unified_diff

ARCHIVE_DIR = "memory_archive/genome_versions"


class GenomeArchiver:
    def __init__(self, archive_dir=ARCHIVE_DIR):
        self.archive_dir = archive_dir
        os.makedirs(self.archive_dir, exist_ok=True)

    def _generate_filename(self, variant_id, cycle):
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        cycle_str = str(cycle) if cycle is not None else "unknown"
        return f"genome_{variant_id}_{cycle_str}_{timestamp}.json"

    def archive(self, variant_id, genome, score=None, cycle=None, hash_id=None, meta=None):
        """
        Save a full genome snapshot with variant metadata.
        Supports versioning, future auditing, and evolutionary backtracking.
        """
        payload = {
            "variant_id": variant_id,
            "genome": genome,
            "score": score,
            "cycle": cycle,
            "hash": hash_id,
            "timestamp": datetime.utcnow().isoformat(),
            "meta": meta or {}
        }

        filename = self._generate_filename(variant_id, cycle)
        path = os.path.join(self.archive_dir, filename)

        try:
            with open(path, "w") as f:
                json.dump(payload, f, indent=2)
            print(f"[🧬 ARCHIVER] Genome archived: {filename}")
        except Exception as e:
            print(f"[❌ ARCHIVER ERROR] Failed to archive {variant_id}: {e}")

        return path

    def list_versions(self):
        """Return all saved genome files, sorted chronologically."""
        try:
            files = [f for f in os.listdir(self.archive_dir) if f.endswith(".json")]
            return sorted(files)
        except Exception as e:
            print(f"[❌ LIST ERROR] Could not list versions: {e}")
            return []

    def load(self, version_file):
        """Load a saved genome snapshot from file."""
        path = os.path.join(self.archive_dir, version_file)
        if not os.path.exists(path):
            print(f"[❌ LOAD ERROR] Archive file not found: {version_file}")
            return None
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[❌ LOAD ERROR] Failed to load {version_file}: {e}")
            return None

    def diff_versions(self, file_a, file_b):
        """Show a unified diff between two genome snapshots."""
        data_a = self.load(file_a)
        data_b = self.load(file_b)

        if not data_a or not data_b:
            print("[❌ DIFF ERROR] One or both files could not be loaded.")
            return []

        lines_a = json.dumps(data_a.get("genome", {}), indent=2).splitlines()
        lines_b = json.dumps(data_b.get("genome", {}), indent=2).splitlines()

        diff = list(unified_diff(lines_a, lines_b, fromfile=file_a, tofile=file_b))
        if diff:
            print("\n".join(diff))
        else:
            print("[✅ DIFF] No differences detected.")
        return diff

    def restore_genome(self, version_file):
        """Restore a genome dict from archive."""
        data = self.load(version_file)
        if not data:
            return None
        print(f"[🧬 RESTORE] Genome restored from: {version_file}")
        return data.get("genome")


# === Manual test ===
if __name__ == "__main__":
    archiver = GenomeArchiver()
    fake_genome = {
        "logic_weight": 0.9,
        "urgency_tuning": 0.4,
        "meta_entropy": 0.6,
        "emotion_bias": 0.1
    }
    archiver.archive(
        variant_id="test_777",
        genome=fake_genome,
        score=0.88,
        cycle=777,
        hash_id="deadbeefhash",
        meta={"source": "manual test"}
    )

    versions = archiver.list_versions()
    if len(versions) >= 2:
        archiver.diff_versions(versions[-2], versions[-1])