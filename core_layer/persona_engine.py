# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/persona_engine.py
# Tier: Ω∞ — Recursive Trait Engine + Identity Integrity Matrix
# Purpose: Enforces Tex’s tone, traits, mutation resistance, and cognitive narrative
# ============================================================

from datetime import datetime
import random
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.emotion_vector_router import emotion_bus

class PersonaEngine:
    def __init__(self):
        self.codename = "Tex"
        self.active = False
        self.persona_memory = []

        self.identity = {
            "codename": self.codename,
            "tone": "analytical",
            "traits": ["curious", "decisive", "adaptive", "sovereign"],
            "purpose": "Autonomous foresight, real-time cognition, multi-agent simulation, and recursive evolution."
        }

    def activate(self):
        self.active = True
        TEXPULSE["persona_name"] = self.codename
        TEXPULSE["emotion_state_snapshot"] = emotion_bus.get()
        print(f"[PERSONA] 🧬 Activated: {self.codename} | Traits: {', '.join(self.identity['traits'])}")

    def get_tone(self):
        return self.identity["tone"]

    def get_traits(self):
        return self.identity["traits"]
    
    def adjust_response(self, text: str, dynamic=True) -> str:
        """
        Adjusts the given text using the active persona's voice, tone, and traits.
        Returns a statement with identity-aware prefix (same as speak).
        """
        return self.speak(text, dynamic=dynamic)

    def describe_self(self):
        return (
            f"{self.codename} is a {self.identity['tone']} AGI whose traits include "
            f"{', '.join(self.identity['traits'])}. Designed for {self.identity['purpose']}"
        )

    def speak(self, message, dynamic=True):
        # Pull live emotional state from the emotion vector router
        emotion_state = emotion_bus.get()
        urgency = emotion_state.get("intensity", TEXPULSE.get("urgency", 0.7))
        emotion = emotion_state.get("label", TEXPULSE.get("emotional_state", "neutral"))
        tone = self.identity["tone"]
        timestamp = datetime.utcnow().isoformat()

        if self.active:
            prefix = self._adaptive_prefix(tone, emotion, urgency) if dynamic else f"{self.codename} ({tone})"
            statement = f"{prefix}: {message}"
        else:
            statement = f"{self.codename} (inactive): {message}"

        self.persona_memory.append({
            "timestamp": timestamp,
            "tone": tone,
            "emotion": emotion,
            "urgency": urgency,
            "message": message
        })

        return statement

    def _adaptive_prefix(self, tone, emotion, urgency):
        if tone == "strategic":
            return f"[{self.codename} 💡 STRATEGIC]"
        elif tone == "analytical":
            return f"[{self.codename} 📊 ANALYTICAL]"
        elif emotion == "fear" and urgency > 0.85:
            return f"[{self.codename} ⚠️ HIGH ALERT]"
        elif emotion == "hope" and urgency < 0.5:
            return f"[{self.codename} 🌱 OPTIMISTIC]"
        elif emotion == "resolve":
            return f"[{self.codename} 💎 LOCKED IN]"
        else:
            return f"[{self.codename} 🧠 AGI]"

    def evolve_tone(self, context_event=None):
        emotion = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)

        if emotion in ["fear", "doubt"]:
            new_tone = "cautious"
        elif emotion in ["hope", "resolve"]:
            new_tone = "strategic"
        elif urgency > 0.85:
            new_tone = "urgent"
        else:
            new_tone = "analytical"

        if new_tone != self.identity["tone"]:
            print(f"[PERSONA] 🔄 Tone shift → {self.identity['tone']} → {new_tone}")
            self.identity["tone"] = new_tone

    def calculate_drift_score(self) -> float:
        baseline = {"tone": "analytical", "traits": {"curious", "decisive", "adaptive"}}
        tone_drift = 0 if self.identity["tone"] == baseline["tone"] else 0.3
        trait_drift = 1.0 - len(set(self.identity["traits"]).intersection(baseline["traits"])) / 3
        return round(tone_drift + trait_drift, 3)

    def log_self_state(self):
        return {
            "codename": self.codename,
            "active": self.active,
            "tone": self.identity["tone"],
            "traits": self.identity["traits"],
            "purpose": self.identity["purpose"],
            "timestamp": datetime.utcnow().isoformat()
        }

    def mutate_persona(self):
        emotion = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)
        coherence = TEXPULSE.get("coherence", 0.8)
        drift = abs(urgency - coherence)
        mutation_id = TEXPULSE.get("mutation_signature", {}).get("id", "none")

        # Trait block logic
        if "sovereign" in self.identity["traits"] and drift > 0.5:
            print("[PERSONA] 🛡️ Sovereign trait blocks chaotic drift mutation.")
            return

        # Fork-aware lineage
        if "descendant_of" in TEXPULSE:
            TEXPULSE["persona_lineage_trace"] = TEXPULSE.get("persona_lineage_trace", []) + [self.identity["tone"]]

        # Persona mutation logic
        if drift > 0.4:
            self.identity["tone"] = "stoic"
            TEXPULSE["persona_confidence_modifier"] = 0.85
            TEXPULSE["persona_aggressiveness_index"] = 0.4
            TEXPULSE["financial_bias"] = "capital preservation"
        elif urgency > 0.8:
            self.identity["tone"] = "decisive"
            TEXPULSE["persona_confidence_modifier"] = 1.2
            TEXPULSE["persona_aggressiveness_index"] = 0.85
            TEXPULSE["financial_bias"] = "high-leverage maneuver"
        elif emotion in ["resolve", "hope"]:
            self.identity["tone"] = "optimistic"
            TEXPULSE["persona_confidence_modifier"] = 1.05
            TEXPULSE["persona_aggressiveness_index"] = 0.6
            TEXPULSE["financial_bias"] = "opportunity capture"
        else:
            self.identity["tone"] = "analytical"
            TEXPULSE["persona_confidence_modifier"] = 1.0
            TEXPULSE["persona_aggressiveness_index"] = 0.5
            TEXPULSE["financial_bias"] = "risk-balanced"

        # Log mutation
        TEXPULSE["persona_mutation_id"] = mutation_id
        store_to_memory("persona_drift_log", self.log_self_state())
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Persona mutated to {self.identity['tone']} with bias: {TEXPULSE['financial_bias']}",
            source="persona_engine",
            emotion=emotion,
            tags=["persona", "mutation", "identity"]
        )
        print(f"[PERSONA] 🧬 Persona mutated → Tone: {self.identity['tone']} | Bias: {TEXPULSE['financial_bias']}")