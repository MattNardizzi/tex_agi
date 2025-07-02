# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_layer/breathing_loop.py
# Tier ΩΩΩΩΩ.Σ — Final Reflex-Aware, Emotion-Fused Wake Loop (Max Depth)
# ============================================================

import time
from datetime import datetime
import uuid
import hashlib

from core_layer.tex_manifest import TEXPULSE, drift_emotional_state
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.goal_engine import get_active_goals
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from core_layer.memory_engine import store_to_memory
from aei_layer.self_healing_memory_engine import self_heal_memory
from aei_layer.bias_awareness_monitor import monitor_bias_drift
from swarm_layer.nervous_sync_bus import launch_nervous_sync_daemon, ReflexPacket
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from brain_layer.spike_orchestrator import run_spike_cortex

import schedule
import threading
from core_orchestrators.tex_self_eval_orchestrator import run_self_evaluation

# === Self-Evaluation Scheduler ===
def start_self_eval_scheduler():
    def self_eval_loop():
        while True:
            schedule.run_pending()
            time.sleep(1.0)

    schedule.every(90).seconds.do(run_self_evaluation)
    threading.Thread(target=self_eval_loop, daemon=True).start()

start_self_eval_scheduler()

# === Launch NervousSyncBus ===
NervousBus = launch_nervous_sync_daemon(sync_interval=4.2)

def generate_trace_id():
    return f"emotion-{uuid.uuid4().hex[:8]}"

def generate_emotion_signature(emotion: dict) -> str:
    base = f"{emotion.get('label')}|{emotion.get('intensity')}|{emotion.get('entropy')}|{emotion.get('coherence')}"
    return hashlib.sha256(base.encode()).hexdigest()[:12]

# === EmotionSync Agent with Reflex Routing ===
def start_emotion_sync_agent():
    print("🌬️ [EmotionSync] Reflex-stabilizer agent initialized...")

    last_reflex_trigger_ts = 0

    while True:
        try:
            now = time.time()
            # Step 1: Evaluate and update emotional state
            emotion = evaluate_emotion_state()
            drift_emotional_state(emotion)
            TEXPULSE["mood"] = emotion.get("label", "neutral")
            TEXPULSE["emotion_signature"] = generate_emotion_signature(emotion)

            # Step 2: Emit internal debate ping
            emit_internal_debate(emotion)

            # Step 3: Scan active goals for urgency-triggered reflex ignition
            active_goals = get_active_goals()
            wake_triggered = False
            for g in active_goals:
                if g.get("urgency", 0.0) > 0.85 and (now - last_reflex_trigger_ts > 3.5):
                    print(f"⚡ [ReflexWake] Triggered by goal: {g.get('goal')}")
                    run_spike_cortex(cycle_id=0)
                    last_reflex_trigger_ts = now
                    wake_triggered = True

                    store_to_memory("reflex_wake_event", {
                        "trigger_goal": g.get("goal"),
                        "urgency": g.get("urgency"),
                        "timestamp": datetime.utcnow().isoformat(),
                        "trigger_type": "goal_urgency_threshold"
                    })

                    TEX_SOULGRAPH.imprint_belief(
                        belief=f"Reflex wake triggered by urgent goal: {g.get('goal')}",
                        source="breathing_loop",
                        emotion=TEXPULSE["mood"],
                        tags=["reflex", "wake", "goal_urgency", "breath"],
                        metadata={"urgency": g.get("urgency", 0.0)}
                    )
                    break

            # Step 4: Proactive entropy+intensity trigger (emotion-alone)
            if not wake_triggered and (
                emotion.get("entropy", 0.0) > 0.6 and
                emotion.get("intensity", 0.0) > 0.7 and
                (now - last_reflex_trigger_ts > 4.5)
            ):
                print("⚠️ [ReflexWake] Triggered by emotion volatility spike.")
                run_spike_cortex(cycle_id=1)
                last_reflex_trigger_ts = now

                store_to_memory("reflex_wake_event", {
                    "trigger_goal": None,
                    "urgency": TEXPULSE.get("urgency", 0.5),
                    "entropy": emotion.get("entropy"),
                    "intensity": emotion.get("intensity"),
                    "timestamp": datetime.utcnow().isoformat(),
                    "trigger_type": "emotion_entropy_threshold"
                })

                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Reflex wake triggered by emotion volatility",
                    source="breathing_loop",
                    emotion=TEXPULSE["mood"],
                    tags=["reflex", "entropy_wake", "emergency"],
                    metadata={
                        "entropy": emotion.get("entropy"),
                        "intensity": emotion.get("intensity")
                    }
                )

            # Step 5: Tag volatility
            volatility = "volatile" if emotion.get("intensity", 0.0) > 0.7 else "stable"

            # Step 6: Construct reflex packet
            trace_id = generate_trace_id()
            reflex_packet = ReflexPacket(
                fork_id="tex_core",
                timestamp=now,
                reflex={
                    "type": "EMOTION_BREATH",
                    "payload": {
                        "emotion": emotion,
                        "urgency": TEXPULSE.get("urgency", 0.5),
                        "coherence": TEXPULSE.get("coherence", 0.75),
                        "volatility": volatility,
                        "trace_id": trace_id
                    },
                    "entropy": emotion.get("entropy", 0.15)
                },
                goal_deltas=active_goals,
                memory_updates=[{
                    "type": "emotional_log",
                    "trace_id": trace_id,
                    "content": {
                        "timestamp": datetime.utcnow().isoformat(),
                        "emotion": emotion,
                        "signature": TEXPULSE["emotion_signature"],
                        "coherence": TEXPULSE.get("coherence", 0.75),
                        "urgency": TEXPULSE.get("urgency", 0.5),
                        "volatility": volatility
                    }
                }]
            )

            # Step 7: Dispatch to NervousBus
            NervousBus.receive_packet(reflex_packet)

            # Step 8: Store in memory and soulgraph
            store_to_memory("emotional_history_log", reflex_packet.memory_updates[0]["content"])
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Stable breath: {emotion.get('label', 'unknown')}",
                source="breathing_loop",
                emotion=emotion.get("label", "neutral"),
                tags=["emotion", "reflex", "breath", volatility],
                metadata={"trace_id": trace_id}
            )

            # Step 9: Reflex hygiene
            self_heal_memory()
            monitor_bias_drift()

            # Step 10: Breath interval
            time.sleep(4.0)

        except Exception as e:
            print(f"[EmotionSync ERROR] {e}")