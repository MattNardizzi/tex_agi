# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/counterfactual_memory_engine.py
# Purpose: Counterfactual Time Reversal Memory (CTRM) Engine
# Tier: ΩΩΩΩΩΩ — Alternate History + Reflex Reversal Logic
# ============================================================

import random
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


class CounterfactualMemoryEngine:
    def __init__(self):
        self.snapshot_cache = []
        self.last_revision = None

    def sample_memories(self, limit=25):
        try:
            memories = sovereign_memory.recall_recent(minutes=180, top_k=limit)
            self.snapshot_cache = [m for m in memories if "spoken" in m.get("data", {})]
            return self.snapshot_cache
        except Exception as e:
            print(f"[CTRM] ⚠️ Error fetching symbolic memory: {e}")
            return []

    def reverse_and_rewrite(self):
        if not self.snapshot_cache:
            self.sample_memories()

        if not self.snapshot_cache:
            print("[CTRM] ⚠️ No valid memories to reverse.")
            fallback_memory = {
                "original": "Tex should evaluate risk exposure.",
                "counterfactual": "Tex should not evaluate risk exposure.",
                "emotion": "doubt",
                "urgency": 0.6,
                "coherence": 0.7,
                "regret_score": 0.83,
                "timestamp": datetime.utcnow().isoformat(),
                "cycle": TEXPULSE.get("cycle", 0)
            }
            sovereign_memory.store(text=fallback_memory["counterfactual"], metadata=fallback_memory)
            self.last_revision = fallback_memory
            print("[CTRM] 🧠 Injected fallback counterfactual.")
            return [fallback_memory]

        counterfactuals = []
        for mem in self.snapshot_cache:
            original = mem["data"].get("spoken", "")
            reversed_logic = self._invert_logic(original)
            regret_score = round(random.uniform(0.4, 0.95), 2)

            # ✅ Scoped import to avoid circular import
            from core_layer.emotion_heuristics import evaluate_emotion_state
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
            sovereign_memory.store(text=reversed_logic, metadata=snapshot)

        self.last_revision = counterfactuals[-1] if counterfactuals else None
        print(f"[CTRM] 🌀 Generated {len(counterfactuals)} counterfactual trace(s).")
        return counterfactuals

    def _invert_logic(self, statement: str) -> str:
        inversions = {
            "should": "should not", "will": "will not", "can": "cannot",
            "increase": "decrease", "buy": "sell", "long": "short",
            "safe": "risky", "opportunity": "threat", "bullish": "bearish",
            "likely": "unlikely"
        }
        for key, val in inversions.items():
            if key in statement:
                statement = statement.replace(key, val)
        return statement

    def log_default_counterfactual(self):
        default = {
            "timestamp": datetime.utcnow().isoformat(),
            "original": "Tex should consider a diversified portfolio.",
            "counterfactual": "Tex should not consider a diversified portfolio.",
            "emotion": "neutral",
            "urgency": 0.5,
            "coherence": 0.7,
            "regret_score": 0.8,
            "cycle": TEXPULSE.get("cycle", 0)
        }
        sovereign_memory.store(text=default["counterfactual"], metadata=default)

    def counterfactual_memory_exists(self) -> bool:
        try:
            recent = sovereign_memory.recall_recent(minutes=120, top_k=20)
            for mem in recent:
                if "counterfactual" in mem.get("data", {}):
                    return True
        except Exception:
            pass
        return False


# === Sovereign Singleton Interface ===

_ct_engine = CounterfactualMemoryEngine()

def run_ct_revision():
    return _ct_engine.reverse_and_rewrite()

def get_last_counterfactual():
    return _ct_engine.last_revision

def counterfactual_memory_exists():
    return _ct_engine.counterfactual_memory_exists()

def log_default_counterfactual():
    return _ct_engine.log_default_counterfactual()