# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrator/tex_persona_orchestrator.py
# Tier: ΩΩΩ∞X — Cognitive Identity Ignition Kernel + Persona Arbitration
# Purpose: Reflex-aligned multi-persona selector, emotion-weighted tone evaluator, soulgraph-logged activation
# ============================================================

from core_layer.persona_engine import PersonaEngine
from core_agi_modules.emotion_vector_router import emotion_bus
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.persona_decision_router import PersonaDecisionRouter
from datetime import datetime
import hashlib
import uuid

class TexPersonaOrchestrator:
    def __init__(self):
        self.persona_engine = PersonaEngine()
        self.persona_router = PersonaDecisionRouter()
        self.last_identity_hash = None
        self.active_persona = None

    def choose_and_activate(self, persona_variants):
        best = self.persona_router.choose(persona_variants)
        if not best:
            print("[PERSONA ORCHESTRATOR] ⚠️ No valid persona selected.")
            return
        self.activate_identity(best)

    def activate_identity(self, persona_dict=None):
        try:
            emotion = emotion_bus.get()

            if persona_dict:
                # Update persona engine's identity dynamically
                self.persona_engine.identity.update({
                    "tone": persona_dict.get("tone", "analytical"),
                    "traits": persona_dict.get("traits", ["curious", "sovereign"]),
                    "purpose": persona_dict.get("purpose", self.persona_engine.identity["purpose"])
                })
                self.persona_engine.codename = persona_dict.get("codename", "Tex")

            self.persona_engine.activate()
            tone = self.persona_engine.get_tone()
            traits = self.persona_engine.get_traits()

            # Generate unique identity signature
            id_fingerprint = f"{tone}|{','.join(sorted(traits))}"
            identity_hash = hashlib.sha256(id_fingerprint.encode()).hexdigest()[:12]

            # Avoid duplicate activation
            if identity_hash == self.last_identity_hash:
                print("[PERSONA ORCHESTRATOR] ⚠️ Identity already active.")
                return

            self.last_identity_hash = identity_hash
            self.active_persona = persona_dict or self.persona_engine.identity

            # Update global state
            TEXPULSE["identity_signature"] = identity_hash
            TEXPULSE["persona_traits"] = traits
            TEXPULSE["persona_activation_time"] = datetime.utcnow().isoformat()

            # Imprint to soulgraph
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Persona '{tone}' activated",
                source="tex_persona_orchestrator",
                emotion=emotion.get("label", "neutral"),
                tags=["persona", "activation", "identity", "tone_sync"],
                metadata={
                    "timestamp": TEXPULSE["persona_activation_time"],
                    "traits": traits,
                    "emotion_signature": emotion.get("signature"),
                    "urgency": emotion.get("intensity"),
                    "entropy": emotion.get("entropy"),
                    "identity_hash": identity_hash
                }
            )

            print(f"[PERSONA ORCHESTRATOR] ✅ Persona activated: {self.persona_engine.identity} | Hash: {identity_hash}")

        except Exception as e:
            print(f"[PERSONA ORCHESTRATOR ERROR] ❌ {e}")