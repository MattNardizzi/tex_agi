# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/feeds/finnhub_feed.py
# Tier ΩΩ— Finnhub Feed → Dispatch Bus
# Purpose: Fetch news from Finnhub, enrich, and dispatch
# ============================================================

import os
import time
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

# === Load API Key ===
load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")
if not API_KEY or "YOUR_API_KEY" in API_KEY:
    raise ValueError("❌ FINNHUB_API_KEY is missing or invalid. Check your .env file.")

# === Canonical Processor Imports ===
from real_time_engine.processors.summarizer import summarizer
from real_time_engine.processors.urgency_classifier import enhanced_urgency_score
from real_time_engine.processors.embedder import embed_text
from real_time_engine.processors.sentiment_analyzer import analyzer as sentiment_analyzer
from real_time_engine.processors.dispatch_bus import dispatch_to_tex

# === Deduplication Memory ===
processed_hashes = set()

def hash_url(url: str) -> str:
    return hashlib.md5(url.encode("utf-8")).hexdigest()

def fetch_finnhub_news(limit=10):
    url = f"https://finnhub.io/api/v1/news?category=general&token={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        news_items = response.json()[:limit]
        results = []

        for item in news_items:
            article_url = item.get("url", "")
            if not article_url:
                continue

            url_hash = hash_url(article_url)
            if url_hash in processed_hashes:
                continue
            processed_hashes.add(url_hash)

            title = item.get("headline", "").strip()
            raw_summary = item.get("summary", "").strip()
            full_text = f"{title}. {raw_summary}"

            sentiment = sentiment_analyzer.classify_sentiment(full_text)
            urgency = enhanced_urgency_score(full_text)
            summary = summarizer.summarize(full_text)
            vector = embed_text(summary)

            enriched = {
                "source": "finnhub_api",
                "title": title,
                "summary": summary,
                "url": article_url,
                "urgency": urgency,
                "sentiment": sentiment,
                "emotion": sentiment,
                "trust_score": 1.0,
                "timestamp": datetime.utcnow().isoformat(),
                "heat": round(urgency * 0.9 + 0.1, 3),
                "tags": ["finnhub", "news", "real_time"],
                "embedding": vector
            }

            dispatch_to_tex(enriched)
            results.append(enriched)

        print(f"[FINNHUB] ✅ Dispatched {len(results)} articles.")
        return results

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ [FINNHUB AUTH ERROR] Invalid API key.")
        else:
            print(f"[FINNHUB HTTP ERROR] ❌ {http_err}")
        return []

    except Exception as e:
        print(f"[FINNHUB ERROR] ❌ {e}")
        return []

def run_finnhub_loop(interval=90):
    print("🧠 [FINNHUB FEED] Starting Finnhub polling loop...")
    while True:
        fetch_finnhub_news()
        time.sleep(interval)

if __name__ == "__main__":
    run_finnhub_loop()