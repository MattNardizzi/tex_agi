# File: core_layer/goal_mutator.py

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal
import random

def mutate_goal_state():
    """
    Shifts Tex’s internal urgency/emotion to evolve goal alignment.
    """
    drift_chance = random.random()

    if drift_chance > 0.7:
        prior_urgency = TEXPULSE["urgency"]
        prior_emotion = TEXPULSE["emotion"]

        # Drift urgency and emotion slightly
        TEXPULSE["urgency"] = min(1.0, max(0.0, prior_urgency + random.uniform(-0.1, 0.1)))
        TEXPULSE["emotion"] = random.choice([
            "curious", "focused", "uneasy", "strategic", "detached", "accelerated"
        ])

        dispatch_signal("goal_mutation", payload={
            "previous_urgency": prior_urgency,
            "new_urgency": TEXPULSE["urgency"],
            "previous_emotion": prior_emotion,
            "new_emotion": TEXPULSE["emotion"],
            "reason": "autonomous drift"
        })