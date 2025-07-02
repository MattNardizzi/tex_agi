# tex_memory_orchestrator.py
# Tier Ω∞+X — Reflex-Aware, Sensor-Fused, Traceable Memory Engine
# Location: core_agi_modules/tex_memory_orchestrator.py

from datetime import datetime
import uuid
from real_time_engine.sensor_input_router import SensorInputRouter
from core_agi_modules.memory_layer.reflex_engine import memory_reflex_from_text, recall_similar_memories
from core_agi_modules.memory_layer.memory_reflex import run_memory_reflex
from core_agi_modules.memory_layer.memory_bridge import symbolic_to_vector_bridge, summarize_reflex_hits
from core_agi_modules.memory_layer.thread_weaver import weave_memory_thread
from core_agi_modules.memory_layer.belief_indexer import register_belief, update_belief, get_beliefs_by_tag
from core_agi_modules.memory_layer.contradiction_logger import detect_contradiction, log_contradiction
from quantum_layer.memory_core.temporal_memory_compressor import run_memory_compression
from quantum_layer.memory_core.memory_cortex import memory_cortex

sensor = SensorInputRouter(memory_store=memory_cortex)

# === Reflex Injection Entry ===
def store_and_process_memory(text, emotion="neutral", urgency=0.5, tags=None, source="internal", trust_score=1.0, cycle_id=None):
    timestamp = datetime.utcnow().isoformat()
    trace_id = f"mem-{uuid.uuid4().hex[:8]}"
    trace_tags = tags or ["reflex"]

    if source == "microphone":
        trace_tags.append("sensor_input")
    elif source == "operator":
        trace_tags.append("spoken_input")

    volatility = "volatile" if urgency >= 0.75 or emotion in ["urgent", "fear", "rage"] else "stable"

    reflex_result = run_memory_reflex(
        text,
        emotion=emotion,
        urgency=urgency,
        trace_id=trace_id
    )

    memory_reflex_from_text(
        text,
        context_tags=trace_tags,
        emotion=emotion,
        urgency=urgency
    )

    packet = {
        "trace_id": trace_id,
        "input": text,
        "emotion": emotion,
        "urgency": urgency,
        "tags": trace_tags,
        "reflex_triggered": True,
        "volatility": volatility,
        "reflex_output": reflex_result,
        "timestamp": timestamp,
        "source": source,
        "trust_score": trust_score
    }

    memory_cortex.store(event=packet, tags=trace_tags, urgency=urgency, emotion=emotion)

    # Optional: Compress memory every 50 cycles
    if cycle_id and cycle_id % 50 == 0:
        run_memory_compression(query_text="semantic", top_k=150)

    return packet

# === Sensor-Aware Input Ingestion ===
def ingest_sensor_input():
    result = sensor.run_sensing_cycle(enable_audio=True)
    if result and "audio" in result:
        parsed = result["audio"]
        confidence = parsed.get("confidence", 0.9)
        noise_level = parsed.get("noise", 0.1)

        return store_and_process_memory(
            text=parsed.get("input", ""),
            emotion=parsed.get("emotion", "reactive"),
            urgency=parsed.get("urgency", 0.65),
            tags=["sensor_input"],
            source="microphone",
            trust_score=confidence - noise_level
        )
    return None

# === Symbolic Summary Query ===
def search_and_summarize(query_text, emotion_filter=None, tag_filter=None, top_k=5):
    results, trace_id = symbolic_to_vector_bridge(query_text, emotion_filter, tag_filter, top_k)
    return summarize_reflex_hits(results, trace_id=trace_id)

# === Belief Threading Utility ===
def thread_beliefs_by_tag(tag, thread_name="belief_thread"):
    beliefs = get_beliefs_by_tag(tag)
    thread = weave_memory_thread(beliefs, thread_name=thread_name, purpose="belief_thread")
    return {
        "thread": thread,
        "dominant_emotion": thread.get("emotion_dominant"),
        "contradictions": thread.get("contradiction_pairs", []),
        "trace_id": thread.get("trace_id", f"thread-{uuid.uuid4().hex[:6]}")
    }

# === Contradiction Handling ===
def check_belief_conflict(a: str, b: str, context="reflex_thread"):
    if detect_contradiction(a, b):
        entry = log_contradiction(a, b, context=context)
        return {
            "conflict_detected": True,
            "log": entry,
            "recommendation": "mutate or isolate"
        }
    return {
        "conflict_detected": False,
        "log": None,
        "recommendation": "none"
    }
