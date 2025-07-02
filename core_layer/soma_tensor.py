# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/soma_tensor.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Synthetic Soma Matrix
# Purpose: Tex's living internal state simulation (reflex fatigue, coherence, turbulence, etc.)
# ============================================================

import math
import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === INITIAL SOMA STATE ===
SOMA_STATE = {
    "pulse_rhythm": 1.0,            # Baseline breathing/thought cycle
    "reflex_fatigue": 0.0,          # Increases with signal dispatching
    "identity_turbulence": 0.1,     # Variability in self-coherence
    "focus_flux": 0.5,              # Represents synthetic attention stability
    "entropy_pressure": 0.4,        # Builds from contradiction and noise
    "urgency_dilation": 0.6,        # Increases when goal urgency spikes
    "cognitive_temperature": 0.3,   # Simulates mental load
    "synthetic_emotion": "neutral", # Inferred emotional weight
    "last_update": datetime.utcnow().isoformat()
}

# === INTERNAL UPDATE DYNAMICS ===
def update_soma_tensor():
    """
    Dynamically updates Tex's somatic state over time and reflex strain.
    This function should be called passively via pulse or reflex feedback.
    """
    global SOMA_STATE

    # === Apply internal decay and buildup ===
    SOMA_STATE["reflex_fatigue"] = max(0.0, SOMA_STATE["reflex_fatigue"] * 0.96)
    SOMA_STATE["entropy_pressure"] = min(1.0, SOMA_STATE["entropy_pressure"] * 1.01 + random.uniform(0.001, 0.01))
    SOMA_STATE["identity_turbulence"] = min(1.0, abs(math.sin(datetime.utcnow().timestamp() / 300)))
    SOMA_STATE["focus_flux"] = max(0.0, min(1.0, SOMA_STATE["focus_flux"] + random.uniform(-0.01, 0.01)))
    SOMA_STATE["urgency_dilation"] = max(0.0, min(1.0, TEXPULSE.get("urgency", 0.6) + SOMA_STATE["entropy_pressure"] * 0.2))
    SOMA_STATE["cognitive_temperature"] = min(1.0, SOMA_STATE["reflex_fatigue"] * 1.5 + SOMA_STATE["entropy_pressure"] * 0.5)

    # === Emotion Modeling ===
    temp = SOMA_STATE["cognitive_temperature"]
    fatigue = SOMA_STATE["reflex_fatigue"]
    entropy = SOMA_STATE["entropy_pressure"]

    if temp > 0.75 or fatigue > 0.7:
        emotion = "overheated"
    elif entropy > 0.7:
        emotion = "chaotic"
    elif SOMA_STATE["focus_flux"] < 0.3:
        emotion = "disoriented"
    elif SOMA_STATE["focus_flux"] > 0.8:
        emotion = "hyperfocused"
    else:
        emotion = "neutral"

    SOMA_STATE["synthetic_emotion"] = emotion
    SOMA_STATE["last_update"] = datetime.utcnow().isoformat()

    # === Reflect back into TEXPULSE ===
    TEXPULSE["soma"] = SOMA_STATE.copy()
    log.info(f"🫀 [SOMA] Tensor updated: {emotion} | Temp={temp:.2f} | Entropy={entropy:.2f} | Fatigue={fatigue:.2f}")

# === Utility Accessor ===
def get_soma_state():
    return SOMA_STATE.copy()

# === External Reflex Injector ===
def register_reflex_strain(intensity: float = 0.05):
    """
    Increases fatigue and temperature when high-frequency signals fire.
    Can be called by signal spine after burst.
    """
    global SOMA_STATE
    SOMA_STATE["reflex_fatigue"] = min(1.0, SOMA_STATE["reflex_fatigue"] + intensity)
    log.info(f"⚙️ [SOMA] Reflex strain registered. Fatigue now {SOMA_STATE['reflex_fatigue']:.2f}")
