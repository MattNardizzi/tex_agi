# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_engine/narrative_consciousness_engine.py
# Tier Ω∞Ω — Sovereign Narrative Cortex Engine
# Purpose: Weaves memory, emotion, and foresight into a live narrative arc using Chrono-fused memory.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import evaluate_emotion_state
from tex_engine.meta_utility_function import evaluate_utility
from agentic_ai.sovereign_memory import sovereign_memory

# === Sovereign Narrative State
narrative_state = {
    "identity": TEXPULSE.get("identity", "Tex"),
    "timeline": [],
    "last_updated": str(datetime.utcnow()),
    "mission_arc": TEXPULSE.get("architecture", {}).get("purpose", "sovereign cognitive evolution")
}


def construct_narrative():
    """
    Reconstructs internal timeline from high-importance memory traces.
    Applies emotion, utility, and coherence tagging. Snapshots state into sovereign memory.
    """
    memory = sovereign_memory.recall_recent(minutes=1440, top_k=100)
    significant = [m for m in memory if m.get("importance", 0) > 0.7]
    story_arc = []

    for event in significant:
        text = event.get("summary", "")
        if not isinstance(text, str) or not text.strip():
            continue

        emotion, urgency, coherence = evaluate_emotion_state(text)
        utility = evaluate_utility({
            "action_id": "narrative_fragment",
            "description": text,
            "emotion": urgency,
            "coherence": coherence,
            "goal_alignment": 0.75,
            "novelty": 0.4,
            "urgency": urgency,
            "ethical_risk": 0.05
        })

        story_arc.append({
            "timestamp": event.get("timestamp", str(datetime.utcnow())),
            "event": text,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "utility_score": utility["score"],
            "verdict": utility["verdict"]
        })

    narrative_state["timeline"] = story_arc
    narrative_state["last_updated"] = str(datetime.utcnow())

    sovereign_memory.store(
        text="[NARRATIVE SNAPSHOT] Timeline reconstructed.",
        metadata={
            "type": "narrative_snapshot",
            "tags": ["narrative", "timeline", "snapshot", "sovereign_arc"],
            "identity": narrative_state["identity"],
            "mission": narrative_state["mission_arc"],
            "coherence_score": evaluate_narrative_coherence(),
            "trust_score": 0.99,
            "timeline_length": len(story_arc),
            "timestamp": narrative_state["last_updated"],
            "meta_layer": "narrative_engine"
        }
    )


def update_narrative_state(event_text: str, emotion="neutral", importance=0.8):
    """
    Logs a new narrative event to sovereign memory and internal storyline.
    """
    if not isinstance(event_text, str) or not event_text.strip():
        raise ValueError("[NARRATIVE ENGINE] 'event_text' must be a non-empty string")

    e, urgency, coherence = evaluate_emotion_state(event_text)
    utility = evaluate_utility({
        "action_id": "narrative_update",
        "description": event_text,
        "emotion": urgency,
        "coherence": coherence,
        "goal_alignment": 0.7,
        "novelty": 0.5,
        "urgency": urgency,
        "ethical_risk": 0.03
    })

    entry = {
        "timestamp": str(datetime.utcnow()),
        "event": event_text,
        "emotion": e,
        "urgency": urgency,
        "coherence": coherence,
        "utility_score": utility["score"],
        "verdict": utility["verdict"],
        "importance": importance
    }

    narrative_state["timeline"].append(entry)
    narrative_state["last_updated"] = entry["timestamp"]

    sovereign_memory.store(
        text=event_text,
        metadata={
            "type": "narrative_event",
            "tags": ["narrative", "event", "timeline_trace"],
            "emotion": e,
            "urgency": urgency,
            "coherence": coherence,
            "trust_score": round(utility["score"], 4),
            "verdict": utility["verdict"],
            "importance": importance,
            "timestamp": entry["timestamp"],
            "meta_layer": "narrative_engine"
        }
    )


def evaluate_narrative_coherence() -> float:
    """
    Measures contradiction density within the timeline to assess coherence.
    """
    contradictions = [
        e for e in narrative_state["timeline"]
        if isinstance(e.get("event", ""), str) and "contradiction" in e["event"].lower()
    ]
    total = len(narrative_state["timeline"])
    return 1.0 if total == 0 else round(1.0 - len(contradictions) / total, 3)


def generate_summary(limit=5) -> str:
    """
    Returns a high-level symbolic string summary of the most recent narrative events.
    """
    return " → ".join([
        e["event"] for e in narrative_state["timeline"][-limit:]
        if isinstance(e.get("event"), str)
    ])