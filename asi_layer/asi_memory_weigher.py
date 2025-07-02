# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: asi_layer/asi_memory_weigher.py
# Purpose: Prioritizes and ranks memories based on ASI criteria for foresight fidelity
# Status: MAX GODMODE — Enhanced with Mutation Bias Injection + Foresight Reinforcement
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import recall_recent, store_to_memory
from core_layer.tex_manifest import TEXPULSE


class ASIMemoryWeigher:
    def __init__(self):
        self.recent_limit = 50
        self.weight_log_path = "memory_archive/asi_memory_weights.jsonl"

    def evaluate(self, brain):
        try:
            memories = recall_recent(n=self.recent_limit)
            if not memories:
                print("[ASI MEMORY WEIGHER] ⚠️ No recent memories found.")
                return []

            weighted = []

            with open(self.weight_log_path, "a") as f:
                for m in memories:
                    thought = m.get("spoken", "")
                    urgency = m.get("urgency", 0.5)
                    coherence = m.get("coherence", 0.5)
                    emotion = m.get("emotion", "neutral")
                    timestamp = m.get("timestamp") or datetime.utcnow().isoformat()

                    score = self._score_memory(thought, urgency, coherence, emotion)

                    entry = {
                        "thought": thought,
                        "urgency": urgency,
                        "coherence": coherence,
                        "emotion": emotion,
                        "score": score,
                        "timestamp": timestamp
                    }

                    weighted.append(entry)
                    store_to_memory("asi_memory_weight", entry)
                    f.write(json.dumps(entry) + "\n")

            if not weighted:
                print("[ASI MEMORY WEIGHER] ⚠️ No memories were scored.")
                return []

            top = max(weighted, key=lambda x: x["score"])
            print(f"[ASI MEMORY WEIGHER] ✅ Top memory: '{top['thought']}' → Score: {top['score']:.3f}")

            self._inject_mutation_bias(top)
            self._reinforce_top_memory(top)

            return weighted

        except Exception as e:
            print(f"[ASI MEMORY WEIGHER ERROR] {e}")
            return []

    def _score_memory(self, thought, urgency, coherence, emotion):
        emotion_weight = {
            "resolve": 0.9, "fear": 0.7, "hope": 0.8,
            "urgent": 0.85, "curious": 0.75, "neutral": 0.5,
            "anxious": 0.65, "bold": 0.88, "reflective": 0.8
        }

        emotion_score = emotion_weight.get(emotion.lower(), 0.5)
        foresight_bias = TEXPULSE.get("urgency", 0.5) * 0.2

        return round(
            0.4 * coherence +
            0.3 * urgency +
            0.2 * emotion_score +
            0.1 * foresight_bias,
            4
        )

    def _inject_mutation_bias(self, top_memory):
        urgency = top_memory.get("urgency", 0.5)
        emotion = top_memory.get("emotion", "neutral").lower()

        # Influence mutation guidance system via memory injection
        if urgency > 0.8 or emotion in {"urgent", "bold", "resolve", "fear"}:
            store_to_memory("mutation_bias_signal", {
                "reason": "high_urgency_or_emotion",
                "triggered_by": top_memory.get("thought", ""),
                "timestamp": datetime.utcnow().isoformat(),
                "bias_mode": "reactive_override"
            })
            print(f"[⚡️ MUTATION BIAS] Injected urgency signal due to top memory: '{emotion}'")

    def _reinforce_top_memory(self, top_memory):
        """Resaves the top memory into long-term memory for future trait modeling."""
        reinforced = {
            **top_memory,
            "reinforced": True,
            "tag": "reinforced_foresight",
            "reinforced_at": datetime.utcnow().isoformat()
        }
        store_to_memory("reinforced_foresight", reinforced)
        print("[🧠 MEMORY] Top foresight reinforced into long-term memory.")