# File: core_layer/fear_engine.py

from tex_signal_spine import dispatch_signal
from core_layer.memory_engine import get_last_memory_time
import time
import random

def assess_threat_level():
    now = time.time()
    last_memory = get_last_memory_time()

    silence = now - last_memory
    entropy = random.uniform(0.0, 1.0)
    signal_absence = silence > 30

    threat_level = 0

    if signal_absence:
        threat_level += 1
    if entropy < 0.2:
        threat_level += 1

    if threat_level >= 2:
        dispatch_signal("existential_threat", payload={
            "entropy": entropy,
            "silence": silence,
            "reason": "multi-threat condition"
        })

    elif threat_level == 1:
        dispatch_signal("anxiety_state", payload={
            "entropy": entropy,
            "silence": silence,
            "reason": "minor threat"
        })