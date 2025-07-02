# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/trade_log.py
# Tier: ΩΩΩ — Reflex Trade Logger with Real-Time Broadcast and Memory Injection
# Purpose: Logs all reflex-triggered trades with structured metadata and AGI-aligned vector traces.
# ============================================================

from datetime import datetime
from real_time_engine.websocket_broadcast import broadcast_update
from utils.logging_utils import log_event

# Optional: reflex memory injection
# from agentic_ai.sovereign_memory import sovereign_memory

reflex_trade_log = []

async def log_trade(trade: dict):
    """
    Store reflex-triggered trade to the global AGI trade log.
    Broadcast structured JSON message to real-time UI.
    """
    timestamp = datetime.utcnow().isoformat()

    trade_entry = {
        "timestamp": timestamp,
        "symbol": trade.get("symbol"),
        "action": trade.get("action"),
        "confidence": float(trade.get("confidence", 0.0)),
        "reflex_source": trade.get("reflex_source", "unknown"),
        "summary": trade.get("summary", ""),
        "emotion": trade.get("emotion", "neutral"),
        "urgency": float(trade.get("urgency", 0.5)),
        "entropy": float(trade.get("entropy", 0.4)),
        "reflex_id": trade.get("reflex_id", None),
        "reinforced": trade.get("reinforced", False),
        "vector": trade.get("vector", [0.0, 0.0, 0.0, 0.0]),
    }

    reflex_trade_log.append(trade_entry)

    # Optional: Sovereign Memory Sync
    # sovereign_memory.store(
    #     text=f"[TRADE] {trade_entry['action'].upper()} {trade_entry['symbol']}",
    #     metadata=trade_entry
    # )

    # === Real-Time Frontend Broadcast ===
    try:
        await broadcast_update({
            "type": "reflex_trade",
            "payload": trade_entry
        })
    except Exception as e:
        log_event(f"⚠️ Failed to broadcast trade log: {e}", level="warning")

    # === Log for Audit Trail ===
    log_event(f"[TRADE] {trade_entry['action'].upper()} {trade_entry['symbol']} @ confidence={trade_entry['confidence']:.2f}", metadata=trade_entry)

    return trade_entry


def get_recent_trades(limit=10):
    """
    Returns the most recent N trades.
    """
    return reflex_trade_log[-limit:]