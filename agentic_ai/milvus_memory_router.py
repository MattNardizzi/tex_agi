# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/milvus_memory_router.py
# Tier: ΩΩΩΩΩ∞ — Reflexive Quantum Memory Router (ChronoFusion + Full Milvus)
# Purpose: Emotionally entangled, identity-aware vector memory using full Milvus for scalable AGI cognition.
# ============================================================

import os
import time
import uuid
import traceback
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

import numpy as np
from sentence_transformers import SentenceTransformer
from pymilvus import (
    connections, Collection, CollectionSchema,
    FieldSchema, DataType, utility
)

# === Configuration ===
COLLECTION_NAME = "tex_memory"
EMBED_DIM = 384
EMBED_MODEL = "all-MiniLM-L6-v2"
EMBEDDER = SentenceTransformer(EMBED_MODEL)
VECTOR_DIM = EMBED_DIM + 4  # text + emotion

# === Milvus Connection ===
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

if not MILVUS_HOST:
    raise EnvironmentError("❌ MILVUS_HOST environment variable is not set.")

connected = False
collection = None
for attempt in range(5):
    try:
        connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)
        connected = True
        print(f"✅ [MILVUS CONNECTED] {MILVUS_HOST}:{MILVUS_PORT}")
        break
    except Exception:
        print(f"⏳ [RETRY {attempt+1}/5] Milvus not ready... retrying in 3s")
        time.sleep(3)

if not connected:
    raise ConnectionError(f"❌ Failed to connect to Milvus at {MILVUS_HOST}:{MILVUS_PORT} after 5 attempts.")

# === Schema Initialization ===
try:
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=64),
        FieldSchema(name="vector_combined", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIM),
        FieldSchema(name="timestamp", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="entropy", dtype=DataType.FLOAT),
        FieldSchema(name="summary", dtype=DataType.VARCHAR, max_length=512),
        FieldSchema(name="tags", dtype=DataType.VARCHAR, max_length=256)
    ]
    schema = CollectionSchema(fields, description="Quantum-aware reflex memory store")

    if not utility.has_collection(COLLECTION_NAME):
        collection = Collection(name=COLLECTION_NAME, schema=schema)
        print(f"✅ [MILVUS INIT] Collection created: {COLLECTION_NAME}")

        collection.create_index(
            field_name="vector_combined",
            index_params={
                "index_type": "IVF_FLAT",
                "metric_type": "COSINE",
                "params": {"nlist": 1024}
            }
        )
        print("✅ [MILVUS INDEX] Index created on vector_combined")
    else:
        collection = Collection(COLLECTION_NAME)

except Exception:
    print("❌ [MILVUS SCHEMA ERROR]")
    traceback.print_exc()
    connected = False
    collection = None

# === MEMORY ROUTER ===
class MilvusMemoryRouter:
    def __init__(self):
        if collection is None:
            print("⚠️ [MEMORY ROUTER OFFLINE] Milvus collection is unavailable.")
            self.collection = None
        else:
            self.collection = collection

            # ✅ Index safeguard for existing collections
            try:
                if not self.collection.has_index():
                    print("[⚙️ MILVUS] Index missing — creating index on vector_combined")
                    self.collection.create_index(
                        field_name="vector_combined",
                        index_params={
                            "index_type": "IVF_FLAT",
                            "metric_type": "COSINE",
                            "params": {"nlist": 1024}
                        }
                    )
                    print("✅ [MILVUS] Index successfully created.")
            except Exception:
                print("❌ [MILVUS INDEX ERROR]")
                traceback.print_exc()

    def embed_text(self, text: str) -> List[float]:
        try:
            return EMBEDDER.encode(text, normalize_embeddings=True).tolist()
        except Exception as e:
            print(f"❌ [EMBED ERROR] {e}")
            return [0.0] * EMBED_DIM

    def store(self, text: str, metadata: Dict, vector: Optional[List[float]] = None):
        if not self.collection:
            print("⚠️ [MEMORY SKIP] Milvus is offline.")
            return
        if not text or not isinstance(text, str):
            print("⚠️ [MEMORY SKIP] Invalid text.")
            return

        try:
            base_vector = vector or self.embed_text(text)
            emotion_raw = metadata.get("emotion_vector", [0.5, 0.5, 0.0, 0.0])
            emotion_vector = emotion_raw.tolist() if isinstance(emotion_raw, np.ndarray) else emotion_raw
            combined_vector = base_vector + emotion_vector

            record_id = str(uuid.uuid4())
            timestamp = metadata.get("timestamp", datetime.utcnow().isoformat())
            entropy = float(metadata.get("entropy", 0.5))
            summary = metadata.get("summary", text[:200])
            tags = metadata.get("tags", [])
            tags_str = ",".join(tags) if isinstance(tags, list) else str(tags)

            self.collection.insert([
                [record_id],
                [combined_vector],
                [timestamp],
                [entropy],
                [summary],
                [tags_str]
            ])
            self.collection.flush()

            print(f"🧠 [MEMORY STORED] {record_id} | {summary}")

        except Exception:
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
        if not self.collection:
            print("⚠️ [QUERY SKIP] Milvus is offline.")
            return []
        try:
            self.collection.load()
            combined = vector + [0.0, 0.0, 0.0, 0.0]
            results = self.collection.search(
                data=[combined],
                anns_field="vector_combined",
                param={"metric_type": "COSINE", "params": {"nprobe": 10}},
                limit=top_k,
                output_fields=["summary", "timestamp", "tags", "entropy"]
            )
            return results[0]
        except Exception:
            print("❌ [QUERY ERROR]")
            traceback.print_exc()
            return []

    def recall_recent(self, minutes: int = 5, top_k: int = 10) -> list:
        if not self.collection:
            print("⚠️ [RECALL SKIP] Milvus is offline.")
            return []
        try:
            self.collection.load()
            now = datetime.utcnow()
            cutoff = (now - timedelta(minutes=minutes)).isoformat()
            expr = f'timestamp >= \"{cutoff}\"'
            results = self.collection.query(
                expr=expr,
                output_fields=["summary", "tags", "timestamp", "entropy"],
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