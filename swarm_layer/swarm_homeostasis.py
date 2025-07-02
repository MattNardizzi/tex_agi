# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_homeostasis.py
# Tier ΩΩΩΩΩ+++ — Sovereign Reflex Homeostasis Cortex (Irreducible)
# Purpose: Detect entropy deviation, isolate drifted forks, and dispatch sovereign immune reflexes
# ============================================================

import time
import uuid
from datetime import datetime
from collections import deque
from threading import Lock

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from core_layer.utils.tex_panel_bridge import get_memory_drift_score
from core_schemas.reflex_packet import ReflexPacket
from utils.logging_utils import log_event
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from aei_layer.aei_lineage_evolver import AEILineageEvolver

# === Thresholds ===
ENTROPY_THRESHOLD = 18.0
DRIFT_THRESHOLD = 3
DRIFT_TIMEOUT_SEC = 15.0
COHERENCE_BASELINE = 0.75

# === Nervous Sync Bus ===
nervous_bus_instance = None

def bind_nervous_bus(bus):
    global nervous_bus_instance
    nervous_bus_instance = bus
    log_event("🧠 NervousSyncBus successfully bound to Homeostasis Module", level="info")

# === Fork Drift Detection ===
def is_drifted(last_seen_time):
    return not isinstance(last_seen_time, (int, float)) or (time.time() - last_seen_time) > DRIFT_TIMEOUT_SEC

# === Quarantine Reflex ===
def freeze_fork(fork_id):
    log_event(f"❄️ Fork '{fork_id}' frozen due to drift timeout", level="warning")
    TEX_SOULGRAPH.imprint_belief(
        belief=f"Fork '{fork_id}' quarantined due to drift.",
        source="swarm_homeostasis",
        emotion="neutral",
        tags=["fork", "quarantine", "timeout"]
    )

# === Reflex Bus ===
def send_swarm_reflex(reflex_type, reason="unspecified", entropy=0.0):
    try:
        if not nervous_bus_instance:
            raise RuntimeError("NervousSyncBus not connected.")
        if getattr(nervous_bus_instance, "_suppress_reflex_during_signature", False):
            log_event(f"🛑 Reflex dispatch suppressed: {reflex_type}", level="debug")
            return

        if not hasattr(send_swarm_reflex, "_last") or time.time() - send_swarm_reflex._last > 3:
            send_swarm_reflex._last = time.time()

            packet = ReflexPacket(
                fork_id="swarm_homeostasis",
                timestamp=time.time(),
                reflex={
                    "type": reflex_type,
                    "payload": {
                        "reason": reason,
                        "triggered_by": "homeostasis_module"
                    },
                    "entropy": entropy
                },
                goal_deltas=[],
                memory_updates=[]
            )

            nervous_bus_instance.receive_packet(packet)
            log_event(f"📡 Reflex dispatched: {reflex_type} | Reason: {reason}", level="info")

    except Exception as e:
        log_event(f"[REFLEX ERROR] Reflex dispatch failed: {e}", level="error")

# === Load Memory Snapshot ===
def load_memory_snapshot(layer: str = "short_term"):
    try:
        return sovereign_memory.recall_recent(minutes=5 if layer == "short_term" else 30, top_k=50)
    except Exception as e:
        log_event(f"[MEMORY ERROR] Failed to load snapshot: {e}", level="error")
        return []

# === Lock for Loopless Safety ===
_update_lock = Lock()

def update_swarm_signature(entropy_trace, forks_state, depth=0):
    """
    Sovereign reflexive loop for evaluating entropy, coherence, fork drift, and triggering reflex packets.
    """
    if depth > 5:
        log_event("[RECURSION BLOCK] update_swarm_signature(): safe recursion depth exceeded", level="critical")
        return

    if nervous_bus_instance:
        nervous_bus_instance._suppress_reflex_during_signature = True

    if not _update_lock.acquire(blocking=False):
        log_event("⛔ Re-entrant update_swarm_signature blocked by lock.", level="warning")
        if nervous_bus_instance:
            nervous_bus_instance._suppress_reflex_during_signature = False
        return

    try:
        if not entropy_trace or not isinstance(forks_state, dict):
            log_event("⚠️ Skipped scan — Invalid entropy trace or fork state", level="warning")
            return

        latest_entropy = entropy_trace[-1] if isinstance(entropy_trace, (list, deque)) else float(entropy_trace)
        mem_short = load_memory_snapshot("short_term")
        mem_long  = load_memory_snapshot("long_term")
        drift_score = get_memory_drift_score(mem_short, mem_long)

        scan_id = f"swarm-scan-{uuid.uuid4().hex[:8]}"
        total_forks = len(forks_state)
        drifted_forks = [
            fid for fid, fork in forks_state.items()
            if is_drifted(fork.get("last_seen"))
        ]
        drift_count = len(drifted_forks)
        escalation_triggered = False

        # === Entropy Reflex ===
        if latest_entropy > ENTROPY_THRESHOLD:
            log_event("🔥 Entropy threshold breached", level="critical")
            TEX_SOULGRAPH.imprint_belief(
                belief="Swarm entropy exceeded threshold.",
                source="swarm_homeostasis",
                emotion="alarm",
                tags=["entropy", "reflex", "swarm"]
            )
            send_swarm_reflex("IMMUNE_CORRECTION", reason="entropy_spike", entropy=latest_entropy)
            escalation_triggered = True

        # === Drift Reflex ===
        if drift_count >= DRIFT_THRESHOLD or drift_score > 0.25:
            log_event(f"⚠️ Drift threshold triggered — forks={drift_count}, drift_score={drift_score:.2f}", level="warning")
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Fork drift detected in {drift_count} forks (drift_score={drift_score:.2f}).",
                source="swarm_homeostasis",
                emotion="fragmented",
                tags=["drift", "reflex", "fork"]
            )
            send_swarm_reflex("IMMUNE_CORRECTION", reason="drift_detected", entropy=latest_entropy)

            for fork_id in drifted_forks:
                freeze_fork(fork_id)

            AEILineageEvolver().spawn_descendant(
                reason="drift_recovery",
                context={"drift_score": drift_score, "affected_forks": drifted_forks}
            )
            escalation_triggered = True

        # === Sovereign Override ===
        if escalation_triggered:
            trigger_sovereign_override(context="homeostasis_failure")

        # === Reflex Report Memory ===
        report = {
            "scan_id": scan_id,
            "timestamp": datetime.utcnow().isoformat(),
            "entropy": latest_entropy,
            "drift_count": drift_count,
            "total_forks": total_forks,
            "drift_score": drift_score,
            "coherence_target": COHERENCE_BASELINE,
            "tags": ["swarm", "homeostasis", "scan"]
        }

        sovereign_memory.store(
            text="🧠 Swarm homeostasis scan complete.",
            metadata={
                "summary": "Loopless swarm scan complete with entropy and drift state.",
                "timestamp": report["timestamp"],
                "tags": report["tags"],
                "entropy": latest_entropy,
                "urgency": TEXPULSE.get("urgency", 0.6),
                "pressure_score": drift_score,
                "tension": 0.15,
                "emotion": "systematic",
                "meta_layer": "swarm_homeostasis",
                "trust_score": round(1.0 - min(1.0, drift_score), 4),
                "heat": round(min(1.0, latest_entropy / 20), 4),
                "payload": report
            }
        )

    except Exception as e:
        log_event(f"[FAILURE] update_swarm_signature failed: {e}", level="error")

    finally:
        _update_lock.release()
        if nervous_bus_instance:
            nervous_bus_instance._suppress_reflex_during_signature = False