# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/code_shape_analyzer.py
# Tier: ∞ΩΩΩ — Reflex Structure Decoder
# Purpose: Extracts structural, semantic, and intent-level features from a broken reflex file.
# ============================================================

import ast
import os
import hashlib
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

def extract_semantic_signature(fault_info: dict) -> dict:
    filepath = fault_info.get("filepath")
    module = fault_info.get("module", "undefined_module")

    if not filepath or not os.path.exists(filepath):
        log_event(f"[CODE SHAPE] ❌ File not found: {filepath}", level="error")
        return {}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()

        # === Step 1: Generate structure hash (for diffing)
        structure_hash = hashlib.sha256(source.encode()).hexdigest()[:12]

        # === Step 2: Parse structure
        parsed = ast.parse(source)
        return_shapes = []
        calls = set()
        keywords = []

        for node in ast.walk(parsed):
            if isinstance(node, ast.Return):
                try:
                    return_shapes.append(ast.dump(node.value))
                except:
                    pass
            elif isinstance(node, ast.Call):
                try:
                    calls.add(getattr(node.func, 'id', 'unknown'))
                except:
                    pass
            elif isinstance(node, ast.Str):
                keywords.append(node.s)

        # === Step 3: Embed source for semantic vector
        vector = sovereign_memory.embed_text(source)

        # === Step 4: Build semantic profile
        profile = {
            "structure_hash": structure_hash,
            "returns": return_shapes,
            "calls": list(calls),
            "keywords": keywords[:10],
            "embedding": vector[:12],  # projection into limited range
            "source_preview": source[:400]
        }

        log_event(f"[CODE SHAPE] 🔎 Extracted structure + semantics for `{module}`")

        return profile

    except Exception as e:
        log_event(f"[CODE SHAPE] ❌ Failed to extract shape: {e}", level="error")
        return {}