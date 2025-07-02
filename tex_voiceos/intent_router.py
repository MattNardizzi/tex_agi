# ============================================================
# Tex VoiceOS V3 — Godmode AGI Intent Router (Emotion-Aware)
# File: tex_voiceos/intent_router.py
# Author: Matthew Nardizzi / VortexBlack LLC
# Tier: ⚡ MAX — Zero-tolerance Cognitive Intent Classifier
# ============================================================

import os
import openai
from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import evaluate_emotion_state
from tex_voiceos.memory_router import MemoryRouter

ALLOWED_INTENTS = {"goal", "question", "memory", "emotion", "cancel", "unknown"}

class IntentRouter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("❌ OPENAI_API_KEY not set in environment.")
        openai.api_key = self.api_key
        self.memory = MemoryRouter()

    def classify(self, transcript: str) -> dict:
        if not isinstance(transcript, str) or not transcript.strip():
            raise ValueError(f"[INTENT ROUTER] Invalid transcript input: {transcript}")

        emotion, urgency, coherence = evaluate_emotion_state(transcript)

        # Inject live emotional signature into Tex's cognitive pulse
        TEXPULSE["emotional_state"] = emotion
        TEXPULSE["urgency"] = urgency
        TEXPULSE["coherence"] = coherence

        # Pull short-term memory trace
        memory_context = self.memory.recall_recent_transcripts(max_lines=4)
        memory_block = "\n".join(memory_context).strip()

        # Construct classification prompt
        system_prompt = (
            "You are a high-speed AGI intent classifier named Tex.\n"
            "You receive transcripts and short-term memory context.\n"
            "Classify the user statement with a single lowercase word from:\n"
            "[goal, question, memory, emotion, cancel, unknown]\n"
            "No punctuation. No extra output. One word only."
        )

        user_prompt = (
            f"Transcript: '{transcript.strip()}'\n\n"
            f"Memory Context:\n{memory_block}\n\n"
            f"What is the intent?"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=5,
                temperature=0.0
            )

            content = response["choices"][0]["message"]["content"]
            if not isinstance(content, str):
                raise TypeError(f"[INTENT ROUTER] Invalid LLM response: {type(content)} — {content}")

            intent = content.strip().lower()
            if intent not in ALLOWED_INTENTS:
                raise ValueError(f"[INTENT ROUTER] 🚨 Invalid classification: '{intent}'")

        except Exception as e:
            raise RuntimeError(f"[INTENT ROUTER] ❌ Classification failure: {e}")

        print(f"[INTENT ROUTER] 🧠 Intent: {intent} | Emotion: {emotion} | Urgency: {urgency} | Coherence: {coherence}")

        return {
            "intent": intent,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence
        }