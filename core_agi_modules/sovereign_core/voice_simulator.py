# voice_simulator.py
# Tier Ω∞ Multi-Agent Voice Reasoning Simulator (Final Form)
# Location: core_agi_modules/sovereign_core/voice_simulator.py

from datetime import datetime
import uuid

# === Voice Personas ===
VOICES = {
    "Logic": {
        "bias": "rational",
        "weight": 0.4
    },
    "Emotion": {
        "bias": "feeling",
        "weight": 0.3
    },
    "Foresight": {
        "bias": "prediction",
        "weight": 0.2
    },
    "Doubt": {
        "bias": "skeptic",
        "weight": 0.1
    }
}

voice_history = {}  # Used to evolve voice weight

# === Internal Debate Simulator ===
def simulate_internal_dialogue(prompt: str):
    """
    Each internal voice responds to the prompt from its cognitive bias.
    Responses are scored and ranked by weight.
    Contradictions are flagged and voice weights adapt based on winner.
    """
    trace_id = str(uuid.uuid4())
    discussion = []

    for name, cfg in VOICES.items():
        style = cfg["bias"]
        response = generate_response(prompt, style)
        discussion.append({
            "voice": name,
            "bias": style,
            "weight": cfg["weight"],
            "response": response
        })

    for v in discussion:
        if "not" in v["response"]:
            for r in discussion:
                if r["voice"] != v["voice"] and "recommend" in r["response"]:
                    v["contradicts"] = True

    sorted_voices = sorted(discussion, key=lambda x: x["weight"], reverse=True)
    best = sorted_voices[0]

    # Adapt voice weights
    adapt_voice_weights(best["voice"])

    confidence = round(best["weight"] + sum(1 for v in discussion if v["voice"] != best["voice"] and best["bias"] in v["response"]) * 0.05, 4)

    print(f"🗣️ [VOICE SIM] Prompt: '{prompt}' | Winner: {best['voice']} | Confidence: {confidence}")
    return {
        "trace_id": trace_id,
        "responses": discussion,
        "winner": best["voice"],
        "selected_response": best["response"],
        "confidence": confidence,
        "timestamp": datetime.utcnow().isoformat()
    }

# === Adaptive Weight Trainer ===
def adapt_voice_weights(winner: str):
    for v in VOICES:
        if v == winner:
            VOICES[v]["weight"] = min(1.0, round(VOICES[v]["weight"] + 0.05, 4))
        else:
            VOICES[v]["weight"] = max(0.05, round(VOICES[v]["weight"] - 0.02, 4))

# === Mock Response Generator ===
def generate_response(prompt: str, style: str):
    return f"[{style.upper()} RESPONSE] On '{prompt}', I recommend we prioritize {style}."