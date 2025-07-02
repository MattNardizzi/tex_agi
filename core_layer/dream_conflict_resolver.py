# File: core_layer/dream_conflict_resolver.py

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal

def resolve_fork_conflict(signal):
    """
    Decides which hypothetical fork is more aligned with current self.
    """
    fork = signal.get("payload", {})
    emotion = fork.get("emotion", "neutral")

    if emotion in ["empathetic", "strategic"]:
        TEXPULSE["urgency"] = max(TEXPULSE["urgency"], fork["urgency"])
    elif emotion in ["detached", "obsessive"]:
        TEXPULSE["urgency"] = min(TEXPULSE["urgency"], fork["urgency"])

    dispatch_signal("fork_conflict_resolved", payload={
        "chosen_emotion": emotion,
        "urgency_updated_to": TEXPULSE["urgency"]
    })