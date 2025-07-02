# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_initializer.py
# Purpose: Initialization of Core Tex Cognitive Modules
# ============================================================

import os, json
from datetime import datetime

from evolution_layer.self_mutator import SelfMutator
from agentic_ai.self_reflective_loop import SelfReflectiveLoop
from agentic_ai.tex_awareness_sync import TexAwarenessSync
from operator_layer.vortex_operator import VortexRuntime
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn
from tex_children.child_manager import TexChildren
from agentic_ai.agent_scorer import AgentScorer

# === Global path to memory_archive ===
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# === Smart loader for latest memory file ===
def get_latest_memory_log():
    memory_dir = os.path.join(ROOT_DIR, "memory_archive")
    files = [f for f in os.listdir(memory_dir) if f.endswith(".jsonl")]

    if not files:
        print("[MEMORY LOADER] ❌ No memory files found.")
        return []

    files.sort(key=lambda f: os.path.getmtime(os.path.join(memory_dir, f)), reverse=True)
    latest_file = os.path.join(memory_dir, files[0])
    print(f"[MEMORY LOADER] 🔍 Loading memory from: {latest_file}")

    with open(latest_file, 'r') as f:
        return [json.loads(line) for line in f]

# === Initialize Cognitive Systems ===

def initialize_mutator():
    return SelfMutator()

def initialize_reflector():
    return SelfReflectiveLoop()

def initialize_awareness():
    return TexAwarenessSync(operator_name="Vortex")

def initialize_vortex():
    return VortexRuntime(fingerprint="Vortex")

def initialize_spawner():
    return QuantumTexSpawn(num_clones=3)

def initialize_children():
    tex_children = TexChildren()
    child_id, aeondelta = tex_children.spawn_child(archetype="AeonDelta")

    # ✅ Load memory logs automatically
    memories = get_latest_memory_log()
    print(f"[MEMORY LOADER] ✅ Loaded {len(memories)} memories.")

    return tex_children, child_id, aeondelta

def initialize_scorer():
    return AgentScorer()