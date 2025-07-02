# temporal_memory_compressor.py
# Tier ΩΩΩ — Episodic Vector Memory Compressor (Enhanced Reflex Edition)
# Location: core_agi_modules/vector_layer/temporal_memory_compressor.py

from datetime import datetime
import numpy as np
from sentence_transformers import SentenceTransformer, util
from core_agi_modules.vector_layer.query_ops import query_similar_vectors
from core_agi_modules.vector_layer.embed_store import embedder, embed_and_store_vector
from core_agi_modules.vector_layer.heat_tracker import adjust_token_weights
from utils.logging_utils import log

model = SentenceTransformer("all-MiniLM-L6-v2")

# === Memory Compression Entry Point ===
def run_memory_compression(query_text="semantic", top_k=200, similarity_threshold=0.82):
    try:
        log.info("[COMPRESSION] 🧠 Running episodic memory compression...")

        query_vector = embedder.encode(query_text, normalize_embeddings=True).tolist()
        results = query_similar_vectors(query_vector, top_k=top_k)
        texts = [r.payload.get("content") for r in results if r.payload.get("content")]
        metadatas = [r.payload for r in results if r.payload.get("content")]

        if len(texts) < 2:
            log.warning("[COMPRESSION] ❌ Not enough entries to compress.")
            return []

        embeddings = model.encode(texts, convert_to_tensor=True)
        sim_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()

        used = set()
        summaries = []

        for i in range(len(texts)):
            if i in used:
                continue
            cluster = [texts[i]]
            cluster_meta = [metadatas[i]]
            used.add(i)
            for j in range(i + 1, len(texts)):
                if j not in used and sim_matrix[i][j] > similarity_threshold:
                    cluster.append(texts[j])
                    cluster_meta.append(metadatas[j])
                    used.add(j)

            if len(cluster) > 1:
                summary = _summarize_cluster(cluster)

                coherence_score = float(np.mean([
                    sim_matrix[i][j] for j in range(len(texts))
                    if j in used and j != i and sim_matrix[i][j] > similarity_threshold
                ]))

                # Derive weighted attributes
                avg_urgency = round(np.mean([m.get("urgency", 0.5) for m in cluster_meta]), 3)
                dominant_emotion = _dominant_emotion([m.get("emotion", "neutral") for m in cluster_meta])
                heat = round(coherence_score * 0.75 + avg_urgency * 0.25, 4)

                meta = {
                    "event": "compressed_memory",
                    "original_count": len(cluster),
                    "coherence_score": round(coherence_score, 4),
                    "dominant_emotion": dominant_emotion,
                    "urgency": avg_urgency,
                    "heat": heat,
                    "tags": ["ltm_compression", "semantic"],
                    "timestamp": datetime.utcnow().isoformat()
                }

                adjust_token_weights(query_vector, meta, heat)
                embed_and_store_vector(summary, metadata=meta)
                summaries.append(meta)

        log.info(f"[COMPRESSION] ✅ {len(summaries)} semantic compressions stored.")
        return summaries

    except Exception as e:
        log.error(f"[COMPRESSION] ❌ Error during compression: {e}")
        return []

# === Summary Builder ===
def _summarize_cluster(texts):
    if len(texts) == 1:
        return texts[0]
    first = texts[0].split(".")[0]
    rest = "; ".join(t[:80] for t in texts[1:])
    return f"{first.strip()}. Related events: {rest.strip()}"

# === Emotion Counter ===
def _dominant_emotion(emotions):
    count = {}
    for e in emotions:
        count[e] = count.get(e, 0) + 1
    sorted_emotions = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_emotions[0][0] if sorted_emotions else "neutral"

# === CLI Test ===
if __name__ == "__main__":
    run_memory_compression(query_text="semantic", top_k=100)