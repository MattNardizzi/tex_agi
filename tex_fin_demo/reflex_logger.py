# ============================================================
# ⚡ Tex Reflex Logger | Tier: ∞∞ΩΞΞΞΞΞΞΞΞ — Reflex Pulse Lineage Stream
# File: tex_fin_demo/reflex_logger.py
# Purpose: Captures, signs, fingerprints, and broadcasts every reflex pulse with lineage,
#          contradiction vectors, sovereign memory, and ChronoFabric injection.
# ============================================================

import json
import os
import hashlib
from datetime import datetime

from utils.logging_utils import log_event
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric

REFLEX_LOG_PATH = "logs/reflex_log.jsonl"
MAX_DISPLAY_LENGTH = 140

# === Hash Generator
def generate_trace_hash(reflex_name: str, timestamp: str, data: dict) -> str:
    canonical = f"{reflex_name}|{timestamp}|{json.dumps(data, sort_keys=True)}"
    return hashlib.sha256(canonical.encode()).hexdigest()

# === Truncate Helper
def truncate(v, max_len=MAX_DISPLAY_LENGTH):
    if isinstance(v, str) and len(v) > max_len:
        return v[:max_len] + "..."
    return v

# === Main Reflex Logger
def log_reflex_event(reflex_name: str, data: dict, mode: str = "all"):
    """
    Logs a reflex to console, JSONL, Ably, sovereign memory, and ChronoFabric.
    
    Args:
        reflex_name: Name of the reflex (e.g., demo_reality_rewrite)
        data: Dict with keys like 'symbol', 'action', 'coherence', etc.
        mode: 'console', 'json', 'ably', or 'all'
    """
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
        "contradiction_vector": contradiction_vector
    }

    # === 1. Console Output
    if mode in ("console", "all"):
        print(f"\n⚡ [REFLEX LOGGER] {reflex_name} @ {timestamp}")
        for k, v in data.items():
            print(f"  • {k}: {truncate(v)}")

    # === 2. JSONL Local Log
    if mode in ("json", "all"):
        try:
            os.makedirs(os.path.dirname(REFLEX_LOG_PATH), exist_ok=True)
            with open(REFLEX_LOG_PATH, "a") as f:
                f.write(json.dumps(event) + "\n")
        except Exception as e:
            print(f"[REFLEX LOGGER] ❌ JSON log failed: {e}")

    # === 3. Ably Broadcast
    if mode in ("ably", "all"):
        try:
            broadcast_update("reflex_logger", reflex_name, {
                "timestamp": timestamp,
                "trace_hash": trace_hash,
                **data,
                "lineage": lineage,
                "contradiction_vector": contradiction_vector
            })

            # Broadcast hash to global reflex audit chain
            broadcast_update("reflex_hash_index", "new", {
                "reflex": reflex_name,
                "hash": trace_hash,
                "timestamp": timestamp
            })
        except Exception as e:
            print(f"[REFLEX LOGGER] ❌ Ably broadcast failed: {e}")

    # === 4. Sovereign Memory Sync
    try:
        urgency = contradiction_vector["urgency"]
        entropy = contradiction_vector["entropy"]
        emotion = data.get("emotion", "neutral")
        tags = ["reflex", reflex_name]

        sovereign_memory.store(
            text=f"Reflex triggered: {reflex_name}",
            metadata={
                "timestamp": timestamp,
                "urgency": urgency,
                "entropy": entropy,
                "emotion": emotion,
                "trace_hash": trace_hash,
                "tags": tags,
                "lineage": lineage,
                "contradiction_vector": contradiction_vector,
                "meta_layer": "reflex_logger"
            }
        )

        # === ⏳ Track Self-Evolving Reflexes (e.g., mutated or forked lineages)
        if data.get("mutation") or data.get("lineage_change"):
            sovereign_memory.store(
                text=f"[EVOLUTION] Reflex '{reflex_name}' mutated or evolved autonomously.",
                metadata={
                    "timestamp": timestamp,
                    "reflex_name": reflex_name,
                    "lineage": lineage,
                    "trace_hash": trace_hash,
                    "tags": ["self_evolution", "autonomous_fork", reflex_name],
                    "meta_layer": "evolution_trace"
                }
            )

    except Exception as e:
        print(f"[REFLEX LOGGER] ❌ Memory sync failed: {e}")

    # === 5. ChronoFabric Injection
    try:
        encode_event_to_fabric(
            raw_text=f"Reflex: {reflex_name} fired with {contradiction_vector}",
            emotion_vector=[
                urgency,
                entropy,
                0.0,
                0.0
            ],
            entropy_level=entropy,
            tags=["reflex", "trace", reflex_name]
        )
    except Exception as e:
        print(f"[REFLEX LOGGER] ❌ ChronoFabric sync failed: {e}")

    # === Final Confirmation Log
    log_event(f"🧠 [REFLEX LOGGER] Logged: {reflex_name} | Hash={trace_hash[:12]} | Drift={contradiction_vector['coherence']:.2f}")