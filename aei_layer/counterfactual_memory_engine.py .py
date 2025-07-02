# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/counterfactual_memory_engine.py
# Purpose: Counterfactual Time Reversal Memory (CTRM) Engine
# Description: Simulates alternate pasts to refine decision evolution
# ============================================================

import random
import json
import os
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import fetch_memory_entries, store_to_memory
from core_layer.emotion_heuristics import evaluate_emotion_state

class CounterfactualMemoryEngine:
    def __init__(self, archive_path="memory_archive/tex.jsonl"):
        self.archive_path = archive_path
        self.snapshot_cache = []
        self.last_revision = None

    def sample_memories(self, limit=25):
        try:
            memories = fetch_memory_entries("tex", limit=limit)
            self.snapshot_cache = [m for m in memories if m.get("spoken")]
            return self.snapshot_cache
        except Exception as e:
            print(f"[CTRM] ⚠️ Error fetching memories: {e}")
            return []

    def reverse_and_rewrite(self):
        if not self.snapshot_cache:
            self.sample_memories()

        if not self.snapshot_cache:
            print("[CTRM] ⚠️ No valid memories to reverse.")
            return None

        counterfactuals = []
        for mem in self.snapshot_cache:
            original = mem.get("spoken", "")
            reversed_logic = self._invert_logic(original)
            regret_score = round(random.uniform(0.4, 0.95), 2)
            alt_emotion, alt_urgency, alt_coherence = evaluate_emotion_state(reversed_logic)

            snapshot = {
                "original": original,
                "counterfactual": reversed_logic,
                "emotion": alt_emotion,
                "urgency": alt_urgency,
                "coherence": alt_coherence,
                "regret_score": regret_score,
                "timestamp": datetime.utcnow().isoformat(),
                "cycle": TEXPULSE.get("cycle", 0)
            }
            counterfactuals.append(snapshot)

            store_to_memory("ct_counterfactuals", snapshot)

        self.last_revision = counterfactuals[-1] if counterfactuals else None
        print(f"[CTRM] 🌀 Generated {len(counterfactuals)} alternate reality trace(s).")
        return counterfactuals

    def _invert_logic(self, statement):
        """
        Simple heuristic to reverse key logic signals in Tex's output.
        """
        inversions = {
            "should": "should not",
            "will": "will not",
            "can": "cannot",
            "increase": "decrease",
            "buy": "sell",
            "long": "short",
            "safe": "risky",
            "opportunity": "threat",
            "bullish": "bearish",
            "likely": "unlikely",
        }
        for key, val in inversions.items():
            if key in statement:
                statement = statement.replace(key, val)
        return statement

# === Singleton interface ===
_ct_engine = CounterfactualMemoryEngine()

def run_ct_revision():
    return _ct_engine.reverse_and_rewrite()

def get_last_counterfactual():
    return _ct_engine.last_revision