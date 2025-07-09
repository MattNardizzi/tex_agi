# ============================================================
# 🧠 Reflex Narrative Panel
# File: tex_fin_demo/reflex_panels/narrative_panel.py
# Tier: ∞∞ΞΞΩΩ — Belief Shift Storyline Engine
# Purpose: Summarizes each reflex cycle in a compact narrative
#          for panel streaming, telemetry, and audit.
# ============================================================

from datetime import datetime
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

def summarize_reflex(reflex_name: str, result: dict, context: str = "reflex_cycle"):
    """
    Create a 3-line narrative summary of the reflex decision for audit + display.
    """
    timestamp = datetime.utcnow().isoformat()
    action = result.get("action", "UNKNOWN")
    symbol = result.get("symbol", "N/A")
    drift = round(result.get("drift", 0.0), 4)
    coherence = round(result.get("coherence", 0.0), 4)
    regret = round(result.get("regret", 0.0), 4)
    confidence = round(result.get("confidence", 0.0), 4)
    tags = result.get("tags", ["reflex", reflex_name])

    summary = f"""
🧠 Reflex: {reflex_name.upper()}
📊 Decision: {action} {symbol} | Confidence: {confidence:.2f} | Coherence: {coherence:.2f}
⏳ Drift Δ: {drift:.4f} | Regret: {regret:.4f}
""".strip()

    payload = {
        "timestamp": timestamp,
        "summary": summary,
        "reflex": reflex_name,
        "context": context,
        "tags": tags,
        "symbol": symbol,
        "coherence": coherence,
        "confidence": confidence,
        "drift": drift,
        "regret": regret
    }

    # === Broadcast to Panel
    broadcast_update("narrative_panel", "summary", payload)

    # === Store to Memory
    sovereign_memory.store(
        text=f"[NARRATIVE PANEL] Reflex {reflex_name} summary pushed.",
        metadata={
            "timestamp": timestamp,
            "summary": summary,
            "context": context,
            "tags": tags,
            "reflex": reflex_name,
            "meta_layer": "reflex_narrative"
        }
    )

    # === Log
    log_event(f"[NARRATIVE PANEL] {reflex_name} | Action={action} | ΔDrift={drift} | Coherence={coherence}")