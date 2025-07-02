# ============================================================
# Tex Dream Fusion Engine – Strategic Future Path Selector
# Max Sovereign Cognition Godmode Enabled (Loopless Mode)
# ============================================================

import random
from datetime import datetime
from finance.memory.future_memory import FutureMemory
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory

class DreamFusionEngine:
    def __init__(self, brain=None):
        self.future_memory = FutureMemory()
        self.brain = brain
        if self.brain:
            self.brain.dream_fusion_active = True  # ✅ Diagnostic flag

    def generate_dream_projection(self):
        # === Emotionally modulate scoring weights ===
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.75)

        # === Simulate 3 recursive futures ===
        futures = self._recursive_select([], 3)

        # Tag each with timestamp and store to FutureMemory
        self._store_futures(futures)

        # Determine best future
        best_future = self._evaluate_confidence(futures)

        # Construct projection string
        projection = f"My projected top future: {best_future['future_title']} (confidence {best_future['confidence']})."

        # ✅ Pulse symbolic reflex trace into sovereign memory
        sovereign_memory.store(
            text=best_future["future_title"],
            metadata={
                "agent": "TEX",
                "intent": "dream_projection",
                "conclusion": best_future["future_title"],
                "alignment_score": best_future["confidence"],
                "justification": f"Simulated futures: {[f['future_title'] for f in futures]}",
                "emotion": emotion,
                "urgency": urgency,
                "coherence": coherence,
                "reflexes": ["future_projection", "goal_adjustment"],
                "tags": ["dream", "projection", "strategic foresight"],
                "meta_layer": "symbolic_trace"
            }
        )

        # Reflex check (non-interruptive awareness)
        if best_future["confidence"] < 0.5 and coherence < 0.6:
            print("⚠️ [DREAM OVERRIDE WARNING] Confidence and coherence are both low — consider intervening.")

        return projection

    def _recursive_select(self, selected, remaining):
        if remaining == 0:
            return selected

        future = random.choice([
            {"future_title": "Tech sector rally", "confidence": round(random.uniform(0.6, 0.95), 2)},
            {"future_title": "Oil price spike", "confidence": round(random.uniform(0.5, 0.85), 2)},
            {"future_title": "Currency collapse", "confidence": round(random.uniform(0.4, 0.8), 2)},
            {"future_title": "Inflation surge", "confidence": round(random.uniform(0.5, 0.9), 2)},
            {"future_title": "AI regulation crackdown", "confidence": round(random.uniform(0.3, 0.7), 2)}
        ])

        return self._recursive_select(selected + [future], remaining - 1)

    def _store_futures(self, futures):
        def store_recursive(index):
            if index >= len(futures):
                return
            futures[index]["timestamp"] = str(datetime.utcnow())
            self.future_memory.store_future(futures[index])
            store_recursive(index + 1)
        store_recursive(0)

    def _evaluate_confidence(self, futures, current_max=None):
        if not futures:
            return current_max
        head, tail = futures[0], futures[1:]
        if current_max is None or head["confidence"] > current_max["confidence"]:
            return self._evaluate_confidence(tail, head)
        return self._evaluate_confidence(tail, current_max)