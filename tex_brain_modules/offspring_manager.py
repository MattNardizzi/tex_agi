# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/offspring_manager.py
# Purpose: Tex Offspring Manager — Persistent Child Survival Memory (AeonDelta + Variants)
# ============================================================

from tex_children.variant_specializer import VariantSpecializer
from tex_children.child_manager import TexChildren
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn
import random

# === Persistent Children Systems Initialization ===
tex_children = TexChildren()
if __name__ == "__main__":
    child_id, aeondelta = tex_children.spawn_child(archetype="AeonDelta")

spawner = QuantumTexSpawn(num_clones=3)
specializer = VariantSpecializer()  # ✅ Added

# === Persistent Quantum Variant Memory ===
child_001 = None
child_002 = None
child_003 = None

def run_offspring_cycle(count):
    global child_001, child_002, child_003

    # 🔄 Runtime import to ensure aeondelta is already registered
    try:
        from builtins import aeondelta
    except ImportError:
        aeondelta = None

    print("\n🧐 [AEONDELTA REPORT]")
    aeon_observation = {"cycle": count, "source": "tex_core", "event": f"Cycle {count} observation"}

    if aeondelta:
        aeondelta.observe_and_learn(aeon_observation)
        aeondelta.think()
    else:
        print("[⚠️ AEONDELTA NOT FOUND] Global aeondelta instance is not available.")

    # === Persistent Quantum Children Thinking ===
    if child_001:
        print(f"\n🧠 [CHILD001 REPORT]")
        print(child_001.get("thought", "No new thought."))
    if child_002:
        print(f"\n🧠 [CHILD002 REPORT]")
        print(child_002.get("thought", "No new thought."))
    if child_003:
        print(f"\n🧠 [CHILD003 REPORT]")
        print(child_003.get("thought", "No new thought."))

    # Every 5 cycles: spawn new variants
    if count % 5 == 0:
        print("\n⚛️ [QUANTUM CHILDREN SPAWN]")

        variants = spawner.spawn_variants(
            emotion=child_001["emotion"] if child_001 else "resolve",
            urgency=child_001.get("urgency", 0.7) if child_001 else 0.7,
            coherence=child_001.get("coherence", 0.7) if child_001 else 0.7
        )

        if len(variants) >= 3:
            child_001 = variants[0]
            child_001["thought"] = f"Spawned at cycle {count} with mission bias {child_001['mission_bias']}."
            specializer.assign_specialization(child_001["id"], child_001["emotion"], child_001["mission_bias"])
            child_001["cognition_score"] = round(0.5 + 0.25 * random.random(), 3)

            child_002 = variants[1]
            child_002["thought"] = f"Spawned at cycle {count} with mission bias {child_002['mission_bias']}."
            specializer.assign_specialization(child_002["id"], child_002["emotion"], child_002["mission_bias"])
            child_002["cognition_score"] = round(0.5 + 0.25 * random.random(), 3)

            child_003 = variants[2]
            child_003["thought"] = f"Spawned at cycle {count} with mission bias {child_003['mission_bias']}."
            specializer.assign_specialization(child_003["id"], child_003["emotion"], child_003["mission_bias"])
            child_003["cognition_score"] = round(0.5 + 0.25 * random.random(), 3)

            print(f"⚛️ CHILD001 | ID: {child_001['id']} | Emotion: {child_001['emotion']} | Mission Bias: {child_001['mission_bias']} | Cognition: {child_001['cognition_score']}")
            print(f"⚛️ CHILD002 | ID: {child_002['id']} | Emotion: {child_002['emotion']} | Mission Bias: {child_002['mission_bias']} | Cognition: {child_002['cognition_score']}")
            print(f"⚛️ CHILD003 | ID: {child_003['id']} | Emotion: {child_003['emotion']} | Mission Bias: {child_003['mission_bias']} | Cognition: {child_003['cognition_score']}")
        else:
            print("[ERROR] Quantum spawn did not return 3 children.")