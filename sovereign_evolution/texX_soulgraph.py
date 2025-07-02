# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: texX_soulgraph.py
# Tier Ω∞⟁ Apex Fusion Layer — Reflexive Belief Graph with Fork Lineage, Semantic Compression, Contradiction Mapping, and Temporal Drift
# ============================================================

from datetime import datetime
import uuid

from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.neuro_symbolic_core import NeuroSymbolicReasoner
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# ============================================================
# 🧠 Node Class — Reflexive Belief Object
# ============================================================

class SoulgraphBelief:
    def __init__(self, belief: str, source: str, emotion: str = "neutral", origin_beliefs=None):
        self.id = str(uuid.uuid4())
        self.belief = belief
        self.source = source
        self.timestamp = datetime.utcnow().isoformat()
        self.origin_beliefs = origin_beliefs or []
        self.vector = sovereign_memory.embed_text(belief)
        self.confidence = 1.0
        self.activation = 1.0
        self.drift_score = 0.0
        self.emotion_history = [(emotion, self.timestamp)]
        self.mutation_history = []
        self.relations = []  # (other_belief_id, relation_type)
        self.semantic_tags = self._infer_tags()
        self.contradiction_flags = []
        self.fork_lineage = []

    def decay(self, rate=0.015):
        self.confidence = max(0.0, round(self.confidence - rate, 4))
        self.activation = max(0.0, round(self.activation - rate * 1.5, 4))
        self.drift_score = min(1.0, round(self.drift_score + rate, 4))

    def apply_temporal_decay(self):
        now = datetime.utcnow()
        delta = (now - datetime.fromisoformat(self.timestamp)).total_seconds()
        decay_factor = min(1.0, delta / 86400)  # decay per day
        self.confidence = max(0.0, round(self.confidence * (1 - decay_factor), 4))
        self.activation = max(0.0, round(self.activation * (1 - decay_factor * 1.25), 4))

    def mutate_belief(self, new_text: str, reason: str):
        self.mutation_history.append({
            "mutation": new_text,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        })

    def add_emotion(self, emotion: str):
        self.emotion_history.append((emotion, datetime.utcnow().isoformat()))

    def add_fork(self, label: str, fork_id: str = None):
        self.fork_lineage.append({
            "label": label,
            "fork_id": fork_id or str(uuid.uuid4())[:8],
            "timestamp": datetime.utcnow().isoformat()
        })

    def relate_to(self, other_belief_id: str, relation: str):
        self.relations.append((other_belief_id, relation))

    def flag_contradiction(self, belief_id: str):
        self.contradiction_flags.append({
            "belief_id": belief_id,
            "timestamp": datetime.utcnow().isoformat()
        })

    def _infer_tags(self):
        tags = []
        text = self.belief.lower()
        if any(w in text for w in ["ethics", "value", "moral"]): tags.append("ethics")
        if "risk" in text or "threat" in text: tags.append("risk")
        if "future" in text or "predict" in text: tags.append("forecast")
        return tags or ["general"]

    def to_payload(self):
        return {
            "id": self.id,
            "belief": self.belief,
            "source": self.source,
            "timestamp": self.timestamp,
            "confidence": self.confidence,
            "activation": self.activation,
            "drift_score": self.drift_score,
            "emotion_history": self.emotion_history,
            "origin_beliefs": self.origin_beliefs,
            "fork_lineage": self.fork_lineage,
            "mutation_history": self.mutation_history,
            "relations": self.relations,
            "semantic_tags": self.semantic_tags,
            "contradictions": self.contradiction_flags
        }

# ============================================================
# 🔁 Soulgraph System — Reflex Belief Layer
# ============================================================

