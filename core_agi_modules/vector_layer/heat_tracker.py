# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/vector_layer/heat_tracker.py
# Tier: ∞ΩΩΩΩ — Reflex Heat Cortex + Entropy Intelligence (Final Sovereign Form)
# Purpose: Tracks reflex heat, flags volatility, scores entropy shifts, and routes mutation-safe overrides.
# ============================================================

from datetime import datetime
from dateutil import parser

from core_agi_modules.intent_object import IntentObject
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE

# === Emotion → Heat Scaling Table ===
EMOTION_SCALE = {
    "neutral": 0.3,
    "curious": 0.4,
    "anticipation": 0.5,
    "concern": 0.6,
    "fear": 0.7,
    "driven": 0.75,
    "awe": 0.9,
    "rage": 1.0
}

class ReflexHeatTracker:
    def __init__(self, session_id: str = "reflex_heat_session"):
        self.session_id = session_id
        self.now = datetime.utcnow()
        self.intent = IntentObject("evaluate heat + entropy across reflex space", source="heat_tracker")
        self.heat_log = []
        self.volatility_flagged = False

    def calculate_heat(self, emotion: str, timestamp: str) -> float:
        base = EMOTION_SCALE.get(emotion.lower(), 0.4)
        try:
            ts = parser.parse(timestamp)
            age_seconds = max(0, (self.now - ts).total_seconds())
            half_life_days = 14 - (base * 6)
            decay = 0.5 ** (age_seconds / (half_life_days * 86400))
            return round(base * decay, 4)
        except Exception:
            return base

    def decay_results(self, results):
        reflex_ready_count = 0

        for r in results:
            try:
                ts = parser.parse(r.payload.get("timestamp"))
                raw = float(r.payload.get("heat", 0.5))
                urgency = float(r.payload.get("urgency", 0.5))
                weight = 0.6 + urgency * 0.4
                decay = 0.5 ** ((self.now - ts).total_seconds() / (14 * 86400))
                effective = max(0.05, round(raw * decay * weight, 4))

                r.payload["effective_heat"] = effective
                if effective > 0.75:
                    r.payload["reflex_ready"] = True
                    reflex_ready_count += 1

                self.heat_log.append({
                    "id": r.id,
                    "effective_heat": effective,
                    "timestamp": r.payload.get("timestamp"),
                    "emotion": r.payload.get("emotion", "neutral"),
                    "tags": r.payload.get("tags", [])
                })

                self.intent.log_trace("heat_tracker", f"⏱️ {r.id} heat={effective}")

            except Exception:
                r.payload["effective_heat"] = r.payload.get("heat", 0.5)

        # Reflex volatility override
        if reflex_ready_count >= 4 and len(results) >= 6:
            self.volatility_flagged = True
            trigger_sovereign_override({
                "input": "reflex_heat_tracker",
                "issue": "reflex volatility detected",
                "heat": 1.0,
                "reflex_ready_count": reflex_ready_count,
                "session": self.session_id
            })

        return sorted(results, key=lambda r: r.payload["effective_heat"], reverse=True)

    def get_trace_log(self):
        return self.heat_log

# === ♨️ Reflex Entropy Shift Delta
def compute_entropy_shift(thread_objects) -> float:
    try:
        timestamps = [parser.parse(t.get("timestamp")) for t in thread_objects if t.get("timestamp")]
        scores = [float(t.get("score", 0.5)) for t in thread_objects if "score" in t]
        if len(scores) < 2:
            return 0.0

        delta = max(scores) - min(scores)
        weighted = round(delta * (1 + len(scores) / 5), 4)

        sovereign_memory.store(
            text=f"Entropy shift across {len(scores)} threads",
            metadata={
                "tags": ["entropy", "reflex", "stability"],
                "prediction": "entropy stable",
                "actual": delta,
                "trust_score": 0.7,
                "emotion": "concern" if delta >= 0.25 else "curious",
                "heat": min(1.0, weighted),
                "timestamp": datetime.utcnow().isoformat(),
                "source": "heat_tracker"
            }
        )
        return weighted
    except Exception:
        return 0.0

# === 🔥 Universal Emotion Heat Scorer
def calculate_heat(emotion: str, timestamp: str) -> float:
    base = {
        "neutral": 0.3,
        "curious": 0.5,
        "tense": 0.7,
        "urgent": 0.9,
        "crisis": 1.0
    }.get(emotion.lower(), 0.4)
    return round(min(1.0, base), 4)

# === 🧠 Token Weight Memory Updater
def adjust_token_weights(vector=None, metadata_dict=None, heat=None, metadata=None):
    if metadata_dict is None and metadata:
        metadata_dict = metadata

    if metadata_dict is None:
        raise ValueError("[adjust_token_weights] metadata_dict is required.")

    timestamp = datetime.utcnow().isoformat()
    vector_valid = isinstance(vector, list) and len(vector) == 384

    store_payload = {
        **metadata_dict,
        "heat": metadata_dict.get("heat", heat or 0.5),
        "timestamp": timestamp,
        "source": "adjust_token_weights"
    }

    if vector_valid:
        sovereign_memory.store(text="Token vector weight update", metadata=store_payload, vector=vector)
    else:
        sovereign_memory.store(text="Token weight adjustment (no vector)", metadata=store_payload)

    return True