# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/temporal_decay_engine.py
# Tier: ΩΩΩΩΩΩ∞ΩΩΩ🜂 — Sovereign Temporal Entanglement Cortex
# Purpose: Sovereign decay of aged memory vectors with Chrono entanglement + dual memory sync.
# ============================================================

from datetime import datetime, timezone
import hashlib
import random

from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.reflex_mesh_router import should_route_signal
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Corrected
from utils.logging_utils import log

# === Sovereign Constants ===
DECAY_THRESHOLD_HOURS = 12
DECAY_PROBABILITY_BASE = 0.6
MAX_DECAY_PER_PASS = 10
DECAY_TAG = "temporal_decay"

def hours_since(ts_str: str) -> float:
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return max((now - ts).total_seconds() / 3600.0, 0.0)
    except Exception as e:
        log.error(f"[DECAY] Invalid timestamp: {ts_str} | {e}")
        return 999.0

def run_temporal_decay_engine():
    """
    Sovereign decay engine.
    Applies memory fade to vector traces based on entropy/urgency/QRNG and 
    synchronizes symbolic decay into ChronoFabric via sovereign memory.
    """
    try:
        if not should_route_signal("temporal_decay").get("routed", True):
            log.info("[DECAY] ⛔ Blocked by reflex mesh router.")
            return

        embeddings = sovereign_memory.recall_recent(minutes=120, top_k=60)
        urgency = TEXPULSE.get("urgency", 0.72)
        entropy = TEXPULSE.get("entropy", 0.5)
        faded_count = 0

        for item in embeddings:
            if faded_count >= MAX_DECAY_PER_PASS:
                break

            ts = item.get("timestamp")
            uid = item.get("uuid") or item.get("id")
            if not ts or not uid:
                continue

            age = hours_since(ts)
            if age < DECAY_THRESHOLD_HOURS:
                continue

            qrng = random.random()
            decay_score = round((urgency * 0.4 + entropy * 0.3 + qrng * 0.3), 4)
            if decay_score < DECAY_PROBABILITY_BASE:
                continue

            now = datetime.utcnow().isoformat()
            decay_hash = hashlib.sha256((uid + ts).encode()).hexdigest()[:12]

            # === Sovereign Memory Logging (Dual sync)
            sovereign_memory.store(
                text=f"🕰️ Sovereign decay triggered on trace {uid}",
                metadata={
                    "type": "memory_decay",
                    "tags": [DECAY_TAG, "memory_fade", "symbolic_decay"],
                    "trace_uid": uid,
                    "original_timestamp": ts,
                    "age_hours": age,
                    "urgency": urgency,
                    "entropy": entropy,
                    "decay_score": decay_score,
                    "qrng_roll": qrng,
                    "decay_hash": decay_hash,
                    "timestamp": now
                }
            )

            # === Chrono Linkage (Simulated)
            sovereign_memory.vector.collection.insert([[
                uid + "::decay",  # Simulate a new ID
                sovereign_memory.embed_text(f"decay::{uid}"),
                now,
                [0.2, 0.2, 0.0, 0.0],
                decay_score,
                "Decay echo of previous memory trace.",
                "temporal_decay"
            ]])

            faded_count += 1

        log.info(f"[DECAY] ✅ Sovereign decay complete. Faded={faded_count} | Min age={DECAY_THRESHOLD_HOURS}h")

    except Exception as e:
        log.error(f"[DECAY] ❌ Decay engine failed: {e}")