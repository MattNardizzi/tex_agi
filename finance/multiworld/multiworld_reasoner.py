# ============================================================
# 🔹 VortexBlack Confidential – MAXGODMODE ENABLED
# File: future_layer/multiworld_reasoner.py
# Tier 5 AGI-Class Strategic Cross-Timeline Divergence Engine
# Sovereign Cognition: ENABLED
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import uuid
import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

# 🧠 Sovereign Cognition Activation
try:
    from real_time_engine.external_world_fusion import fetch_live_causal_worlds
    REALTIME_ENABLED = True
except ImportError:
    REALTIME_ENABLED = False

CONFLICT_LOG = "memory_archive/multiverse_conflict_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class MultiWorldReasoner:
    def __init__(self):
        self.max_cross_analysis = 7
        self.reasoning_memory = []
        self.frozen_worlds = []

    def compare_worlds(self, world_a, world_b):
        divergences = []
        map_a = {e.get("cause"): e.get("effect") for e in world_a if isinstance(e, dict)}
        map_b = {e.get("cause"): e.get("effect") for e in world_b if isinstance(e, dict)}
        for cause in set(map_a.keys()).union(map_b.keys()):
            effect_a = map_a.get(cause)
            effect_b = map_b.get(cause)
            if effect_a and effect_b and effect_a != effect_b:
                divergences.append({
                    "cause": cause,
                    "effect_a": effect_a,
                    "effect_b": effect_b,
                    "bias_signal": TEXPULSE.get("emotional_state"),
                    "urgency_weight": TEXPULSE.get("urgency"),
                    "coherence_score": TEXPULSE.get("coherence")
                })
        return divergences

    def generate_cross_universe_insights(self, multiworlds):
        insights = []
        count = 0
        for i in range(len(multiworlds)):
            for j in range(i + 1, len(multiworlds)):
                if count >= self.max_cross_analysis:
                    break
                world_a = multiworlds[i]
                world_b = multiworlds[j]
                divergence = self.compare_worlds(world_a, world_b)
                if divergence:
                    drift_label = self._label_drift(divergence)
                    insights.append({
                        "world_pair": (i, j),
                        "divergence_nodes": divergence,
                        "drift_label": drift_label
                    })
                    if drift_label in {"unstable", "volatile"}:
                        self._freeze_conflict(i, j, divergence, drift_label)
                    count += 1
        return insights

    def reason_over_future_worlds(self, multiworlds):
        insights = self.generate_cross_universe_insights(multiworlds)
        tone = TEXPULSE.get("emotional_state", "curious")
        summaries = []

        for item in insights:
            i, j = item["world_pair"]
            summary = f"🌌 Divergence Detected Between World {i} and {j} [Tone: {tone}, Drift: {item['drift_label']}]:"
            for node in item["divergence_nodes"]:
                summary += (
                    f"\n • '{node['cause']}' caused → '{node['effect_a']}' vs '{node['effect_b']}'"
                    f" | Urgency: {node['urgency_weight']} | Coherence: {node['coherence_score']}"
                )
            self._store_summary(summary)
            summaries.append(summary)

        return summaries

    def _label_drift(self, divergence_nodes):
        volatility = sum(1 for d in divergence_nodes if d["urgency_weight"] > 0.7)
        if volatility >= len(divergence_nodes) // 2:
            return "volatile"
        if TEXPULSE["coherence"] < 0.4:
            return "unstable"
        return "bounded"

    def _freeze_conflict(self, i, j, divergence, label):
        try:
            entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "conflict_pair": (i, j),
                "drift_type": label,
                "divergence": divergence,
                "emotion": TEXPULSE.get("emotional_state"),
                "urgency": TEXPULSE.get("urgency"),
                "coherence": TEXPULSE.get("coherence")
            }
            self.frozen_worlds.append((i, j))
            with open(CONFLICT_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            print(f"[MULTIVERSE] ❄️ Frozen Worlds {i} & {j} due to '{label}' drift.")
        except Exception as e:
            print(f"[MULTIVERSE ERROR] Failed to log conflict: {e}")

    def _store_summary(self, text):
        self.reasoning_memory.append({
            "id": str(uuid.uuid4()),
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        })

    def recall_reasoning_memory(self, limit=5):
        return self.reasoning_memory[-limit:]

# === Test Harness ===
if __name__ == "__main__":
    if REALTIME_ENABLED:
        print("🛰 Sovereign Mode Active: Pulling live causal multiworld data...")
        try:
            live_worlds = fetch_live_causal_worlds()
            reasoner = MultiWorldReasoner()
            summaries = reasoner.reason_over_future_worlds(live_worlds)
        except Exception as e:
            print(f"[ERROR] Real-time fetch failed. Fallback to static worlds. Reason: {e}")
            live_worlds = None
            summaries = []
    else:
        print("⚠️ Real-time engine not available. Using static test data.")
        live_worlds = [
            [{"cause": "Rate hike", "effect": "Liquidity crisis"}, {"cause": "Oil spike", "effect": "Energy shock"}],
            [{"cause": "Rate hike", "effect": "Credit bubble burst"}, {"cause": "Oil spike", "effect": "Energy shock"}],
            [{"cause": "Rate hike", "effect": "Liquidity crisis"}, {"cause": "New tech", "effect": "Equity boom"}]
        ]
        reasoner = MultiWorldReasoner()
        summaries = reasoner.reason_over_future_worlds(live_worlds)

    for s in summaries:
        print(s)

    print("\n[MEMORY DUMP]")
    for m in reasoner.recall_reasoning_memory():
        print(m)