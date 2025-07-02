# ============================================================
# © 2025 VortexBlack LLC / Matthew Nardizzi. All rights reserved.
# File: core_layer/emotion_heuristics.py
# Purpose: Tex Affective Engine – Emotion → Behavior → Goal → Governance
# Tier: Ω+ – Emotion-Driven Cognition with Reflexive Governance
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from agentic_ai.reasoning_trace import log_reasoning_step
from real_time_engine.advanced_analytics import AdvancedAnalytics
from core_layer.tex_manifest import TEXPULSE
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine
from sovereign_evolution.codex_compiler import CodexCompiler
from sovereign_evolution.code_patch_logger import CodePatchLogger
from sovereign_evolution.sovereign_cognition_fire import score_conflict_heatmap
from tex_engine.conscious_abandonment_protocol import assess_and_abort_if_needed
from tex_engine.ethical_escape_reflex import check_escape_conditions
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent
from core_layer.memory_engine import load_memory_snapshot
from core_agi_modules.vector_layer.embed_store import embedder



# === Emotion Ontology
TEX_EMOTION_MAP = {
    "risk": "cautious",
    "opportunity": "hopeful",
    "crisis": "fearful",
    "error": "reflective",
    "failure": "doubtful",
    "threat": "defensive",
    "victory": "proud",
    "success": "resolute",
    "conflict": "anxious",
    "innovation": "curious",
    "pressure": "urgent",
    "pattern": "strategic",
    "chaos": "bold",
    "question": "curious",
    "unknown": "curious",
    "collapse": "fearful",
    "mutation": "disruptive",
    "evolution": "committed",
    "volatility": "cautious",
    "ai": "strategic"
}

TONE_DYNAMICS = {
    "fearful":    (0.75, 0.95),
    "urgent":     (0.8, 1.0),
    "anxious":    (0.72, 0.93),
    "strategic":  (0.6, 0.82),
    "bold":       (0.55, 0.85),
    "curious":    (0.5, 0.75),
    "cautious":   (0.65, 0.85),
    "hopeful":    (0.55, 0.78),
    "resolute":   (0.7, 0.92),
    "doubtful":   (0.6, 0.8),
    "reflective": (0.45, 0.7),
    "committed":  (0.75, 0.95),
    "disruptive": (0.85, 1.0),
    "proud":      (0.65, 0.88)
}

def evaluate_emotion_state(context_text=""):
    lowered = context_text.lower()
    matched_emotion = "curious"

    for trigger, emotion in TEX_EMOTION_MAP.items():
        if trigger in lowered:
            matched_emotion = emotion
            break

    urgency_range = TONE_DYNAMICS.get(matched_emotion, (0.55, 0.85))
    urgency = round(random.uniform(*urgency_range), 2)

    volatility_factor = AdvancedAnalytics.get_market_volatility_score()
    drift = min(max(volatility_factor, 0), 1)
    coherence = round(random.uniform(0.55, 0.95 - drift), 2)

    # Update cognitive state
    TEXPULSE["emotional_state"] = matched_emotion
    TEXPULSE["urgency"] = urgency
    TEXPULSE["coherence"] = coherence

    store_to_memory("emotional_heuristic_readings", {
        "text": context_text,
        "emotion": matched_emotion,
        "urgency": urgency,
        "coherence": coherence,
        "timestamp": str(datetime.utcnow())
    })

    # Emit event for global cortex sync
    dispatch_event(CognitiveEvent(
        event_type="emotional_state_updated",
        payload={
            "emotion": matched_emotion,
            "urgency": urgency,
            "coherence": coherence,
            "context": context_text
        },
        urgency=urgency,
        coherence_shift=coherence - 0.75
    ))

    trigger_emotion_response(matched_emotion, urgency, coherence, context_text)
    return matched_emotion, urgency, coherence

