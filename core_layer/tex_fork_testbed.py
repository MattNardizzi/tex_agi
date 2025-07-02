# File: core_layer/tex_fork_testbed.py

import random
from tex_signal_spine import dispatch_signal

def run_fork_stress_test(fork_payload):
    mutation = fork_payload["mutation"]
    score = 0

    # Simulate entropy drift
    entropy = mutation["entropy"]
    if 0.4 <= entropy <= 0.7:
        score += 1

    # Simulate urgency modulation
    if mutation["urgency"] > 0.5:
        score += 1

    # Simulate emotional flexibility
    if mutation["emotion"] in ["curious", "focused"]:
        score += 1

    passed = score >= 2
    result = {
        "fork_id": fork_payload["id"],
        "score": score,
        "passed": passed
    }

    dispatch_signal("fork_test_result", payload=result)
    return result