# ============================================================
# 🧠 VortexBlack Reflex Cortex | Tier 12 — Alpha Signal Fuser (Symbolic Fusion Engine)
# File: finance/strategy/alpha_signal_fuser.py
# Purpose: Fuses rationale, strategy, and performance feedback into long-term AGI trace memory.
# Architecture: Loopless | Reflex-aligned | Drift-aware | Memory-stacked.
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# ============================================================

import uuid
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

class AlphaSignalFuser:
    def __init__(self, agent="TEX", tag="alpha_signal", horizon_minutes=240):
        self.agent = agent
        self.tag = tag
        self.horizon_minutes = horizon_minutes

    def fuse_signals(self, rationale: str, strategy: dict, performance: dict = None):
        """
        Creates a long-term symbolic fusion trace combining AGI rationale,
        tactical portfolio choice, and performance outcome.
        """
        fusion_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        try:
            sovereign_memory.store(
                text=f"[ALPHA FUSION] ID={fusion_id}",
                metadata={
                    "agent": self.agent,
                    "intent": "alpha_signal_fusion",
                    "conclusion": f"Long-term fusion ID {fusion_id}",
                    "tags": [self.tag, "tier12_fusion", "alpha_signal"],
                    "timestamp": timestamp,
                    "reflexes": ["alpha_fusion", "cognitive_trace"],
                    "meta_layer": "alpha_fusion_engine",
                    "metadata": {
                        "rationale": rationale,
                        "strategy_snapshot": strategy,
                        "performance": performance or {},
                        "fusion_id": fusion_id
                    }
                }
            )
        except Exception as e:
            log_event(f"[FUSION ERROR] Memory store failed: {e}", level="error")

        print(f"✅ [FUSION STORED] Alpha signal fused → ID: {fusion_id}")
        return fusion_id

    def recall_recent_signals(self, n=5):
        """
        Loopless query for recent alpha signal fusion memories.
        """
        return sovereign_memory.recall_recent(
            minutes=self.horizon_minutes,
            top_k=n,
            filters={"tags": [self.tag]}
        )

    def summarize_alpha_trends(self, top_n=8):
        """
        Summarizes recent fused alpha rationales for pattern reasoning.
        """
        entries = self.recall_recent_signals(top_n)
        return self._compress_trend_log(entries, 0, [])

    def _compress_trend_log(self, entries, i, acc):
        if i >= len(entries):
            return "\n".join(acc) if acc else "No alpha fusion signals in memory."
        try:
            meta = entries[i].get("metadata", {})
            rationale = meta.get("rationale", "[no rationale found]")
            ts = meta.get("timestamp", "unknown")
            acc.append(f"→ {ts}: {rationale}")
        except Exception as e:
            log_event(f"[TREND ERROR] Failed to parse entry: {e}", level="warning")
        return self._compress_trend_log(entries, i + 1, acc)

# === Reflex Harness ===
if __name__ == "__main__":
    fuser = AlphaSignalFuser()
    fused = fuser.fuse_signals(
        rationale="Rotation into AI-weighted momentum sectors due to sovereign risk recalibration.",
        strategy={"assets": ["NVDA", "AAPL", "SMCI"], "mode": "momentum_biased"},
        performance={"gain": 0.126, "drawdown": 0.03, "volatility": 0.041}
    )

    print("\n[🧠 RECENT SIGNALS]")
    for s in fuser.recall_recent_signals():
        print(s)

    print("\n[🧠 ALPHA SUMMARY]")
    print(fuser.summarize_alpha_trends())