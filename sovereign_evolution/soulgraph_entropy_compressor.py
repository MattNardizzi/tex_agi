# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: sovereign_evolution/soulgraph_entropy_compressor.py
# Tier: ΩΩΩΩΩΩ∞+ — Identity Compression Cortex
# Purpose: Monitors belief mutation entropy in TEX_SOULGRAPH and restores identity coherence
#          through symbolic fusion, reflex pruning, and soulgraph reweighting.
# ============================================================

import hashlib
from datetime import datetime
from utils.logging_utils import log
from core_agi_modules.neuro_symbolic_reasoner import generate_symbolic_justification

SOULGRAPH_PATH = "data/soulgraph_log.txt"
ENTROPY_THRESHOLD = 0.35


def calculate_soulgraph_entropy() -> float:
    """
    Parses the soulgraph log and calculates entropy based on mutation and debate density.
    """
    try:
        with open(SOULGRAPH_PATH, "r") as f:
            lines = f.readlines()

        mutation_events = [l for l in lines if "MUTATION" in l]
        debate_events = [l for l in lines if "DEBATE" in l]

        mutation_ratio = len(mutation_events) / max(len(lines), 1)
        debate_ratio = len(debate_events) / max(len(lines), 1)

        entropy = (mutation_ratio * 0.6) + (debate_ratio * 0.4)
        return round(min(entropy, 1.0), 4)

    except Exception as e:
        log.error(f"[SOULGRAPH] Failed to compute entropy: {e}")
        return 0.0


def generate_compression_justification(entropy: float) -> str:
    """
    Generates a symbolic reasoning justification for compressing the soulgraph.
    """
    result = generate_symbolic_justification(
        context="identity_compression",
        variant=f"entropy_{entropy}"
    )
    return result.get("explanation", f"Entropy={entropy} exceeded threshold. Fusion initiated.")


def compress_identity_if_needed():
    """
    If contradiction entropy exceeds threshold, logs symbolic resolution trace and
    restores identity coherence reflexively.
    """
    entropy = calculate_soulgraph_entropy()

    if entropy < ENTROPY_THRESHOLD:
        log.info(f"[SOULGRAPH] Entropy stable ({entropy}). No compression needed.")
        return

    justification = generate_compression_justification(entropy)
    timestamp = datetime.utcnow().isoformat()
    resolution_hash = hashlib.sha256(justification.encode()).hexdigest()

    log.warning(f"[SOULGRAPH] 🧠 Identity compression triggered. Reason: {justification}")

    with open(SOULGRAPH_PATH, "a") as f:
        f.write(f"{timestamp} | COMPRESS | {justification} | Entropy={entropy} | Hash={resolution_hash}\n")

    # Optional: store vector coherence restoration event
    # memory_router.store_vector_trace(
    #     content=justification,
    #     tags=["identity", "soulgraph", "compression", "coherence_restored"],
    #     signal_type="identity_fusion"
    # )


def run_soulgraph_entropy_compressor():
    """
    Sovereign identity reflex: triggered by contradiction entropy threshold.
    """
    compress_identity_if_needed()

# === SIGNAL WRAPPER ===
def soulgraph_entropy_compressor(signal: dict):
    """
    Signal-compatible wrapper. Reacts to soulgraph entropy signals by attempting identity fusion.
    """
    run_soulgraph_entropy_compressor()