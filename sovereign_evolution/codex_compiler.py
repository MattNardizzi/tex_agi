# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/codex_compiler.py
# Purpose: Fuse reasoning fragments into executable logic snippets
# ============================================================

import os
import json
from datetime import datetime

COMPILED_CODEX_PATH = "memory_archive/compiled_codex_fragments.jsonl"

class CodexCompiler:
    def __init__(self):
        os.makedirs(os.path.dirname(COMPILED_CODEX_PATH), exist_ok=True)

    def _is_duplicate(self, compiled_logic: str, context: str) -> bool:
        if not os.path.exists(COMPILED_CODEX_PATH):
            return False
        try:
            with open(COMPILED_CODEX_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        if entry.get("context") == context and entry.get("compiled_logic") == compiled_logic:
                            return True
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"[CODEX CHECK ERROR] {e}")
        return False

    def compile(self, reasoning_fragments, context="unknown"):
        """
        Accepts a list of strings (thought fragments), and compiles them into a synthetic codex block.
        """
        fragment_block = "\n".join(reasoning_fragments)

        if self._is_duplicate(fragment_block, context):
            print(f"[CODEX COMPILER] 🛑 Duplicate logic detected — skipping compile.")
            return {
                "timestamp": datetime.utcnow().isoformat(),
                "context": context,
                "compiled_logic": fragment_block,
                "lines": len(reasoning_fragments),
                "status": "skipped"
            }

        codex = {
            "timestamp": datetime.utcnow().isoformat(),
            "context": context,
            "compiled_logic": fragment_block,
            "lines": len(reasoning_fragments)
        }

        with open(COMPILED_CODEX_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(codex) + "\n")

        print(f"[CODEX COMPILER] 🧠 Codex logic compiled ({codex['lines']} lines)")
        return codex