# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/reflex_auditor.py
# Tier: ΩΩ∞∞Ω — Semantic Reflex Health Analyzer
# Purpose: Audits a crashed module or reflex to determine if a repair is required.
# ============================================================

import ast
import os
from utils.logging_utils import log_event

def analyze_faulty_module(fault_info: dict) -> dict:
    """
    Audits the given file to check for syntax errors, structural breaks, or dead logic.
    Returns a status report: 'healthy' or 'corrupted'
    """
    filepath = fault_info.get("filepath")
    module = fault_info.get("module", "undefined_module")

    if not filepath or not os.path.exists(filepath):
        log_event(f"[AUDITOR] ❌ File does not exist: {filepath}", level="error")
        return {"status": "corrupted", "reason": "file_missing"}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()

        # Attempt to parse syntax tree
        ast.parse(source)

        # Basic health check: must define one _pulse() function
        if f"{module}_pulse" not in source:
            log_event(f"[AUDITOR] ⚠️ Reflex `{module}` missing _pulse() function.")
            return {"status": "corrupted", "reason": "missing_pulse_function"}

        # Optional: flag suspicious keywords
        if "undefined" in source or ("pass" in source and "return" not in source):
            log_event(f"[AUDITOR] ⚠️ Reflex `{module}` may contain incomplete logic.")
            return {"status": "corrupted", "reason": "incomplete_logic"}

        log_event(f"[AUDITOR] ✅ File `{module}` is syntactically valid.")
        return {"status": "healthy"}

    except SyntaxError as se:
        log_event(f"[AUDITOR] ❌ Syntax error in `{module}`: {se}", level="error")
        return {"status": "corrupted", "reason": "syntax_error", "details": str(se)}

    except Exception as e:
        log_event(f"[AUDITOR] ❌ Unexpected exception auditing `{module}`: {e}", level="error")
        return {"status": "corrupted", "reason": "unknown_error", "details": str(e)}