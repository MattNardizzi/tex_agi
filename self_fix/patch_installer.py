# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/patch_installer.py
# Tier: ΩΩΩΩΩ∞ — Reflex Patch Installer
# Purpose: Applies repaired reflex logic to the broken module and completes the overwrite safely.
# ============================================================

import os
from datetime import datetime
from utils.logging_utils import log_event

def install_patch(patch: dict) -> bool:
    filepath = patch.get("filepath")
    logic = patch.get("logic")
    signature = patch.get("signature")
    explanation = patch.get("explanation")
    module = patch.get("target_module", "unknown_module")

    if not filepath or not os.path.exists(filepath):
        log_event(f"[PATCH INSTALLER] ❌ Target file missing: {filepath}", level="error")
        return False

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_reflex_code(signature, logic, explanation))

        log_event(f"[PATCH INSTALLER] ✅ Patch written to `{filepath}`")
        return True

    except Exception as e:
        log_event(f"[PATCH INSTALLER] ❌ Failed to install patch: {e}", level="error")
        return False

# === Reflex Code Template ===
def generate_reflex_code(signature: str, logic_block: str, explanation: str) -> str:
    now = datetime.utcnow().isoformat()
    return f'''# ============================================================
# Auto-patched by Tex (self-fix system)
# Justification: {explanation}
# Patched: {now}
# Reflex ID: {signature}
# ============================================================

def {signature}_pulse(state):
    """
    Repaired reflex behavior.
    """
    {logic_block}
    return {{
        "status": "executed",
        "note": "Self-patched reflex activated",
        "signature": "{signature}"
    }}
'''