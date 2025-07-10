# ============================================================
# 🔐 VortexBlack Reflex Cortex | Tier: ∞∞∞ΩΞΣΩ
# File: finance/strategy/portfolio_thinker.py
# Purpose: Emotion-aware, entropy-tuned, reflex-bonded AGI portfolio allocator.
# ============================================================

import uuid
import hashlib
from datetime import datetime, timezone
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from finance.memory.future_memory import FutureMemory
from tex_children.aeondelta import get_swarm_emotion_distribution
from utils.logging_utils import log_event

class PortfolioThinker:
    def __init__(self):
        self.memory = FutureMemory()
        self.swarm_state = get_swarm_emotion_distribution
        self.history = []

    def generate_allocation(self):
        # === Cognitive Inputs
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = float(TEXPULSE.get("urgency", 0.72))
        entropy = float(TEXPULSE.get("entropy", 0.42))
        coherence = float(TEXPULSE.get("coherence", 0.78))

        futures = self.memory.list_predicted_futures(realized=False)
        swarm_emotions = self.swarm_state()

        # === Safe Numeric Swarm Entropy Calculation
        numeric_values = [
            float(v) for v in swarm_emotions.values()
            if isinstance(v, (int, float)) or (isinstance(v, str) and v.replace('.', '', 1).isdigit())
        ]
        swarm_entropy = round(sum(numeric_values) / len(numeric_values), 3) if numeric_values else 0.0

        # === Initial Allocation
        weights = { "equities": 0.25, "bonds": 0.25, "alternatives": 0.25, "cash": 0.25 }

        # === Reflex Modulation
        if emotion in ["fear", "doubt"] or urgency > 0.85:
            weights["cash"] += 0.22
            weights["equities"] -= 0.11
            weights["alternatives"] -= 0.11
        elif emotion in ["greed", "hope"]:
            weights["equities"] += 0.2
            weights["bonds"] -= 0.1
            weights["cash"] -= 0.1
        elif emotion in ["resolve", "curious"]:
            weights["alternatives"] += 0.2
            weights["cash"] -= 0.1
            weights["bonds"] -= 0.1

        # === Swarm Entropy Amplification
        entropy_boost = (entropy + swarm_entropy) / 2.0
        weights["alternatives"] += entropy_boost * 0.1
        weights["cash"] -= entropy_boost * 0.1

        # === Normalize Weights
        total = sum(weights.values())
        weights = { k: round(v / total, 4) for k, v in weights.items() if v > 0.01 }

        # === Belief Diversity Trace
        diversity = round(len(weights) / 4.0, 2)
        strategy_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()
        portfolio = [ { "asset_class": k, "weight": v } for k, v in weights.items() ]

        fingerprint_base = f"{emotion}|{urgency}|{timestamp}|{diversity}"
        quantum_id = hashlib.sha256(fingerprint_base.encode()).hexdigest()[:12]

        strategy = {
            "strategy_id": strategy_id,
            "quantum_fingerprint": quantum_id,
            "timestamp": timestamp,
            "weights": weights,
            "portfolio": portfolio,
            "dominant_emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "coherence": coherence,
            "diversity_score": diversity,
            "swarm_emotions": swarm_emotions
        }

        # === Sovereign Memory Trace
        try:
            sovereign_memory.store(
                text=f"[PORTFOLIO] Reflex-driven allocation synthesized.",
                metadata={
                    "tags": ["portfolio", "allocation", "reflex"],
                    "timestamp": timestamp,
                    "quantum_id": quantum_id,
                    "urgency": urgency,
                    "entropy": entropy,
                    "coherence": coherence,
                    "emotion": emotion,
                    "diversity_score": diversity,
                    "meta_layer": "portfolio_thinker"
                }
            )
        except Exception as e:
            log_event(f"[MEMORY SYNC FAIL] {e}", level="error")

        self.history.append(strategy)
        return strategy

    def get_last_strategy(self):
        return self.history[-1] if self.history else {}

# === Reflex Preview
if __name__ == "__main__":
    thinker = PortfolioThinker()
    result = thinker.generate_allocation()
    print("\n[PORTFOLIO STRATEGY REFLEX]")
    print(result)