# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/sovereign_codex_differ.py
# Tier ΩΩΩ-State FINALX — Codex Mutation Diff Engine with Reflex Utility Wrapper & Sovereign Vector Traceability
# ============================================================

from difflib import unified_diff, SequenceMatcher
from datetime import datetime
from sentence_transformers import SentenceTransformer

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE

embedder = SentenceTransformer("all-MiniLM-L6-v2")

class SovereignCodexDiffer:
    def __init__(self):
        self.last_diff = None

    def compare_codex_fragments(self, original_lines, mutated_lines, context: str = "unknown") -> dict:
        try:
            diff_output = list(unified_diff(
                original_lines,
                mutated_lines,
                lineterm='',
                fromfile='original',
                tofile='mutated'
            ))

            original_text = "\n".join(original_lines)
            mutated_text = "\n".join(mutated_lines)
            similarity = SequenceMatcher(None, original_text, mutated_text).ratio()
            divergence_score = round(1.0 - similarity, 5)
            timestamp = datetime.utcnow().isoformat()
            summary = f"[CODEX_DIFF] Δ={divergence_score} | Context={context}"
            vector = embedder.encode(summary, normalize_embeddings=True).tolist()

            metadata = {
                "summary": summary,
                "timestamp": timestamp,
                "context": context,
                "original": original_text,
                "mutated": mutated_text,
                "diff_output": diff_output,
                "lines_changed": len(diff_output),
                "divergence_score": divergence_score,
                "urgency": divergence_score,
                "entropy": round(1 - similarity, 4),
                "pressure_score": round(divergence_score * 1.25, 4),
                "emotion": TEXPULSE.get("emotion", "reflective"),
                "agent_id": TEXPULSE.get("agent_id", "TEX"),
                "meta_layer": "codex_diff_reflex",
                "tags": ["codex", "diff", "mutation", "reflex", context],
                "source": "sovereign_codex_differ"
            }

            sovereign_memory.store(
                text=summary,
                metadata=metadata,
                vector=vector
            )

            self.last_diff = metadata
            print(f"[CODEX DIFFER] 