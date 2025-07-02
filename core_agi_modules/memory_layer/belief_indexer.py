# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: core_agi_modules/memory_layer/belief_indexer.py
# Tier ΩΩΩ — Belief Indexer Cortex: Drift-Aware, Reflex-Linked, Contradiction-Auditing
# ============================================================

import hashlib
import difflib
from datetime import datetime

class BeliefIndexer:
    def __init__(self):
        self.index = {}  # belief_id → metadata

    def imprint(self, belief: str, source: str = "unknown", emotion: str = "neutral", tags: list = None, trust_score: float = 1.0):
        belief_id = self._hash(belief)
        timestamp = datetime.utcnow().isoformat()

        if belief_id in self.index:
            print(f"🧠 [BELIEF INDEX] 🔄 Already indexed: {belief_id[:10]}")
            return belief_id

        self.index[belief_id] = {
            "text": belief,
            "tags": tags or ["belief"],
            "emotion": emotion,
            "trust_score": trust_score,
            "timestamp": timestamp,
            "source": source,
            "updates": 1,
            "drift_score": 0.0,
            "history": [],
            "contradictions_with": []
        }
        print(f"📌 [BELIEF INDEX] ✅ Registered: {belief_id[:10]} | Source: {source} | Tags: {tags}")
        return belief_id

    def update(self, belief_id: str, new_text: str, trust_delta: float = 0.0):
        if belief_id not in self.index:
            print(f"⚠️ [BELIEF INDEX] Unknown belief ID: {belief_id}")
            return

        belief = self.index[belief_id]
        old_text = belief["text"]
        belief["history"].append(old_text)

        drift = self._drift_score(old_text, new_text)
        belief["text"] = new_text
        belief["trust_score"] = max(0.0, min(1.0, belief["trust_score"] + trust_delta))
        belief["timestamp"] = datetime.utcnow().isoformat()
        belief["updates"] += 1
        belief["drift_score"] = drift

        print(f"🔁 [BELIEF UPDATE] {belief_id[:10]} | Δtrust={trust_delta} | Drift={drift}")
        return belief

    def register_contradiction(self, source_id: str, conflict_id: str):
        if source_id in self.index:
            self.index[source_id].setdefault("contradictions_with", []).append(conflict_id)
        if conflict_id in self.index:
            self.index[conflict_id].setdefault("contradictions_with", []).append(source_id)
        print(f"⚡ [BELIEF CONTRADICTION] {source_id[:10]} ↔ {conflict_id[:10]}")

    def get_by_tag(self, tag: str):
        return [b for b in self.index.values() if tag in b.get("tags", [])]

    def all_beliefs(self):
        return list(self.index.values())

    def belief_exists(self, text: str) -> bool:
        return self._hash(text) in self.index

    def _hash(self, text: str):
        return hashlib.sha256(text.encode()).hexdigest()

    def _drift_score(self, a: str, b: str):
        return round(1.0 - difflib.SequenceMatcher(None, a, b).ratio(), 4)