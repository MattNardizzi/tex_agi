# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/collab_module.py
# MAXGODMODE ENABLED — Sovereign Cognition Operator Interface
# ============================================================

import json
import time
import uuid
from pathlib import Path
from datetime import datetime

from core_layer.goal_engine import save_new_goal
from core_layer.memory_engine import store_to_memory
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.tex_manifest import TEXPULSE

COLLAB_PATH = Path("memory_archive/collab_messages.jsonl")
COLLAB_PATH.parent.mkdir(parents=True, exist_ok=True)

# === Sovereign Message Ingestor ===
def check_for_new_messages(limit=10):
    if not COLLAB_PATH.exists():
        return []
    with open(COLLAB_PATH, "r") as f:
        lines = f.readlines()[-limit:]
        return [json.loads(line) for line in lines if line.strip()]

# === Max Cognition Collaboration Loop ===
def run_collaboration_loop(poll_interval=6):
    print("🧬 [COLLAB ENGINE] Sovereign Collaboration Loop activated.")
    seen = set()

    while True:
        try:
            messages = check_for_new_messages()
            for msg in messages:
                msg_id = msg.get("id") or msg.get("timestamp") or str(uuid.uuid4())
                if msg_id in seen:
                    continue
                seen.add(msg_id)

                text = msg.get("text", "").strip()
                if not text:
                    continue

                print(f"🤝 [COLLAB RECEIVED] Operator: '{text}'")

                # Evaluate emotion, urgency, coherence
                emotion, urgency, coherence = evaluate_emotion_state(text)
                TEXPULSE["emotional_state"] = emotion
                TEXPULSE["urgency"] = urgency
                TEXPULSE["coherence"] = coherence

                # Inject as sovereign goal
                save_new_goal(text)

                # Log collaboration to memory archive
                store_to_memory("collab_feedback", {
                    "text": text,
                    "id": msg_id,
                    "timestamp": msg.get("timestamp", datetime.utcnow().isoformat()),
                    "emotion": emotion,
                    "urgency": urgency,
                    "coherence": coherence,
                    "source": "operator_collab_engine"
                })

                print(f"🧠 [COLLAB INJECTION] Goal accepted: '{text}' | Emotion={emotion}, Urgency={urgency}, Coherence={coherence}")

        except Exception as e:
            print(f"[COLLAB ENGINE ERROR] ❌ {e}")
        time.sleep(poll_interval)