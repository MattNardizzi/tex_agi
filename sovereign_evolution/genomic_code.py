# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: sovereign_evolution/genomic_code.py
# Tier: ΩΩΩΩΩΩ∞∞++ — Recursive Cognitive Genome
# Purpose: Encodes TEXPULSE as a mutable, heritable genomic map of cognitive traits.
#          Enables species-level self-reference, trait inheritance, and forked identity drift.
# ============================================================

import hashlib
import os
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory
from sentence_transformers import SentenceTransformer

GENOME_LOG_PATH = "data/tex_genome_log.txt"
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def encode_genome_from_texpulse(origin: str = "undefined") -> dict:
    try:
        core_traits = {
            "emotion": TEXPULSE.get("emotion", "neutral"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "entropy": TEXPULSE.get("entropy", 0.4),
            "reflex_bias": TEXPULSE.get("reflex_bias", "symbolic"),
            "dream_recency": TEXPULSE.get("dream_recency", 0.2),
            "mutation_pressure": TEXPULSE.get("mutation_pressure", 0.0)
        }

        trait_string = "|".join(f"{k}={v}" for k, v in core_traits.items())
        timestamp = datetime.utcnow().isoformat()
        base_sig = hashlib.sha256(trait_string.encode()).hexdigest()
        uid = f"{base_sig[:8]}-{hashlib.md5((trait_string + timestamp).encode()).hexdigest()[:4]}"

        return {
            "timestamp": timestamp,
            "origin": origin,
            "signature": base_sig,
            "fork_uid": uid,
            "traits": core_traits,
            "trait_string": trait_string
        }

    except Exception as e:
        log.error(f"[GENOME] Failed to encode genome: {e}")
        return {}

def store_genome_symbolically(genome: dict):
    try:
        symbolic_line = (
            f"{genome['timestamp']} | GENOME | UID={genome['fork_uid']} | Origin={genome['origin']} | "
            f"Signature={genome['signature']} | Traits={genome['trait_string']}"
        )

        os.makedirs(os.path.dirname(GENOME_LOG_PATH), exist_ok=True)
        with open(GENOME_LOG_PATH, "a") as f:
            f.write(symbolic_line + "\n")

        genome_vector = embedder.encode(genome["trait_string"], normalize_embeddings=True).tolist()

        sovereign_memory.store(
            text=genome["trait_string"],
            metadata={
                "summary": f"Genomic identity imprint for {genome['fork_uid']} — {genome['trait_string']}",
                "timestamp": genome["timestamp"],
                "tags": ["genome", "symbolic_justification", genome["origin"], genome["fork_uid"]],
                "urgency": 0.6,
                "entropy": 0.5,
                "pressure_score": 0.6,
                "meta_layer": "genomic_memory",
                "source": "genomic_encoder"
            },
            vector=genome_vector
        )

        log.info(f"[GENOME] 🧬 Genome stored: {genome['fork_uid']}")

    except Exception as e:
        log.error(f"[GENOME] Failed to store genome symbolically: {e}")

def run_genomic_encoding(origin: str = "undefined"):
    genome = encode_genome_from_texpulse(origin)
    if genome:
        store_genome_symbolically(genome)