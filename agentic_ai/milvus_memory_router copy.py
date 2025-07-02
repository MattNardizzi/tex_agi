# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/milvus_memory_router.py
# Tier: ΩΩΩΩΩ∞ — Reflexive Quantum Memory Router (ChronoFusion + MilvusLite)
# Purpose: Emotionally entangled, identity-aware vector memory using MilvusLite for embedded AGI cognition.
# ============================================================

import os
import uuid
import traceback
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

import numpy as np
from sentence_transformers import SentenceTransformer
from pymilvus import (
    connections, utility, Collection, CollectionSchema,
    FieldSchema, DataType
)

# === Configuration ===
COLLECTION_NAME = "tex_memory"
EMBED_DIM = 384
EMBED_MODEL = "all-MiniLM-L6-v2"
MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

# === Connect to MilvusLite ===
connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)

# === Define Schema ===
fields = [
    FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=64),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=EMBED_DIM),
    FieldSchema(name="timestamp", dtype=DataType.VARCHAR, max_length=64),
    FieldSchema(name="emotion", dtype=DataType.FLOAT_VECTOR, dim=4),
    FieldSchema(name="entropy", dtype=DataType.FLOAT),
    FieldSchema(name="summary", dtype=DataType.VARCHAR, max_length=512),
    FieldSchema(name="tags", dtype=DataType.VARCHAR, max_length=256)
]

schema = CollectionSchema(fields, description="Quantum-aware reflex memory store")

if not utility.has_collection(COLLECTION_NAME):
    collection = Collection(name=COLLECTION_NAME, schema=schema)
    print(f"✅ [MILVUS INIT] Collection created: {COLLECTION_NAME}")
else:
    collection = Collection(COLLECTION_NAME)

collection.load()

# === Embedder Init ===
embedder = SentenceTransformer(EMBED_MODEL)

# === MEMORY ROUTER ===
class MilvusMemoryRouter:
    def __init__(self):
        self.collection = collection

    def embed_text(self, text: str) -> List[float]:
        try:
            return embedder.encode(text, normalize_embeddings=True).tolist()
        except Exception as e:
            print(f"❌ [EMBED ERROR] {e}")
            return [0.0] * EMBED_DIM

    def store(self, text: str, metadata: Dict, vector: Optional[List[float]] = None):
        if not text or not isinstance(text, str):
            print("⚠️ [MEMORY SKIP] Invalid input text.")
            return

        try:
            vector = vector or self.embed_text(text)
            record_id = str(uuid.uuid4())
            timestamp = metadata.get("timestamp", datetime.utcnow().isoformat())
            entropy = float(metadata.get("entropy", 0.5))
            emotion_raw = metadata.get("emotion_vector", [0.5, 0.5, 0.0, 0.0])
            emotion_vector = emotion_raw.tolist() if isinstance(emotion_raw, np.ndarray) else emotion_raw
            tags = metadata.get("tags", [])
            tags_str = ",".join(tags) if isinstance(tags, list) else str(tags)
            summary = metadata.get("summary", text[:200])

            self.collection.insert([[
                record_id,
                vector,
                timestamp,
                emotion_vector,
                entropy,
                summary,
                tags_str
            ]])
            print(f"🧠 [MEMORY STORED] {record_id} | {summary}")
        except Exception as e:
            print("❌ [STORE ERROR]")
            traceback.print_exc()

    def store_vector_trace(self, vector: List[float], summary: str, tags: Union[List[str], str]):
        metadata = {
            "summary": summary,
            "timestamp": datetime.utcnow().isoformat(),
            "tags": tags if isinstance(tags, list) else [tags],
            "entropy": 0.5,
            "emotion_vector": [0.5, 0.5, 0.0, 0.0]
        }
        self.store(summary, metadata, vector)

    def query(self, text: str, top_k: int = 5):
        vector = self.embed_text(text)
        return self.query_by_vector(vector, top_k=top_k)

    def query_by_vector(self, vector: List[float], top_k: int = 5):
        try:
            self.collection.load()
            results = self.collection.search(
                data=[vector],
                anns_field="vector",
                param={"metric_type": "COSINE", "params": {"nprobe": 10}},
                limit=top_k,
                output_fields=["summary", "timestamp", "tags", "entropy", "emotion"]
            )
            return results[0]
        except Exception:
            print("❌ [QUERY ERROR]")
            traceback.print_exc()
            return []

    def recall_recent(self, minutes: int = 5, top_k: int = 10) -> list:
        try:
            now = datetime.utcnow()
            cutoff = (now - timedelta(minutes=minutes)).isoformat()
            expr = f'timestamp >= "{cutoff}"'
            results = self.collection.query(
                expr=expr,
                output_fields=["summary", "tags", "timestamp", "entropy", "emotion"],
                limit=top_k
            )
            return results
        except Exception:
            print("❌ [RECALL ERROR]")
            traceback.print_exc()
            return []

# === Cortex Export ===
memory_router = MilvusMemoryRouter()

def embed_text(text: str) -> List[float]:
    return memory_router.embed_text(text)