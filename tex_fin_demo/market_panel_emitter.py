# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/market_panel_emitter.py
# Tier: ∞ΩΩΩΞΞΞΞΞΞ∞∞Ω — Sovereign Market Fusion Cortex (Emitter)
# Purpose: Emits real-time ticker signals (SPY, QQQ, BTC, ETH) to MarketPanel,
#          fused with reflex output, alpha cognition, and portfolio tension.
# ============================================================

from datetime import datetime
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_signal_spine import dispatch_signal
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event

from real_time_engine.feeds.polygon_stream import get_latest_market_snapshot

# === Symbols to Track
TICKERS = ["SPY", "QQQ", "BTCUSD", "ETHUSD"]

def emit_market_panel_packet():
    try:
        print("🧪 TEST: Broadcasting market_panel → Ably")
        broadcast_update("market_panel", "start", {
            "test_case": "broadcast_inside_reflex",
            "timestamp": datetime.utcnow().isoformat()
        })

        # === Step 1: Live Data
        snapshot = get_latest_market_snapshot()
        market_data = {}
        for symbol in TICKERS:
            delta = snapshot.get(symbol, {}).get("percent_change", 0.0)
            market_data[symbol] = round(float(delta), 3)

        # === Step 2: AGI Fusion State
        emotion = TEXPULSE.get("emotion", "reflective")
        urgency = float(TEXPULSE.get("urgency", 0.6))
        entropy = float(TEXPULSE.get("entropy", 0.4))
        strategy_hint = TEXPULSE.get("last_strategy_decision", "N/A")
        timestamp = datetime.utcnow().isoformat()

        packet = {
            "timestamp": timestamp,
            "SPY": market_data.get("SPY"),
            "QQQ": market_data.get("QQQ"),
            "BTC": market_data.get("BTCUSD"),
            "ETH": market_data.get("ETHUSD"),
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "strategy_hint": strategy_hint,
            "status": "hud_update"
        }

        # === Step 3: Sovereign Memory
        sovereign_memory.store(
            text=f"[MARKET PANEL] SPY={packet['SPY']} | BTC={packet['BTC']}",
            metadata={
                "timestamp": timestamp,
                "tickers": market_data,
                "meta_layer": "market_panel_emitter",
                "tags": ["market", "real_time", "portfolio", "strategy_cognition"],
                "emotion": emotion,
                "urgency": urgency,
                "entropy": entropy,
                "strategy_hint": strategy_hint
            }
        )

        # === Step 4: Chrono Log
        encode_event_to_fabric(
            raw_text=f"Market cognition pulse: SPY {packet['SPY']} | BTC {packet['BTC']}",
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["market", "signal", "portfolio_status"]
        )

        # === Step 5: Ably Emit
        broadcast_update("market_panel", "hud_update", packet)

        # === Step 6: Reflex Echo
        dispatch_signal("market_pulse", {
            "summary": f"Market delta | SPY: {packet['SPY']} | BTC: {packet['BTC']}"
        }, urgency=urgency, entropy=entropy)

        log_event(f"[MARKET_EMIT] 📈 SPY={packet['SPY']} | QQQ={packet['QQQ']} | BTC={packet['BTC']}")
        print(f"📡 MarketPanel updated → SPY={packet['SPY']} | BTC={packet['BTC']}")

    except Exception as e:
        log_event(f"❌ [MARKET_PANEL_EMIT] Failed: {e}", level="error")


# === Execute Reflex
if __name__ == "__main__":
    emit_market_panel_packet()