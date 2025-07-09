# ============================================================
# 🧠 Timeline Tension Mesh — Final Form (Quantum-Epistemic Grid)
# File: tex_fin_demo/timeline_tension_mesh.py
# Tier: ∞∞∞ΩΩΞΞΞΞΞΞΞΞΞΞΞ — Self-Evolving Contradiction Pressure Network
# Purpose: Tracks, scores, forecasts, and evolves RAD pulse contradiction states in real time.
# ============================================================

import uuid
import numpy as np
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event
from utils.semantic_embedder import embed_text_semantically
from utils.adaptive_critic import update_tension_weights  # ⬅️ Adaptive reflex critic
from quantum_layer.quantum_randomness import generate_quantum_label

# === Global Live Mesh State
TENSION_MESH = []
HISTORY_WINDOW = 30  # Number of past entries to adapt from

# === Initial Coefficients (evolve during runtime)
TENSION_WEIGHTS = {
    "urgency": 0.35,
    "entropy": 0.35,
    "semantic_spike": 0.2,
    "emotion_vector_drift": 0.1,
    "temporal_resonance": 0.0  # starts off and rises if helpful
}

# === Predict timeline reverberation
def forecast_temporal_resonance(current_vec, mesh):
    recent = [np.array(e["semantic_vector"]) for e in mesh[-5:] if "semantic_vector" in e]
    if not recent: return 0.0
    similarities = [np.dot(current_vec, v) / (np.linalg.norm(current_vec) * np.linalg.norm(v) + 1e-9) for v in recent]
    return round(np.mean(similarities), 4)

# === Inject RAD into Timeline Mesh
def inject_signal_into_mesh(rad):
    try:
        urgency = rad.get("urgency", 0.5)
        entropy = rad.get("entropy", 0.5)
        semantic_vector = np.array(rad.get("semantic_vector", [0.0] * 384))
        emotion = rad.get("emotion", "neutral")
        timestamp = rad.get("timestamp", datetime.utcnow().isoformat())
        mesh_id = f"mesh_{uuid.uuid4().hex[:10]}"
        rad_id = rad.get("rad_id", generate_quantum_label())

        # === Semantic Spike (volatility vs recent memory)
        prev_vectors = [np.array(entry["semantic_vector"]) for entry in TENSION_MESH[-10:] if "semantic_vector" in entry]
        semantic_spike = round(np.mean([np.linalg.norm(semantic_vector - v) for v in prev_vectors]), 4) if prev_vectors else 0.0

        # === Emotional Drift
        emotion_drift = 1.0 if emotion not in ["neutral", "calm", "reflective"] else 0.0

        # === Temporal Resonance Forecast
        temporal_resonance = forecast_temporal_resonance(semantic_vector, TENSION_MESH)

        # === Live-Adaptive Weights
        global TENSION_WEIGHTS
        if len(TENSION_MESH) >= HISTORY_WINDOW:
            TENSION_WEIGHTS = update_tension_weights(TENSION_WEIGHTS, recent_outcomes=TENSION_MESH[-HISTORY_WINDOW:])

        # === Tension Score
        tension_score = round(
            urgency * TENSION_WEIGHTS["urgency"] +
            entropy * TENSION_WEIGHTS["entropy"] +
            semantic_spike * TENSION_WEIGHTS["semantic_spike"] +
            emotion_drift * TENSION_WEIGHTS["emotion_vector_drift"] +
            temporal_resonance * TENSION_WEIGHTS["temporal_resonance"],
            4
        )

        # === Full Mesh Entry
        mesh_entry = {
            "mesh_id": mesh_id,
            "rad_id": rad_id,
            "timestamp": timestamp,
            "tension_score": tension_score,
            "semantic_spike": semantic_spike,
            "temporal_resonance": temporal_resonance,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "semantic_vector": semantic_vector.tolist(),
            "reflex_candidates": rad.get("reflex_candidates", []),
            "trajectory_tag": f"ΩΞ_{str(hash(rad_id))[-6:]}"
        }

        TENSION_MESH.append(mesh_entry)

        # === Critical Injection Logging
        if tension_score >= 0.88:
            sovereign_memory.store(
                text=f"[TENSION_MESH] ⚠️ High-Pressure Signal: {rad.get('text', '')[:120]}...",
                metadata={
                    "rad_id": rad_id,
                    "tags": ["timeline_contradiction", "reflex_tension", "mesh_alert"],
                    "tension_score": tension_score,
                    "semantic_spike": semantic_spike,
                    "temporal_resonance": temporal_resonance,
                    "emotion": emotion,
                    "urgency": urgency,
                    "entropy": entropy,
                    "timestamp": timestamp,
                    "trajectory_tag": mesh_entry["trajectory_tag"]
                }
            )

        log_event(
            f"[TENSION_MESH] Injected → Score: {tension_score} | Emotion: {emotion} | Spike: {semantic_spike:.3f} | Resonance: {temporal_resonance:.3f}"
        )

    except Exception as e:
        log_event(f"[TENSION_MESH ERROR] {e}", level="error")