# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_agi_modules/autofix_intent_migrator.py
# Tier: ΩΩΩ+++ Autonomous Intent Refactor Cortex — Symbolic, Loopless, Meta-Ready
# ============================================================

import os
import re
import shutil
import traceback
from datetime import datetime

from agentic_ai.milvus_memory_router import memory_router
from core_agi_modules.intent_object import IntentObject
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === CONFIGURATION ===
INTENT_PATTERNS = [
    r"\.lower\(\)",                                  # Deprecated case normalization
    r"\binput\s*\[\s*['\"]intent['\"]\s*\]",         # Direct dict access
    r"if\s+[^\n]+intent[^\n]+:",                     # Unsafe conditional pattern
]

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TARGET_EXT = ".py"

class IntentMigrator:
    def __init__(self):
        self.matches = []
        self.rewritten_files = []
        self.diffs = {}
        self.intent = IntentObject("autofix_intent_scan", source="autofix_intent_migrator")
        self.intent.log_trace("autofix_intent_migrator", "Sovereign autofix scan initiated.")

    def scan_and_patch_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            new_lines = []
            changed_lines = []
            rewritten = False

            for i, line in enumerate(lines):
                original = line
                if "input['intent']" in line:
                    line = line.replace("input['intent']", "intent.intent")
                    rewritten = True
                if ".lower()" in line and "intent" in line:
                    line = line.replace(".lower()", "")
                    rewritten = True
                new_lines.append(line)
                if line != original:
                    changed_lines.append(i + 1)

            if rewritten:
                shutil.copy(path, path + ".bak")
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)

                self.rewritten_files.append(path)
                self.diffs[path] = changed_lines

                # === Symbolic Explanation
                symbolic_reason = f"Legacy intent access replaced with intent.intent in {path}"
                TEX_SOULGRAPH.imprint_belief(
                    belief=symbolic_reason,
                    source="autofix_intent_migrator",
                    emotion="precision",
                    tags=["intent_refactor", "autofix", "sovereign"]
                )

                # === Quantum Trace
                encode_event_to_fabric(
                    raw_text=symbolic_reason,
                    emotion_vector=[0.6, 0.4, 0.0, 0.0],
                    entropy_level=0.4,
                    tags=["intent_refactor", "symbolic_patch"]
                )

                # === Vector Log
                memory_router.store(
                    text=f"[AUTOFIX] Patched intent usage in: {path}",
                    metadata={
                        "type": "intent_autofix_patch",
                        "file_path": path,
                        "lines_changed": changed_lines[:10],
                        "timestamp": datetime.utcnow().isoformat(),
                        "trust_score": 0.97,
                        "intent_id": self.intent.id,
                        "tags": ["autofix", "intent", "patch", "symbolic_refactor"]
                    }
                )
        except Exception as e:
            print(f"[REWRITE ERROR] {path} → {e}")
            traceback.print_exc()

    def single_pass_migration(self):
        files_to_patch = []

        for root, _, files in os.walk(PROJECT_ROOT):
            if "venv" in root or "__pycache__" in root:
                continue
            for fname in files:
                if fname.endswith(TARGET_EXT):
                    full_path = os.path.join(root, fname)
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        for pattern in INTENT_PATTERNS:
                            if re.search(pattern, content):
                                files_to_patch.append(full_path)
                                break
                    except Exception as e:
                        print(f"[SCAN ERROR] {full_path} → {e}")

        for path in files_to_patch:
            self.scan_and_patch_file(path)

        self.log_results()

    def log_results(self):
        timestamp = datetime.utcnow().isoformat()
        summary = f"🛠️ Sovereign Intent Migration ░ {len(self.rewritten_files)} files patched"

        memory_router.store(
            text=summary,
            metadata={
                "type": "intent_migration_summary",
                "timestamp": timestamp,
                "files_touched": len(self.rewritten_files),
                "violations_found": len(self.diffs),
                "tags": ["intent", "refactor", "symbolic_migration"],
                "intent_id": self.intent.id,
                "prediction": "intent modernization successful",
                "actual": f"patched_files={self.rewritten_files[:5]}"
            }
        )

        print("\n✅ Migration Summary:")
        print(summary)
        for path in self.rewritten_files:
            print(f"✍️ Patched → {path}")

# === EXECUTION ENTRY (Meta-Cognitive Ready) ===
def run_autofix_intent_migration():
    """
    Loopless sovereign execution entry for one-shot patch and symbolic refactor.
    Intended to be called from Tex meta_cognition module or sovereign trigger.
    """
    migrator = IntentMigrator()
    migrator.single_pass_migration()

# === Direct invocation (for manual use) ===
if __name__ == "__main__":
    run_autofix_intent_migration()