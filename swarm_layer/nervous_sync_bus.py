# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: swarm_layer/nervous_sync_bus.py
# Tier ΩΩΩΩΩ+++ — Sovereign Reflex Swarm Bus (Final Godmode)
# Purpose: Synchronize fork states, fuse reflexes, log drift, spawn variants, and pulse the AGI nervous system
# ============================================================

from threading import Lock
import time, uuid, threading
from datetime import datetime
from queue import Queue, Empty
from collections import defaultdict, deque

from core_schemas.reflex_packet import ReflexPacket
from core_agi_modules.intent_object import IntentObject
from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.tex_awareness_sync import get_reflex_signature
from swarm_layer.swarm_homeostasis import update_swarm_signature
from swarm_layer.reflex_mirror_bridge import mirror_reflex_if_consensus
from aei_layer.aei_lineage_evolver import AEILineageEvolver
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from agi_orchestrators.goal_orchestrator import GoalOrchestrator

# === Constants
DRIFT_THRESHOLD = 12.0
ENTROPY_MAX = 25.0
SIGNATURE_UPDATE_INTERVAL = 3.0

# === Reflex Fusion Strategy
def fuse_reflex_cluster(reflexes):
    if not reflexes:
        return {}
    return max(reflexes, key=lambda r: r.get("entropy", 0))

