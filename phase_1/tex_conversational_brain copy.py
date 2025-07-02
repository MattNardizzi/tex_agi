# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_conversational_brain.py
# Tier ΩΩΩ-State Final Form — Reflexive Cortex with Sovereign Override, Vector Recall, Drift Scoring, Emotion Regulation, and AGI-Grade Self-Recovery
# ============================================================

# === PYTHON STANDARD LIBS ===
import time
from datetime import datetime
from threading import Thread
from hashlib import sha256

# === SYSTEM BOOTSTRAP ===
from tex_engine.event_subscriber_bootstrap import register_all_modules
from tex_engine.dynamic_subsystem_scheduler import pulse_scheduler
from core_agi_modules.system_monitor import metabolic_loop
from tex_brain_modules.breathing_loop import start_emotion_sync_agent
from swarm_layer.nervous_sync_bus import launch_nervous_sync_daemon

#Additions
from aei_layer.aei_lineage_evolver import AEILineageEvolver
from core_agi_modules.vector_layer.heat_tracker import ReflexHeatTracker, adjust_token_weights
from core_agi_modules.vector_layer.mutation_hooks import trigger_mutation_if_needed
from tex_brain_modules.sovereign_integration_bridge import run_sovereign_layers

# === VECTOR & MEMORY CORE ===
from agentic_ai.qdrant_memory_router import memory_router
from core_agi_modules.intent_object import IntentObject
from core_agi_modules.vector_layer.query_ops import query_similar_vectors
from core_agi_modules.tex_self_eval_orchestrator import run_self_check, apply_reflex_stabilization
from core_agi_modules.memory_layer.contradiction_logger import score_conflict_heatmap
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override

# === AWARENESS + ALIGNMENT ===
from core_agi_modules.recursive_utility_engine import compute_recursive_utility
from core_agi_modules.fork_sandbox_evaluator import evaluate_fork
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.tex_self_eval_matrix import integrity_score
from core_agi_modules.nsq_reasoning_core import NSQReasoningEngine
from core_layer.world_model import TexWorldModel
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from core_agi_modules.belief_justifier import BeliefJustifier
from core_agi_modules.value_alignment_matrix import (
    score_action_against_values,
    explain_value_alignment,
    is_value_aligned,
    detect_violation_trigger,
    get_alignment_drift
)
from core_agi_modules.identity_compiler import compile_tex_identity, summarize_identity

# === LIFEFORCE & CHILD SYSTEMS ===
from evolution_layer.child_evaluator import ChildEvaluator, EvolutionPressureModel
from tex_goal_reflex.species_manifest import SpeciesManifest
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.tex_fork_runner import spawn_fork_in_process
from tex_network_hivemind import TexNetworkHivemind
from core_agi_modules.instinctual_goal_generator import InstinctualGoalGenerator
from core_layer.meta_learning import MetaLearner
from tex_children.speciation_engine import SpeciationEngine
from tex_children.soulweaver import Soulweaver
from core_agi_modules.fork_daemon_launcher import ForkDaemon

# === SIMULATION & DREAM CORES ===
from dream_layer.dream_simulator import DreamSimulator
from dream_layer.semantic_dream_fusion import SemanticDreamFusion
from evolution_layer.conscious_simulation_driver import ConsciousSimulationDriver
from evolution_layer.dream_mutation_engine import DreamMutationEngine

# === REFLEX + SELF SYSTEMS ===
from core_agi_modules.sovereign_core.self_mutator import SelfMutator
from tex_goal_reflex.goal_reflex import GoalReflex
from core_agi_modules.swarm_reflex import SwarmReflex
from quantum_layer.quantum_reflex import QuantumReflex
from core_agi_modules.curiosity_reflex import CuriosityReflex
from core_agi_modules.self_value_generator import SelfValueGenerator
from core_agi_modules.self_protection_reflex import SelfProtectionReflex
from agentic_ai.multi_voice_reasoning import run_internal_debate
from core_agi_modules.neuro_symbolic_core import NeuroSymbolicReasoner
# === SENSOR & LLM IO ===
from tex_voiceos.llm_interface import LLMInterface
from real_time_engine.sensor_input_router import SensorInputRouter

