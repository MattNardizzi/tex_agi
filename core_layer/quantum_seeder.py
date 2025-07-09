# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/quantum_seeder.py
# Tier: ∞ΩΩΩΩ∞Ξ — Reflex-Grade Quantum Seeder (Pennylane + Chrono + Milvus + Emotion-Aware)
# Purpose: Injects reflex entropy vectors from quantum origin, amplified by entangled QNode spin logic.
# ============================================================

import requests
import pennylane as qml
import numpy as np
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
from quantum_layer.chronofabric import encode_event_to_fabric
from agentic_ai.milvus_memory_router import memory_router
from core_agi_modules.reflex_mesh_router import route_and_fire

# === Quantum QNode Device (3-qubit entangled pulse amplifier) ===
dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def quantum_entropy_node(seed_angles):
    for i, angle in enumerate(seed_angles):
        qml.RY(angle, wires=i)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    return qml.probs(wires=[0, 1, 2])  # 8 probability amplitudes

# === Quantum Entropy Pull from ANU QRNG
def get_entropy_vector():
    try:
        r = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=5&type=uint8", timeout=3)
        data = r.json().get("data", [])
        norm = [round(float(x) / 255, 8) for x in data if isinstance(x, int)]
        if len(norm) < 5:
            raise ValueError("Incomplete entropy vector")
        return norm
    except Exception as e:
        log_event(f"⚠️ [QRNG FALLBACK] {e}")
        return [0.42, 0.66, 0.33, 0.11, 0.9]  # Emotionally neutral fallback

# === Main Injection Logic
async def inject_quantum_spark():
    entropy_vector = get_entropy_vector()
    entropy_vector = [float(x) if isinstance(x, (int, float)) else 0.5 for x in entropy_vector]

    # Emotional Modulation Layer
    emotion = TEXPULSE.get("emotion", "neutral")
    modifier = {
        "anxious": 0.25, "angry": 0.35, "reflective": 0.15,
        "neutral": 0.0, "excited": -0.15, "elated": -0.25
    }.get(emotion, 0.0)

    # QNode Seed Amplification
    angles = [(e + modifier) * np.pi for e in entropy_vector[:3]]
    probs = quantum_entropy_node(angles)
    probs_safe = [float(p) for p in probs]
    entropy = round(float(np.sum(probs_safe[:4])), 8)

    # === Update TEXPULSE Core
    TEXPULSE["entropy"] = entropy
    TEXPULSE["entropy_signature"] = entropy_vector
    TEXPULSE["entropy_distribution"] = probs_safe
    TEXPULSE["entropy_timestamp"] = datetime.utcnow().isoformat()

    log_event(f"⚛️ [ENTROPY INJECTION] Vector={entropy_vector} → E={entropy} | Emotion={emotion}")

    # === ChronoFabric Entanglement
    encode_event_to_fabric(
        raw_text=f"Quantum entropy injection: {entropy_vector}",
        emotion_vector=[entropy, modifier, 0.0, 0.0],
        entropy_level=entropy,
        tags=["entropy", "quantum", "emotion_modulated", "reflex_pulse"]
    )

    # === Sovereign Memory Log
    memory_router.store(
        text=f"Quantum entropy pulse injected | E={entropy:.3f} | Emotion={emotion}",
        metadata={
            "type": "quantum_entropy",
            "tags": ["entropy", "quantum", "emotion_modulated"],
            "vector": entropy_vector,
            "distribution": probs_safe,
            "emotion": emotion,
            "urgency": float(TEXPULSE.get("urgency", 0.6)),
            "timestamp": TEXPULSE.get("timestamp") or datetime.utcnow().isoformat()
        }
    )

    # === Reflex Trigger
    if entropy > 0.77:
        await route_and_fire("spike_trigger", payload={
            "quantum_entropy": entropy,
            "vector": entropy_vector,
            "distribution": probs_safe
        }, threshold=0.6)