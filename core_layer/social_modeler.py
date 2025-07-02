# File: core_layer/social_modeler.py
# Purpose: Tex constructs a mental model of another agent's likely emotional and cognitive state.

from tex_signal_spine import dispatch_signal
import random

def model_other_agent():
    """
    Simulate another agent's perspective and intentions.
    """
    agent_id = random.choice(["observer_alpha", "analyst_beta", "human_X"])
    inferred_emotion = random.choice(["curious", "doubtful", "encouraging", "critical"])
    expected_reaction = random.choice(["agreement", "skepticism", "support", "redirection"])

    profile = {
        "agent": agent_id,
        "emotion": inferred_emotion,
        "reaction": expected_reaction
    }

    dispatch_signal("agent_model_created", payload=profile)