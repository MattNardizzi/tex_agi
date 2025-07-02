# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/reflex_sandbox.py
# Tier: ΩΩΩ∞Ω∞Ω — Reflex Simulation Firewall
# Purpose: Executes and validates new reflex modules in a controlled sandboxed state.
# ============================================================

import importlib.util
import traceback
import os
from utils.logging_utils import log_event

# === Reflex Test Payloads ===
SANDBOX_STATES = [
    {"urgency": 0.9, "entropy": 0.6, "conflict_detected": True, "identity_fragility": 0.4},
    {"urgency": 0.3, "entropy": 0.2, "conflict_detected": False},
    {"urgency": 0.7, "entropy": 0.85, "identity_fragility": 0.2}
]

# === Reflex Validator ===
def simulate_reflex_safely(reflex_metadata: dict) -> bool:
    try:
        filepath = reflex_metadata.get("filepath")
        signature = reflex_metadata.get("signature")

        if not filepath or not signature:
            log_event("[SANDBOX] ❌ Missing reflex file or signature.", level="error")
            return False

        module = _load_module(filepath, signature)
        reflex_func = getattr(module, f"{signature}_pulse", None)

        if not callable(reflex_func):
            log_event(f"[SANDBOX] ❌ Reflex function `{signature}_pulse` not found.", level="error")
            return False

        for i, state in enumerate(SANDBOX_STATES):
            result = reflex_func(state)
            if not isinstance(result, dict) or "status" not in result:
                log_event(f"[SANDBOX] ⚠️ Reflex output invalid at iteration {i}.", level="warning")
                return False

        log_event(f"[SANDBOX] ✅ Reflex `{signature}` passed all safety checks.")
        return True

    except Exception as e:
        log_event(f"[SANDBOX] ❌ Exception during reflex execution: {e}", level="error")
        traceback.print_exc()
        return False

# === Dynamic Module Loader ===
def _load_module(filepath: str, signature: str):
    spec = importlib.util.spec_from_file_location(signature, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module