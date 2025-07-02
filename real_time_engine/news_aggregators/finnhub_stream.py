# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/finnhub_stream.py
# Tier ΩΩ — Finnhub Stream → Sovereign Memory + Reflex Goals
# Purpose: Ingests real-time news from Finnhub API into sovereign memory and reflex signal loop.
# ============================================================

import os, requests, time, hashlib
from datetime import datetime
from dotenv import load_dotenv

from agentic_ai.sovereign_memory import sovereign_memory

try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

# === Load Finnhub API Key ===
load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")
if not API_KEY or "YOUR_API_KEY" in API_KEY:
    raise ValueError("❌ FINNHUB_API_KEY is missing or invalid. Check your .env file.")

# === Sentiment Classifier ===
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon", quiet=True)
analyzer = SentimentIntensityAnalyzer()

processed_hashes = set()


def get_sentiment(text):
    try:
        score = analyzer.polarity_scores(text)["compound"]
        if score >= 0.25:
            return "positive"
        elif score <= -0.25:
            return "negative"
        else:
            return "neutral"
    except:
        return "neutral"


def hash_url(url):
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
            summary = item.get("summary", "").strip()
            full_text = f"{title} {summary}"

            sentiment = get_sentiment(full_text)
            urgency_score = round(min(1.0, 0.1 + 0.2 * summary.lower().count("urgent")), 2)

            metadata = {
                "summary": title,
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["finnhub", "news", "real_time"],
                "emotion": sentiment,
                "urgency": urgency_score,
                "entropy": round(1 - urgency_score, 2),
                "pressure_score": round(urgency_score * 0.8 + 0.2, 3),
                "source": "finnhub_api",
                "url": article_url,
                "meta_layer": "finnhub_news_ingest"
            }

            sovereign_memory.store(text=title, metadata=metadata)
            if FUSION_ENABLED:
                register_signal(metadata)

            if any(word in title.lower() for word in ["fed", "inflation", "sell", "default", "crash", "rise", "openai"]):
                goal = {
                    "summary": f"Respond to headline: {title}",
                    "timestamp": metadata["timestamp"],
                    "tags": ["goal", "finnhub_trigger"],
                    "emotion": "alert",
                    "urgency": 0.88,
                    "entropy": 0.7,
                    "pressure_score": 0.92,
                    "meta_layer": "goal_seed",
                    "source": "finnhub_api"
                }
                sovereign_memory.store(text=goal["summary"], metadata=goal)

            results.append(metadata)

        print(f"[FINNHUB] ✅ Stored {len(results)} articles.")
        return results

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ [FINNHUB AUTH ERROR] Invalid API key — please check .env (FINNHUB_API_KEY).")
        else:
            print(f"[FINNHUB HTTP ERROR] ❌ {http_err}")
        return []

    except Exception as e:
        print(f"[FINNHUB ERROR] ❌ {e}")
        return []


def fetch_finnhub_news_loop(limit=10):
    print("