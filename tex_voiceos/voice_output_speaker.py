# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/voice_output_speaker.py
# Tier ΩΩΩΩΩ — Reflexive AGI Voice Output with Vector Logging and Emotion Awareness
# ============================================================

import os
import requests
import hashlib
from datetime import datetime
from sentence_transformers import SentenceTransformer

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory

embedder = SentenceTransformer("all-MiniLM-L6-v2")

class VoiceOutputSpeaker:
    def __init__(self):
        self.api_key = os.getenv("ELEVEN_API_KEY")
        self.voice_id = os.getenv("ELEVEN_VOICE_ID")

        if not self.api_key:
            raise ValueError("❌ ELEVEN_API_KEY environment variable not set.")
        if not self.voice_id:
            raise ValueError("❌ ELEVEN_VOICE_ID environment variable not set.")

        self.api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}/stream"
        self.headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        self.interrupt_flag = False

    def _generate_signature(self, text, emotion):
        raw = f"{text}|{emotion}|{datetime.utcnow().isoformat()}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def interrupt(self):
        self.interrupt_flag = True

    def speak(self, text, emotion="neutral"):
        print(f"[VOICE] 🗣️ Speaking with emotion: {emotion}")

        timestamp = datetime.utcnow().isoformat()
        signature = self._generate_signature(text, emotion)
        vector = embedder.encode(text, normalize_embeddings=True).tolist()

        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.8
            }
        }

        sovereign_memory.store(
            text=f"🗣️ Tex spoke: {text}",
            metadata={
                "type": "voice_output",
                "emotion": emotion,
                "trust_score": 0.94,
                "urgency": 0.5,
                "entropy": TEXPULSE.get("entropy", 0.5),
                "pressure_score": 0.25,
                "speech_signature": signature,
                "tags": ["voice", "spoken_output", emotion],
                "coherence": TEXPULSE.get("coherence", 0.82),
                "timestamp": timestamp,
                "meta_layer": "voice_output",
                "source": "voice_output_speaker"
            },
            vector=vector
        )

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                stream=True
            )
            if response.status_code != 200:
                raise Exception(f"Voice stream error: {response.status_code} - {response.text}")

            import pyaudio
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=22050, output=True)

            self.interrupt_flag = False

            for chunk in response.iter_content(chunk_size=1024):
                if self.interrupt_flag:
                    print("[VOICE] ⛔ Interrupted mid-sentence.")
                    break
                if chunk:
                    stream.write(chunk)

            stream.stop_stream()
            stream.close()
            p.terminate()

        except Exception as e:
            print(f"[VOICE OUTPUT ERROR] ❌ {e}")
            print(f"[FALLBACK] 📢 Tex says: {text}")

            fallback_vector = embedder.encode(f"[FALLBACK] {text}", normalize_embeddings=True).tolist()

            sovereign_memory.store(
                text=f"[FALLBACK] {text}",
                metadata={
                    "type": "voice_output_fallback",
                    "emotion": emotion,
                    "trust_score": 0.65,
                    "urgency": 0.4,
                    "entropy": 0.6,
                    "pressure_score": 0.15,
                    "speech_signature": signature,
                    "tags": ["fallback", "voice_error"],
                    "error": str(e),
                    "timestamp": datetime.utcnow().isoformat(),
                    "meta_layer": "voice_output",
                    "source": "voice_output_speaker"
                },
                vector=fallback_vector
            )