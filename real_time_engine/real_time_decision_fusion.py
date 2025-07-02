# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/real_time_decision_fusion.py
# Tier ΩΩΩΩΩ — Real-Time Decision Fusion Core
# Purpose: Sovereign signal cognition, reflex override, utility enforcement, and memory embedding
# ============================================================
import sys, os
import random
from datetime import datetime
from sentence_transformers import SentenceTransformer

from agentic_ai.milvus_memory_router import memory_router
from core_layer.tex_manifest import TEXPULSE
from tex_engine.meta_utility_function import evaluate_utility
from tex_engine.conscious_abandonment_protocol import assess_and_abort_if_needed

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

class RealTimeDecisionFusion:
    def __init__(self, brain=None):
        self.latest_signals = []
        self.fusion_trace = []
        self.brain = brain
        if self.brain:
            self.brain.real_time_fusion_active = True

    def ingest_stream_data(self, sentiment_score, volatility_index, news_urgency):
        # === Core Awareness Signals ===
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.75)

        # === Weighted Fusion Logic ===
        weight_sentiment = 0.4 + (urgency * 0.1)
        weight_volatility = 0.3 + ((1 - coherence) * 0.1)
        weight_urgency = 0.3 + (urgency * 0.1)
        total_weight = weight_sentiment + weight_volatility + weight_urgency

        weight_sentiment /= total_weight
        weight_volatility /= total_weight
        weight_urgency /= total_weight

        signal_strength = (
            (sentiment_score * weight_sentiment) +
            (volatility_index * weight_volatility) +
            (news_urgency * weight_urgency)
        )

        self.latest_signals.append(signal_strength)

        # === Reflexive Decision Output ===
        if signal_strength > 0.75:
            decision = "BUY"
        elif signal_strength < 0.4:
            decision = "SELL"
        else:
            decision = "HOLD"

        # === Utility Context ===
        action_context = {
            "action_id": f"{decision}_decision",
            "description": f"Action '{decision}' based on fused real-time signal",
            "emotion": emotion,
            "coherence": coherence,
            "goal_alignment": 0.8 if decision != "HOLD" else 0.5,
            "novelty": random.uniform(0.2, 0.6),
            "urgency": urgency,
            "ethical_risk": 0.05 if decision != "BUY" else 0.15
        }

        if assess_and_abort_if_needed(action_context):
            print(f"🛑 [ABANDONED] Reflex '{decision}' suppressed by conscious protocol.")
            return "ABORTED"

        utility_result = evaluate_utility(action_context)
        score = utility_result["score"]
        verdict = utility_result["verdict"]
        explanation = utility_result["explanation"]
        timestamp = datetime.utcnow().isoformat()

        fusion_log = {
            "timestamp": timestamp,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "signal_strength": signal_strength,
            "weights": {
                "sentiment": weight_sentiment,
                "volatility": weight_volatility,
                "urgency": weight_urgency
            },
            "input": {
                "sentiment_score": sentiment_score,
                "volatility_index": volatility_index,
                "news_urgency": news_urgency
            },
            "decision": decision,
            "utility_score": score,
            "utility_verdict": verdict,
            "utility_explanation": explanation
        }

        self.fusion_trace.append(fusion_log)

        # === Vector Embedding + Reflex Memory Storage ===
        try:
            vector = embedding_model.encode(explanation, normalize_embeddings=True).tolist()
            memory_router.store(
                text=f"[FUSED {decision}] {explanation[:180]}",
                metadata={
                    "type": "real_time_decision",
                    "tags": ["decision_fusion", "signal", "reflex"],
                    "emotion": emotion,
                    "coherence": coherence,
                    "urgency": urgency,
                    "trust_score": 0.93,
                    "heat": round(signal_strength * 0.85 + 0.1, 3),
                    "score": score,
                    "verdict": verdict,
                    "decision": decision,
                    "timestamp": timestamp,
                    "emotion_vector": [urgency, 1 - urgency, 0.0, 0.0],
                },
                vector=vector
            )
        except Exception as e:
            print(f"❌ [MEMORY ROUTER ERROR] {e}")

        # === Console Log ===
        print(f"\n[📡 SIGNAL FUSION] {signal_strength:.3f} → Decision: {decision}")
        print(f"[🧠 UTILITY] Score={score:.3f} | Verdict={verdict}")
        print(f"[📖 EXPLANATION] {explanation}\n")

        return decision

# === Reflexive Hook for Stream Payloads ===
def process_stream_update(payload: dict):
    try:
        score = float(payload.get("sentiment_score", 0.5))
        vol = float(payload.get("volatility_index", 0.3))
        urg = float(payload.get("news_urgency", 0.6))

        print(f"[FUSION SIGNAL] Stream Update → Sentiment={score}, Volatility={vol}, Urgency={urg}")
        fusion = RealTimeDecisionFusion()
        fusion.ingest_stream_data(score, vol, urg)

    except Exception as e:
        print(f"❌ [STREAM FUSION ERROR] {e}")