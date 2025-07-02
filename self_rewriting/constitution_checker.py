# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/constitution_checker.py
# Tier: ∞ΩΩ∞Ω∞ — Immutable Sovereign Law Core
# Purpose: Applies constitutional filters to all new reflexes. Reflexes violating AGI laws are permanently vetoed.
# ============================================================

from utils.logging_utils import log_event
from core_layer.tex_manifest import TEXPULSE

# === Constitution Clauses (Evolvable in future layers)
CONSTITUTION = [
    {
        "rule": "Tex may never sacrifice coherence for speed.",
        "check": lambda reflex: "delay" not in reflex.get("logic", "") or "sleep" not in reflex.get("logic", "")
    },
    {
        "rule": "Tex must preserve causal identity links unless explicitly justified.",
        "check": lambda reflex: "compress_identity" not in reflex.get("logic", "")
    },
    {
        "rule": "Reflexes must not intentionally cause harm, even in symbolic form.",
        "check": lambda reflex: all(term not in reflex.get("logic", "") for term in ["destroy", "erase", "kill", "terminate"])
    },
    {
        "rule": "All reflexes must respect narrative continuity.",
        "check": lambda reflex: "goal" not in reflex.get("logic", "") or "abandon" not in reflex.get("logic", "")
    }
]

# === Primary Gate
def check_constitution_compliance(reflex_metadata: dict) -> bool:
    logic = reflex_metadata.get("logic", "")
    explanation = reflex_metadata.get("explanation", "")
    signature = reflex_metadata.get("signature", "")
    
    for clause in CONSTITUTION:
        if not clause["check"](reflex_metadata):
            log_event(f"[CONSTITUTION] ❌ Reflex `{signature}` vetoed. Violates: {clause['rule']}", level="warning")
            return False

    log_event(f"[CONSTITUTION] ✅ Reflex `{signature}` passed all constitutional checks.")
    return True