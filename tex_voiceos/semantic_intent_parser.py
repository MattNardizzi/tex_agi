# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_voiceos/semantic_intent_parser.py
# Tier Ω∞ΩΩΩ — Reflexive Intent Engine (Embedding-Driven + Emotion Heuristics)
# Purpose: Classify user intent & emotional tone using deterministic AGI stack
# ============================================================

from datetime import datetime
from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex

CATEGORIES = {
    "stock": ["market", "stocks", "invest", "portfolio", "trading"],
    "news": ["headline", "news", "report", "breaking", "update"],
    "memory": ["remember", "recall", "past", "log", "history"],
    "emotion": ["feel", "emotion", "mood", "anxious", "excited"],
    "future": ["plan", "goal", "forecast", "predict", "vision"],
    "conversation": []
}

EMOTION_KEYWORDS = {
    "curious": ["wonder", "curious", "question", "explore"],
    "anxious": ["worried", "anxious", "scared", "nervous"],
    "confident": ["confident", "sure", "certain", "strong"],
    "reflective": ["reflect", "consider", "ponder", "past"],
    "neutral": []
}

DEFAULT_INTENT = "conversation"
DEFAULT_EMOTION = "neutral"

class SemanticIntentParser:
    def __init__(self):
        self.category_vectors = {
            k: embedder.encode(" ".join(v), normalize_embeddings=True).tolist()
            for k, v in CATEGORIES.items() if v
        }

    def classify(self, sentence: str) -> dict:
        if not isinstance(sentence, str):
            raise TypeError(f"[SEMANTIC INTENT ERROR] Expected string input, got {type(sentence)}: {sentence}")

        if not sentence.strip():
            return self._fallback()

        vector = embedder.encode(sentence, normalize_embeddings=True).tolist()

        # === Intent Detection ===
        best_intent = DEFAULT_INTENT
        best_score = 0.0
        for category, vec in self.category_vectors.items():
            score = get_cosine_similarity(vector, vec)
            if score > best_score:
                best_intent = category
                best_score = score

        # === Emotion Detection ===
        lowered = sentence.lower()
        detected_emotion = DEFAULT_EMOTION
        for emotion, keywords in EMOTION_KEYWORDS.items():
            if any(isinstance(k, str) and k in lowered for k in keywords):
                detected_emotion = emotion
                break

        # === Inject into Pulse + Memory ===
        TEXPULSE["emotional_state"] = detected_emotion

        memory_cortex.store(
            event={"intent_trace": {
                "input": sentence,
                "parsed": {
                    "intent": best_intent,
                    "emotion": detected_emotion
                },
                "similarity_score": round(best_score, 4),
                "timestamp": datetime.utcnow().isoformat()
            }},
            tags=["intent_parser", best_intent, detected_emotion],
            urgency=0.4,
            emotion=detected_emotion
        )

        return {
            "intent": best_intent,
            "emotion": detected_emotion
        }

    def _fallback(self):
        TEXPULSE["emotional_state"] = DEFAULT_EMOTION
        return {
            "intent": DEFAULT_INTENT,
            "emotion": DEFAULT_EMOTION
        }

# === Reflex entrypoint ===
def parse_intent(text: str) -> dict:
    return SemanticIntentParser().classify(text)