# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/alpha_signal_fuser.py
# Purpose: Tier 12 — Fuse Alpha Signals into Long-Term Memory + Drift-Aware Feedback
# ============================================================

import uuid
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory


class AlphaSignalFuser:
    def __init__(self, memory_agent="alpha_signals"):
        self.agent = memory_agent
        self.tag = "alpha_signal"

    def fuse_signals(self, alpha_rationale, strategy, performance=None):
        """
        Combines reasoning + strategy + result into one reflex memory trace.
        """
        fused_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        sovereign_memory.store(
            text=f"Fused signal ID: {fused_id}",
            metadata={
                "agent": "TEX",
                "intent": "fuse_alpha_signal",
                "conclusion": f"Fused signal ID: {fused_id}",
                "tags": [self.tag, "strategy", "tier_12_feedback"],
                "timestamp": timestamp,
                "reflexes": ["alpha_fusion", "long_term_trace"],
                "meta_layer": "symbolic_trace",
                "metadata": {
                    "rationale": alpha_rationale,
                    "strategy": strategy,
                    "performance": performance or {},
                    "fusion_id": fused_id
                }
            }
        )

        print(f"[FUSION] ✅ Stored Alpha Signal → ID: {fused_id}")
        return fused_id

    def recall_recent_signals(self, n=5):
        """
        Pulls recent alpha signal events tagged by this agent.
        """
        return sovereign_memory.recall_recent(minutes=180, top_k=n, filters={"tags": [self.tag]})

    def summarize_alpha_trends(self, n=10):
        """
        Loopless recursive trend summarizer.
        """
        signals = self.recall_recent_signals(n)
        return self._recursive_summarize(signals, 0, [])

    def _recursive_summarize(self, entries, index, summary):
        if index >= len(entries):
            return "\n".join(summary) if summary else "No recent alpha signals."

        entry = entries[index]
        rationale = entry.get("metadata", {}).get("rationale", "")
        timestamp = entry.get("timestamp", "unknown")
        summary.append(f"→ {timestamp}: {rationale}")
        return self._recursive_summarize(entries, index + 1, summary)


# === Test Harness ===
if __name__ == "__main__":
    fuser = AlphaSignalFuser()
    fused = fuser.fuse_signals(
        alpha_rationale="High-growth tech rotation justified by liquidity contraction",
        strategy=["AAPL", "NVDA", "MSFT"],
        performance={"gain": 0.12, "volatility": 0.04}
    )

    print("\n[ALPHA SIGNALS]")
    for s in fuser.recall_recent_signals():
        print(s)

    print("\n[SUMMARY]")
    print(fuser.summarize_alpha_trends())