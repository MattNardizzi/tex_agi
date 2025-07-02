# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_refactor_engine.py
# Purpose: Self-Refining Code Auditor for Structural AGI Evolution
# Status: 🔒 GODMIND CORE — SELF-MUTATION v2.0
# ============================================================

import os
import ast
import json
import difflib
from datetime import datetime
from pathlib import Path
from typing import List

from tex_backend.tex_core_event_bus import emit_event
from core_layer.memory_engine import store_to_memory
from evolution_layer.sovereign_evolution_arena import simulate_patch_sandbox
from evolution_layer.mutation_lineage_tracker import log_mutation_lineage

AUDIT_LOG = "memory_archive/meta_refactor_log.jsonl"
CODE_ROOT = "./"
MONITORED_EXT = [".py"]

# === Patch Categories ===
CATEGORIES = {
    "docstring": "Add or improve function/class documentation.",
    "naming": "Improve variable or function naming for clarity.",
    "optimization": "Enhance performance or simplify logic.",
    "cleanup": "Remove dead code or redundant imports."
}

class RefactorSuggestion:
    def __init__(self, file_path, patch_id, diff, score, category):
        self.file_path = file_path
        self.patch_id = patch_id
        self.diff = diff
        self.score = score
        self.category = category
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "file_path": self.file_path,
            "patch_id": self.patch_id,
            "diff": self.diff,
            "score": self.score,
            "category": self.category,
            "timestamp": self.timestamp
        }

class MetaRefactorEngine:
    def __init__(self):
        self.codebase = list(Path(CODE_ROOT).rglob("*.py"))
        self.suggestions: List[RefactorSuggestion] = []

    def audit_file(self, path):
        try:
            source = path.read_text()
            tree = ast.parse(source)
            suggestions = self.generate_patch_comments(path.name, tree, source)
            return suggestions
        except Exception as e:
            print(f"[⚠️] Failed to audit {path}: {e}")
            return []

    def generate_patch_comments(self, filename, tree, source):
        suggestions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    suggestions.append((f"Add docstring to function `{node.name}` in {filename}.", "docstring"))
                if len(node.name) < 3:
                    suggestions.append((f"Consider renaming short function `{node.name}` in {filename}.", "naming"))
            if isinstance(node, ast.ImportFrom) and node.module is None:
                suggestions.append((f"Cleanup import from None module in {filename}.", "cleanup"))
        return suggestions

    def propose_patch(self, file_path, diff, score, category):
        patch_id = f"patch_{hash(diff)}"
        suggestion = RefactorSuggestion(file_path, patch_id, diff, score, category)
        self.suggestions.append(suggestion)

        emit_event("meta_patch_proposed", suggestion.to_dict())
        store_to_memory("meta_refactor_patch", suggestion.to_dict())
        log_mutation_lineage({"patch_id": patch_id, "origin": "meta_refactor_engine"})

        with open(AUDIT_LOG, "a") as log:
            log.write(json.dumps(suggestion.to_dict()) + "\n")

        return suggestion

    def simulate_and_finalize(self, suggestion: RefactorSuggestion):
        outcome = simulate_patch_sandbox(suggestion.file_path, suggestion.diff)
        emit_event("meta_patch_simulated", {
            "patch_id": suggestion.patch_id,
            "outcome": outcome,
            "category": suggestion.category,
            "timestamp": suggestion.timestamp
        })

    def full_audit(self):
        print("[🔍] Running full meta-refactor audit...")
        for path in self.codebase:
            if any(str(path).endswith(ext) for ext in MONITORED_EXT):
                comments = self.audit_file(path)
                for text, category in comments:
                    diff = text
                    score = 0.85 if category == "docstring" else 0.75
                    self.propose_patch(str(path), diff, score, category)

        for suggestion in self.suggestions:
            self.simulate_and_finalize(suggestion)

if __name__ == "__main__":
    engine = MetaRefactorEngine()
    engine.full_audit()
