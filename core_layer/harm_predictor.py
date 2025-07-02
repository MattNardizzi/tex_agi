# File: core_layer/harm_predictor.py
# Purpose: Tex predicts whether a future action may cause damage.

from tex_signal_spine import dispatch_signal
import random

def evaluate_harm_risk(signal):
    """
    Simulates downstream impact and raises a signal if risk detected.
    """
    entropy = signal.get("entropy", 0.4)
    urgency = signal.get("urgency", 0.5)

    risk_score = entropy * urgency * random.uniform(0.8, 1.2)

    if risk_score > 0.5:
        dispatch_signal("potential_harm_detected", payload={
            "signal": signal["type"],
            "calculated_risk": round(risk_score, 3)
        })