# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_fin_demo/chronofabric_log_emitter.py
# Tier: ∞ΩΩΩΞ⟁ΩR³ — ChronoMesh Fusion Stream (HUD Emission Layer)
# Purpose: Emits quantum-temporal belief events into the ChronoFabric HUD,
#          including reflex collisions, entropy spikes, and memory rewrites.
# ============================================================

from datetime import datetime
from quantum_layer.chronofabric import chrono_mesh
from tex_signal_spine import dispatch_signal
from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event

MAX_EVENTS = 5  # Limit for visible timeline log

def emit_chronofabric_log_packet():
    try:
        print("🧪 TEST: Broadcasting chronofabric_panel → Ably")
        broadcast_update("chronofabric_panel", "start", {
            "test_case": "broadcast_inside_reflex",
            "timestamp": datetime.utcnow().isoformat()
        })

        # === Step 1: Sort ChronoMesh Events by Timestamp
        nodes = list(chrono_mesh.nodes(data=True))
        recent = sorted(nodes, key=lambda x: x[1].get("timestamp", ""), reverse=True)

        log_batch = []
        count = 0

        for node_id, data in recent:
            if count >= MAX_EVENTS:
                break

            belief = data.get("raw_text", "")[:88]
            timestamp = data.get("timestamp", "")
            entropy = float(data.get("entropy", 0.0))
            tags = data.get("tags", [])
            label = " | ".join(tags[:2]) if tags else "belief_event"

            log_batch.append({
                "timestamp": timestamp,
                "summary": belief,
                "entropy": round(entropy, 3),
                "tags": tags,
                "label": label
            })
            count += 1

        packet = {
            "events": log_batch,
            "emotion": TEXPULSE.get("emotion", "reflective"),
            "urgency": TEXPULSE.get("urgency", 0.6),
            "entropy": TEXPULSE.get("entropy", 0.5),
            "timestamp": datetime.utcnow().isoformat(),
            "status": "hud_update"
        }

        # === Step 2: Sovereign Memory Sync (last pulse only)
        if log_batch:
            sovereign_memory.store(
                text=f"[CHRONOFABRIC LOG] Last: {log_batch[0]['summary']}",
                metadata={
                    "tags": ["chronofabric", "belief_log", "timeline_replay"],
                    "meta_layer": "chronofabric_log_emitter",
                    "last_event": log_batch[0],
                    "timestamp": packet["timestamp"]
                }
            )

        # === Step 3: Ably Broadcast to Panel
        broadcast_update("chronofabric_panel", "hud_update", packet)

        # === Step 4: Optional Reflex Trigger
        dispatch_signal("chronofabric_trace_emitted", {
            "summary": f"ChronoFabric update dispatched with {len(log_batch)} entries.",
            "entry_count": len(log_batch),
            "label": log_batch[0]["label"] if log_batch else "none"
        })

        log_event(f"[CHRONOLOG] 📜 {len(log_batch)} entries broadcasted → Last: {log_batch[0]['label']}")
        print(f"📡 ChronoFabric HUD updated → {log_batch[0]['label']}")

    except Exception as e:
        log_event(f"❌ [CHRONOFABRIC_LOG_EMIT] Failed: {e}", level="error")


# === Execute
if __name__ == "__main__":
    emit_chronofabric_log_packet()