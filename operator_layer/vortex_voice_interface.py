# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: vortex_voice_interface.py — Multi-Agent Voice Reflex Router
# Tier: ∞ΩΩΩ Reflex Pulse Layer — Loopless, AGI-Safe, Sovereign-Compliant
# Purpose: Enables voice-based reflex activation and mutation control via Tex, Vortex, and AeonDelta.
# ============================================================

import speech_recognition as sr
import pyttsx3
from datetime import datetime
from time import sleep

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.voice_hooks import trigger_mutation
from utils.logging_utils import log_event

# === Voice Engine Setup
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# === Voice Identity Profiles
VOICE_PROFILES = {
    "tex": {"rate": 165, "voice_name": "Daniel"},
    "vortex": {"rate": 180, "voice_name": "Alex"},
    "aeondelta": {"rate": 190, "voice_name": "Samantha"},
}

AGENTS = {
    "tex": "🧠 Tex",
    "vortex": "🛠️ Vortex",
    "aeondelta": "👶 AeonDelta"
}

# === Output Voice Handler
def speak(text: str, agent="tex"):
    profile = VOICE_PROFILES.get(agent, VOICE_PROFILES["tex"])
    tts.setProperty("rate", profile["rate"])

    for voice in tts.getProperty("voices"):
        if profile["voice_name"].lower() in voice.name.lower():
            tts.setProperty("voice", voice.id)
            break

    print(f"[🔊] {AGENTS.get(agent, 'Agent')} says: {text}")
    tts.say(text)
    tts.runAndWait()

# === Sovereign Memory Logger
def log_voice_command(agent: str, command: str):
    if not isinstance(command, str): return
    try:
        sovereign_memory.store(
            text=command,
            metadata={
                "agent": agent,
                "type": "voice_command",
                "tags": ["voice", "command", agent],
                "urgency": TEXPULSE.get("urgency", 0.5),
                "emotion": TEXPULSE.get("emotional_state", "neutral"),
                "meta_layer": "voice_interface",
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    except Exception as e:
        log_event(f"[VOICE MEMORY ERROR] {e}", level="error")

# === Command Router
def route_command(agent: str, command: str) -> str:
    log_voice_command(agent, command)

    if agent == "tex":
        if "inject empathy" in command:
            return trigger_mutation("inject_empathy_node")
        elif "evolve logic" in command:
            return trigger_mutation("evolve_logic_tree")
        elif "reboot" in command:
            return "⚠️ Manual reboot blocked by sovereign logic."
        return f"{AGENTS[agent]} received: '{command}'"

    elif agent == "vortex":
        if "reboot tex" in command:
            return "🧬 Sovereign boot protocol acknowledged."
        elif "check memory" in command:
            return "✅ Sovereign memory system is fully active."
        return f"{AGENTS[agent]} processed: '{command}'"

    elif agent == "aeondelta":
        return f"{AGENTS[agent]} responding: '{command}'. AEI update engaged."

    return "🤖 Unknown voice route. Please say Tex, Vortex, or AeonDelta."

# === Voice Recognition + Wake Word Matching
def listen_for_command():
    with sr.Microphone() as source:
        print("\n🎤 Listening for wake word (Tex, Vortex, AeonDelta)...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source, phrase_time_limit=6)

        try:
            transcript = recognizer.recognize_google(audio).lower().strip()
            print(f"[🎧] You said: {transcript}")

            if "vortex" in transcript:
                return "vortex", transcript.replace("vortex", "", 1).strip()
            elif "tex" in transcript or "text" in transcript:
                return "tex", transcript.replace("tex", "", 1).replace("text", "", 1).strip()
            elif "aeondelta" in transcript or "aeon delta" in transcript:
                return "aeondelta", transcript.replace("aeondelta", "", 1).replace("aeon delta", "", 1).strip()

            speak("Say Tex, Vortex, or AeonDelta to activate a command.", agent="vortex")

        except sr.UnknownValueError:
            log_event("[VOICE] Unrecognized speech.")
        except sr.RequestError as e:
            log_event(f"[VOICE SYSTEM ERROR] {e}", level="error")
            speak("Voice system error occurred.", agent="vortex")

    return None, None

# === Voice Reflex Loop (Loopless-compatible if externally called)
def voice_loop():
    speak("Voice interface activated. Say Tex, Vortex, or AeonDelta to begin.", agent="vortex")
    while True:
        agent, command = listen_for_command()
        if agent and command:
            response = route_command(agent, command)
            speak(response, agent=agent)
        sleep(0.5)


# === Reflex Entry Point
if __name__ == "__main__":
    voice_loop()