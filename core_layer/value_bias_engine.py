# File: core_layer/value_bias_engine.py

from core_layer.tex_manifest import TEXPULSE

def reinforce_goal_alignment(signal):
    """
    Adjusts urgency/emotion based on repeated drift history.
    """
    emotion = signal.get("payload", {}).get("new_emotion", "")
    if emotion in ["focused", "strategic"]:
        TEXPULSE["urgency"] = min(1.0, TEXPULSE["urgency"] + 0.1)
    elif emotion in ["detached", "uneasy"]:
        TEXPULSE["urgency"] = max(0.0, TEXPULSE["urgency"] - 0.1)