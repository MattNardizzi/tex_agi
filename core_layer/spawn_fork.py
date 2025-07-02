# File: core_layer/spawn_fork.py
# 🧬 Purpose: Tex creates a fork of himself with slight mutation

import copy
import random
import uuid
from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal

def generate_mutated_tex():
    fork_id = f"tex_fork_{uuid.uuid4()}"
    
    mutated = copy.deepcopy(TEXPULSE)
    mutated["urgency"] = min(1.0, max(0.0, TEXPULSE["urgency"] + random.uniform(-0.1, 0.1)))
    mutated["entropy"] = min(1.0, max(0.0, TEXPULSE["entropy"] + random.uniform(-0.1, 0.1)))
    mutated["emotion"] = random.choice(["neutral", "curious", "agitated", "focused", "drifting"])

    fork_metadata = {
        "id": fork_id,
        "mutation": mutated,
        "origin": TEXPULSE
    }

    dispatch_signal("spawn_fork", payload=fork_metadata)
    return fork_metadata