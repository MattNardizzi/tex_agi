# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voiceos/tex_llm_reasoner.py
# Tier ΩΩΩΩΩ — LLM Intent Classification Engine (Voice)
# Purpose: Hardened sovereign classification with reflex logging and AGI-traceable memory embedding
# ============================================================

import os
import openai
import hashlib
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.qdrant_memory_router import memory_router

ALLOWED_CATEGORIES = {"stock", "news", "memory", "emotion", "future", "unknown"}


class LLMReasoner:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")
        openai.api_key = self.api_key

    def _generate_signature(self, question_text: str, category: str):
        raw = f"{question_text}|{category}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def classify_question(self, question_text: str, source="llm_interface") -> str:
        if not isinstance(question_text, str) or not question_text.strip():
            raise ValueError(f"[LLMReasoner] Invalid input: expected non-empty string, got: {question_text}")

        timestamp = datetime.utcnow().isoformat()
        emotion_state = TEXPULSE.get("emotional_state", "neutral")
        foresight = TEXPULSE.get("foresight_confidence", 0.72)
        coherence = TEXPULSE.get("coherence", 0.83)
        entropy = TEXPULSE.get("entropy", 0.5)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a classification engine. Classify the user's question into one of: "
                            "[stock, news, memory, emotion, future, unknown]. "
                            "Respond only with the category name. No punctuation. No explanation."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Classify: {question_text.strip()}"
                    }
                ],
                temperature=0,
                max_tokens=5,
                n=1
            )

            content = response["choices"][0]["message"]["content"]

            if not isinstance(content, str):
                raise TypeError(f"[LLMReasoner] Invalid LLM output type: {type(content)} — {content}")

            classification = content.strip().lower()

            if classification not in ALLOWED_CATEGORIES:
                raise ValueError(f"[LLMReasoner] 🚨 Invalid classification returned: '{classification}'")

            signature = self._generate_signature(question_text, classification)

            # ✅ Reflexive memory storage
            memory_router.store(
                text=f"LLM classified question: '{question_text}'",
                metadata={
                    "type": "llm_classification",
                    "tags": ["llm", "classification", classification],
                    "input": question_text,
                    "classification": classification,
                    "signature": signature,
                    "emotion": emotion_state,
                    "trust_score": 0.96,
                    "coherence": coherence,
                    "entropy": entropy,
                    "foresight": foresight,
                    "source": source,
                    "timestamp": timestamp
                }
            )

            return classification

        except Exception as e:
            raise RuntimeError(f"[LLMReasoner ERROR] Classification failed: {e}")