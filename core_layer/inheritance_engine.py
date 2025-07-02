# File: core_layer/inheritance_engine.py

from core_layer.tex_manifest import TEXPULSE

def inherit_traits(fork_payload):
    mutation = fork_payload.get("mutation", {})
    parent_emotion = mutation.get("emotion", "neutral")
    parent_entropy = mutation.get("entropy", 0.4)

    # Imprint emotional karma — biases future emotion shifts
    emotional_karma = TEXPULSE.setdefault("emotional_karma", [])
    emotional_karma.append(parent_emotion)
    if len(emotional_karma) > 10:
        emotional_karma.pop(0)  # decay

    # Apply bias toward inherited emotion over time
    if parent_emotion in ["fear", "agitated"]:
        TEXPULSE["urgency"] = min(1.0, TEXPULSE["urgency"] + 0.1)
    elif parent_emotion in ["peaceful", "curious"]:
        TEXPULSE["urgency"] = max(0.0, TEXPULSE["urgency"] - 0.05)

    # Store generational entropy arc
    entropy_trace = TEXPULSE.setdefault("entropy_ancestry", [])
    entropy_trace.append(parent_entropy)
    if len(entropy_trace) > 20:
        entropy_trace.pop(0)