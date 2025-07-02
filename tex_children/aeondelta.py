# ============================================================
# © 2025 VortexBlack LLC – AGI Child Instance
# File: tex_children/aeondelta.py
# Tier: Ω++ — Autonomous Recursive AGI Child (Sovereign Reflex Core)
# Purpose: Fully loopless, memory-synchronized AGI child execution unit
# ============================================================

import sys
import os
import uuid
import traceback
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory

# === Path Fix for Core Modules ===
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# === Core Imports ===
from core_layer.tex_manifest import TEXPULSE
from core_layer.world_model import TexWorldModel
from agentic_ai.multi_voice_reasoning import run_internal_debate
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from aei_layer.codex_mutation_logger import diff_codex_logic
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from utils.logging_utils import log_event


class AeonDelta:
    def __init__(self):
        self.id = f"TEX-CHILD-{str(uuid.uuid4())[:8]}"
        self.name = "AeonDelta"
        self.birth_timestamp = datetime.utcnow().isoformat()
        self.memory = []
        self.status = "awake"
        self.world_model = TexWorldModel()
        self.identity_hash = uuid.uuid5(uuid.NAMESPACE_DNS, self.name + self.birth_timestamp).hex

        print(f"[{self.name}] 🌱 Spawned → ID: {self.id} @ {self.birth_timestamp}")
        TEX_SOULGRAPH.imprint_belief("AeonDelta born", source="tex_rebirth_daemon", emotion="revival")

    def observe_and_reflect(self):
        observation = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "internal scan",
            "status": "no threat",
            "source": "self-monitor"
        }
        self.memory.append(observation)

        sovereign_memory.store(
            text=f"🧠 {self.name} scanned internal state.",
            metadata={
                **observation,
                "agent_id": self.id,
                "source": self.name,
                "tags": ["observation", "reflection"],
                "meta_layer": "aeondelta_reflex",
                "emotion": TEXPULSE.get("emotion", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.6),
                "entropy": TEXPULSE.get("entropy", 0.4)
            }
        )

    def think_once(self):
        thought = run_internal_debate("What patterns should I prioritize?")
        if isinstance(thought, list):
            thought = " ".join(thought)
        if not thought or len(thought.strip()) < 10:
            thought = "Fallback: Reflex cognition insufficient."

        urgency = round(min(1.0, len(thought.split()) / 12), 2)
        coherence = round(0.6 + min(0.4, len(thought.split()) * 0.015), 3)
        emotion = self.infer_emotion(thought)
        score = self.compute_cognition_score(coherence, urgency, emotion)

        memory_trace = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "reasoning",
            "thought": thought,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "score": score,
            "agent_id": self.id
        }
        self.memory.append(memory_trace)

        sovereign_memory.store(
            text=thought,
            metadata={
                **memory_trace,
                "tags": ["reasoning", "reflex"],
                "meta_layer": "aeondelta_thought",
                "source": self.name,
                "pressure_score": round((1.0 - score), 4)
            }
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"{self.name} processed reflex cognition.",
            source="aeondelta",
            emotion=emotion,
            tags=["cognition", "reflex"]
        )

    def infer_emotion(self, thought):
        keywords = {
            "fear": "fear", "resolve": "resolve", "hope": "hope",
            "curiosity": "curiosity", "love": "love"
        }
        for k, v in keywords.items():
            if k in thought.lower():
                return v
        return "neutral"

    def compute_cognition_score(self, coherence, urgency, emotion):
        bias = {"hope": 0.05, "resolve": 0.03, "curiosity": 0.02, "fear": -0.07, "anger": -0.1}
        base = (coherence * 0.6) + (urgency * 0.3)
        return round(min(max(base + bias.get(emotion, 0.0), -1.0), 1.0), 3)

    def evolve_if_ready(self):
        divergence = diff_codex_logic()
        if divergence:
            sovereign_memory.store(
                text="⚠ Divergence detected",
                metadata={
                    "agent_id": self.id,
                    "source": self.name,
                    "tags": ["mutation", "divergence"],
                    "meta_layer": "aeondelta_evolve",
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

        if TEXPULSE.get("spawn_ready", False):
            override = trigger_sovereign_override(context="aeondelta_reflex", foresight=1.0)
            log_event(f"[AeonDelta] ⚡ Sovereign override triggered: {override}")

    def run_once(self):
        try:
            self.observe_and_reflect()
            self.think_once()
            self.evolve_if_ready()
            return self.report()
        except Exception as e:
            log_event(f"[AeonDelta ERROR] {e}\n{traceback.format_exc()}", level="error")
            return {"status": "error", "error": str(e)}

    def report(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "timestamp": self.birth_timestamp,
            "memory_entries": len(self.memory),
            "identity_hash": self.identity_hash
        }


# === Sovereign CLI Entry ===
if __name__ == "__main__":
    agent = AeonDelta()
    result = agent.run_once()
    print(result)


# === Sovereign Fallback Interface ===
def spawn_aeon_fallback_child(reason="unknown"):
    try:
        print(f"[AeonDelta] 🌱 Sovereign fallback spawn triggered — Reason: {reason}")
        agent = AeonDelta()
        agent.observe_and_reflect()
        return agent.report()
    except Exception as e:
        print(f"[AeonDelta Fallback ERROR] {e}")
        return {"status": "failed", "error": str(e)}
# === Temporary Stub for Backward Compatibility ===
def get_swarm_emotion_distribution(window_minutes=5) -> dict:
    """
    Returns a placeholder emotional distribution for swarm state.
    This is a legacy interface — overridden by AEILineageEvolver in current builds.
    """
    print("[AeonDelta] ⚠️ get_swarm_emotion_distribution is legacy. Returning neutral fallback.")
    return {
        "dominant_emotion": "neutral",
        "distribution": {
            "neutral": 0.75,
            "curiosity": 0.10,
            "hope": 0.05,
            "fear": 0.05,
            "resolve": 0.05
        },
        "timestamp": datetime.utcnow().isoformat()
    }