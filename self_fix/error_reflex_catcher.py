# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/error_reflex_catcher.py
# Tier: ΩΩ∞∞ — Runtime Fault Context Extractor
# Purpose: Captures reflex or agent failure signals and parses key context for downstream repair.
# ============================================================

import traceback
from datetime import datetime
from utils.logging_utils import log_event

def capture_failure_context(payload: dict) -> dict:
    """
    Extracts file/module/trace context from a failed reflex, fork, or agent.
    """
    error_type = payload.get("error_type", "unknown_exception")
    traceback_str = payload.get("traceback", "")
    filepath = payload.get("filepath")
    module = payload.get("module_name", "undefined_module")

    # Attempt minimal parsing of traceback for last error line
    line = "unknown"
    if traceback_str and isinstance(traceback_str, str):
        lines = traceback_str.strip().splitlines()
        for l in reversed(lines):
            if "File" in l and ", line" in l:
                line = l.strip()
                break

    if not filepath:
        log_event("[ERROR CATCHER] ❌ No filepath found in signal — skipping.", level="error")
        return {}

    log_event(f"🛠 [ERROR CATCHER] Captured failure in `{module}` | {error_type} @ {line}")

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "error_type": error_type,
        "trace": traceback_str,
        "filepath": filepath,
        "line": line,
        "module": module
    }