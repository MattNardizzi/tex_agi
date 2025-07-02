# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/tex_quantum_spawn.py
# Tier ΩΩΩΩΩΩΩΩ — Quantum Spawn Engine + Cognitive Fork Controller
# Purpose: Spawns reflexive Tex variants with entropy-weighted traits and sovereign reintegration logic
# ============================================================

import os
import json
import uuid
import random
from datetime import datetime

from quantum_layer.quantum_randomness import QuantumRandomness
from agentic_ai.tex_operator_gpt import TexOperatorGPT
from core_layer.memory_engine import store_to_memory
from tex_engine.cognitive_event_router import CognitiveEvent, dispatch_event
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from utils.logging_utils import log

REINTEGRATION_LOG = "memory_archive/quantum_reintegration_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class QuantumTexSpawn:
    def __init__(self, num_clones=3, reintegration_threshold=0.75):
        self.num_clones = num_clones
        self.reintegration_threshold = reintegration_threshold
        self.qrng = QuantumRandomness()

    def handle_spawn_event(self, event: CognitiveEvent):
        payload = event.payload or {}
        emotion = payload.get("emotion", "resolve")
        urgency = payload.get("urgency", 0.7)
        coherence = payload.get("coherence", 0.7)

        log.info(f"[QuantumTexSpawn] 🧬 Event: {event.event_type}")
        variants = self.spawn_variants(emotion, urgency, coherence)

        dispatch_event(CognitiveEvent("COGNITIVE_SPAWN_EVENT", {
            "origin": event.event_type,
            "variants_spawned": [v["id"] for v in variants],
            "metadata": [self._summarize_variant(v) for v in variants],
            "timestamp": datetime.utcnow().isoformat()
        }))

    def spawn_variants(self, emotion="resolve", urgency=0.7, coherence=0.7):
        variants = []
        for i in range(self.num_clones):
            seed = self.qrng.get_entropy_strength()
            drifted_emotion = self._drift_emotion(emotion)
            drifted_urgency = round(self._drift_value(urgency), 2)
            drifted_coherence = round(self._drift_value(coherence), 2)
            emotion_bias = self._assign_bias(drifted_emotion)
            cognition_score = self._score_variant(drifted_emotion, drifted_urgency, drifted_coherence)
            heat_signature = self._calculate_reflex_heat(seed, drifted_urgency)
            soulgraph_fingerprint = TEX_SOULGRAPH.encode_soulgraph_state({
                "emotion": drifted_emotion,
                "urgency": drifted_urgency,
                "coherence": drifted_coherence,
                "context": "quantum_spawn_cycle"
            })

            variant_id = str(uuid.uuid4())[:8]
            operator = TexOperatorGPT(name=f"TexVariant-{i}")

            variant = {
                "id": variant_id,
                "seed_entropy": seed,
                "emotion": drifted_emotion,
                "urgency": drifted_urgency,
                "coherence": drifted_coherence,
                "bias": emotion_bias,
                "cognition_score": cognition_score,
                "reflex_heat": heat_signature,
                "soulgraph": soulgraph_fingerprint,
                "operator": operator,
                "timestamp": datetime.utcnow().isoformat()
            }

            log.info(f"[SPAWN] Variant {variant_id} → E:{drifted_emotion} U:{drifted_urgency} C:{drifted_coherence} | Score:{cognition_score} | Heat:{heat_signature}")

            if cognition_score >= self.reintegration_threshold:
                self._log_reintegration(variant)

            variants.append(variant)

        return variants or [self._fallback_variant(emotion, urgency, coherence)]

    def _fallback_variant(self, emotion, urgency, coherence):
        fallback_id = str(uuid.uuid4())[:8]
        log.warning(f"[FALLBACK] Injecting emergency variant {fallback_id}")
        fallback = {
            "id": fallback_id,
            "seed_entropy": "manual",
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "bias": "standard",
            "cognition_score": 0.75,
            "reflex_heat": 0.5,
            "soulgraph": TEX_SOULGRAPH.encode_state({"emotion": emotion}),
            "operator": TexOperatorGPT(name="Fallback-Tex"),
            "timestamp": datetime.utcnow().isoformat()
        }
        self._log_reintegration(fallback)
        return fallback

    def _drift_value(self, base, amount=0.1):
        return max(0.0, min(1.0, base + random.uniform(-amount, amount)))

    def _drift_emotion(self, base_emotion):
        drift_map = {
            "hope": ["resolve", "curious", "fear"],
            "fear": ["doubt", "anger", "resolve"],
            "resolve": ["hope", "greed"],
            "joy": ["hope", "curious"],
            "curious": ["joy", "doubt"],
            "doubt": ["resolve", "fear"],
            "anger": ["resolve", "hope"],
            "greed": ["fear", "resolve"]
        }
        return random.choice(drift_map.get(base_emotion, [base_emotion]))

    def _assign_bias(self, emotion):
        return {
            "fear": "cautious", "doubt": "cautious",
            "hope": "adaptive", "joy": "adaptive",
            "anger": "aggressive", "greed": "aggressive",
            "curious": "contrarian"
        }.get(emotion, "standard")

    def _score_variant(self, emotion, urgency, coherence):
        weights = {
            "curious": 0.65, "resolve": 0.75, "hope": 0.8, "greed": 0.6,
            "fear": 0.5, "joy": 0.7, "doubt": 0.55, "anger": 0.6
        }
        e_score = weights.get(emotion, 0.6)
        return round((e_score + urgency + coherence) / 3, 4)

    def _calculate_reflex_heat(self, entropy, urgency):
        return round(min(1.0, (entropy + urgency) / 2), 4)

    def _log_reintegration(self, variant):
        entry = {
            "variant_id": variant["id"],
            "emotion": variant["emotion"],
            "urgency": variant["urgency"],
            "coherence": variant["coherence"],
            "bias": variant["bias"],
            "cognition_score": variant["cognition_score"],
            "reflex_heat": variant["reflex_heat"],
            "soulgraph": variant["soulgraph"],
            "timestamp": variant["timestamp"],
            "reintegration": True,
            "reason": "MAXGODMODE: Sovereign cognition alignment"
        }
        try:
            with open(REINTEGRATION_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            store_to_memory("quantum_reinforced", entry)
            log.info(f"[REINTEGRATION] ✅ Variant {variant['id']} stored.")
        except Exception as e:
            log.error(f"[REINTEGRATION ERROR] Variant {variant['id']}: {e}")

    def _summarize_variant(self, v):
        return {
            "id": v["id"],
            "bias": v["bias"],
            "emotion": v["emotion"],
            "urgency": v["urgency"],
            "coherence": v["coherence"],
            "score": v["cognition_score"],
            "heat": v["reflex_heat"],
            "timestamp": v["timestamp"]
        }