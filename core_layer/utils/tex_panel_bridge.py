# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/utils/tex_panel_bridge.py
# Purpose: Emit real-time dashboard state updates for all panels
# ============================================================

from datetime import datetime
from typing import List, Dict, Any

from core_layer.utils.tex_state import tex_state
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Unified spike memory

def now_iso() -> str:
    return datetime.utcnow().isoformat()

# === Panel: Sovereign Cognition ===
def emit_sovereign_cognition(cycle: int, foresight: Dict[str, Any], orchestrator: Any):
    snapshot = {
        "trustScore": foresight.get("confidence", 0.0),
        "overrideTriggered": foresight.get("override_triggered", False),
        "godmindActive": True,
        "anchorTether": foresight.get("anchor_tether", "unknown"),
        "lastSpawnedPersona": getattr(orchestrator, "last_persona", "AeonDelta"),
        "ghostForks": getattr(orchestrator, "ghost_forks", ["variant_x1"]),
        "sovereignSignal": foresight.get("sovereign_signal", f"Cycle {cycle} → Foresight confidence unknown"),
        "timestamp": now_iso(),
    }

    tex_state.update_state("sovereign_cognition", snapshot)
    print("[📡] Panel: Sovereign Cognition updated.")

# === Panel: Strategy Overview ===
def emit_strategy_overview(cycle: int, ranked: List[Dict[str, Any]]):
    snapshot = {
        "cycle": cycle,
        "topStrategies": ranked[:5] if ranked else [],
        "timestamp": now_iso(),
    }

    tex_state.update_state("strategy_overview", snapshot)
    print("[📡] Panel: Strategy Overview updated.")

# === Panel: Simulacrum Feed ===
def emit_simulacrum_feed(cycle: int, variants: List[Dict[str, Any]]):
    snapshot = {
        "cycle": cycle,
        "latestForks": variants[-5:] if variants else [],
        "timestamp": now_iso(),
    }

    tex_state.update_state("simulacrum_feed", snapshot)
    print("[📡] Panel: Simulacrum Feed updated.")

# === Panel: Internal Debate Viewer ===
def emit_internal_debate(cycle: int, debate_log: List[Dict[str, Any]]):
    if not debate_log or not isinstance(debate_log, list) or len(debate_log) == 0:
        print("[⚠️] Internal Debate log is empty or invalid — injecting fallback.")
        debate_log = [{
            "agent": "Tex-Fallback",
            "text": "[No debate generated]",
            "confidence": 0.0,
            "regret": 0.0,
            "triggeredOverride": False,
            "timestamp": now_iso()
        }]

    vector_data = {
        "cycle": cycle,
        "log": debate_log,
        "timestamp": now_iso(),
    }

    sovereign_memory.store_vector_trace(
        content=str(vector_data),
        tags=["debate", "cycle", "internal"],
        signal_type="internal_debate"
    )

    cleaned_entries = [
        {
            "agent": entry.get("agent", "UNKNOWN"),
            "text": entry.get("text", ""),
            "confidence": float(entry.get("confidence", 0.0)),
            "regret": float(entry.get("regret", 0.0)),
            "triggeredOverride": bool(entry.get("triggeredOverride", False)),
            "timestamp": entry.get("timestamp", now_iso()),
        }
        for entry in debate_log[-10:]
    ]

    snapshot = {
        "cycle": cycle,
        "entries": cleaned_entries,
        "timestamp": now_iso(),
    }

    tex_state.update_state("internal_debate", snapshot)
    print(f"[📡] Panel: Internal Debate updated with {len(cleaned_entries)} entries.")

# === Memory-Native Species Vector Encoder ===
def encode_species_vector(label: str, vector_data: Any):
    """
    Converts any vector into embedded memory storage — replaces json.dumps().
    """
    if isinstance(vector_data, dict):
        text = str(dict(vector_data))
    else:
        text = f"[RAW VECTOR] {str(vector_data)}"

    sovereign_memory.store_vector_trace(
        content=text,
        tags=["species", "vector", label],
        signal_type="species_vector"
    )

    return f"[MEMORY STORED] species vector for {label}"

# === Unified Panel Emit Function ===
def emit_all_panels(
    cycle: int,
    foresight: Dict[str, Any],
    orchestrator: Any,
    ranked: List[Dict[str, Any]] = None,
    variants: List[Dict[str, Any]] = None,
    debate_log: List[Dict[str, Any]] = None,
):
    emit_sovereign_cognition(cycle, foresight, orchestrator)
    emit_strategy_overview(cycle, ranked or [])
    emit_simulacrum_feed(cycle, variants or [])
    emit_internal_debate(cycle, debate_log or [])

# === Memory Drift Score (temporary legacy support) ===
def get_memory_drift_score(mem_a, mem_b):
    if not isinstance(mem_a, dict) or not isinstance(mem_b, dict):
        return 1.0  # complete drift

    score = 0.0
    shared_keys = set(mem_a.keys()).intersection(mem_b.keys())

    for key in shared_keys:
        if mem_a[key] != mem_b[key]:
            score += 0.5
        else:
            score += 0.0

    return min(score, 1.0)