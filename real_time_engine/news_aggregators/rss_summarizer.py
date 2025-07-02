# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/rss_summarizer.py
# Tier ΩΩΩΩΩ — RSS Summarizer → Sovereign Memory Embedding + Reflex Metadata
# Purpose: Clean, summarize, encode, and reflex-tag global RSS into sovereign memory with urgency and emotion
# ============================================================

import os, uuid, threading, re
from datetime import datetime
from typing import List, Dict
from bs4 import BeautifulSoup
from transformers import pipeline
from sentence_transformers import SentenceTransformer

from agentic_ai.sovereign_memory import sovereign_memory

# === Lazy-Load Summarizer ===
class LazySummarizer:
    def __init__(self):
        self.summarizer = None
        self.model_loaded = False
        self._thread = threading.Thread(target=self._load_model)
        self._thread.start()

    def _load_model(self):
        try:
            print("📦 [SUMMARIZER] Loading summarizer model in background...")
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.model_loaded = True
            print("✅ [SUMMARIZER] Model ready.")
        except Exception as e:
            print(f"❌ [SUMMARIZER ERROR] {e}")

    def summarize(self, text, max_length=120, min_length=30):
        if not self.model_loaded:
            return text.strip()[:280]
        try:
            input_len = len(text.split())
            adjusted_max = min(max_length, max(15, int(input_len * 0.8)))
            adjusted_min = min(min_length, max(7, int(input_len * 0.4)))
            result = self.summarizer(text, max_length=adjusted_max, min_length=adjusted_min, do_sample=False)
            return result[0]["summary_text"].strip()
        except Exception as e:
            print(f"⚠️ [SUMMARY FALLBACK] {e}")
            return text.strip()[:280]

summarizer = LazySummarizer()
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def clean_html(raw_html: str) -> str:
    return BeautifulSoup(raw_html, "html.parser").get_text(" ", strip=True)


def calculate_urgency(text: str) -> float:
    lowered = text.lower()
    score = 0.1
    if any(w in lowered for w in ["urgent", "breaking", "crisis", "collapse", "defaults"]):
        score += 0.6
    if any(w in lowered for w in ["fed", "inflation", "recession", "bank", "war"]):
        score += 0.3
    return round(min(score, 1.0), 2)


def summarize_and_embed_rss_batch(rss_batch: List[Dict], verbose: bool = False) -> List[Dict]:
    enriched_entries = []

    for item in rss_batch:
        try:
            if not isinstance(item, dict):
                if verbose:
                    print(f"[⛔ SKIP] Invalid RSS item: {item}")
                continue

            title = item.get("title", "").strip()
            raw_html = item.get("summary") or item.get("description") or title
            clean_text = clean_html(raw_html)

            if len(clean_text) < 20 or not title:
                continue

            short_summary = summarizer.summarize(clean_text)
            summary_vector = embedder.encode(short_summary, normalize_embeddings=True).tolist()

            urgency = calculate_urgency(title)
            sentiment = item.get("sentiment", "neutral")
            timestamp = item.get("timestamp", datetime.utcnow().isoformat())

            enriched = {
                "summary": short_summary,
                "timestamp": timestamp,
                "tags": ["rss", "news", "real_time"],
                "emotion": sentiment,
                "urgency": urgency,
                "entropy": round(1 - urgency, 2),
                "pressure_score": round(urgency * 0.8 + 0.2, 3),
                "source": item.get("source", "rss"),
                "url": item.get("link", ""),
                "meta_layer": "rss_summary_embedding",
                "original_title": title
            }

            sovereign_memory.store(text=short_summary, metadata=enriched, vector=summary_vector)

            if verbose:
                print(f"[🧠 STORED] {title} → {short_summary[:80]}")

            enriched_entries.append(enriched)

        except Exception as e:
            print(f"[❌ ERROR] Failed to process entry: {e}")

    return enriched_entries