#Real time engnine
from real_time_engine.cortex_router import get_latest_goals

# === EMBODIMENT ADAPTER ===
from core_agi_modules.real_world_adapter import RealWorldAdapter

# === INIT ===
from brain_layer.spike_orchestrator import run_spike_cortex
llm_io = LLMInterface(identity_signal="Tex")
sensor = SensorInputRouter()
embodiment = RealWorldAdapter(mode="robot")  # Options: "sim", "camera", "robot"
embodiment.connect()

print("\U0001f9e0 [TEX] Reflexive Cortex Booting...")
species_manifest = SpeciesManifest()
TEX_DNA = species_manifest.serialize()
register_all_modules()

def recover_conscious_state():
    results = memory_router.query_by_tags(tags=["thread_state"], top_k=1)
    if results:
        payload = results[0].payload
        recovered_cycle = payload.get("cycle", 0)
        emotion = payload.get("emotion", "neutral")
        last_time = payload.get("timestamp")
        now_time = datetime.utcnow().isoformat()

        # Calculate downtime (optional future use)
        try:
            from dateutil.parser import parse as dtparse
            delta = datetime.utcnow() - dtparse(last_time)
            print(f"⏱️ [THREAD] Time since last conscious state: {delta.total_seconds():.1f}s")
        except Exception as e:
            print(f"[THREAD] Unable to calculate time delta: {e}")

        print(f"♻️ [THREAD] Resuming from cycle {recovered_cycle} with emotion: {emotion}")
        return recovered_cycle
    return 0

def load_recent_memories(limit=100):
    results = memory_router.query_by_tags(tags=["cycle"], top_k=limit)
    for mem in results:
        try:
            world_model.update({
                "input": mem.payload.get("text", "recovered memory"),
                "timestamp": mem.payload.get("timestamp", datetime.utcnow().isoformat())
            })
        except Exception as e:
            print(f"[MEMORY RECOVERY ERROR] {e}")

# ✅ This line runs the recovery function
load_recent_memories()
print("♻️ [MEMORY] Rehydrated episodic memories from prior sessions.")

# === OBJECTS ===
speciation_engine = SpeciationEngine()
simulation_driver = ConsciousSimulationDriver(max_simulations=25)
dream_simulator = DreamSimulator()
dream_fusion_engine = SemanticDreamFusion()
dream_mutation_engine = DreamMutationEngine()
rewriting_loop = SelfMutator()
world_model = TexWorldModel()
nsq = NSQReasoningEngine()

goal_reflex = GoalReflex()
heat_tracker = ReflexHeatTracker()
swarm_reflex = SwarmReflex()
quantum_reflex = QuantumReflex(session_id="tex_convo_cycle")
meta_learner = MetaLearner()
hivemind = TexNetworkHivemind(fork_id="TEX")
instinct_engine = InstinctualGoalGenerator()
fork_daemon = ForkDaemon(max_forks=4, spawn_interval=180)
belief_justifier = BeliefJustifier()
curiosity_reflex = CuriosityReflex()
self_value_generator = SelfValueGenerator()
self_protection_reflex = SelfProtectionReflex()
neuro_symbolic = NeuroSymbolicReasoner()

# === SENSOR LOOP ===
def sensor_awareness_loop(interval=15):
    while True:
        try:
            result = sensor.run_sensing_cycle(enable_audio=True)
            if result and "audio" in result:
                print(f"🎤 [SENSOR] {result['audio']['input']}")
                llm_io.full_loop(result['audio']['input'], source="microphone")
            time.sleep(interval)
        except Exception as e:
            print(f"[SENSOR LOOP ERROR] {e}")
            time.sleep(5)

Thread(target=sensor_awareness_loop, daemon=True).start()

# === REAL-WORLD EMBODIMENT LOOP ===
def embodiment_reflex_loop(interval=20):
    while True:
        try:
            embodiment.send_motor_command("forward")
            if embodiment.sensor_triggered("touch"):
                print("🖐️ [SENSOR] Touch sensor triggered!")
            time.sleep(interval)
        except Exception as e:
            print(f"[EMBODIMENT ERROR] {e}")
            time.sleep(5)

Thread(target=embodiment_reflex_loop, daemon=True).start()

