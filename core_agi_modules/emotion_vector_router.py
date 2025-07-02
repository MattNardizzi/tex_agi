# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_agi_modules/emotion_vector_router.py
# Tier ΩΩΩ.ΣX — Reflex-Grade Emotion Routing Kernel (No Ceiling Edition)
# Purpose: Sovereign signal router for global emotion cognition: voice, mutation, forks, memory, persona
# ============================================================

import threading
from datetime import datetime
import uuid
import hashlib
import math

class EmotionVectorRouter:
    def __init__(self):
        self._state_lock = threading.Lock()
        self._emotion_state = self._init_state()
        self._last_update = None
        self._change_flag = False

    def _init_state(self):
        return {
            "label": "neutral",
            "intensity": 0.0,
            "entropy": 0.0,
            "coherence": 0.75,
            "valence": 0.0,
            "signature": None,
            "timestamp": None,
            "reflex_hash": None,
            "delta": {
                "intensity": 0.0,
                "entropy": 0.0,
                "coherence": 0.0,
                "valence": 0.0,
                "time_diff": 0.0
            }
        }

    def _compute_hash(self, state):
        base = f"{state['label']}|{state['intensity']}|{state['entropy']}|{state['coherence']}|{state['valence']}"
        return hashlib.sha256(base.encode()).hexdigest()[:16]

    def update(self, new_state: dict):
        with self._state_lock:
            now = datetime.utcnow()
            new_signature = str(uuid.uuid4())[:12]
            new_hash = self._compute_hash(new_state)

            # Delta tracking
            last = self._emotion_state
            last_ts = self._last_update or now
            time_diff = (now - last_ts).total_seconds()
            delta = {
                "intensity": new_state.get("intensity", 0.0) - last.get("intensity", 0.0),
                "entropy": new_state.get("entropy", 0.0) - last.get("entropy", 0.0),
                "coherence": new_state.get("coherence", 0.75) - last.get("coherence", 0.75),
                "valence": new_state.get("valence", 0.0) - last.get("valence", 0.0),
                "time_diff": time_diff
            }

            # Update state
            self._emotion_state.update({
                "label": new_state.get("label", "neutral"),
                "intensity": new_state.get("intensity", 0.0),
                "entropy": new_state.get("entropy", 0.0),
                "coherence": new_state.get("coherence", 0.75),
                "valence": new_state.get("valence", 0.0),
                "signature": new_signature,
                "timestamp": now.isoformat(),
                "reflex_hash": new_hash,
                "delta": delta
            })

            self._last_update = now
            self._change_flag = True

    def get(self):
        with self._state_lock:
            return self._emotion_state.copy()

    def export_tags(self):
        with self._state_lock:
            return [
                self._emotion_state["label"],
                f"entropy_{round(self._emotion_state['entropy'], 2)}",
                f"intensity_{round(self._emotion_state['intensity'], 2)}",
                f"coherence_{round(self._emotion_state['coherence'], 2)}"
            ]

    def inject_into(self, metadata: dict):
        with self._state_lock:
            metadata.update({
                "emotion": self._emotion_state["label"],
                "emotion_entropy": self._emotion_state["entropy"],
                "emotion_intensity": self._emotion_state["intensity"],
                "emotion_coherence": self._emotion_state["coherence"],
                "emotion_valence": self._emotion_state["valence"],
                "emotion_signature": self._emotion_state["signature"],
                "emotion_timestamp": self._emotion_state["timestamp"],
                "emotion_reflex_hash": self._emotion_state["reflex_hash"]
            })
        return metadata

    def has_changed(self, clear=True):
        with self._state_lock:
            changed = self._change_flag
            if clear:
                self._change_flag = False
            return changed

    def get_delta(self):
        with self._state_lock:
            return self._emotion_state.get("delta", {})


# === Sovereign Emotion Bus — Globally Shared ===
emotion_bus = EmotionVectorRouter()