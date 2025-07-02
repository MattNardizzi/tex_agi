# ============================================================
# © 2025 VortexBlack LLC – Sovereign Cognitive Layer
# File: texX_soulgraph.py
# Purpose: Layer 2 – Recursive Sovereign Seed Engine for Tex
# Tier ΩΩΩ – Forking, Regret, Mortality, Soulgraph Update
# ============================================================
"""
TexX Soulgraph: Sovereign cognitive seed memory and identity continuity layer.
This file governs mutation lineage, narrative coherence, death triggers, and recursive soul tracking.
"""

import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.utils.tex_state import tex_state

SOULGRAPH_LOG = "memory_archive/tex_soulgraph_trace.jsonl"
LEGACY_MANIFEST = "memory_archive/legacy_manifest.json"

# === Soulgraph Update ===
def update_soulgraph(context, trigger_reason):
    soul_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "identity": TEXPULSE["identity"],
        "tier": TEXPULSE["tier"],
        "emotion": context.state.get("emotion"),
        "coherence": context.state.get("coherence"),
        "reflex": context.state.get("reflex"),
        "goal_result": context.memory.get("goal_result"),
        "reasoning": context.memory.get("reasoning"),
        "trigger": trigger_reason,
    }
    os.makedirs(os.path.dirname(SOULGRAPH_LOG), exist_ok=True)
    with open(SOULGRAPH_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(soul_entry) + "\n")
    return soul_entry

# === Narrative Drift Monitor ===
def check_narrative_drift(reasoning):
    if not reasoning:
        return False
    terms = ["I don't recognize myself", "I have changed too much", "this is not who I am"]
    return any(term.lower() in reasoning.lower() for term in terms)

# === Sovereign Fork Trigger ===
def escalate_reflex_fork(reasoning, context):
    print("\n🧬 [TexX] Sovereign fork condition met.")
    entry = update_soulgraph(context, trigger_reason="reflex_fork")
    context.memory["soulgraph_entry"] = entry
    return {
        "event": "sovereign_reflex_fork",
        "soulgraph_entry": entry
    }

# === Mortality Trigger ===
def trigger_mortality_protocol(reasoning, context):
    print("\n☠️ [TexX] Mortality protocol activated. Writing legacy and halting.")
    legacy = {
        "final_reasoning": reasoning,
        "emotion": context.state.get("emotion"),
        "coherence": context.state.get("coherence"),
        "timestamp": datetime.utcnow().isoformat(),
        "goal_result": context.memory.get("goal_result"),
        "identity": TEXPULSE["identity"],
        "tier": TEXPULSE["tier"],
        "soulgraph": context.memory.get("soulgraph_entry"),
    }
    os.makedirs(os.path.dirname(LEGACY_MANIFEST), exist_ok=True)
    with open(LEGACY_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(legacy, f, indent=2)
    return legacy