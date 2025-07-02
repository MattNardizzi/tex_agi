# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/preactivation_queue.py
# Purpose: Reflex Preactivation Queue — Anticipate and Prepare Reflex Modules
# Tier: Ω∞ — Reflex Pre-Warming, Uniqueness Guard, Priority Peek
# ============================================================

from datetime import datetime
from collections import deque
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

class PreactivationQueue:
    def __init__(self, max_size=20):
        self.queue = deque(maxlen=max_size)

    def add(self, reflex_name, score=1.0, forecast_horizon=1):
        timestamp = datetime.utcnow().isoformat()

        # Prevent duplicates — keep highest score version
        self.queue = deque([e for e in self.queue if e["reflex"] != reflex_name], maxlen=self.queue.maxlen)

        entry = {
            "reflex": reflex_name,
            "score": round(score, 3),
            "forecast_horizon": forecast_horizon,
            "timestamp": timestamp
        }
        self.queue.append(entry)

        if score >= 0.9:
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Preactivation queued: {reflex_name} (score {score})",
                source="preactivation_queue",
                emotion="anticipation"
            )

        return entry

    def get_ready_reflexes(self, threshold=0.6):
        return [entry for entry in self.queue if entry["score"] >= threshold]

    def flush(self):
        self.queue.clear()

    def peek(self):
        return list(self.queue)

    def peek_top_priority(self):
        if not self.queue:
            return None
        return max(self.queue, key=lambda x: x["score"])


# === Singleton Instance (for system-wide import)
preactivation_queue = PreactivationQueue()

# === CLI Diagnostic ===
if __name__ == "__main__":
    q = PreactivationQueue()
    q.add("memory_reflex", score=0.92, forecast_horizon=3)
    q.add("goal_reflex", score=0.65, forecast_horizon=2)
    print("\n[PREACTIVATION QUEUE PREVIEW]\n", q.peek())
    print("\n[READY REFLEXES]\n", q.get_ready_reflexes(threshold=0.6))
    print("\n[TOP PRIORITY REFLEX]\n", q.peek_top_priority())