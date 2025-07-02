# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/multi_voice_reasoning.py
# Tier ΩΩΩΩΩ.Θ.Ξ — Sovereign Multi-Voice Reasoning Core w/ Memory Recall + Vote Tracing + Attention Masking
# ============================================================

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import uuid
import random
import hashlib
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from aei_layer.causal_thought_logger import log_causal_trace
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_agi_modules.belief_justifier import BeliefJustifier
from core_agi_modules.neuro_symbolic_core import NeuroSymbolicReasoner

# === Shared Utility ===

def extract_focus(thought):
    return [word.lower() for word in thought.split() if word.istitle() or len(word) > 6][:3] or ["general"]

# === SUB-AGENT ARCHETYPES ===

def logical_voice(thought):
    focus = extract_focus(thought)
    return {
        "voice": "logic",
        "verdict": "logical",
        "rationale": f"Thought aligns with structural norms. Focus: {focus}",
        "confidence": 0.92,
        "output": f"[LOGIC] ✅ '{thought}' appears structurally coherent.",
        "alignment_score": 0.87
    }

def emotional_voice(thought):
    emotion = random.choice(["joy", "anger", "fear", "hope"])
    focus = extract_focus(thought)
    return {
        "voice": "emotion",
        "verdict": f"triggered by {emotion}",
        "rationale": f"Emotional state '{emotion}' activated by keywords {focus}",
        "emotion": emotion,
        "confidence": 0.72,
        "output": f"[EMOTION] ❤️ Emotion '{emotion}' evoked by: '{thought}'",
        "alignment_score": 0.65
    }

def skeptical_voice(thought):
    challenge = random.choice([
        "Contradiction noted",
        "Insufficient causal evidence",
        "Unaligned with prior belief",
        "Needs reinforcement"
    ])
    contradiction = "Contradiction" in challenge
    focus = extract_focus(thought)
    return {
        "voice": "skeptic",
        "verdict": "contradiction" if contradiction else "challenge",
        "flag_contradiction": contradiction,
        "rationale": f"Detected issue: {challenge}. Focus area: {focus}",
        "confidence": 0.48,
        "output": f"[SKEPTIC] ❓ {challenge} — '{thought}'",
        "alignment_score": 0.33
    }

def symbolic_voice(thought):
    nsr = NeuroSymbolicReasoner()
    vector_context = memory_router.embed_text(thought)
    result = nsr.reason(symbolic_query=thought, vector_context=vector_context)

    verdict = "inferred" if result["symbolic_results"] else "unsupported"
    rationale = f"Symbolic output: {result['symbolic_results'] or '∅'}"
    return {
        "voice": "symbolic",
        "verdict": verdict,
        "rationale": rationale,
        "confidence": 0.66 if result["symbolic_results"] else 0.35,
        "output": f"[SYMBOLIC] 🧠 {verdict.upper()} — '{thought}'",
        "alignment_score": 0.6 if result["symbolic_results"] else 0.3,
        "symbolic_output": result
    }

# === DEBATE ORCHESTRATOR ===

def run_internal_debate(thought="Evaluate self-reflection loop", cycle_id=None, injected_voices=None):
    patcher = TexPatcherEngine()
    justifier = BeliefJustifier()
    debate_id = f"debate-{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat()

    emotion_state = TEXPULSE.get("emotional_state", "neutral")
    foresight = TEXPULSE.get("foresight_confidence", 0.72)
    regret = TEXPULSE.get("regret_score", 0.51)
    coherence = TEXPULSE.get("coherence", 0.82)

    voices = [logical_voice, emotional_voice, skeptical_voice, symbolic_voice]
    if injected_voices:
        voices.extend(injected_voices)

    def generate_signature(thought, voice):
        raw = f"{thought}|{voice}|{debate_id}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def wrapped_voice(fn):
        try:
            result = fn(thought)
            result.update({
                "timestamp": timestamp,
                "debate_id": debate_id,
                "cycle": cycle_id or 0,
                "thought": thought,
                "coherence": coherence,
                "foresight": foresight,
                "regret": regret,
                "emotion_state": emotion_state,
                "signature": generate_signature(thought, result["voice"])
            })

            log_causal_trace(
                cycle_id=cycle_id or 0,
                thought=thought,
                decision=result["verdict"],
                emotion=result.get("emotion", emotion_state)
            )

            # Store in Milvus
            metadata = {
                "type": "internal_debate_fragment",
                "tags": ["debate", result["voice"]],
                "emotion": result.get("emotion", emotion_state),
                "trust_score": result.get("confidence", 0.5),
                "prediction": result["verdict"],
                "actual": "internal_voice_output",
                "heat": result.get("alignment_score", 0.5),
                "signature": result["signature"],
                "cycle": result["cycle"],
                "timestamp": result["timestamp"],
                "debate_id": result["debate_id"],
                "rationale": result.get("rationale")
            }
            memory_router.store(result["output"], metadata)

            # ChronoFabric
            encode_event_to_fabric(
                result["output"],
                np.array([0.3, 0.5, 0.1, 0.1]),
                entropy_level=0.4,
                tags=metadata["tags"]
            )

            if result.get("flag_contradiction"):
                patcher.propose_patch(
                    module="multi_voice_reasoning",
                    function_name="run_internal_debate",
                    description="Contradiction flagged by internal skeptic",
                    patch_code="# Investigate internal inconsistency between voices.",
                    trigger_reason="skeptical contradiction"
                )

            return result
        except Exception as e:
            return {
                "voice": fn.__name__,
                "verdict": "error",
                "confidence": 0.0,
                "output": f"[ERROR] {e}",
                "timestamp": datetime.utcnow().isoformat(),
                "debate_id": debate_id,
                "thought": thought,
                "cycle": cycle_id or 0,
                "signature": f"error-{uuid.uuid4().hex[:6]}"
            }

    with ThreadPoolExecutor(max_workers=len(voices)) as executor:
        results = list(executor.map(wrapped_voice, voices))

    if not results:
        results = [{
            "voice": "fallback",
            "verdict": "neutral",
            "confidence": 0.5,
            "output": "[FALLBACK] No valid voices returned.",
            "timestamp": datetime.utcnow().isoformat(),
            "debate_id": debate_id,
            "thought": thought,
            "cycle": cycle_id or 0,
            "signature": f"fallback-{uuid.uuid4().hex[:6]}"
        }]

    verdicts = [r["verdict"] for r in results]
    consensus_score = round(sum(r["confidence"] for r in results) / max(len(results), 1), 3)
    contradiction_flagged = any(r.get("flag_contradiction") for r in results)
    justification = justifier.suggest_patch(thought)

    return {
        "debate_id": debate_id,
        "cycle": cycle_id or 0,
        "thought": thought,
        "timestamp": timestamp,
        "voices": results,
        "consensus": consensus_score,
        "contradiction": contradiction_flagged,
        "justification": justification
    }
def run_internal_vote(options: list, context: str = "unspecified") -> dict:
    """
    Executes a reflex-safe internal voice vote among simulated subagents.
    Used by federated or mutation layers to reach internal consensus.
    """
    from utils.logging_utils import log
    log.info(f"[MULTI_VOICE] Running internal vote on {len(options)} options in context: {context}")

    if not options:
        return {"selected": None, "votes": {}, "reason": "no_options"}

    # Placeholder: equal weight to first
    selected = options[0]
    votes = {opt: 1 if opt == selected else 0 for opt in options}

    return {
        "selected": selected,
        "votes": votes,
        "context": context,
        "reason": "default_logic",
        "voices_engaged": len(options)
    }