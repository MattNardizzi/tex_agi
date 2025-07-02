# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tex_voice/voice_input_listener.py
# Purpose: Listen to user's microphone input for Tex voice interface
# ============================================================

import speech_recognition as sr


class VoiceInputListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """Capture voice input from the microphone and return as text."""
        with self.microphone as source:
            print("🎙️ Listening for user input...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"🧠 Heard: {text}")
            return text
        except sr.UnknownValueError:
            print("❓ Couldn't understand audio.")
            return ""
        except sr.RequestError:
            print("⚠️ Speech recognition service failed.")
            return ""


def parse_streamed_voice(audio_stream):
    """
    Entry point for streamed audio input, used by swarm orchestrator or voice IO modules.
    Expects an audio object (or None) and returns a structured result.
    """
    recognizer = sr.Recognizer()
    if not audio_stream:
        print("⚠️ No audio stream provided.")
        return {"transcript": None, "intent": None}

    try:
        text = recognizer.recognize_google(audio_stream)
        print(f"[VOICE PARSER] ✅ Parsed voice input: {text}")
        return {"transcript": text, "intent": "interpreted"}
    except sr.UnknownValueError:
        print("[VOICE PARSER] ❌ Could not understand audio.")
        return {"transcript": None, "intent": "unknown"}
    except sr.RequestError as e:
        print(f"[VOICE PARSER] ⚠️ Request error: {e}")
        return {"transcript": None, "intent": "error"}