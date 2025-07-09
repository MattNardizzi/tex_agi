# ============================================================
# 🔹 VortexBlack Confidential – MAXGODMODE ENABLED
# File: future_layer/multiworld_reasoner.py
# Tier ∞∞∞ΩΞΣΩ — Tex Reflex: Cross-Timeline Divergence Inference Cortex
# Purpose: Strategic divergence detection across futures with sovereign memory fusion.
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

try:
    from real_time_engine.external_world_fusion import fetch_live_causal_worlds
    REALTIME_ENABLED = True
except ImportError:
    REALTIME_ENABLED = False

class MultiWorldReasoner:
    def __init__(self):
        self.max_cross_analysis = 7
        self.reasoning_memory = []
        self.frozen_worlds = []

    def compare_worlds(self, world_a, world_b):
        divergences = []
        map_a = {e.get("cause"): e.get("effect") for e in world_a}
        map_b = {e.get("cause"): e.get("effect") for e in world_b}
        for cause in set(map_a.keys()).union(map_b.keys()):
            ea, eb = map_a.get(cause), map_b.get(cause)
            if ea and eb and ea != eb:
                divergences.append({
                    "cause": cause,
                    "effect_a": ea,
                    "effect_b": eb,
                    "emotion": TEXPULSE.get("emotional_state", "neutral"),
                    "urgency": TEXPULSE.get("urgency", 0.72),
                    "coherence": TEXPULSE.get("coherence", 0.81),
                    "timestamp": datetime.utcnow().isoformat()
                })
        return divergences

    def generate_cross_universe_insights(self, multiworlds):
        insights = []
        count = 0
        for i in range(len(multiworlds)):
            for j in range(i + 1, len(multiworlds)):
                if count >= self.max_cross_analysis:
                    return insights
                divs = self.compare_worlds(multiworlds[i], multiworlds[j])
                if divs:
                    drift_label = self._label_drift(divs)
                    insights.append({
                        "world_pair": (i, j),
                        "divergence_nodes": divs,
                        "drift_label": drift_label
                    })
                    if drift_label in {"volatile", "unstable"}:
                        self._store_synthetic_conflict(i, j, divs, drift_label)
                    count += 1
        return insights

    def reason_over_future_worlds(self, multiworlds):
        insights = self.generate_cross_universe_insights(multiworlds)
        summaries = []

        for item in insights:
            i, j = item["world_pair"]
            drift = item["drift_label"]
            tone = TEXPULSE.get("emotional_state", "curious")
            summary = f"🌌 Divergence between World {i} and {j} | Drift: {drift} | Tone: {tone}"

            for node in item["divergence_nodes"]:
                summary += (
                    f"\n • '{node['cause']}' → '{node['effect_a']}' vs '{node['effect_b']}'"
                    f" | U: {node['urgency']} | C: {node['coherence']}"
                )

            self._store_summary(summary)
            summaries.append(summary)

        return summaries

    def _label_drift(self, divergence_nodes):
        urgency_values = [d["urgency"] for d in divergence_nodes]
        if sum(u > 0.7 for u in urgency_values) >= len(urgency_values) // 2:
            return "volatile"
        if TEXPULSE.get("coherence", 0.5) < 0.4:
            return "unstable"
        return "bounded"

    def _store_synthetic_conflict(self, i, j, divergence, label):
        try:
            conflict_id = str(uuid.uuid4())
            sovereign_memory.store(
                text=f"[DIVERGENCE] World {i} vs {j} → {label.upper()} drift detected.",
                metadata={
                    "tags": ["multiverse", "drift", label],
                    "timestamp": datetime.utcnow().isoformat(),
                    "meta_layer": "multiverse_reasoning",
                    "urgency": TEXPULSE.get("urgency", 0.72),
                    "coherence": TEXPULSE.get("coherence", 0.81),
                    "emotion": TEXPULSE.get("emotional_state", "curious"),
                    "divergence_nodes": divergence,
                    "conflict_id": conflict_id
                }
            )
            self.frozen_worlds.append((i, j))
        except Exception as e:
            log_event(f"[DIVERGENCE MEMORY ERROR] {e}", level="error")

    def _store_summary(self, summary_text):
        self.reasoning_memory.append({
            "id": str(uuid.uuid4()),
            "summary": summary_text,
            "timestamp": datetime.utcnow().isoformat()
        })

    def recall_reasoning_memory(self, limit=5):
        return self.reasoning_memory[-limit:]

# === Manual Reflex Test ===
if __name__ == "__main__":
    if REALTIME_ENABLED:
        print("🛰 Sovereign Mode Active: Fetching live causal multiworlds...")
        try:
            live_worlds = fetch_live_causal_worlds()
            reasoner = MultiWorldReasoner()
            for s in reasoner.reason_over_future_worlds(live_worlds):
                print(s)
        except Exception as e:
            print(f"[REALTIME FETCH ERROR] {e}")
    else:
        print("⚠️ Real-time disabled. Using test data.")
        test_worlds = [
            [{"cause": "Rate hike", "effect": "Liquidity crisis"}, {"cause": "Oil shock", "effect": "Energy crash"}],
            [{"cause": "Rate hike", "effect": "Credit crunch"}, {"cause": "Oil shock", "effect": "Energy crash"}],
            [{"cause": "New tech", "effect": "Equity surge"}, {"cause": "Fed pivot", "effect": "Market rally"}]
        ]
        reasoner = MultiWorldReasoner()
        for s in reasoner.reason_over_future_worlds(test_worlds):
            print(s)

    print("\n🧠 [SUMMARY DUMP]")
    for m in reasoner.recall_reasoning_memory():
        print(m)