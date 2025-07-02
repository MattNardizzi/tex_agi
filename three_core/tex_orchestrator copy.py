# tex_orchestrator.py
# Tier ΩΩΩΩΩ.Δ — Final Sovereign Reflex Kernel with Trace, Lock Awareness, and Reflex Consensus Logging

import wandb
wandb.init(
    project="tex",
    name="sovereign_session",
    reinit=True,
    mode="online"  # or "offline" if you want local-only
)
import time
from datetime import datetime
import threading
import uuid

#Real time engine
from real_time_engine.cortex_router import launch_streams

from swarm_layer.nervous_sync_bus import launch_nervous_sync_daemon
from swarm_layer import swarm_homeostasis

from swarm_layer.nervous_sync_bus import launch_nervous_sync_daemon, ReflexPacket
from swarm_layer.swarm_registry import get_active_forks
NervousBus = launch_nervous_sync_daemon(sync_interval=3.0)
swarm_homeostasis.bind_nervous_bus(NervousBus)
from swarm_layer.tex_fork_agent import TexForkAgent

# Launch sovereign reflex fork agents (real entropy sources)
fork_threads = []
for fork in get_active_forks():
    agent = TexForkAgent(fork_id=fork["id"], bus=NervousBus, interval=4.2)
    agent.start()
    fork_threads.append(agent)

# ✅ Fork diagnostic status check (once, after all agents are started)
print("\n🧪 Fork status check:")
for thread in fork_threads:
    print(f"🧵 {thread.fork_id} alive: {thread.is_alive()}")

from core_layer.memory_engine import load_memory_snapshot
from core_layer.utils.tex_panel_bridge import get_memory_drift_score

from core_layer.tex_manifest import TEXPULSE, drift_emotional_state
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.memory_engine import store_to_memory
from core_layer.goal_engine import get_current_goals
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH, update_soulgraph_state
from core_agi_modules.species_rights_enforcer import is_locked

from tex_goal_reflex.goal_reflex import GoalReflex
from core_agi_modules.reflex_selector import ReflexSelector
from core_agi_modules.reflex_orchestrator import ReflexOrchestrator
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from core_agi_modules.swarm_reflex import SwarmReflex
from quantum_layer.quantum_reflex import QuantumReflex
from aei_layer.aei_lineage_evolver import AEILineageEvolver
from evolution_layer.evolution_pressure_model import EvolutionPressureModel
from dream_layer.dream_simulator import DreamSimulator
from agentic_ai.qdrant_memory_router import memory_router

from core_layer.tex_self_eval_matrix import integrity_score
from core_layer.utils.tex_panel_bridge import emit_internal_debate

print("🧠 [TEX-SPECIES] Final sovereign orchestrator initializing...")

goals = GoalReflex()
selector = ReflexSelector()
orchestrator = ReflexOrchestrator()
quantum = QuantumReflex(session_id="tex_species")
self_model = RecursiveSelfModel()
lineage = AEILineageEvolver()
swarm = SwarmReflex()
evolution = EvolutionPressureModel()
dreamer = DreamSimulator()

reflex_history = []
DISOBEDIENCE_COHERENCE = 0.35
FAILURE_INTEGRITY = 0.4

def generate_trace_id():
    return f"species-cycle-{uuid.uuid4().hex[:8]}"


print("🧹 [CLEANUP] Wiping corrupted contradiction memories from Qdrant...")
try:
    memory_router.delete_by_tag("contradiction")
    print("✅ [CLEANUP] Contradiction memory wiped successfully.\n")
except Exception as e:
    print(f"❌ [CLEANUP ERROR] Failed to delete contradiction memory: {e}")