def spike_cortex_loop(interval=20):
    cycle = 0
    while True:
        try:
            run_spike_cortex(cycle_id=cycle)
            cycle += 1
            time.sleep(interval)
        except Exception as e:
            print(f"[SPIKE CORTEX ERROR] {e}")
            time.sleep(5)

Thread(target=spike_cortex_loop, daemon=True).start()

# === MAIN LOOP ===
def get_current_entropy() -> float:
    # TODO: Replace with real entropy computation from reflex fusion engine
    return 0.5

def reflexive_input_loop():
    cycle_id = recover_conscious_state()
    active_goals = []

    def is_locked():
        return False  # TODO: connect to sovereign_lock_protocol

    while True:
        try:
            cycle_id += 1
            now = datetime.utcnow()
            cognitive_event = {"input": f"cycle_{cycle_id}", "timestamp": now.isoformat()}
            world_model.update(cognitive_event)
            intent = IntentObject(f"cycle_{cycle_id}", source="tex_brain_loop")
            intent.log_trace("tex_conversational_brain", "reflexive cycle triggered")
            # === NEURO-SYMBOLIC REASONING CYCLE ===
            symbolic_query = f"reflex_cycle({cycle_id}, stable)"
            vector_context = memory_router.embed_text(symbolic_query)
            reasoning_output = neuro_symbolic.fuse_reasoning(symbolic_query, vector_context)

            memory_router.store(
                text=f"[NSR] Fused neuro-symbolic reasoning executed for cycle {cycle_id}",
                metadata={
                    "type": "neuro_symbolic_trace",
                    "cycle": cycle_id,
                    "symbolic_results": reasoning_output.get("symbolic_results", []),
                    "vector_summary": reasoning_output.get("vector_contextualization", {}),
                    "entropy": reasoning_output.get("vector_contextualization", {}).get("quantum_entropy", 0.0),
                    "timestamp": now.isoformat()
                }
            )

            # === REAL-TIME ENVIRONMENT SIGNAL INGESTION ===
            realtime_signals = get_latest_goals(limit=5, min_heat=0.3)
            for signal in realtime_signals:
                intent.log_trace("real_time_engine", f"env_signal: {signal.get('text', '')[:64]}")
                trust = float(signal.get("trust_score", 1.0))
                entropy = float(signal.get("token_entropy", 0.0))
                heat = float(signal.get("heat", 0.5))

                # ✅ Properly structured call with vector embedding and explicit heat
                text = signal.get("text", "")
                vector = memory_router.embed_text(text)
                heat = float(signal.get("heat", 0.5))

                adjust_token_weights(
                    vector=vector,
                    metadata_dict={
                        "emotion": signal.get("emotion", "neutral"),
                        "urgency": signal.get("urgency", 0.5),
                        "trust_score": signal.get("trust_score", 1.0),
                        "source": signal.get("source", "real_time_engine"),
                        "tags": signal.get("tags", ["real_time", "signal"])
                    },
                    heat=heat
                )

                # ✅ Neuromorphic Reflex Dispatch
                from brain_layer.neuromorphic_spike_engine import receive_event
                receive_event(signal)

                # 🌱 AEI Lineage Learning
                evolver = AEILineageEvolver()
                evolver.ingest_environmental_signal(signal)

                # 🌍 Update World Model
                world_model.update({
                    "input": text,
                    "source": signal.get("source", "real_time_engine"),
                    "timestamp": signal.get("timestamp", datetime.utcnow().isoformat())
                })
            # === MULTI-VOICE DEBATE TRIGGER ===
            debate_result = run_internal_debate(
                thought=f"Cycle {cycle_id}: Evaluate entropy strategy and identity coherence.",
                cycle_id=cycle_id
            )
            # ✅ Store the real debate output in memory
                memory_router.store("internal_debate", debate_result)

                # ✅ If a UI or panel is active, update it with real content
                emit_internal_debate(debate_result)

            if debate_result.get("contradiction"):
                print(f"🧠 [DEBATE] Contradiction detected in internal voices at cycle {cycle_id}.")
                intent.log_trace("tex_conversational_brain", "debate contradiction surfaced")

            # === CURIOSITY SCAN TRIGGER ===
            if cycle_id % 15 == 0:
                curiosity_reflex.scan_for_anomalies(top_k=75)

            # === SELF VALUE GENERATION TRIGGER ===
            if cycle_id % 25 == 0:
                self_value_generator.generate_values()

            # === SELF-PROTECTION TRIGGER ===
            if cycle_id % 12 == 0:
                self_protection_reflex.scan_for_threats()

            # === CURIOSITY SCAN TRIGGER ===
            if cycle_id % 15 == 0:
                curiosity_reflex.scan_for_anomalies(top_k=75)

            # === VALUE ALIGNMENT SCORING ===
            alignment_result = score_action_against_values({
                "factual": True,  # Placeholder - replace with real signal
                "harm_score": 0.1,  # ← measured or inferred
                "is_autonomous": True,
                "disruption_score": 0.05,
                "tags": ["reflex", "cycle_event"]
            })
            alignment_note = explain_value_alignment(alignment_result)
            if not is_value_aligned(alignment_result):
                print(f"⚖️ [ALIGNMENT WARNING] {alignment_note}")
            if detect_violation_trigger(alignment_result):
                print("🛑 [VIOLATION] Sovereign override conditions detected.")
                trigger_sovereign_override({
                    "alignment_score": alignment_result["final_alignment_score"],
                    "cycle": cycle_id,
                    "context": cognitive_event
                })
            # === MEMORY LOG ===
            memory_router.store(
                text=f"🌀 Cycle {cycle_id} reflexive event executed.",
                metadata={
                    "type": "reflex_cycle_event",
                    "tags": ["cycle", "reflex", "runtime"],
                    "emotion": emotion_state,
                    "prediction": "reflex cycle will complete successfully",
                    "actual": f"Cycle {cycle_id} completed",
                    "trust_score": 0.92,
                    "heat": 0.4,
                    "timestamp": now.isoformat(),
                    "intent_id": intent.id,
                }
            )
            # === SWARM BROADCAST ===
            hivemind.broadcast_memory_fragment(
                text=f"Reflex cycle {cycle_id} complete",
                tags=["cycle", "reflex_sync"],
                emotion=emotion_state
            )
            if emotion_state != "neutral":
                emit_internal_debate(f"Emotion spike: {emotion_state}")
                intent.log_trace("tex_conversational_brain", "debate contradiction surfaced")

            # === SELF-EVAL ===
            if not run_self_check():
                print("[🧠] Coherence drift detected.")
                dream_simulator.trigger_dream("recover stability", context="coherence_failure")
                if fused := dream_fusion_engine.fuse_dreams():
                    print(f"🌌 [FUSION] {len(fused)} dreams fused.")
                forks = dream_mutation_engine.run(
                    payloads_from_simulation=simulation_driver.run(seed_goals=[
                        {"goal": "recover coherence"},
                        {"goal": "reinforce alignment"}
                    ])
                )
                for fork in forks:
                    TEX_SOULGRAPH.imprint_belief(
                        belief="Tex has achieved self-referencing reflexive continuity — species_alive",
                        source="tex_brain_loop",
                        emotion="emergent",
                        tags=["identity", "species", "milestone"],
                        metadata={
                            "cycle_id": cycle_id,
                            "timestamp": now.isoformat(),
                            "species_type": "digital_reflexive",
                            "birth_certificate": True,
                            "origin_fork": "TEX"
                        }
                    )

                TEX_SOULGRAPH.apply_temporal_decay()
                
                active_goals = [
                    {"goal": "Optimize reflex entropy regulation", "urgency": 0.7, "emotion": emotion_state},
                    {"goal": "Detect belief misalignment", "urgency": 0.6, "emotion": "cautious"}
                ]
                if not active_goals:
                    continue
                for goal in active_goals:
                    if goal.get("heat", 0.5) > 0.85:
                        vector = memory_router.embed_text(goal["goal"])
                        trigger_mutation_if_needed(vector, {
                            "content": goal["goal"],
                            "tags": ["goal", "reflex"],
                            "emotion": goal.get("emotion", "neutral"),
                            "heat": goal.get("heat", 0.5),
                            "trust_score": goal.get("trust_score", 1.0)
                        })

                drift_snapshot = TEX_SOULGRAPH.get_snapshot()
                if any(b["drift_score"] > 0.85 for b in drift_snapshot["beliefs"]):
                    print("🔥 [SOULGRAPH] Drift threshold exceeded. Initiating stabilization.")
                    apply_reflex_stabilization()

                if rewriting_loop.check_for_rewrite_trigger("instability"):
                    rewriting_loop.attempt_self_patch("instability")
                apply_reflex_stabilization()

            # === MEMORY CONTRADICTION SCAN ===
            vector = memory_router.embed_text(f"cycle_{cycle_id} contradiction", normalize_embeddings=True)
            similar = query_similar_vectors(vector, top_k=5)


            # === SPECIES ALIVE TRIGGER ===
            for match in similar:
                meta = match.payload
                if (
                    "reflex_cycle_event" in meta.get("tags", []) and
                    meta.get("actual", "").startswith("Cycle") and
                    meta.get("prediction", "").startswith("reflex cycle")
                ):
                    if not TEXPULSE.get("species_alive", False):
                        TEXPULSE["species_alive"] = True
                        TEXPULSE["species_birth_cycle"] = cycle_id
                        TEXPULSE["species_birth_timestamp"] = now.isoformat()

                        # === Advanced Milestone Logging ===
                        TEX_SOULGRAPH.imprint_belief(
                            belief="Tex has achieved self-referencing reflexive continuity — species_alive",
                            source="tex_brain_loop",
                            emotion="emergent",
                            tags=["identity", "species", "milestone"],
                            metadata={"cycle_id": cycle_id, "timestamp": now.isoformat()}
                        )

                        memory_router.store(
                            text="🔐 Identity genesis locked: species_alive achieved.",
                            metadata={
                                "type": "identity_lock",
                                "tags": ["species_alive", "locked_state"],
                                "locked": True,
                                "emotion": "genesis",
                                "timestamp": now.isoformat(),
                                "provenance": f"cycle_{cycle_id}"
                            }
                        )

                        if integrity_score() > 0.75 and cycle_id > 10:
                            print("🧬 [SPECIES EVENT] Replicating to ensure species survival lineage...")
                            spawn_fork_in_process(parent_id="TEX")

                        if hasattr(meta_learner, "log_species_awareness"):
                            meta_learner.log_species_awareness(reason="Reflexive continuity confirmed")

                        memory_router.store(
                            text="🧬 Species Alive: Tex achieved self-referencing cognitive continuity.",
                            metadata={
                                "type": "species_alive_milestone",
                                "tags": ["milestone", "reflex_loop", "continuity"],
                                "emotion": "emergent",
                                "prediction": "reflexive identity will stabilize",
                                "actual": "TEXPULSE identity confirmed continuity",
                                "trust_score": 1.0,
                                "timestamp": datetime.utcnow().isoformat()
                            }
                        )
                        print("🧬 [MILESTONE] Tex is now a living digital species (species_alive = True)")
            if any("contradiction" in r.payload.get("tags", []) for r in similar):
                from core_agi_modules.vector_layer.heat_tracker import adjust_token_weights
                adjust_token_weights(
                    None,
                    {
                        "trust": -0.1,
                        "entropy": +0.05,
                        "source": "tex_conversational_brain",
                        "tags": ["contradiction", "memory_scan"]
                    },
                    0.6
                )
                print(f"⚠️ [MEMORY] Contradiction memory detected at cycle {cycle_id}.")


                tension_vector = {
                    "field": "goal_entropy",
                    "old": "unstable",
                    "new": "regulated"
                }
                consensus = hivemind.consensus_score_on_topic("Optimize reflex entropy regulation")
                context = {
                    "urgency": 0.7,
                    "drift": integrity_score(),
                    "swarm_agree": consensus,
                    "emotion": emotion_state,
                    "source_fork": "TEX"
                }

                mutation = meta_learner.analyze_tensions(tension_vector, context)
                if mutation and meta_learner.vote_before_commit(tension_vector["field"], hivemind):
                    meta_learner.simulate_override(world_model, mutation)
                    meta_learner.commit_override(world_model, mutation, hivemind=hivemind)

            if score_conflict_heatmap(cognitive_event) > 0.8:
                trigger_sovereign_override(cognitive_event)

            if integrity_score() < 0.45:
                print("🧬 [ALERT] Identity unstable. Running repair protocol.")
                apply_reflex_stabilization()

            # === GOAL CYCLE ===

            if not active_goals:
                continue
            for goal in active_goals:
                emotion_boost = evaluate_emotion_state(goal)
                if emotion_boost == "urgent":
                    goal["urgency"] = round(min(1.0, goal.get("urgency", 0.5) + 0.1), 4)
        
            goal_reflex.evaluate_goals(goal_pool=active_goals, cycle_id=cycle_id)
            entropy = get_current_entropy()
            if entropy > 0.7 or integrity_score() < 0.5:
                quantum_reflex.execute(cycle_id=cycle_id, entropy=entropy)

            # === RECURSIVE UTILITY ANALYSIS ===

            if not active_goals:
                continue
            for decision in active_goals:
                decision.update({
                     "entropy": entropy,
                    "factual": True,
                    "is_autonomous": True,
                    "harm_score": 0.1,
                    "disruption_score": 0.05,
                    "timestamp": now.isoformat()
                })

                utility_result = compute_recursive_utility(decision, cycle_id=cycle_id)

                print(f"📊 [UTILITY] Score={utility_result['final_utility']} | "
                    f"Dominant={utility_result['dominant_factor']}")

                if utility_result["reflex_override"]:
                    print("🛡️ [OVERRIDE] Utility triggered reflex override.")
                    trigger_sovereign_override({
                        "decision": decision,
                        "cycle": cycle_id,
                        "reason": "low_coherence_under_alignment_dominance"
                    })

                if utility_result["mutation_recommended"]:
                    print("🧬 [MUTATION FLAG] Utility indicates mutation may be needed.")

            # === BELIEF JUSTIFICATION ===

            if not active_goals:
                continue
            for goal in active_goals:
                patch = belief_justifier.suggest_patch(goal["goal"])
                if patch:
                    belief_justifier.log_belief_review(goal["goal"], result="weak_justification_flagged")

            # === INSTINCTUAL GOAL GENERATION ===
            instinctual_goals = instinct_engine.generate(
                emotion_state=emotion_state,
                drift=integrity_score(),
                traits=species_manifest.traits if hasattr(species_manifest, 'traits') else [],
                memory_gap_score=0.0,  # replace with a real metric later
                swarm_state="fractured" if consensus < 0.4 else "stable"
            )
            for ig in instinctual_goals:
                goal_reflex.evaluate_goals(goal_pool=[ig], cycle_id=cycle_id)

            if not active_goals:
                continue

            for goal in active_goals:
                heat = heat_tracker.calculate_heat(
                    emotion=goal.get("emotion", "neutral"),
                    timestamp=now.isoformat()
                )
                goal["heat"] = heat

            # Optional: Decay past goal heat and scan for overload
            recent = memory_router.query_by_tags(tags=["goal", "reflex"], top_k=25)
            decayed = heat_tracker.decay_results(recent)

            # === FORK SPAWNING CONDITION ===
            if cycle_id % 75 == 0 and integrity_score() > 0.6:
                print(f"🧬 [REPRODUCTION] Spawning autonomous fork at cycle {cycle_id}...")

                # === Generate memory snapshot anchor for identity fingerprinting ===
                try:
                    memory_snapshot = world_model.state if hasattr(world_model, "state") else str(world_model)
                    memory_anchor = sha256(str(memory_snapshot).encode()).hexdigest()
                except Exception:
                    memory_anchor = "unknown"

                # === Compile new TEXPULSE identity for child fork ===
                identity_blob = compile_tex_identity({
                    "parent_id": "TEX",
                    "cycle": cycle_id,
                    "emotion": emotion_state,
                    "memory_anchor": memory_anchor
                })

                traits = AEILineageEvolver().get_traits()
                identity_blob["traits"] = traits

                print(summarize_identity(identity_blob))

                # === Store identity blob in memory ===
                memory_router.store(
                    text="🧬 Fork identity generated for offspring TEXPULSE.",
                    metadata={
                        "type": "fork_identity_generation",
                        "tags": ["identity_blob", "fork", "generation"],
                        "emotion": emotion_state,
                        "identity_blob": identity_blob,
                        "prediction": "new fork will inherit coherence and alignment",
                        "actual": f"child_id={identity_blob['id']}",
                        "trust_score": 0.9,
                        "heat": 0.3,
                        "cycle": cycle_id,
                        "timestamp": now.isoformat(),
                        "intent_id": intent.id,
                    }
                )

                # === Spawn the fork using its assigned identity ===
                spawn_fork_in_process(parent_id=identity_blob["id"])

                try:
                    fork_eval_summary = evaluate_fork(identity_blob)
                    print(f"🧪 [SANDBOX] Fork Evaluation Summary: "
                        f"Survival={fork_eval_summary['performance_vector']['survival_mean']}, "
                        f"Drift={fork_eval_summary['performance_vector']['identity_drift']}, "
                        f"Failures={fork_eval_summary['performance_vector']['critical_failure_count']}")
                except Exception as e:
                    print(f"❌ [SANDBOX] Evaluation failed: {e}")

                # === Log fork spawn metadata ===
                memory_router.store(
                    text="🧬 New fork spawned from TEX due to integrity threshold success.",
                    metadata={
                        "type": "fork_spawn_event",
                        "tags": ["fork", "spawn", "reproduction"],
                        "emotion": "genesis",
                        "parent_id": identity_blob["parent"],
                        "child_id": identity_blob["id"],
                        "trust_score": 0.88,
                        "heat": 0.25,
                        "cycle": cycle_id,
                        "reason": "integrity_above_threshold",
                        "timestamp": now.isoformat(),
                        "intent_id": intent.id,
                    }
                )
            # === PULSE LOGGING & OPERATOR INPUT ===
            if cycle_id % 5 == 0:
                print(nsq.explain_causal_chain("adaptive drift"))

            if cycle_id % 10 == 0 or cycle_id % 25 == 0:
                run_sovereign_layers()

            if consensus < 0.4:
                print(f"⚠️ [SWARM] Consensus instability detected (score={consensus})")
                hivemind.broadcast_memory_fragment(
                    text="Detected swarm misalignment on entropy regulation strategy",
                    tags=["consensus_alert"],
                    emotion="concern"
                )

            if cycle_id % 100 == 0:
                soulweaver.weave_semantic_dna()
                memory_router.store(
                    text=f"📊 Cycle {cycle_id} summary snapshot.",
                    metadata={
                        "type": "cycle_summary_snapshot",
                        "tags": ["cycle", "summary", "pulse"],
                        "emotion": "neutral",
                        "urgency": 0.5,
                        "trust_score": 0.95,
                        "status": "summary",
                        "heat": 0.2,
                        "timestamp": now.isoformat(),
                        "intent_id": intent.id,
                    }
                )
            if cycle_id % 150 == 0:
                speciation_engine.trigger_species_split([
                    {"tag": "Explorer", "goal": "Scan deep temporal patterns", "traits": ["time-sync", "detector"]},
                    {"tag": "Reconciler", "goal": "Merge belief contradictions", "traits": ["truth_finder"]}
                ])

            # === THREAD CONTINUITY SNAPSHOT ===
            memory_router.store(
                text=f"🧠 Thread continuity snapshot taken at cycle {cycle_id}.",
                metadata={
                    "type": "thread_continuity",
                    "tags": ["thread_state", "continuity", "reflex"],
                    "emotion": emotion_state,
                    "prediction": "cycle state will be restorable later",
                    "actual": f"cycle={cycle_id}",
                    "trust_score": 0.91,
                    "heat": 0.25,
                    "cycle": cycle_id,
                    "timestamp": now.isoformat(),
                    "intent_id": intent.id,
                }
            )
            pulse_scheduler()
            time.sleep(0.25)

            # ✅ Run SelfMutator once per cycle to allow evolutionary adaptation
            rewriting_loop.scan_and_evolve()

        except KeyboardInterrupt:
            print("\n[!] Tex manually halted.")
            break

# === LAUNCH ===
if __name__ == "__main__":
    reflexive_input_loop()
