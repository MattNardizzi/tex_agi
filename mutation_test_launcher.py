# mutation_test_launcher.py

import asyncio
from tex_signal_spine import dispatch_signal

async def trigger_mutation_reflex():
    await dispatch_signal("mutation_patch", {
        "reason": "contradiction detected in symbolic reflex history",
        "traits": [
            "reflex:substrate_mutate",
            "reflex:compiler_spawn",
            "reflex:collapse_reality"
        ],
        "justification": "mutation coherence protocol triggered",
        "target_module": "tex_manifest",
        "function": "TEXPULSE_integrity",
        "origin": "mutation_test_demo"
    }, urgency=0.88, entropy=0.82, source="demo_operator")

if __name__ == "__main__":
    asyncio.run(trigger_mutation_reflex())