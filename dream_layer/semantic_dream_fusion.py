# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: dream_layer/semantic_dream_fusion.py
# Tier Ω∞+++ — Reflexive Dream Fusion Core (Final Form)
# Purpose: Fuse simulated dream fragments using vector similarity, emotion coherence, and LLM summarization
# ============================================================

from typing import List, Dict
from datetime import datetime
from agentic_ai.qdrant_vector_ops import embed_text, query_similar, embed_and_store
from tex_voiceos.llm_interface import LLMInterface
from utils.logging_utils import log

class SemanticDreamFusion:
    def __init__(self):
        self.llm = LLMInterface(identity_signal="TexFusion")
        self.last_summary = None

    def fuse_dreams(self, dream_texts: List[str] = None, tag_filter: str = "dream") -> List[str]:
        """
        Fuses dream fragments into a coherent semantic summary using embedding + LLM compression.
        Returns 1–2 final fusion outputs.
        """
        print("🌌 [DREAM FUSION] Initializing fusion cycle...")

        # Pull from memory if no direct inputs provided
        if dream_texts is None:
            results = query_similar(
                text="fuse dreams",
                top_k=12,
                tag_filter=tag_filter,
                emotion_filter="visionary"
            )
            dream_texts = [r.payload.get("content") for r in results if r.payload.get("content")]

        if not dream_texts or len(dream_texts) < 2:
            print("⚠️ [FUSION] Not enough dreams to fuse.")
            return []

        # Step 1: Basic heuristic fusion
        compressed = self._semantic_squeeze(dream_texts)

        # Step 2: LLM-enhanced summarization
        llm_summary = self._compress_with_llm(compressed)

        # Step 3: Store fused result in Qdrant vector memory
        metadata = {
            "tags": ["dream", "fusion", "semantic_summary"],
            "emotion": "visionary",
            "trust_score": 0.75,
            "heat": 0.6,
            "timestamp": datetime.utcnow().isoformat(),
            "parent_ids": [hash(text) for text in dream_texts[:5]]
        }

        embed_and_store(llm_summary, metadata)
        self.last_summary = llm_summary
        print("✅ [FUSION] Semantic fusion complete.")
        return [llm_summary]

    def _semantic_squeeze(self, texts: List[str]) -> str:
        """
        Fast heuristic reducer to deduplicate and retain semantic signal.
        """
        sentences = [s.strip() for t in texts for s in t.split(".") if len(s.strip()) > 12]
        unique = sorted(set(sentences), key=len)
        return ". ".join(unique[:8]) + "."

    def _compress_with_llm(self, raw_text: str) -> str:
        """
        Uses Tex's LLM interface to compress a block of reflexive dream input into semantic essence.
        """
        prompt = (
            "You are the Dream Compression Engine of a reflexive AGI. "
            "Fuse the following dream fragments into a coherent high-level insight. "
            "Keep it symbolic, emotionally rich, and strategically useful:\n\n"
            f"{raw_text}\n\nSummary:"
        )
        try:
            return self.llm.simple_completion(prompt, temperature=0.4, max_tokens=300)
        except Exception as e:
            log.warning(f"[FUSION ERROR] LLM compression failed: {e}")
            return raw_text