# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/deep_memory_editor.py
# Purpose: Memory Compression + Conceptual Threading for AGI Memory Coherence
# Status: 🔒 GODMIND CORE — DEEP SEMANTIC EDITOR v1.0
# ============================================================

import json
import os
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
from core_layer.memory_engine import recall_values, store_to_memory
from tex_backend.tex_core_event_bus import emit_event

model = SentenceTransformer("all-MiniLM-L6-v2")

COMPRESSION_THRESHOLD = 0.84
OUTPUT_LOG = "memory_archive/deep_semantic_threads.jsonl"


def compress_memory(memory_entries, min_cluster_size=3):
    texts = [entry.get("text") or entry.get("goal") or "" for entry in memory_entries]
    embeddings = model.encode(texts, convert_to_tensor=True)
    similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()

    used = set()
    clusters = []

    for i, base in enumerate(texts):
        if i in used:
            continue
        cluster = [memory_entries[i]]
        used.add(i)
        for j in range(i + 1, len(texts)):
            if j not in used and similarity_matrix[i][j] > COMPRESSION_THRESHOLD:
                cluster.append(memory_entries[j])
                used.add(j)
        if len(cluster) >= min_cluster_size:
            clusters.append(cluster)

    return clusters


def abstract_thread(cluster):
    joined = "\n".join([c.get("text") or c.get("goal") for c in cluster])
    abstracted = f"Thread: {joined[:300]}..."  # Placeholder
    return abstracted


def deep_edit():
    print("[MEMORY EDITOR] ✨ Starting deep semantic memory compression...")
    entries = recall_values("tex_memory", limit=1000)
    clusters = compress_memory(entries)

    for cluster in clusters:
        thread = abstract_thread(cluster)
        timestamp = datetime.utcnow().isoformat()
        record = {
            "timestamp": timestamp,
            "summary": thread,
            "source_count": len(cluster),
            "type": "deep_thread"
        }
        store_to_memory("semantic_threads", record)
        emit_event("semantic_thread_created", record)

        with open(OUTPUT_LOG, "a") as f:
            f.write(json.dumps(record) + "\n")

    print(f"[MEMORY EDITOR] ✅ Completed compression: {len(clusters)} threads formed.")


if __name__ == "__main__":
    deep_edit()
