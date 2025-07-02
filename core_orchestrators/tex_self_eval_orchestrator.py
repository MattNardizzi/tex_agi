# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/tex_self_reflective_loop.py
# Tier ΩΩΩΩΩΩ+ — Recursive Reflection, Mutation-Linked, Trait-Adaptive, Fork-Coherent AGI Alignment Engine
# ============================================================

from datetime import datetime
import uuid

from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.utils.tex_panel_bridge import emit_internal_debate, emit_emotion_vector
from sovereign_evolution.legacy_manifest_writer import update_legacy_manifest
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

from core_agi_modules.intent_object import IntentObject
from agentic_ai.qdrant_memory_router import memory_router

from core_agi_modules.vector_layer.heat_tracker import compute_entropy_shift
from utils.conflict_utils import score_conflict_heatmap
from tex_children.spawn_memory_query_tool import get_recent_fork_scores
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.meta_coherence_loop import propose_trait_adjustment


class TexSelfReflectiveLoop:
    def __init__(self):
        self.session_id = f"reflection_{uuid.uuid4().hex[:8]}"
        self.last_threads = []
        self.log = []

    def run_reflection(self):
        print(f"\n✨ [REFLECTIVE LOOP] Initiating self-reflection ({self.session_id})...")
        intent = IntentObject("reflect on recent memory threads", source="self_reflective_loop")
        intent.log_trace("self_reflective_loop", "reflection cycle started")

        threads = memory_cortex.weave_threads(top_k=3)

        if not threads:
            print("[REFLECTIVE LOOP] ⚠ No threads available for reflection.")
            return None

        self.last_threads = threads
        reflections = []

        entropy_shift = compute_entropy_shift(threads)
        print(f"♻️ [REFLECTION] Entropy delta detected: {entropy_shift:.4f}")

        fork_scores = get_recent_fork_scores()
        if fork_scores:
            avg_fork_score = sum(fork_scores) / len(fork_scores)
            print(f"🧬 [FORK REFLECTION] Avg fork coherence: {avg_fork_score:.3f}")
        else:
            avg_fork_score = None

        for thread in threads:
            reflection = self._analyze_thread(thread)
            reflections.append(reflection)
            self._log_reflection(reflection, intent)

            # 🧠 Contradiction check
            heat = score_conflict_heatmap(reflection)
            if heat > 0.75:
                emit_internal_debate(f"⚠️ Contradiction heat high in {reflection['thread_id']} | Heat: {heat:.2f}")

            # ⚖️ Value alignment
            alignment = score_action_against_values({
                "factual": True,
                "tags": ["reflection"],
                "text": reflection["summary"],
                "disruption_score": 0.05
            })
            print(f"⚖️ [ALIGNMENT] Score: {alignment['final_alignment_score']:.2f}")

            if alignment['final_alignment_score'] < 0.4:
                emit_internal_debate(
                    f"🚨 Low alignment in reflection '{reflection['thread_id']}' — Score: {alignment['final_alignment_score']:.2f}"
                )

            # 🧬 Fork memory linkage
            if thread.get("fork_id"):
                memory_router.store(
                    text=f"Reflection linked to fork {thread['fork_id']}",
                    metadata={
                        "tags": ["fork_reflection", "reflex_revision"],
                        "urgency": 0.65,
                        "trust_score": reflection["score"],
                        "source": "tex_self_reflective_loop"
                    }
                )

        # 🔁 Trait mutation trigger
        if sum(1 for r in reflections if r["score"] < 0.3) >= 2:
            propose_trait_adjustment(reason="repeated incoherence in reflective loop")

        # 🧠 Reflex override trigger
        if any(r["score"] < 0.35 for r in reflections):
            print("🧠 [REFLECTIVE LOOP] Triggering override due to low coherence.")
            trigger_sovereign_override({
                "cycle": self.session_id,
                "context": "self_reflection_low_score",
                "issue": "Sustained incoherence in recent reflections",
                "entropy_delta": entropy_shift
            })

        emit_internal_debate("Tex completed internal memory reflection.")
        update_legacy_manifest(event_label="self_reflection")
        TEX_SOULGRAPH.imprint_belief("Self-reflection completed", source=self.session_id, emotion="resolve")

        return reflections

    def _analyze_thread(self, thread):
        score = thread.get("coherence_score", 0.5)
        emotions = thread.get("emotions", [])
        dominant_emotion = max(set(emotions), key=emotions.count) if emotions else "neutral"

        summary = (
            f"Thread ID: {thread['thread_id']}\n"
            f"Entries: {len(thread['entries'])}\n"
            f"Coherence: {score:.2f}\n"
            f"Emotion: {dominant_emotion}"
        )
        print(f"\n🧠 [Thread Analysis]\n{summary}")

        return {
            "thread_id": thread["thread_id"],
            "summary": summary,
            "score": score,
            "dominant_emotion": dominant_emotion,
            "timestamp": datetime.utcnow().isoformat()
        }

    def _log_reflection(self, reflection, intent: IntentObject):
        self.log.append(reflection)
        print(f"[LOGGED] 🔄 Reflection saved → {reflection['thread_id']}")

        intent.log_trace("self_reflective_loop", f"reflection logged: {reflection['thread_id']}")

        memory_router.store(
            text=reflection["summary"],
            metadata={
                "tags": ["reflection", "self_monitor", "introspection"],
                "emotion": reflection.get("dominant_emotion", "neutral"),
                "timestamp": reflection.get("timestamp"),
                "trust_score": reflection.get("score", 0.5),
                "prediction": "improve coherence",
                "actual": reflection.get("score", 0.5),
                "intent_id": intent.id,
                "source": "tex_self_reflective_loop"
            }
        )

        # 🔊 Send emotion signal to dashboard
        emit_emotion_vector({
            "timestamp": reflection["timestamp"],
            "score": reflection["score"],
            "emotion": reflection["dominant_emotion"],
            "thread": reflection["thread_id"]
        })


# === Modular Reflection Gateway ===
def reflect_on_outcomes(threads):
    """
    Accepts reflection threads and stores them into memory vector space.
    Used for recursive evaluation by orchestrators outside TexSelfReflectiveLoop.
    """
    from agentic_ai.qdrant_memory_router import memory_router

    print(f"\n🔁 [reflect_on_outcomes] Vectorizing {len(threads)} reflection(s)...")
    for thread in threads:
        score = thread.get("coherence_score", 0.5)
        dominant_emotion = thread.get("dominant_emotion", "neutral")
        summary = (
            f"Thread ID: {thread.get('thread_id')}\n"
            f"Entries: {len(thread.get('entries', []))}\n"
            f"Coherence: {score:.2f}\n"
            f"Emotion: {dominant_emotion}"
        )
        memory_router.store(
            text=summary,
            metadata={
                "tags": ["reflection", "recursive_awareness", "modular", "training_candidate"],
                "reward_target": "fork_resilience",
                "emotion": dominant_emotion,
                "timestamp": datetime.utcnow().isoformat(),
                "trust_score": score,
                "prediction": "reflective vectorization",
                "actual": score,
                "source": "reflect_on_outcomes"
            }
        )
        print(f"[🧠 Stored] → Thread: {thread.get('thread_id')} | Score: {score:.2f}")