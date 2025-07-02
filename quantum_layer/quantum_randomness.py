# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: quantum_layer/quantum_randomness.py
# Tier: ΩΩΩΩΩ∞ — Quantum Entropy Engine (Sovereign Reflex Link)
# Purpose: Emits reflex-modulating entropy signals for mutation, override, and swarm drift using loopless sovereign memory.
# ============================================================

import uuid
import random
import hashlib
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log


class QuantumEntropyEngine:
    def __init__(self):
        self.session_id = f"qrng-{uuid.uuid4().hex[:6]}"
        self.entropy_log = []

    def get_entropy_strength(self) -> float:
        """
        Emits a quantum-derived entropy value ∈ [0.0, 1.0].
        Powers reflex prioritization, override oscillation, and mutation forking.
        """
        entropy = round(random.uniform(0.0, 1.0), 8)
        timestamp = datetime.utcnow().isoformat()
        signature = self._generate_signature(entropy, timestamp)

        payload = {
            "summary": f"Quantum entropy pulse: {entropy}",
            "timestamp": timestamp,
            "emotion": "neutral",
            "tags": ["quantum", "entropy", "mutation_seed", "reflex_trigger"],
            "urgency": entropy,
            "entropy": entropy,
            "pressure_score": entropy,
            "meta_layer": "quantum_entropy_engine",
            "signature": signature
        }

        sovereign_memory.store(text=payload["summary"], metadata=payload)
        self.entropy_log.append({**payload, "entropy": entropy})

        log.info(f"[QRNG] ⚛️ Entropy pulse: {entropy} | Signature: {signature}")
        return entropy

    def get_noise_scalar(self, variance: float = 0.1) -> float:
        """
        Gaussian micro-noise for drift modulation and stochastic effects.
        Centered near 0, used for emotional or reflex variation.
        """
        return round(random.gauss(0.0, variance), 6)

    def _generate_signature(self, value: float, timestamp: str) -> str:
        seed = f"{value}-{timestamp}"
        return hashlib.sha256(seed.encode()).hexdigest()[:12]

    def summarize_session(self):
        total = len(self.entropy_log)
        log.info(f"[QRNG] Entropy session summary: {total} samples collected.")
        for entry in self.entropy_log[-5:]:
            value = entry.get("entropy", "?")
            source = entry.get("signature", "N/A")
            log.info(f"  • Sample: {value} from {source}")


# === Legacy-Compatible Entropy Sample Wrapper ===
def quantum_entropy_sample(bits: int = 128, source: str = "qrng_sim") -> str:
    """
    Generates a binary entropy string using secure randomness. Used for mutation seeds and override logic.
    """
    import secrets
    return ''.join(str(secrets.randbits(1)) for _ in range(bits))

def generate_quantum_label(prefix: str = "fork", entropy: float = None) -> str:
    """
    Generates a symbolic quantum-labeled string used for tagging forks, mutations, or reflex chains.
    Example output: "fork-ϟ82a9-rev13"
    """
    if entropy is None:
        entropy = QuantumEntropyEngine().get_entropy_strength()

    symbol = random.choice(["ϟ", "ψ", "℧", "⚛", "∇", "Ω", "λ"])
    digest = hashlib.sha1(f"{entropy}{datetime.utcnow()}".encode()).hexdigest()[:5]
    revision = random.randint(1, 99)

    return f"{prefix}-{symbol}{digest}-rev{revision}"