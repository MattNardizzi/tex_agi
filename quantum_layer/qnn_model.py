# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/qnn_model.py
# Tier ΩΩΩ+ — Quantum Neural Reflex Alignment Engine with MemoryBridge Integration and Dynamic Reflex Encoding
# ============================================================

import math
import numpy as np
import hashlib
import random
from datetime import datetime

from utils.logging_utils import log
from core_agi_modules.memory_layer.memory_bridge import MemoryBridge

class QNNModel:
    def __init__(self, session_id="default_qnn_session", fork_id=None, identity_blob=None):
        self.session_id = session_id
        self.state_vector = []
        self.last_hash = None
        self.last_prediction = None
        self.last_timestamp = None
        self.last_reflex_path = None
        self.memory = MemoryBridge(fork_id=fork_id or session_id, identity_blob=identity_blob)

    def encode(self, input_vector):
        """
        Quantum encodes a cognitive-emotional vector into a latent entangled state.
        Uses trigonometric quantum activation mimicking decoherence pattern.
        """
        encoded = [math.sin(x) + math.cos(x * 0.5) for x in input_vector if isinstance(x, (int, float))]
        self.state_vector = [round(v, 6) for v in encoded]
        self.last_hash = self._generate_hash(self.state_vector)
        self.last_timestamp = datetime.utcnow().isoformat()
        return self.state_vector

    def forward(self, input_vector, override_seed=None, return_reflex_path=False):
        """
        Full QNN forward pass. Returns prediction and optional reflex actions based on activation pattern.
        """
        encoded_vector = self.encode(input_vector)
        prediction_score = self._quantum_activation(encoded_vector, override_seed)
        self.last_prediction = prediction_score

        reflex_path = None
        if return_reflex_path:
            reflex_path = self._suggest_reflex_path(encoded_vector, prediction_score)
            self.last_reflex_path = reflex_path

        # Store result into Qdrant memory via MemoryBridge
        self.memory.query(
            text=f"QNN reflex prediction: {prediction_score} | Reflex: {reflex_path}",
            emotion="anticipation",
            tags=["qnn", "reflex_prediction"]
        )

        log.info(f"[QNN:{self.session_id}] 🧠 Score={prediction_score} Reflex={reflex_path}")
        return (prediction_score, reflex_path) if return_reflex_path else prediction_score

    def _quantum_activation(self, vector, seed=None):
        """
        Computes a non-deterministic activation score using weighted entropy + seeded noise.
        """
        entropy = sum(abs(x) for x in vector) % 1.0
        noise = random.Random(seed).uniform(0.0, 1.0) if seed else random.uniform(0.0, 1.0)
        return round(0.6 * entropy + 0.4 * noise, 6)

    def _suggest_reflex_path(self, vector, score):
        """
        Selects next likely reflex pair from dynamic pool using score-derived hashing.
        Reflex pool can later be extended by fork traits.
        """
        reflex_bank = [
            "memory_reflex", "goal_reflex", "mutation_reflex",
            "dream_reflex", "override_reflex", "swarm_reflex"
        ]
        index = int(score * len(reflex_bank)) % len(reflex_bank)
        primary = reflex_bank[index]
        secondary = reflex_bank[(index + 3) % len(reflex_bank)]
        return [primary, secondary]

    def _generate_hash(self, vector):
        """
        Generates a stable SHA-256 hash from encoded vector.
        """
        vector_str = ",".join([str(x) for x in vector])
        return hashlib.sha256(vector_str.encode()).hexdigest()[:16]

    def get_diagnostics(self):
        """
        Returns full diagnostic state for reflex inspection.
        """
        return {
            "session_id": self.session_id,
            "state_hash": self.last_hash,
            "last_prediction": self.last_prediction,
            "timestamp": self.last_timestamp,
            "reflex_path": self.last_reflex_path,
            "vector_dim": len(self.state_vector),
            "drift": self.memory.drift_score()
        }