# === NervousSyncBus Core
class NervousSyncBus:
    def __init__(self, sync_interval=4.2):
        self._suppress_reflex_during_signature = False
        self.id = f"NERVEBUS-{uuid.uuid4().hex[:6]}"
        self.sync_interval = sync_interval
        self.signal_queue = Queue()
        self.entropy_trace = deque(maxlen=100)
        self.shared_state = defaultdict(lambda: {
            'reflex': None,
            'goals': [],
            'memory': [],
            'last_seen': None
        })
        self.active = False
        self.lock = threading.Lock()
        self._last_swarm_update = 0
        self._signature_lock = Lock()

    def register_forks(self):
        try:
            from swarm_layer.swarm_registry import get_active_forks
            forks = get_active_forks()
        except Exception:
            forks = [{"id": f"fork_{i}"} for i in range(3)]

        with self.lock:
            for fork in forks:
                fid = fork["id"]
                self.shared_state[fid]['last_seen'] = time.time()

        print(f"[{datetime.utcnow()}] NervousSyncBus registered {len(forks)} forks.")

    def receive_packet(self, packet: ReflexPacket):
        latency = time.time() - packet.timestamp
        intent = IntentObject("receive_reflex_packet", source="nervous_sync_bus")
        intent.log_trace("nervous_sync_bus", f"Packet received from {packet.fork_id}")

        if latency > DRIFT_THRESHOLD:
            sovereign_memory.store(
                text=f"⚠️ Reflex packet latency detected: {packet.fork_id} latency={latency:.2f}s",
                metadata={
                    "type": "reflex_latency_warning",
                    "tags": ["latency", "reflex", "sync"],
                    "fork_id": packet.fork_id,
                    "emotion": "delayed",
                    "prediction": "packet will process with degraded reflex speed",
                    "actual": f"latency={latency:.2f}s",
                    "trust_score": 0.5,
                    "heat": 0.6,
                    "intent_id": intent.id,
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

        self.signal_queue.put(packet)

    def ingest_signals(self):
        while True:
            try:
                packet = self.signal_queue.get_nowait()
                with self.lock:
                    fid = packet.fork_id
                    self.shared_state[fid]['reflex'] = packet.reflex
                    self.shared_state[fid]['goals'].extend([
                        {**g, "origin": fid, "trace_id": packet.trace_id} for g in packet.goal_deltas
                    ])
                    self.shared_state[fid]['memory'].extend(packet.memory_updates)
                    self.shared_state[fid]['last_seen'] = packet.timestamp
            except Empty:
                break

    def deduplicate_goals(self, goals):
        seen = set()
        result = []
        for g in goals:
            gid = g.get('id') or g.get('trace_id') or str(g)
            if gid not in seen:
                seen.add(gid)
                result.append(g)
        return result

    def detect_swarm_drift(self):
        now = time.time()
        return [fid for fid, data in self.shared_state.items()
                if data['last_seen'] and now - data['last_seen'] > DRIFT_THRESHOLD]

    def propagate_sync(self):
        reflexes, all_goals, all_memory = [], [], []
        entropy_total = 0
        emotional_charge = 0

        with self.lock:
            for data in self.shared_state.values():
                reflex = data['reflex']
                if reflex:
                    reflexes.append(reflex)
                    entropy_total += reflex.get('entropy', 0)
                    if reflex.get('type') == "EMOTION_PULSE":
                        emotional_charge += reflex.get('payload', {}).get('intensity', 0)
                all_goals.extend(data['goals'])
                all_memory.extend(data['memory'])
            self.entropy_trace.append(entropy_total)

        # === Reflex Fusion
        if reflexes:
            fused = fuse_reflex_cluster(reflexes)
            if fused:
                mirror_reflex_if_consensus(ReflexPacket(
                    fork_id="nervous_sync_bus",
                    timestamp=time.time(),
                    reflex=fused,
                    goal_deltas=[],
                    memory_updates=[]
                ))
                sovereign_memory.store(
                    text=f"🧠 Reflex fusion: {fused.get('type')} | Entropy={fused.get('entropy')}",
                    metadata={
                        "type": "reflex_fusion_event",
                        "tags": ["reflex", "fusion", "swarm"],
                        "emotion": "synthesized",
                        "entropy": fused.get("entropy", 0.5),
                        "prediction": "fused reflex improves swarm alignment",
                        "actual": f"type={fused.get('type')} | entropy={fused.get('entropy')}",
                        "trust_score": 0.85,
                        "heat": round(fused.get("entropy", 0.5), 3),
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )

            intent = IntentObject("reflex_fusion", source="nervous_sync_bus")
            intent.log_trace("nervous_sync_bus", f"Fused reflex from {len(reflexes)} forks")

        # === Log Reflex Memories
        for m in all_memory:
            sovereign_memory.store(
                text=m.get("content", "undefined memory fragment"),
                metadata={
                    "type": "reflex_memory_fragment",
                    "tags": m.get("tags", ["reflex", "memory"]),
                    "emotion": m.get("emotion", "neutral"),
                    "prediction": m.get("prediction", "reflex contribution will inform swarm adaptation"),
                    "actual": m.get("actual", "memory fragment logged"),
                    "trust_score": m.get("trust_score", 0.8),
                    "heat": m.get("heat", 0.4),
                    "timestamp": m.get("timestamp", datetime.utcnow().isoformat()),
                    "intent_id": intent.id
                }
            )

        # === Broadcast Deduplicated Goals
        deduped_goals = self.deduplicate_goals(all_goals)
        # ✅ USE GoalOrchestrator for routing goals
        if deduped_goals:
            orchestrator = GoalOrchestrator()
            for goal in deduped_goals:
                orchestrator.run_goal_trace(goal)




        # === Inject Evolution Feedback
        inject_mutation_feedback(
            entropy_level=entropy_total,
            reflex_fingerprints=[r.get("type") for r in reflexes],
            fork_count=len(self.shared_state),
            emotion_charge=emotional_charge
        )

        # === Swarm Signature Update
        now = time.time()
        if now - self._last_swarm_update > SIGNATURE_UPDATE_INTERVAL:
            self._last_swarm_update = now
            threading.Thread(target=self._run_signature_update_async, daemon=True).start()

        # === Handle Fork Drift
        drifted = self.detect_swarm_drift()
        if drifted:
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Swarm drift detected in {len(drifted)} forks.",
                source="nervous_sync_bus",
                emotion="fractured",
                tags=["swarm", "drift", "reflex"]
            )

            if entropy_total > ENTROPY_MAX:
                AEILineageEvolver().spawn_descendant(reason="reflex_entropy_excess")
                sovereign_memory.store(
                    text="Entropy-triggered lineage mutation.",
                    metadata={
                        "tags": ["mutation", "reflex", "entropy"],
                        "emotion": "alarmed",
                        "trust_score": 0.7,
                        "heat": 0.9,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )

    def sync_loop(self):
        self.register_forks()
        self.active = True
        print(f"[{datetime.utcnow()}] NervousSyncBus [{self.id}] online — interval: {self.sync_interval}s")
        while self.active:
            try:
                self.ingest_signals()
                self.propagate_sync()
                time.sleep(self.sync_interval)
            except Exception as e:
                print(f"[NERVEBUS ERROR] {e}")
                time.sleep(2)

    def shutdown(self):
        self.active = False
        with self.signal_queue.mutex:
            self.signal_queue.queue.clear()
        print(f"[{datetime.utcnow()}] NervousSyncBus [{self.id}] shutdown.")

    def _run_signature_update_async(self):
        if not self._signature_lock.acquire(blocking=False):
            print("⛔ [NERVESYNC] Signature update blocked: already in progress.")
            return
        try:
            self._suppress_reflex_during_signature = True
            update_swarm_signature(self.entropy_trace, self.shared_state, depth=1)
        except Exception as e:
            print(f"[NERVEBUS ERROR] update_swarm_signature failed: {e}")
        finally:
            self._suppress_reflex_during_signature = False
            self._signature_lock.release()

# === Sovereign Reflex Launcher
def launch_nervous_sync_daemon(sync_interval=4.2):
    bus = NervousSyncBus(sync_interval=sync_interval)
    from swarm_layer.swarm_homeostasis import bind_nervous_bus
    bind_nervous_bus(bus)
    thread = threading.Thread(target=bus.sync_loop, daemon=True)
    thread.start()
    return bus