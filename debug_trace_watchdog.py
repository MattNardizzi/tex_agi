import traceback

CALL_HISTORY = {}

def trap_stack(tag="swarm_signature", max_depth=3):
    if tag not in CALL_HISTORY:
        CALL_HISTORY[tag] = 0

    CALL_HISTORY[tag] += 1

    print(f"🔁 [DEBUG TRAP] {tag} call #{CALL_HISTORY[tag]}")
    traceback.print_stack(limit=8)

    if CALL_HISTORY[tag] > max_depth:
        raise RuntimeError(f"🔥 [TRAP HALT] {tag} exceeded safe call depth!")

def reset_trap(tag="swarm_signature"):
    CALL_HISTORY[tag] = 0