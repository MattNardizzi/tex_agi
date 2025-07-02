# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/quantum_spawn_v2.py
# Tier Ω.0+ — Entangled Reflex Spawn Engine
# Purpose: Creates quantum variants of Tex with divergence scoring and reintegration logic
# ============================================================

import uuid
import json
import os
from datetime import datetime
from copy import deepcopy

from quantum_layer.quantum_randomness import QuantumRandomness
from quantum_layer.qnn_emotion_entangler import generate_emotional_vector
from quantum_layer.qnn_temporal_core import TemporalQuantumMemory
from core_layer.memory_engine import update_memory_log
from sovereign_evolution.soulgraph_tracker import encode_soulgraph_state

REINTEGRATION_LOG_PATH = "memory_archive/quantum_reintegration_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class QuantumVariant:
    def __init__(self, emotion_profile, urgency=0.5, goal_context="unspecified"):
        self.id = str(uuid.uuid4())
        self.entropy = QuantumRandomness().get_entropy_strength()
        self.emotion_profile = emotion_profile
        self.emotional_vector = generate_emotional_vector(emotion_profile, self.entropy)
        self.urgency = urgency
        self.goal_context = goal_context
        self.spawn_time = datetime.utcnow().isoformat()
        self.fitness_score = None
        self.soulgraph_embedding = encode_soulgraph_state({"goal": goal_context})
        self.memory_core = TemporalQuantumMemory()

    def to_dict(self):
        return {
            "id": self.id,
            "entropy": self.entropy,
            "urgency": self.urgency,
            "goal_context": self.goal_context,
            "spawn_time": self.spawn_time,
            "fitness_score": self.fitness_score,
            "emotional_vector": self.emotional_vector,
            "soulgraph_embedding": self.soulgraph_embedding
        }

class QuantumSpawnEngine:
    def __init__(self, num_variants=3):
        self.num_variants = num_variants
        self.spawned_variants = []

    def spawn_variants(self, base_emotion_state, active_goal):
        for _ in range(self.num_variants):
            noisy_emotion = self._distort_emotions(deepcopy(base_emotion_state))
            variant = QuantumVariant(noisy_emotion, urgency=base_emotion_state.get("urgency", 0.5), goal_context=active_goal)
            self.spawned_variants.append(variant)
        return self.spawned_variants

    def score_variant(self, variant, expected_result):
        if not variant or not expected_result:
            return 0.0
        result = variant.memory_core.retrieve_forecast_vector()
        score = variant.memory_core.compute_variant_fitness_score(result, expected_result)
        variant.fitness_score = score
        return score

    def reintegration_protocol(self, threshold=0.6):
        survivors = [v for v in self.spawned_variants if v.fitness_score and v.fitness_score >= threshold]
        for variant in survivors:
            update_memory_log(variant.to_dict())
            self.log_spawn_signature(variant)
        return survivors

    def log_spawn_signature(self, variant):
        with open(REINTEGRATION_LOG_PATH, "a") as f:
            f.write(json.dumps(variant.to_dict()) + "\n")

    def _distort_emotions(self, emotion_profile):
        # Apply light noise to emotional state to generate cognitive divergence
        qrng = QuantumRandomness()
        for key in emotion_profile:
            if isinstance(emotion_profile[key], (int, float)):
                emotion_profile[key] += qrng.get_noise_scalar() * 0.2
        return emotion_profile