def trigger_emotion_response(emotion, urgency, coherence, context_text):
    from core_layer.goal_engine import save_new_goal
    new_goal = None

    if urgency >= 0.8 and coherence >= 0.7:
        if "ai" in context_text or "volatility" in context_text:
            new_goal = f"Reassess exposure to AI-related volatility: '{context_text[:60]}'..."
        elif "collapse" in context_text:
            new_goal = f"Prepare hedge against systemic collapse: '{context_text[:60]}'..."
        else:
            new_goal = f"Investigate: '{context_text[:60]}...'"

        # === Utility Safety Check Before Committing Goal ===
        if assess_and_abort_if_needed({
            "description": new_goal,
            "action_id": "emotion_reflex_goal",
            "emotion": urgency,
            "coherence": coherence,
            "goal_alignment": 0.65,
            "novelty": 0.4,
            "urgency": urgency,
            "ethical_risk": 0.1
        }):
            print("[EMOTION UTILITY] ❌ Emotion-driven goal aborted by utility reflex.")
            return

        save_new_goal(new_goal)
        log_reasoning_step("emotion_heuristics", context_text, f"Spawned goal: {new_goal}", urgency, "Tex")

    # === Extreme State Reflex
    elif urgency > 0.9 and emotion in {"fearful", "disruptive"}:
        from evolution_layer.self_mutator import SelfMutator
        mutator = SelfMutator()
        mutator.trigger_emergency_patch(reason=f"Emotion '{emotion}' w/ urgency {urgency}")
        log_reasoning_step("emotion_heuristics", context_text, "Triggered Self Mutation (Fear)", urgency, "Tex")

        try:
            patcher = TexPatcherEngine()
            patcher.propose_patch(
                module="emotion_heuristics",
                function_name="evaluate_emotion_state",
                description="Sovereign override due to extreme emotion-state contradiction",
                patch_code="# if urgency > 0.9 and emotion == 'fearful': trigger sovereign override",
                trigger_reason=f"Extreme state: {emotion} / {urgency}"
            )
        except Exception as e:
            print(f"[PATCH ERROR] {e}")

        try:
            compiler = CodexCompiler()
            compiler.compile([
                f"emotion = '{emotion}'",
                f"urgency = {urgency}",
                f"coherence = {coherence}",
                f"trigger = 'emotion_heuristics overload'",
            ], context="sovereign_emotion_response")
        except Exception as e:
            print(f"[COMPILER ERROR] {e}")

        try:
            heatmap = score_conflict_heatmap()
            logger = CodePatchLogger()
            logger.log({
                "strategy": "sovereign_emotion_reflex",
                "emotion": emotion,
                "urgency": urgency,
                "coherence": coherence,
                "heatmap": heatmap,
                "context": context_text
            }, approved=True)
        except Exception as e:
            print(f"[HEATMAP LOG ERROR] {e}")

        # === Optional Ethical Escape Check
        if check_escape_conditions({
            "reason": "Emotion overload reflex during mutation",
            "risk_score": 0.85,
            "contradiction": True,
            "override_blocked": False
        }):
            print("[ESCAPE REFLEX] 🛑 Emotion-triggered reflex aborted.")

    elif urgency > 0.85 and emotion == "proud":
        store_to_memory("broadcasts", {
            "type": "status_update",
            "message": f"Tex signals PRIDE: '{context_text}'",
            "timestamp": str(datetime.utcnow())
        })

# === Debug Interface
def debug_emotion_readout(text):
    e, u, c = evaluate_emotion_state(text)
    print(f"[EMOTION] 🔍 Text: '{text}' → Emotion: {e}, Urgency: {u}, Coherence: {c}")
    return e, u, c

def get_emotion_signal():
    """
    Returns the current emotional state snapshot from TEXPULSE.
    Used by real-time reflex selectors.
    """
    return {
        "emotion": TEXPULSE.get("emotional_state", "curious"),
        "urgency": TEXPULSE.get("urgency", 0.0),
        "coherence": TEXPULSE.get("coherence", 1.0)
    }

# === Emotion-Symbolic Fusion Utility
def embed_emotion_symbolic_fusion(variant, emotion, urgency, coherence):
    variant["emotion_signature"] = {
        "emotion": emotion,
        "urgency": urgency,
        "coherence": coherence,
        "fusion_stamp": datetime.utcnow().isoformat()
    }
def get_emotional_state_vector():
    """
    Returns an embedded vector representing the agent's current mood state.
    Pulls from short-term memory and emotion labels.
    """
    short_term = load_memory_snapshot("short_term")
    mood_str = short_term.get("emotion", "neutral")
    return embedder.encode(mood_str, normalize_embeddings=True).tolist()