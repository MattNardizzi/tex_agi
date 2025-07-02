# thread_weaver.py
# Tier Ω∞ Temporal & Thematic Memory Thread Weaver (Final Form)
# Location: core_agi_modules/memory_layer/thread_weaver.py

from datetime import datetime
import hashlib
import numpy as np
from core_agi_modules.memory_layer.contradiction_logger import detect_contradiction

# === Belief Thread Constructor ===
def weave_memory_thread(events: list, thread_name="untitled_thread", purpose="reflex_recall"):
    """
    Weaves a list of semantically or temporally linked memory events into a coherent thread.
    Includes emotion entropy, contradiction scanning, and symbolic tags.
    """
    if not events or len(events) < 2:
        print("⚠️ [THREAD_WEAVER] Not enough events to weave.")
        return None

    events = sorted(events, key=lambda e: e.get("timestamp", ""))
    segments = [f"[{e['emotion']}] {e['content']}" for e in events]
    thread_body = "\n→ ".join(segments)
    combined = "".join(e["content"] for e in events)
    thread_id = hashlib.sha256(combined.encode()).hexdigest()

    emotion_entropy = thread_entropy(events)
    dominant = dominant_emotion(events)

    conflicts = [(a["content"], b["content"]) for a in events for b in events
                 if a != b and detect_contradiction(a["content"], b["content"])]

    summary = {
        "thread_name": thread_name,
        "thread_body": thread_body,
        "emotion_dominant": dominant,
        "emotion_entropy": emotion_entropy,
        "event_count": len(events),
        "timestamp": datetime.utcnow().isoformat(),
        "thread_id": thread_id,
        "thread_purpose": purpose,
        "tags": ["coherent", "emotion_traced"]
    }

    if conflicts:
        summary["contains_contradiction"] = True
        summary["contradiction_pairs"] = conflicts[:3]

    print(f"🧵 [THREAD] '{thread_name}' built. Entropy={emotion_entropy} | Dominant={dominant}")
    return summary

# === Emotion Dominance Helper ===
def dominant_emotion(events):
    tally = {}
    for e in events:
        emo = e.get("emotion", "neutral")
        tally[emo] = tally.get(emo, 0) + 1
    sorted_tally = sorted(tally.items(), key=lambda item: item[1], reverse=True)
    return sorted_tally[0][0] if sorted_tally else "neutral"

# === Entropy Scorer ===
def thread_entropy(events):
    emotions = [e.get("emotion", "neutral") for e in events]
    unique = set(emotions)
    ratios = [emotions.count(u)/len(emotions) for u in unique]
    entropy = -sum(p * np.log2(p) for p in ratios)
    return round(entropy, 4)