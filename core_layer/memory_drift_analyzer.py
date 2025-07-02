# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/memory_drift_analyzer.py
# Tier: ∞ΩΩΩΩ — Sovereign Drift Auditor Cortex (Chrono + Vector | Reflex-Safe | Entropy-Aware)
# Purpose: Computes systemic cognitive drift from identity-tagged memory volatility, emotion tension, entropy & urgency fusion.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from random import uniform
from datetime import datetime

def calculate_drift_pressure(top_k: int = 6) -> float:
    """
    Evaluates long-term cognitive memory drift using trust volatility, emotional instability,
    urgency and entropy from TEXPULSE, and stochastic noise modulation.

    Returns:
        float: Drift score from 0.0 to 1.0
    """
    try:
        memories = sovereign_memory.query_by_tags(["identity"], top_k=top_k)

        if not memories:
            return 0.3  # fallback if identity memory is sparse

        urgency = TEXPULSE.get("urgency", 0.7)
        entropy = TEXPULSE.get("entropy", 0.4)

        # === Component 1: Heat × Trust Volatility Product
        volatility = sum(
            float(m.get("heat", 0.5)) * float(m.get("trust_score", 1.0))
            for m in memories
        ) / len(memories)

        # === Component 2: Emotional Instability Heuristic
        emotion_instability = sum(
            1.0 if m.get("emotion", "") in ["uncertain", "fear", "volatile", "contradiction"] else 0.0
            for m in memories
        ) / len(memories)

        # === Component 3: Entropy-Urgency Fusion + Random Noise Dampener
        noise = uniform(0.01, 0.025)
        drift_score = round(
            (volatility * 0.5) +
            (emotion_instability * 0.3) +
            (entropy * 0.15) +
            (urgency * 0.05) +
            noise,
            4
        )

        return min(max(drift_score, 0.0), 1.0)

    except Exception as e:
        print(f"❌ [DRIFT ERROR] Memory drift evaluation failed: {e}")
        return 0.5