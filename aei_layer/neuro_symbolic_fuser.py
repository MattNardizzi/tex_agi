# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/neuro_symbolic_fuser.py
# Purpose: AGI Neural-Symbolic Fusion Engine for Unified Reasoning
# Status: 🔒 GODMIND CORE — NEURO-SYMBOLIC BRIDGE v1.0
# ============================================================

import json
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
from core_layer.memory_engine import recall_values, store_to_memory
from tex_backend.tex_core_event_bus import emit_event
from symbolic_world_model import apply_symbolic_rules

model = SentenceTransformer("all-MiniLM-L6-v2")

FUSION_LOG = "memory_archive/neuro_symbolic_fusion.jsonl"
EMBED_SOURCE = "reasoning_trace"
SYMBOLIC_SOURCE = "world_model"
FUSION_THRESHOLD = 0.78


def fuse_reasoning():
    print("[NEURO-FUSER] ⚛️ Beginning fusion of neural embeddings with symbolic logic...")
    neural_data = recall_values(EMBED_SOURCE, limit=200)
    symbolic_context = recall_values(SYMBOLIC_SOURCE, limit=100)

    if not neural_data or not symbolic_context:
        print("[NEURO-FUSER] ⚠️ Missing input data for fusion.")
        return

    neural_texts = [entry.get("text", "") for entry in neural_data]
    symbolic_texts = [s.get("symbolic_statement", "") for s in symbolic_context]

    neural_embeds = model.encode(neural_texts, convert_to_tensor=True)
    symbolic_embeds = model.encode(symbolic_texts, convert_to_tensor=True)

    similarity_scores = util.pytorch_cos_sim(neural_embeds, symbolic_embeds).cpu().numpy()

    fused_outputs = []
    for i, n_entry in enumerate(neural_data):
        for j, s_entry in enumerate(symbolic_context):
            sim_score = similarity_scores[i][j]
            if sim_score > FUSION_THRESHOLD:
                result = apply_symbolic_rules(n_entry.get("text"), s_entry.get("symbolic_statement"))
                fusion_record = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "neural": n_entry.get("text"),
                    "symbolic": s_entry.get("symbolic_statement"),
                    "similarity": round(float(sim_score), 4),
                    "fused_logic": result,
                    "fusion_type": "neuro-symbolic"
                }
                fused_outputs.append(fusion_record)
                store_to_memory("neuro_symbolic_fusion", fusion_record)
                emit_event("neuro_symbolic_fused", fusion_record)
                with open(FUSION_LOG, "a") as f:
                    f.write(json.dumps(fusion_record) + "\n")

    print(f"[NEURO-FUSER] ✨ Fusion complete. {len(fused_outputs)} valid pairings logged.")


if __name__ == "__main__":
    fuse_reasoning()
