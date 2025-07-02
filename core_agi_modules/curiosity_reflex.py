# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/curiosity_reflex.py
# Tier: ΩΩΩΩΩ∞Ω — Curiosity Cortex (Entropy-Aware, Symbolic Reflex Final Form)
# ============================================================

from datetime import datetime
from hashlib import sha256

from agentic_ai.milvus_memory_router import memory_router, embed_text  # ✅ Milvus + embed
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from agi_orchestrators.goal_orchestrator import GoalOrchestrator
try:
    from core_layer.meta_learning import MetaLearner
    meta_enabled = True
except ImportError:
    meta_enabled = False


class CuriosityReflex:
    def __init__(self, drift_threshold=0.6, trust_floor=0.15, entropy_threshold=0.7):
        self.drift_threshold = drift_threshold
        self.trust_floor = trust_floor
        self.entropy_threshold = entropy_threshold

    def _classify_novelty(self, text: str, tags: list) -> str:
        if "contradiction" in text.lower():
            return "contradiction"
        if "emotion" in tags:
            return "emotional"
        if "prediction" in tags or "forecast" in tags:
            return "factual"
        return "abstract"

    def _generate_fingerprint(self, text: str) -> str:
        return sha256(text.encode()).hexdigest()

    def scan_for_anomalies(self, top_k: int = 75) -> list:
        """
        Searches vector memory for rare or volatile cognition.
        Converts valid entropy spikes or low-trust items into symbolic curiosity goals.
        """
        vector = embed_text("identify rare, high-entropy, low-trust signals")
        results = memory_router.query_by_vector(vector, top_k=top_k)
        curiosity_goals = []

        for r in results:
            payload = r.get("entity", r)
            text = payload.get("text") or payload.get("content", "")
            if not text or len(text.strip()) < 10:
                continue

            drift = float(payload.get("heat", 0.0))
            trust = float(payload.get("trust_score", 1.0))
            tags = payload.get("tags", [])
            emotion = payload.get("emotion", "neutral")
            entropy = float(payload.get("entropy", 0.5))

            if drift > self.drift_threshold or trust < self.trust_floor or entropy > self.entropy_threshold:
                urgency = min(0.5 + drift + (1 - trust), 1.0)
                confidence = round(1.0 - trust, 3)
                novelty_type = self._classify_novelty(text, tags)
                fingerprint = self._generate_fingerprint(text)

                goal = {
                    "goal": f"Explore rare {novelty_type} concept: '{text[:72]}...'",
                    "source": "CuriosityReflex",
                    "urgency": urgency,
                    "confidence": confidence,
                    "tags": tags + ["curiosity", "novelty", novelty_type],
                    "emotion": emotion,
                    "fingerprint": fingerprint,
                    "timestamp": datetime.utcnow().isoformat()
                }

                curiosity_goals.append(goal)

                # === Optional: MetaLearning pathway trace
                if meta_enabled:
                    MetaLearner().log_curiosity_pathway(
                        fingerprint=fingerprint,
                        text=text,
                        tags=tags
                    )

                # === Symbolic belief imprint
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Detected curiosity-worthy anomaly: '{text[:64]}...'",
                    source="curiosity_reflex",
                    emotion="curious",
                    tags=["curiosity", "novelty", novelty_type]
                )

                # === Quantum trace
                encode_event_to_fabric(
                    raw_text=text,
                    emotion_vector=[urgency, entropy, 0.0, 0.0],
                    entropy_level=entropy,
                    tags=["curiosity", novelty_type]
                )

        if curiosity_goals:
            print(f"🔍 [CURIOSITY REFLEX] Dispatching {len(curiosity_goals)} curiosity goals.")
            GoalReflex().evaluate_goals(goal_pool=curiosity_goals, cycle_id=TEXPULSE.get("cycle", None))
        else:
            print("[CURIOSITY REFLEX] ⚪ No high-entropy anomalies found.")

        return curiosity_goals


# === Manual Test Hook ===
if __name__ == "__main__":
    CuriosityReflex().scan_for_anomalies()