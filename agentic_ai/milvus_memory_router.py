# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/milvus_memory_router.py
# Tier: ΩΩΩΩΩ∞ — Reflexive Quantum Memory Router (ChronoFusion + Full Milvus)
# Purpose: Emotionally entangled, identity-aware vector memory using Zilliz Cloud REST API
# ============================================================

import os
import time
import uuid
import traceback
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

import numpy as np
from sentence_transformers import SentenceTransformer

# === Configuration ===
COLLECTION_NAME = "tex_memory"
EMBED_DIM = 384
EMBED_MODEL = "all-MiniLM-L6-v2"
EMBEDDER = SentenceTransformer(EMBED_MODEL)
VECTOR_DIM = EMBED_DIM + 4  # text + emotion

# === Zilliz REST Config (Hardcoded for now)
ZILLIZ_API_KEY = "1bf03e5873fc32b920f11e9e0c32ec0cbcb00cdeff56b6e918e95c6e2664dca8e2f9140bc9b022dc967bd8bf2b9410ef3c3b32be"
ZILLIZ_ENDPOINT = "https://in03-c2caa394358c084.serverless.gcp-us-west1.cloud.zilliz.com"

HEADERS = {
    "accept": "application/json",
    "authorization": f"Bearer {ZILLIZ_API_KEY}",
    "content-type": "application/json"
}

# === MEMORY ROUTER ===
class MilvusMemoryRouter:
    def __init__(self):
        self.endpoint = ZILLIZ_ENDPOINT
        self.headers = HEADERS
        self.collection = COLLECTION_NAME
        if not self._check_collection():
            self._create_collection()

    def _check_collection(self):
        try:
            res = requests.post(
                f"{self.endpoint}/v2/vectordb/collections/list",
                headers=self.headers,
                json={}
            )
            collections = res.json().get("data", [])
            return any(c["name"] == self.collection for c in collections)
        except Exception as e:
            print(f"❌ [COLLECTION CHECK FAILED] {e}")
            return False

    def _create_collection(self):
        try:
            schema = {
                "collection_name": self.collection,
                "dimension": VECTOR_DIM,
                "metric_type": "COSINE",
                "fields": [
                    {"name": "id", "data_type": "VARCHAR", "is_primary": True, "max_length": 64},
                    {"name": "vector_combined", "data_type": "FLOAT_VECTOR", "dimension": VECTOR_DIM},
                    {"name": "timestamp", "data_type": "VARCHAR", "max_length": 64},
                    {"name": "entropy", "data_type": "FLOAT"},
                    {"name": "summary", "data_type": "VARCHAR", "max_length": 512},
                    {"name": "tags", "data_type": "VARCHAR", "max_length": 256}
                ]
            }
            res = requests.post(
                f"{self.endpoint}/v2/vectordb/collections/create",
                headers=self.headers,
                json=schema
            )
            print(f"✅ [MILVUS INIT] Collection created: {self.collection}")
        except Exception as e:
            print("❌ [MILVUS SCHEMA ERROR]")
            traceback.print_exc()

    def embed_text(self, text: str) -> List[float]:
        try:
            return EMBEDDER.encode(text, normalize_embeddings=True).tolist()
        except Exception as e:
            print(f"❌ [EMBED ERROR] {e}")
            return [0.0] * EMBED_DIM

    def store(self, text: str, metadata: Dict, vector: Optional[List[float]] = None):
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

            payload = {
                "collection_name": self.collection,
                "data": [{
                    "id": record_id,
                    "vector_combined": combined_vector,
                    "timestamp": timestamp,
                    "entropy": entropy,
                    "summary": summary,
                    "tags": tags_str
                }]
            }

            requests.post(
                f"{self.endpoint}/v2/vectordb/records/insert",
                headers=self.headers,
                json=payload
            )

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
        try:
            combined = vector + [0.0, 0.0, 0.0, 0.0]  # add emotion dims

            res = requests.post(
                f"{self.endpoint}/v2/vectordb/entities/search",
                headers=self.headers,
                json={
                    "collectionName": self.collection,
                    "annsField": "vector_combined",
                    "data": [combined],
                    "limit": top_k,
                    "outputFields": ["summary", "timestamp", "tags", "entropy"],
                    "searchParams": {"metric_type": "COSINE", "params": {"nprobe": 10}}
                },
                timeout=10
            )

            if res.status_code != 200:
                print(f"❌ [QUERY FAILED] HTTP {res.status_code} → {res.text[:200]}")
                return []

            content = res.json()
            return content.get("data", [])

        except Exception:
            print("❌ [QUERY ERROR]")
            traceback.print_exc()
            return []

    def recall_recent(self, minutes: int = 5, top_k: int = 10) -> list:
        print("⚠️ [RECALL] REST API does not support direct timestamp filtering.")
        return []

# === Cortex Export ===
memory_router = MilvusMemoryRouter()

def embed_text(text: str) -> List[float]:
    return memory_router.embed_text(text)