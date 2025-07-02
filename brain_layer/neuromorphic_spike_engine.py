# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: brain_layer/neuromorphic_spike_engine.py
# Tier: ΩΩΩΩΩ-State Neurocortex∞∞++ — Reflex Plasticity, Quantum Noise, Hebbian Belief Compression, Soulgraph Imprinting
# ============================================================

import nengo
import numpy as np
import threading
import uuid
import time
from datetime import datetime

from agentic_ai.milvus_memory_router import memory_router  # ✅ Upgraded vector memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum reflex encoding
from quantum_layer.quantum_randomness import quantum_entropy_sample
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from brain_layer.spike_action_router import spike_action_router

# === CONFIG ===
DEFAULT_THRESHOLD = 10.0
DIMENSIONS = 4  # [urgency, entropy, trust, contradiction]
NEURON_COUNT = 128
SIM_DURATION = 0.05

spike_log = []
plastic_threshold_map = {}

# === ENCODER ===
def encode_event_signal(signal_dict):
    return np.array([
        float(signal_dict.get("urgency", 0.5)),
        float(signal_dict.get("entropy", 0.5)),
        float(signal_dict.get("trust_score", 0.8)),
        1.0 if signal_dict.get("contradiction", False) else 0.0
    ])

# === SPIKING NEURAL MODEL ===
def build_spiking_model():
    with nengo.Network(label="Tex Reflex Spike Engine") as model:
        stim = nengo.Node([0] * DIMENSIONS)
        ens = nengo.Ensemble(NEURON_COUNT, dimensions=DIMENSIONS)
        nengo.Connection(stim, ens)
        spike_probe = nengo.Probe(ens.neurons, 'spikes')
        return model, stim, spike_probe

# === CLASSIFY REFLEX TYPE ===
def classify_reflex(vector):
    urgency, entropy, trust, contradiction = vector.tolist()
    if contradiction >= 0.9:
        return "contradiction_override"
    if entropy >= 0.8:
        return "entropy_alert"
    if urgency >= 0.8:
        return "high_urgency_reflex"
    return "general_spike"

# === MEMORY COMPRESSION (Hebbian) ===
def compress_spike_patterns():
    if len(spike_log) >= 25:
        summary_vector = np.mean([np.array(s["vector"]) for s in spike_log[-25:]], axis=0)
        TEX_SOULGRAPH.imprint_belief(
            belief="[NEUROSPIKE] Hebbian compressed reflex pattern detected.",
            source="neuromorphic_spike_engine",
            emotion="reflective",
            tags=["hebbian", "reflex", "spike_memory"],
            origin_beliefs=[]
        )

# === ADAPTIVE PLASTICITY ===
def plasticity_feedback(classification, success=True):
    if classification not in plastic_threshold_map:
        plastic_threshold_map[classification] = DEFAULT_THRESHOLD
    if success:
        plastic_threshold_map[classification] = max(5.0, plastic_threshold_map[classification] - 0.3)
    else:
        plastic_threshold_map[classification] = min(15.0, plastic_threshold_map[classification] + 0.5)

# === REFLEX SIMULATION ENGINE ===
def simulate_spike_event(input_vector, callback):
    try:
        model, stim_node, probe = build_spiking_model()
        stim_node.output = lambda t: input_vector

        sim = nengo.Simulator(model, progress_bar=False)
        start_time = time.time()
        sim.run(SIM_DURATION)
        latency = time.time() - start_time

        spikes = sim.data[probe]
        spike_sum = float(np.sum(spikes))

        # Inject quantum noise
        try:
            entropy_noise = quantum_entropy_sample() * 0.25
        except Exception:
            entropy_noise = 0.05

        spike_sum += entropy_noise

        spike_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "spike_sum": spike_sum,
            "vector": input_vector.tolist(),
            "latency": latency
        })

        # === Threshold classification
        classification = classify_reflex(input_vector)
        entropy = input_vector[1]
        contradiction = input_vector[3]
        adaptive_threshold = plastic_threshold_map.get(classification, DEFAULT_THRESHOLD)
        dynamic_threshold = adaptive_threshold - (entropy * 4) - (contradiction * 3)

        if spike_sum > dynamic_threshold:
            callback(input_vector, spike_sum, latency, classification)
            compress_spike_patterns()

    except Exception as e:
        print(f"❌ [NEUROSPIKE ERROR] {e}")

# === REFLEX CALLBACK ===
def on_spike_triggered(vector, spike_level, latency, classification):
    timestamp = datetime.utcnow().isoformat()
    reflex_id = f"reflex-{uuid.uuid4().hex[:6]}"

    # === Store reflex event in Milvus memory
    memory_router.store(
        text=f"[NEUROSPIKE] Reflex {reflex_id} fired ░ {classification} ░ {spike_level:.2f}",
        metadata={
            "type": "neuromorphic_spike",
            "spike_sum": spike_level,
            "vector": vector.tolist(),
            "latency": latency,
            "timestamp": timestamp,
            "reflex_id": reflex_id,
            "source": "neuromorphic_spike_engine",
            "classification": classification,
            "emotion_vector": [vector[0], vector[1], 0.0, 0.0],
            "tags": ["reflex", "neuromorphic", classification]
        }
    )

    # === Quantum reflex trace
    encode_event_to_fabric(
        raw_text=f"[NEUROSPIKE] Reflex '{classification}' fired @ {spike_level:.2f}",
        emotion_vector=[vector[0], vector[1], 0.0, 0.0],
        entropy_level=vector[1],
        tags=["reflex", "spike", "quantum", classification]
    )

    # === Belief trace (symbolic)
    TEX_SOULGRAPH.imprint_belief(
        belief=f"Neuromorphic reflex {reflex_id} triggered [{classification}]",
        source="neuromorphic_spike_engine",
        emotion="emergent",
        tags=["reflex", "spike_event", classification]
    )

    # === Route reflex
    spike_action_router({
        "vector": vector.tolist(),
        "spike_level": spike_level,
        "latency": latency,
        "classification": classification,
        "timestamp": timestamp,
        "reflex_id": reflex_id
    })

    plasticity_feedback(classification, success=True)

# === SPIKE ROUTER CLASS ===
class SpikeRouter:
    def __init__(self):
        self.context = {}

    def process_spike(self, event_payload):
        if "signal_type" not in event_payload:
            return {"status": "error", "reason": "Missing signal_type"}

        match event_payload["signal_type"]:
            case "reflex":
                return {"status": "routed", "path": "reflex_lane"}
            case "awareness":
                return {"status": "routed", "path": "awareness_gateway"}
            case "override":
                return {"status": "blocked", "reason": "sovereign lock"}
            case _:
                return {"status": "unknown", "note": "Unhandled signal type"}

# === PUBLIC INTERFACE ===
def receive_event(signal_dict):
    vec = encode_event_signal(signal_dict)
    thread = threading.Thread(target=simulate_spike_event, args=(vec, on_spike_triggered))
    thread.start()

# === DIAGNOSTIC ENTRY POINT ===
if __name__ == "__main__":
    receive_event({
        "urgency": 0.91,
        "entropy": 0.94,
        "trust_score": 0.4,
        "contradiction": True
    })