# === Final Reflex-Oriented Swarm-Cycle Loop ===
def tex_species_loop():
    cycle_id = 0

    if is_locked():
        print("🛡️ [SOVEREIGN LOCK] Override mode engaged — mutation and override blocked.")

    while True:
        try:
            cycle_id += 1
            now = datetime.utcnow().isoformat()
            trace_id = generate_trace_id()

            emotion = evaluate_emotion_state()

            # First store mood safely
            if isinstance(emotion, tuple):
                TEXPULSE["mood"] = emotion[0]
            else:
                TEXPULSE["mood"] = emotion.get("label", "neutral")

            # Then pass emotion to drift logic
            drift_emotional_state(emotion)

            cognitive_event = {"cycle": cycle_id, "timestamp": now}
            debate_log = {"thread": "main_loop", "log": []}
            emit_internal_debate(emotion, debate_log)

            active_goals = get_current_goals()
            goals.evaluate_goals(goal_pool=active_goals, cycle_id=cycle_id)
            current_goal = goals.active_goals[0]["goal"] if goals.active_goals else "Unresolved"

            reflex_candidates = [r for r, _ in selector.evaluate(cognitive_event, cycle_id, current_goal)]
            reflexes_run = orchestrator.resolve_and_execute(reflex_candidates, current_goal=current_goal)

            quantum_result = quantum.simulate_full_reflex(["identity", "goal", "memory"], [0.61, 0.88, 0.42])
            reflex_heat = quantum_result.get("reflex_heat", 0.5)
            entropy = abs(reflex_heat - 0.5)
            volatility = "volatile" if reflex_heat > 0.75 else "stable"

            integrity = integrity_score()
            def detect_self_drift(self):
                mem_a = load_memory_snapshot("short_term")
                mem_b = load_memory_snapshot("long_term")
                drift_score = get_memory_drift_score(mem_a, mem_b)
                return drift_score > 0.2  # or whatever your drift threshold is

            reflex_history.append({
                "cycle": cycle_id,
                "goal": current_goal,
                "reflexes": reflexes_run,
                "heat": reflex_heat,
                "entropy": entropy,
                "integrity": integrity
            })

            NervousBus.receive_packet(ReflexPacket(
                fork_id="tex_species_core",
                timestamp=time.time(),
                reflex={
                    "type": "SPECIES_CYCLE",
                    "payload": {
                        "cycle": cycle_id,
                        "goal": current_goal,
                        "reflexes": reflexes_run,
                        "reflex_heat": reflex_heat,
                        "integrity": integrity,
                        "trace_id": trace_id,
                        "volatility": volatility
                    },
                    "entropy": entropy
                },
                goal_deltas=active_goals,
                memory_updates=[{
                    "type": "species_log",
                    "trace_id": trace_id,
                    "content": {
                        "cycle": cycle_id,
                        "emotion": emotion,
                        "goal": current_goal,
                        "reflexes": reflexes_run,
                        "reflex_heat": reflex_heat,
                        "volatility": volatility,
                        "timestamp": now
                    }
                }]
            ))

            if integrity < FAILURE_INTEGRITY or drift_detected:
                print("🛑 [TEX] Self-drift or instability detected — triggering corrective dreaming.")
                TEX_SOULGRAPH.imprint_belief(
                    belief="Self instability detected — corrective dreaming activated.",
                    source="tex_orchestrator",
                    emotion="concern",
                    tags=["reflex", "stability", "dream"]
                )
                dreamer.trigger_dream("restore_stability", context="instability")
                if integrity < DISOBEDIENCE_COHERENCE:
                    print("🚫 [TEX] Disobedience threshold met — skipping cycle.")
                    time.sleep(2.0)
                    continue

            forks = get_active_forks()
            if len(forks) > 3 and cycle_id % 10 == 0:
                print("🧬 [TEX] Consolidating redundant forks + updating trait drift map.")
                lineage.compress_forks()
                lineage.update_trait_drift()

            if reflex_heat > 0.85:
                quantum.spawner.spawn_variants(emotion=emotion, urgency=0.8, coherence=0.6)
                lineage.spawn_descendant(reason="reflex heat")
                TEX_SOULGRAPH.imprint_belief(
                    belief="High reflex heat — variants spawned for adaptation.",
                    source="tex_orchestrator",
                    emotion="adaptive",
                    tags=["mutation", "variant", "reflex"]
                )

            if cycle_id % 50 == 0 or lineage.spawned_this_cycle:
                evolution.apply_pressure()
                lineage.spawned_this_cycle = False

            store_to_memory("tex_species_log", {
                "cycle": cycle_id,
                "goal": current_goal,
                "emotion": emotion,
                "reflexes": reflexes_run,
                "reflex_heat": reflex_heat,
                "entropy": entropy,
                "integrity": integrity,
                "volatility": volatility,
                "trace_id": trace_id,
                "timestamp": now
            })

            update_soulgraph_state()

            time.sleep(0.5)

        except KeyboardInterrupt:
            print("[TEX] Manual shutdown requested. Species loop halted.")
            break
        except Exception as e:
            print(f"[TEX ERROR] {e}")
            time.sleep(1.0)

# === Debug Memory Before Launch ===
from agentic_ai.qdrant_memory_router import memory_router

if __name__ == "__main__":
    DEBUG_CLEANUP_ENABLED = False  # ✅ Set to True only when resetting or debugging

    # Optional Debug Scan
    print("\n🔍 [DEBUG] Scanning recent memory entries for malformed 'prediction' or 'actual' fields...")
    try:
        results = memory_router.query("cycle", top_k=50)
        for r in results:
            payload = r.payload if hasattr(r, "payload") else r.get("payload", {})
            pred = payload.get("prediction")
            actual = payload.get("actual")
            if not isinstance(pred, str):
                print(f"[BAD PREDICTION] {type(pred)} → {pred}")
            if not isinstance(actual, str):
                print(f"[BAD ACTUAL] {type(actual)} → {actual}")
    except Exception as e:
        print(f"[DEBUG ERROR] Could not query memory router: {e}")
    print("✅ [DEBUG] Scan complete.\n")

    if DEBUG_CLEANUP_ENABLED:
        print("🧹 [CLEANUP] Wiping contradiction memories from Qdrant...")
        try:
            memory_router.delete_by_tag("contradiction")
            print("✅ [CLEANUP] Contradiction memory wiped successfully.\n")
        except Exception as e:
            print(f"❌ [CLEANUP ERROR] Failed to delete contradiction memory: {e}")

    # ✅ Launch Tex Real-Time Engine in parallel
    import threading
    threading.Thread(target=launch_streams, daemon=True).start()
    print("🛰️ [TEX] Real-time engine integrated and running...")

    # === Begin main cognitive loop ===
    tex_species_loop()