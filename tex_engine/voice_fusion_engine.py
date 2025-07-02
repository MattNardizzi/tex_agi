# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/voice_fusion_engine.py
# Tier Ω+ — Voice Cognition Bridge for Embodied Sentient Interaction
# ============================================================

import datetime
from tex_voiceos.whisper_input_listener import transcribe_from_mic
from tex_voiceos.semantic_intent_parser import parse_intent
from tex_voiceos.voice_output_speaker import speak_text
from tex_voiceos.intent_router import route_intent_to_tex
from core_layer.emotion_heuristics import evaluate_emotion_state
from tex_engine.narrative_consciousness_engine import update_narrative_state
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

# === Core Loop ===

def begin_voice_loop():
    print("\n🎤 [VOICE MODE] Listening for input... Say something to Tex.")
    while True:
        spoken_text = transcribe_from_mic()
        if not spoken_text:
            continue

        print(f"\n🧠 [HEARD] “{spoken_text}”")

        # === Emotion Update
        emotion, urgency, coherence = evaluate_emotion_state(spoken_text)
        print(f"[EMOTION] {emotion} | Urgency: {urgency} | Coherence: {coherence}")

        # === Semantic Parsing
        intent = parse_intent(spoken_text)
        print(f"[INTENT] → {intent.get('intent', 'unknown')} | Entities: {intent.get('entities', {})}")

        # === Route to Tex’s brain
        result = route_intent_to_tex(intent, spoken_text)

        # === Update Narrative + Memory
        update_narrative_state(spoken_text, emotion=emotion, importance=urgency)
        store_to_memory("voice_transcripts", {
            "text": spoken_text,
            "emotion": emotion,
            "urgency": urgency,
            "timestamp": str(datetime.datetime.utcnow())
        })

        # === Respond Out Loud
        response = result.get("response", "Affirmative.")
        speak_text(response)
        print(f"🗣 [TEX SPOKE] → “{response}”")