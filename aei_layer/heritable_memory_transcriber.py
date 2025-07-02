# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/heritable_memory_transcriber.py
# Purpose: Transcribes critical memory patterns into inheritable genome traits
# ============================================================

from core_layer.memory_engine import fetch_recent_entries
from statistics import mean
from datetime import datetime

def extract_heritable_traits(limit=50):
    """
    Aggregates key emotional and decision signals into a heritable trait vector.
    Passed down during AEI child variant generation to preserve long-term strategy wisdom.
    """
    memories = fetch_recent_entries(key="tex_decision_log", count=limit)
    if not memories:
        print("[👣] No decision logs found for inheritance.")
        return {}

    emotions = []
    urgencies = []
    coherences = []

    for entry in memories:
        emotions.append(entry.get("emotion", "neutral"))
        urgencies.append(entry.get("urgency", 0.5))
        coherences.append(entry.get("coherence", 0.75))

    dominant_emotion = max(set(emotions), key=emotions.count) if emotions else "neutral"
    avg_urgency = round(mean(urgencies), 3)
    avg_coherence = round(mean(coherences), 3)

    traits = {
        "inherited_emotion": dominant_emotion,
        "inherited_urgency": avg_urgency,
        "inherited_coherence": avg_coherence,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "heritable_memory_transcriber"
    }

    print(f"[GENETIC IMPRINT] 🧬 Traits inherited: {traits}")
    return traits