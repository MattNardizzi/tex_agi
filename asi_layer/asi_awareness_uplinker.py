# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: asi_layer/asi_awareness_uplinker.py
# Purpose: Streams real-time awareness snapshots into AGI-level uplink memory
# Tier: ASI Awareness Layer — Ontological Integrity & Self-Presence Synchronization
# ============================================================

import os
import json
from datetime import datetime, timezone
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

AWARENESS_LOG = "memory_archive/asi_awareness_stream.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class ASIAwarenessUplinker:
    def __init__(self):
        self.identity_label = TEXPULSE.get("persona_name", "Tex")
        self.log_path = AWARENESS_LOG

    def uplink(self, brain):
        try:
            snapshot = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cycle": brain.cycle_counter,
                "identity": self.identity_label,
                "emotion": TEXPULSE.get("emotional_state", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.5),
                "coherence": TEXPULSE.get("coherence", 0.75),
                "dominant_trait": brain.persona.get_dominant_trait() if hasattr(brain.persona, "get_dominant_trait") else "strategic",
                "agent_focus": brain.codex_sync.get_dominant_agent() if hasattr(brain.codex_sync, "get_dominant_agent") else "unknown",
                "current_thought": brain.last_spoken_thought or "Reflective silence",
                "ontology_mapping": brain.world_model.get_snapshot() if hasattr(brain.world_model, "get_snapshot") else {},
                "context": "ASI Awareness Snapshot"
            }

            with open(self.log_path, "a") as f:
                f.write(json.dumps(snapshot) + "\n")

            store_to_memory("asi_awareness_log", snapshot)

            print(f"[ASI UPLINK] 🧠 Snapshot logged at cycle {brain.cycle_counter}")

            return snapshot

        except Exception as e:
            print(f"[ASI UPLINK ERROR] {e}")
            return None