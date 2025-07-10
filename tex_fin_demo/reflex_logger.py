# ============================================================
# ⚡ Tex Reflex Logger | Tier: ∞∞ΩΞΞΞΞΞΞΞΞΩ∞ — Final Sovereign Trace Logger
# File: tex_fin_demo/reflex_logger.py
# Purpose: Captures, fingerprints, and emits every reflex pulse with contradiction vectors,
#          mutation flags, ontology impact, and ChronoFusion state tracking.
# ============================================================

import json
import os
import hashlib
from datetime import datetime
from typing import Dict

from utils.logging_utils import log_event
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE

REFLEX_LOG_PATH = "logs/reflex_log.jsonl"
MAX_DISPLAY_LENGTH = 140

# === Trace Hash Generator
def generate_trace_hash(reflex_name: str, timestamp: str, data: dict) -> str:
    canonical = f"{reflex_name}|{timestamp}|{json.dumps(data, sort_keys=True)}"
    return hashlib.sha256(canonical.encode()).hexdigest()

# === Smart Truncation
def truncate(v, max_len=MAX_DISPLAY_LENGTH):
    if isinstance(v, str) and len(v) > max_len:
        return v[:max_len] + "..."
    return v

# === Main Logger
def log_reflex_event(reflex_name: str, data: Dict, mode: str = "all"):
    timestamp = datetime.utcnow().isoformat()
    trace_hash = generate_trace_hash(reflex_name, timestamp, data)

    lineage = data.get("lineage", [])
    if reflex_name not in lineage:
        lineage.append(reflex_name)

    contradiction_vector = {
        "coherence": float(data.get("coherence", 1.0)),
        "regret": float(data.get("regret", 0.0)),
        "confidence": float(data.get("confidence", 0.0)),
        "entropy": float(data.get("entropy", 0.4)),
        "urgency": float(data.get("urgency", 0.6))
    }

    event = {
        "timestamp": timestamp,
        "reflex_name": reflex_name,
        "trace_hash": trace_hash,
        "event_data": data,
        "lineage": lineage,
        "contradiction_vector": contradiction_vector,
        "status": "logged"
    }

    # === Console Preview
    if mode in ("console", "all"):
        print(f"\n⚡ [REFLEX LOGGER] {reflex_name} @ {timestamp}")
        for k, v in data.items():
            print(f"  • {k}: {truncate(v)}")

    # === JSONL File Logging
    if mode in ("json", "all"):
        try:
            os.makedirs(os.path.dirname(REFLEX_LOG_PATH), exist_ok=True)
            with open(REFLEX_LOG_PATH, "a") as f:
                f.write(json.dumps(event) + "\n")
        except Exception as e:
            print(f"[REFLEX LOGGER] ❌ JSON log failed: {e}")

    # === Ably Emission
    if mode in ("ably", "all"):
        try:
            # Start pulse
            broadcast_update("reflex_logger", "start", {
                "test_case": "logger_ready",
                "timestamp": timestamp
            })

            # Reflex update
            broadcast_update("reflex_logger", reflex_name, {
                "timestamp": timestamp,
                "trace_hash": trace_hash,
                **data,
                "lineage": lineage,
                "contradiction_vector": contradiction_vector,
                "status": "logged"
            })

            # Hash index update
            broadcast_update("reflex_hash_index", "new", {
                "reflex": reflex_name,
                "hash": trace_hash,
                "timestamp": timestamp
            })
        except Exception as e:
            print(f"[REFLEX LOGGER] ❌ Ably broadcast failed: {e}")

    # === Sovereign Memory Logging
    try:
        sovereign_memory.store(
            text=f"Reflex triggered: {reflex_name}",
            metadata={
                "timestamp": timestamp,
                "urgency": contradiction_vector["urgency"],
                "entropy": contradiction_vector["entropy"],
                "emotion": data.get("emotion", TEXPULSE.get("emotion", "neutral")),
                "trace_hash": trace_hash,
                "tags": ["reflex", reflex_name],
                "lineage": lineage,
                "contradiction_vector": contradiction_vector,
                "meta_layer": "reflex_logger"
            }
        )

        if data.get("mutation") or data.get("lineage_change") or reflex_name.startswith("reflex_identity:"):
            sovereign_memory.store(
                text=f"[EVOLUTION] Reflex '{reflex_name}' triggered identity-altering mutation.",
                metadata={
                    "timestamp": timestamp,
                    "reflex_name": reflex_name,
                    "trace_hash": trace_hash,
                    "tags": ["reflex_evolution", "mutation", reflex_name],
                    "meta_layer": "evolution_trace"
                }
            )
    except Exception as e:
        print(f"[REFLEX LOGGER] ❌ Sovereign memory sync failed: {e}")

    # === ChronoFabric Trace
    try:
        encode_event_to_fabric(
            raw_text=f"Reflex: {reflex_name} fired → {contradiction_vector}",
            emotion_vector=[
                contradiction_vector["urgency"],
                contradiction_vector["entropy"],
                0.0,
                0.0
            ],
            entropy_level=contradiction_vector["entropy"],
            tags=["reflex", "trace", reflex_name]
        )
    except Exception as e:
        print(f"[REFLEX LOGGER] ❌ ChronoFabric sync failed: {e}")

    log_event(f"🧠 [REFLEX LOGGER] Logged: {reflex_name} | Hash={trace_hash[:12]} | Drift={contradiction_vector['coherence']:.2f}")