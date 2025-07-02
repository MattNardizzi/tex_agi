# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/alpaca_trade_adapter.py
# Tier: ⚡ Reflex-Capable Trade Execution Layer
# Purpose: Enables Tex to place paper trades with reflex memory tracking and traceable error handling
# ============================================================

import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST
from utils.logging_utils import log_event

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

client = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

def execute_stock_trade(symbol: str, side: str, qty: int = 1, reflex_meta: dict = None):
    """
    Submits a market order via Alpaca Paper API with reflex metadata logging.
    """
    try:
        order = client.submit_order(
            symbol=symbol,
            qty=qty,
            side=side.lower(),
            type='market',
            time_in_force='gtc'
        )

        msg = f"✅ TRADE EXECUTED: {side.upper()} {qty} {symbol}"
        print(msg)

        log_event(
            msg,
            metadata={
                "symbol": symbol,
                "side": side,
                "qty": qty,
                "type": "market",
                "origin": reflex_meta.get("source") if reflex_meta else "alpaca_trade_adapter",
                "urgency": reflex_meta.get("urgency") if reflex_meta else None,
                "entropy": reflex_meta.get("entropy") if reflex_meta else None,
                "emotion": reflex_meta.get("emotion") if reflex_meta else None
            },
            level="info"
        )

        return order

    except Exception as e:
        err_msg = f"❌ TRADE ERROR: {e}"
        print(err_msg)

        log_event(
            err_msg,
            metadata={
                "symbol": symbol,
                "side": side,
                "qty": qty,
                "error": str(e),
                "origin": reflex_meta.get("source") if reflex_meta else "alpaca_trade_adapter",
                "urgency": reflex_meta.get("urgency") if reflex_meta else None,
                "entropy": reflex_meta.get("entropy") if reflex_meta else None,
                "emotion": reflex_meta.get("emotion") if reflex_meta else None
            },
            level="error"
        )

        return None