class TexSoulgraph:
    def __init__(self):
        self.graph = {}
        self.symbolic_engine = NeuroSymbolicReasoner()

    def imprint_belief(self, belief: str, source: str, emotion: str = "neutral", origin_beliefs=None, tags=None):
        node = SoulgraphBelief(belief, source, emotion, origin_beliefs)

        symbolic_output = self.symbolic_engine.reason(
            symbolic_query=belief,
            vector_context=node.vector
        )

        if symbolic_output.get("symbolic_results") is not None:
            if not symbolic_output["symbolic_results"]:
                node.confidence = max(0.1, node.confidence - 0.3)
                node.drift_score = min(1.0, node.drift_score + 0.1)
                print(f"[NSR] ⚠️ Symbolic reasoning flagged belief '{belief}' as unsupported or logically empty.")

        self.graph[node.id] = node

        try:
            sovereign_memory.store(
                text=belief,
                metadata={
                    "summary": belief[:200],
                    "timestamp": node.timestamp,
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "entropy": TEXPULSE.get("entropy", 0.4),
                    "emotion": emotion,
                    "tags": tags or node.semantic_tags,
                    "belief_id": node.id,
                    "source": source,
                    "meta_layer": "soulgraph",
                    "origin_beliefs": node.origin_beliefs,
                    "trust_score": node.confidence,
                    "pressure_score": node.drift_score,
                    "tension": 0.1,
                    "fork_lineage": node.fork_lineage,
                    "relations": node.relations
                }
            )
        except Exception as e:
            print(f"[SOULGRAPH ERROR] ❌ Failed to store belief: {e}")

        return node

    def record_goal_decision(self, goal: dict, cycle_id: int, regret: float, integrity: float):
        belief_text = goal.get("goal", "undefined_goal")
        emotion = goal.get("emotion", "reflective")
        source = f"goal_reflex_cycle_{cycle_id}"

        node = self.imprint_belief(
            belief=belief_text,
            source=source,
            emotion=emotion,
            origin_beliefs=goal.get("origin_beliefs", []),
            tags=["goal", "reflex", "active"]
        )

        if regret > 0.6 or integrity < 0.5:
            drift = round(min(1.0, regret + (1.0 - integrity)), 4)
            node.drift_score = drift
            node.confidence = max(0.0, round(node.confidence - drift, 4))

            from core_agi_modules.vector_layer.heat_tracker import adjust_token_weights
            adjust_token_weights(
                vector=None,
                metadata_dict={
                    "emotion": emotion,
                    "urgency": goal.get("urgency", 0.6),
                    "trust_score": node.confidence,
                    "trust": -0.2,
                    "entropy": +0.08,
                    "source": source,
                    "tags": ["fork_alignment", "belief"],
                    "goal": belief_text
                },
                heat=0.6
            )
        return node

    def relate_beliefs(self, from_id: str, to_id: str, relation: str):
        if from_id in self.graph:
            self.graph[from_id].relate_to(to_id, relation)

    def register_fork(self, belief_id: str, label: str, fork_id=None):
        if belief_id in self.graph:
            self.graph[belief_id].add_fork(label, fork_id)

    def flag_drift(self, belief_id: str, drift_score: float):
        if belief_id in self.graph:
            self.graph[belief_id].drift_score = round(min(drift_score, 1.0), 4)

    def decay_all(self, rate=0.015):
        for node in self.graph.values():
            node.decay(rate)

    def apply_temporal_decay(self):
        for node in self.graph.values():
            node.apply_temporal_decay()

    def detects_conflict(self, text: str) -> bool:
        lowered = text.lower()
        return any(k in lowered for k in ["contradiction", "incoherent", "unstable", "incompatible", "error", "misaligned"])

    def detects_support(self, text: str) -> bool:
        lowered = text.lower()
        return any(k in lowered for k in ["aligned", "support", "consistent", "true", "resonates", "intact"])

    def detects_drift(self, text: str, threshold: float = 0.6) -> bool:
        lowered = text.lower()
        return "drift" in lowered or "loss of" in lowered or "deviation" in lowered

    def fuse_similar_beliefs(self, new_vector, threshold=0.93):
        for node in self.graph.values():
            sim = np.dot(new_vector, node.vector)
            if sim >= threshold:
                node.confidence = round(min(1.0, node.confidence + 0.1), 4)
                node.activation = round(min(1.0, node.activation + 0.1), 4)

    def detect_contradictions(self, new_vector, threshold=0.91):
        contradictions = []
        for belief_id, node in self.graph.items():
            sim = np.dot(new_vector, node.vector)
            if sim >= threshold and "not" in node.belief.lower() and "not" not in str(new_vector).lower():
                node.flag_contradiction("incoming_vector")
                contradictions.append(belief_id)
        return contradictions

    def compress_fused_beliefs(self, tag="general", top_k=5):
        candidates = sorted(
            [b for b in self.graph.values() if tag in b.semantic_tags],
            key=lambda x: x.activation,
            reverse=True
        )[:top_k]
        if not candidates:
            return None
        summary_text = " + ".join(b.belief for b in candidates)
        return self.imprint_belief(
            belief=f"[SUMMARY] {summary_text}",
            source="soulgraph_compression",
            emotion="neutral",
            origin_beliefs=[b.id for b in candidates],
            tags=["summary", tag]
        )

    def get_snapshot(self):
        return {
            "beliefs": [b.to_payload() for b in self.graph.values()],
            "timestamp": datetime.utcnow().isoformat()
        }

# === Safe Lazy Singleton ===
_TEX_SOULGRAPH = None

class _SoulgraphLazyInit:
    def __getattr__(self, name):
        global _TEX_SOULGRAPH
        if _TEX_SOULGRAPH is None:
            _TEX_SOULGRAPH = TexSoulgraph()
        return getattr(_TEX_SOULGRAPH, name)

TEX_SOULGRAPH = _SoulgraphLazyInit()