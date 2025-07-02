# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: reflex_mirror_bridge.py
# Tier ΩΩΩΩΩ.Δ — Final Sovereign Reflex Mirror Bridge with Traceability, Consensus Fingerprinting, and Override Immunity
# ============================================================

import time
from datetime import datetime

from core_layer.memory_engine import store_to_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from swarm_layer.swarm_registry import get_active_forks
from core_agi_modules.reflex_orchestrator import ReflexOrchestrator
from core_schemas.reflex_packet import ReflexPacket
from core_layer.tex_manifest import TEXPULSE

MIRRORED_HISTORY = {}
mirror_orchestrator = ReflexOrchestrator()

REFLEX_ENTROPY_QUORUM = 0.75
MIRROR_IMMUNITY_KEY = "mirror_immunity"
TRUST_THRESHOLD = 0.6

def mirror_reflex_if_consensus(reflex_packet):
    try:
        # ✅ SAFETY: Class-safe check
        if not reflex_packet or not isinstance(reflex_packet, ReflexPacket):
            print("[REFLEX_MIRROR] ❌ Invalid or missing ReflexPacket.")
            return

        packet_data = reflex_packet.to_dict() if hasattr(reflex_packet, "to_dict") else {}
        reflex_data = packet_data.get("reflex", {})

        if TEXPULSE.get(MIRROR_IMMUNITY_KEY, False):
            print("[REFLEX_MIRROR] ⛔ Mirror blocked — agent in immunity mode.")
            return

        payload     = reflex_data.get("payload", {})
        reflex_type = reflex_data.get("type")
        entropy     = reflex_data.get("entropy", 0.0)
        cycle_id    = payload.get("cycle", 0)
        goal        = payload.get("goal", "Unspecified")
        trace_id    = packet_data.get("trace_id", f"mirror-{reflex_type}-{cycle_id}")

        if trace_id in MIRRORED_HISTORY:
            return

        forks = get_active_forks()
        trusted_forks = [f for f in forks if f.get("trust", 0.5) >= TRUST_THRESHOLD]

        if len(trusted_forks) < 2:
            print("[REFLEX_MIRROR] 🟡 Not enough trusted forks for mirror quorum.")
            return

        total_entropy = sum(f.get("reflex_entropy", 0.0) for f in trusted_forks)
        avg_entropy = total_entropy / max(1, len(trusted_forks))

        if avg_entropy < REFLEX_ENTROPY_QUORUM:
            print(f"[REFLEX_MIRROR] 🚫 Reflex entropy quorum not met ({avg_entropy:.2f})")
            return

        projected = mirror_orchestrator.preview(reflex_type)
        if projected and projected.get("conflict", False):
            print("[REFLEX_MIRROR] ⚠️ Reflex mirror aborted — conflict detected.")
            return

        mirror_orchestrator.resolve_and_execute([reflex_type], current_goal=goal)
        mirrored_at = datetime.utcnow().isoformat()
        MIRRORED_HISTORY[trace_id] = mirrored_at

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Consensus reflex '{reflex_type}' mirrored at cycle {cycle_id}",
            source="reflex_mirror_bridge",
            emotion="unison",
            tags=["reflex", "mirror", reflex_type],
            metadata={
                "trace_id": trace_id,
                "entropy_quorum": round(avg_entropy, 4),
                "mirrored_at": mirrored_at,
                "trusted_fork_count": len(trusted_forks)
            }
        )

        store_to_memory("reflex_mirror_log", {
            "reflex_type": reflex_type,
            "goal": goal,
            "cycle": cycle_id,
            "mirrored_at": mirrored_at,
            "trace_id": trace_id,
            "entropy": entropy,
            "forks_considered": len(forks),
            "trusted_forks": len(trusted_forks),
            "source": "reflex_mirror_bridge"
        })

        try:
            from swarm_layer.nervous_sync_bus import NervousBus
            NervousBus.receive_packet(ReflexPacket(
                fork_id="reflex_mirror_bridge",
                timestamp=time.time(),
                reflex={
                    "type": "MIRRORED_REFLEX_ACK",
                    "payload": {
                        "original_type": reflex_type,
                        "cycle": cycle_id,
                        "agent": TEXPULSE.get("agent_id", "Tex"),
                        "trace_id": trace_id
                    },
                    "entropy": 0.01
                },
                goal_deltas=[],
                memory_updates=[],
                trace_id=trace_id
            ))
        except Exception as e:
            print(f"[REFLEX_MIRROR] ⚠️ NervousBus mirror ACK failed: {e}")

    except Exception as e:
        print(f"[REFLEX_MIRROR ERROR] {e}")