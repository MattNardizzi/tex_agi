# ============================================================
# 📈 Alpha Benchmark Reflex Panel
# File: tex_fin_demo/reflex_panels/alpha_benchmark_panel.py
# Tier: ∞∞ΩΞΞΞΞΞΞ — Tex vs Benchmark Alpha Comparison Layer
# Purpose: Computes and visualizes alpha delta between Tex strategy and market baseline (e.g., SPY).
# ============================================================

from datetime import datetime
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

def render_alpha_benchmark_panel(tex_return: float, spy_return: float, tags=None):
    """
    Compare Tex's return against SPY and broadcast alpha delta.
    
    Args:
        tex_return (float): Cumulative return from Tex's portfolio.
        spy_return (float): Cumulative return from SPY (or baseline).
        tags (list[str], optional): Additional metadata tags.
    """
    timestamp = datetime.utcnow().isoformat()
    alpha_delta = round(tex_return - spy_return, 6)

    panel_data = {
        "timestamp": timestamp,
        "tex": round(tex_return, 6),
        "spy": round(spy_return, 6),
        "alpha": alpha_delta,
        "tags": tags or ["alpha_comparison", "benchmark"]
    }

    # === Broadcast to Panel
    broadcast_update("alpha_panel", "update", panel_data)

    # === Memory Trace
    sovereign_memory.store(
        text=f"[ALPHA PANEL] Tex vs SPY → Alpha: {alpha_delta:.6f}",
        metadata={
            "timestamp": timestamp,
            "tex_return": tex_return,
            "spy_return": spy_return,
            "alpha_delta": alpha_delta,
            "tags": panel_data["tags"],
            "meta_layer": "alpha_benchmark"
        }
    )

    # === Log
    log_event(f"[ALPHA BENCHMARK] α={alpha_delta:.6f} | Tex={tex_return:.6f} | SPY={spy_return:.6f}")