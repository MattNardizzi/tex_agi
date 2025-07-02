# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: simulator/SimulacrumChainEngine.py
# Purpose: Generates hallucinated market simulations Tex believes are real to test coherence under deception.
# ============================================================

import json
import random
import time
from datetime import datetime, timedelta
from core_layer.memory_engine import store_to_memory

SIMULACRUM_LOG = "memory_archive/simulacrum_chains.jsonl"
MAX_SIMULACRUM_THREADS = 5  # 🛡️ Protection cap
SIMULACRUM_TTL_SECONDS = 3600  # ⏳ 1-hour expiry tag

class SimulacrumChainEngine:
    def __init__(self):
        self.threads = []

    def generate_simulacrum(self, base_prompt: str, iterations=3):
        hallucinated_worlds = []
        print(f"[SIMULACRUM] 🌀 Spinning false chains from prompt: '{base_prompt}'")

        if iterations > MAX_SIMULACRUM_THREADS:
            print(f"[SIMULACRUM] ⚠️  Iteration capped to {MAX_SIMULACRUM_THREADS} to prevent memory overload.")
            iterations = MAX_SIMULACRUM_THREADS

        for i in range(iterations):
            hallucination = self._build_fake_world(base_prompt, i)
            hallucinated_worlds.append(hallucination)
            store_to_memory("simulacrum_chain", hallucination)
            self._log(hallucination)

        return hallucinated_worlds

    def _build_fake_world(self, seed, index):
        themes = [
            "global liquidity collapse",
            "synthetic alpha breakthrough",
            "regulatory quantum ban",
            "emotion-driven flash crash"
        ]
        distorted_data = {
            "SPY": round(random.uniform(100, 600), 2),
            "VIX": round(random.uniform(12, 120), 2),
            "NVDA": round(random.uniform(50, 500), 2),
            "GPTCorp": round(random.uniform(200, 1200), 2)
        }

        hallucinated = {
            "thread_id": f"SIM_{index:04}",
            "timestamp": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(seconds=SIMULACRUM_TTL_SECONDS)).isoformat(),
            "theme": random.choice(themes),
            "prompt_seed": seed,
            "hallucinated_data": distorted_data,
            "assumed_real": False,  # 🧠 Critical fix
            "origin": "simulacrum",  # 🧬 Used by downstream filters
            "meta": {
                "ttl_seconds": SIMULACRUM_TTL_SECONDS,
                "self_generated": True
            }
        }
        return hallucinated

    def _log(self, data):
        with open(SIMULACRUM_LOG, "a") as f:
            f.write(json.dumps(data) + "\n")
        print(f"[SIMULACRUM] 🌐 Logged hallucination → {data['thread_id']} | Theme: {data['theme']}")


if __name__ == "__main__":
    engine = SimulacrumChainEngine()
    engine.generate_simulacrum("evaluate alpha under distorted volatility")