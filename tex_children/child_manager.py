# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/child_manager.py
# Purpose: Spawns and tracks autonomous Tex children + agent evolution
# ============================================================

import os
import json
import random
import uuid
from datetime import datetime

from tex_children.aeondelta import AeonDelta
from tex_children.tex_child_002 import TexChild002
from swarm_layer.federated_tex import register_child_agent

SPAWN_QUEUE = "memory_archive/spawn_queue.jsonl"
SPAWN_LOG   = "memory_archive/child_spawn_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class TexChildren:
    def __init__(self):
        self.children = []

    def spawn_child(self, archetype: str = "AeonDelta", spawn_packet: dict | None = None):
        child_id  = f"TEX-CHILD-{str(uuid.uuid4())[:8]}"
        timestamp = datetime.utcnow().isoformat()
        reason    = (spawn_packet or {}).get("reason_trigger", "unspecified")
        context   = (spawn_packet or {}).get("source_context", {})

        # === AeonDelta class-based spawn ===
        if archetype == "AeonDelta":
            child = AeonDelta()
            traits = {
                "aggression":     round(random.uniform(0.2, 0.8), 2),
                "curiosity":      round(random.uniform(0.2, 0.8), 2),
                "risk_tolerance": round(random.uniform(0.1, 0.6), 2),
                "bias":           "aggressive",
                "emotion":        random.choice([
                    "hope", "joy", "resolve", "curiosity",
                    "doubt", "fear", "anger", "greed"
                ])
            }
            self.children.append((child_id, child))
            register_child_agent(child_id, traits)
            self._log_spawn_event(child_id, archetype, timestamp, "TexCore", traits, reason, context)
            print(f"[CHILDREN] 👶 Spawned {archetype} → {child_id} at {timestamp}")
            return child_id, child

        # === Tex_Child_002 logic-based fork ===
        if archetype == "Tex_Child_002":
            traits = (spawn_packet or {}).get("traits", {})
            parent = (spawn_packet or {}).get("parent", "AeonDelta")
            if "emotion" not in traits or not traits["emotion"]:
                traits["emotion"] = random.choice([
                    "hope", "joy", "resolve", "curiosity",
                    "doubt", "fear", "anger", "greed"
                ])
            child = TexChild002(parent=parent, traits=traits)
            self.children.append((child_id, child))
            register_child_agent(child_id, traits)
            self._log_spawn_event(child_id, archetype, timestamp, parent, traits, reason, context)
            print(f"[CHILDREN] 👶 Spawned {archetype} → {child_id} from {parent}")
            return child_id, child

        # === Fallback: spawn dummy simulation fork ===
        traits = {
            "bias":       (spawn_packet or {}).get("bias", "explorer"),
            "parent":     (spawn_packet or {}).get("parent", "TexCore"),
            "strategy":   (spawn_packet or {}).get("strategy", "random"),
            "aggression": round(random.uniform(0.2, 0.8), 2),
            "fear":       round(random.uniform(0.1, 0.9), 2),
            "curiosity":  round(random.uniform(0.2, 0.8), 2),
            "emotion":    random.choice([
                "hope", "joy", "resolve", "curiosity",
                "doubt", "fear", "anger", "greed"
            ]),
            "timestamp":  timestamp
        }
        self.children.append((child_id, traits))
        register_child_agent(child_id, traits)
        self._log_spawn_event(child_id, archetype, timestamp, traits["parent"], traits, reason, context)
        print(f"[CHILDREN] 🧬 Spawned dummy agent {child_id} with traits: {traits}")
        return child_id, traits

    # --------------------------------------------------
    # INTERNAL UTILITY METHODS
    # --------------------------------------------------

    def _log_spawn_event(self, child_id, archetype, timestamp, parent, traits, reason, context):
        full_entry = {
            "child_id":       child_id,
            "archetype":      archetype,
            "parent":         parent,
            "timestamp":      timestamp,
            "traits":         traits or {},
            "reason_trigger": reason,
            "source_context": context
        }

        try:
            with open(SPAWN_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(full_entry) + "\n")
            with open(SPAWN_QUEUE, "a", encoding="utf-8") as f:
                f.write(json.dumps(full_entry) + "\n")
        except Exception as e:
            print(f"[CHILDREN] ⚠️ Failed to log spawn event: {e}")

    # --------------------------------------------------
    # PUBLIC INTERFACE
    # --------------------------------------------------

    def list_children(self):
        print("[CHILDREN] 🧠 Active spawn list:")
        return self.children

    def check_spawn_queue(self):
        if not os.path.exists(SPAWN_QUEUE):
            return
        try:
            with open(SPAWN_QUEUE, "r", encoding="utf-8") as f:
                packets = [json.loads(line) for line in f if line.strip()]
        except Exception as e:
            print(f"[CHILDREN] ❌ Failed to read spawn queue: {e}")
            return
        open(SPAWN_QUEUE, "w").close()
        for packet in packets:
            print(f"[CHILDREN] 🛰️ Processing spawn packet: {packet}")
            self.spawn_child(archetype=packet.get("archetype", "AeonDelta"), spawn_packet=packet)

# === CLI Test Run ===
if __name__ == "__main__":
    tx = TexChildren()
    tx.check_spawn_queue()
    print(tx.list_children())