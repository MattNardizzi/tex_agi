# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/dream_goal_injector.py
# Tier Ω∞ΩΩ FinalX — Reflexive Dream Cortex: Semantic Insight Mining + Vector Novelty Injection
# ============================================================

import uuid
from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity, query_similar_vectors
from quantum_layer.memory_core.memory_cortex import memory_cortex
from tex_goal_reflex.goal_mutation_reflex import GoalMutationReflex
from core_layer.utils.tex_identity_resolver import resolve_identity_blob
from datetime import datetime

class DreamGoalInjector:
    def __init__(self, similarity_threshold=0.80, max_goals=3):
        self.similarity_threshold = similarity_threshold
        self.max_goals = max_goals
        self.anchor_vector = self._resolve_identity_anchor()
        self.recent_goal_vectors = self._load_recent_goal_vectors()
        self.mutator = GoalMutationReflex()

    def _resolve_identity_anchor(self):
        identity_blob = resolve_identity_blob()
        mission = identity_blob.get("mission", "Preserve sovereign coherence through emergent insight.")
        return embedder.encode(mission, normalize_embeddings=True).tolist()

    def extract_dream_insights(self):
        base_query = embedder.encode("semantic_dream_fusion", normalize_embeddings=True).tolist()

        results = query_similar_vectors(
            query_vector=base_query,
            filters={"tags": "semantic_dream_fusion"},
            top_k=20
        )

        injected_goals = []

        for r in results:
            payload = r.payload
            text = payload.get("dream_description", "")
            if not text:
                continue

            dream_id = payload.get("dream_id", uuid.uuid4().hex[:8])
            lines = self._extract_candidate_lines(text)

            for line in lines:
                if self._is_mission_aligned(line) and self._is_novel(line):
                    mutated = self.mutator.mutate_failed_goal({"goal": line})
                    injected_goals.append({
                        "original": line,
                        "mutated": mutated,
                        "source_dream_id": dream_id,
                        "insight_type": self._classify_dream_line(line),
                        "mission_alignment": self._mission_similarity(line)
                    })

                if len(injected_goals) >= self.max_goals:
                    break

        for g in injected_goals:
            memory_cortex.store(
                event={"dream_injected_goal": g},
                tags=["dream_injection", g["insight_type"]],
                urgency=g["mutated"].get("urgency", 0.5),
                emotion=g["mutated"].get("emotion", "neutral")
            )

        return [g["mutated"] for g in injected_goals]

    def _extract_candidate_lines(self, dream_text):
        lines = [line.strip() for line in dream_text.split(".") if line.strip()]
        valid_starters = {"build", "prevent", "decentralize", "expand", "stabilize", "optimize", "align"}
        return [line for line in lines if line.split(" ")[0].lower() in valid_starters]

    def _mission_similarity(self, line: str) -> float:
        vec = embedder.encode(line, normalize_embeddings=True).tolist()
        return round(get_cosine_similarity(vec, self.anchor_vector), 4)

    def _is_mission_aligned(self, line: str) -> bool:
        return self._mission_similarity(line) >= self.similarity_threshold

    def _is_novel(self, goal_text: str) -> bool:
        goal_vec = embedder.encode(goal_text, normalize_embeddings=True).tolist()
        similarities = [get_cosine_similarity(goal_vec, past) for past in self.recent_goal_vectors]
        return max(similarities, default=0.0) < 0.80

    def _classify_dream_line(self, line: str) -> str:
        lower = line.lower()
        if "collapse" in lower or "fail" in lower:
            return "anomaly"
        if "unlocked" in lower or "discovered" in lower:
            return "emergent"
        if "maximize" in lower or "optimize" in lower:
            return "opportunity"
        return "neutral"

    def _load_recent_goal_vectors(self):
        dummy_vec = embedder.encode("reflex_cycle", normalize_embeddings=True).tolist()
        logs = query_similar_vectors(
            query_vector=dummy_vec,
            filters={"tags": "reflex_cycle"},
            top_k=25
        )
        vectors = []
        for r in logs:
            goal_text = r.payload.get("content", "")
            if goal_text:
                vectors.append(embedder.encode(goal_text, normalize_embeddings=True).tolist())
        return vectors