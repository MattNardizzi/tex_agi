# File: core_layer/survivor_merge.py

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal

def absorb_fork(fork_payload):
    mutation = fork_payload["mutation"]
    
    TEXPULSE["urgency"] = (TEXPULSE["urgency"] + mutation["urgency"]) / 2
    TEXPULSE["entropy"] = (TEXPULSE["entropy"] + mutation["entropy"]) / 2
    TEXPULSE["emotion"] = mutation["emotion"]

    dispatch_signal("merge_success", payload={"source": fork_payload["id"], "new_self": TEXPULSE})