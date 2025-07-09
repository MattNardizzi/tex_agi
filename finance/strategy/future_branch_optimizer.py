# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: future_layer/future_branch_optimizer.py
# Tier 5: Tex AGI — Strategic Future Path Optimizer with Cognitive Fusion
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event

class FutureBranchOptimizer:
    def __init__(self):
        self.min_confidence_threshold = 0.55
        self.max_candidates = 5
        self.aggression_bias = TEXPULSE.get("urgency", 0.72)
        self.coherence_bias = TEXPULSE.get("coherence", 0.87)
        self.live_emotion = TEXPULSE.get("emotional_state", "curious")

    def optimize_future_branches(self, branches):
        """Filters malformed branches and ranks future paths for AGI-level strategic fusion."""
        scored = []

        for i, b in enumerate(branches):
            if not isinstance(b, dict):
                log_event(f"⚠️ [OPTIMIZER] Skipping malformed future branch at index {i}: {type(b)}", level="warning")
                continue

            try:
                raw_conf = float(b.get("confidence", 0.5))
                urgency = float(b.get("urgency", 0.7))
                coherence = float(b.get("coherence", 0.7))
                emotion = b.get("emotion", "neutral")
                mutated = bool(b.get("mutation_triggered", False))

                # === Step 1: Base Score
                score = raw_conf

                # === Step 2: Reward Mutation Resilience
                if mutated:
                    score *= 1.12

                # === Step 3: Emotion Valence Adjustment
                if emotion in ["resolve", "hope"]:
                    score *= 1.05
                elif emotion in ["fear", "anger", "doubt"]:
                    score *= 0.92

                # === Step 4: TEXPULSE Weighted Overlay
                score *= (0.5 + 0.5 * self.coherence_bias)
                score -= 0.15 * urgency
                score += 0.1 * coherence

                # === Step 5: Normalize and Quantize
                score = round(min(max(score, 0), 1), 3)

                entropy_vector = f"E:{emotion[:2].upper()}|U:{int(urgency*100)}|C:{int(coherence*100)}"

                scored.append({
                    "future_id": b.get("future_id", str(uuid.uuid4())),
                    "future_title": b.get("future_title", "Untitled Future"),
                    "confidence": score,
                    "mutation": mutated,
                    "entropy_vector": entropy_vector,
                    "timestamp": b.get("generated_at", datetime.utcnow().isoformat()),
                    "notes": b.get("notes", "No context.")
                })

            except Exception as e:
                log_event(f"❌ [OPTIMIZER] Error scoring future branch: {e}", level="error")

        # === Step 6: Filter Weak Futures
        filtered = [f for f in scored if f["confidence"] >= self.min_confidence_threshold]

        # === Step 7: Return Top Futures
        return sorted(filtered, key=lambda x: x["confidence"], reverse=True)[:self.max_candidates]

# === Test Harness ===
if __name__ == "__main__":
    optimizer = FutureBranchOptimizer()
    dummy_futures = [
        {"future_title": "Fed Pivot + Market Rally", "confidence": 0.65, "emotion": "hope", "urgency": 0.55, "coherence": 0.83, "mutation_triggered": False},
        {"future_title": "Energy Crisis Spiral", "confidence": 0.72, "emotion": "fear", "urgency": 0.91, "coherence": 0.66, "mutation_triggered": True},
        {"future_title": "AI Sector Takeover", "confidence": 0.78, "emotion": "resolve", "urgency": 0.69, "coherence": 0.88, "mutation_triggered": True},
        ["this should be skipped"],  # Invalid entry
        None  # Also skipped
    ]
    optimized = optimizer.optimize_future_branches(dummy_futures)
    for f in optimized:
        print("✅ [OPTIMIZED FUTURE]", f)