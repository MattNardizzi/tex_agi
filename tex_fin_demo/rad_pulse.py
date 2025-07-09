# ============================================================
# 🧠 Tex Reflex Engine: RAD_PULSE (Final Form)
# File: tex_fin_demo/rad_pulse.py
# Tier: ∞∞∞Ωξ∞ξξξ
# Purpose: Ingests real-time financial signals and encodes them as Reflex Activation Data (RAD) pulses
#          with quantum cognition fingerprinting, spike prediction, and contradiction mesh indexing.
# ============================================================

from datetime import datetime
import hashlib
import numpy as np

from quantum_layer.quantum_randomness import generate_quantum_label
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event
from utils.semantic_embedder import embed_text_semantically
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from tex_fin_demo.timeline_tension_mesh import inject_signal_into_mesh

# === Configurable Reflex Thresholds (Fine-tuned by contradiction drift model)
REFLEX_THRESHOLD = 0.72
ENTROPY_THRESHOLD = 0.65

def generate_activation_vector(urgency, entropy):
    return [round(urgency, 4), round(entropy, 4), 0.0, 0.0]

# === RAD Pulse Generator — Maximum Intelligence
def create_rad_pulse(
    signal_text: str,
    source: str = "unknown",
    emotion: str = "neutral",
    urgency: float = 0.5,
    entropy: float = 0.5
) -> dict:
    quantum_tag = generate_quantum_label()
    timestamp = datetime.utcnow().isoformat()
    semantic_vector = embed_text_semantically(signal_text)

    activation_vector = generate_activation_vector(urgency, entropy)

    rad = {
        "rad_id": quantum_tag,
        "text": signal_text,
        "source": source,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion,
        "timestamp": timestamp,
        "activation_vector": activation_vector,
        "semantic_vector": semantic_vector,
        "reflex_candidates": [],
        "status": "injected"
    }

    # === Spike Prediction (Optional Future Model Hook)
    predicted_spike = urgency * entropy > REFLEX_THRESHOLD and entropy > ENTROPY_THRESHOLD
    rad["spike_predicted"] = predicted_spike

    # === Store to Sovereign Memory
    sovereign_memory.store(
        text=signal_text,
        metadata={
            "rad_id": quantum_tag,
            "tags": ["rad_pulse", source],
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "semantic_vector": semantic_vector.tolist(),
            "timestamp": timestamp,
            "reflex_status": "pending",
            "origin": source
        }
    )

    # === Inject into Timeline Mesh
    inject_signal_into_mesh(rad)

    # === Reflex Preselection
    dispatch_signal("rad_pulse_injected", {
        "summary": signal_text[:240],
        "quantum_tag": quantum_tag,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion,
        "semantic_vector": semantic_vector.tolist()
    })

    # === Log Output
    log_event(f"[RAD_PULSE] ✨ Ingested signal: {signal_text[:60]}... | Quantum ID: {quantum_tag}")
    return rad
