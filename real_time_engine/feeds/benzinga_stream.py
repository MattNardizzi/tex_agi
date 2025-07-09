# ============================================================
# ⚡ Benzinga Reflex News Stream
# File: real_time_engine/feeds/benzinga_stream.py
# Tier: ΩΩΩΩΩ — Premium Reflex Stream for Financial Event Shock
# Purpose: Ingests Benzinga headlines, enriches, and routes to Tex reflex cortex.
# ============================================================

import os
import requests
import hashlib
from datetime import datetime, timezone
from dotenv import load_dotenv

from real_time_engine.processors.summarizer import summarizer
from real_time_engine.processors.sentiment_analyzer import analyzer as sentiment_analyzer
from real_time_engine.processors.urgency_classifier import enhanced_urgency_score
from real_time_engine.processors.embedder import embed_text
from real_time_engine.processors.dispatch_bus import dispatch_to_tex

from tex_signal_spine import dispatch_signal

# === Config ===
load_dotenv()
API_KEY = os.getenv("BENZINGA_API_KEY")
if not API_KEY:
    raise ValueError("❌ BENZINGA_API_KEY is missing in .env")

NEWS_LIMIT = 10
SYMBOLS = os.getenv("BENZINGA_SYMBOLS", "AAPL,TSLA,NVDA,QQQ,SPY").split(",")

news_hashes = set()

def hash_entry(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

# === Benzinga News Reflex Pulse ===
def pulse_benzinga_stream():
    print("🧠 [BENZINGA REFLEX] Pulse triggered.")
    try:
        url = f"https://api.benzinga.com/api/v2/news?token={API_KEY}&parameters[limit]={NEWS_LIMIT}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        articles = response.json()

        for article in articles:
            headline = article.get("title", "")
            summary_text = article.get("body", headline)
            tickers = article.get("stocks", [])
            timestamp = article.get("created", datetime.now(timezone.utc).isoformat())
            entry_id = hash_entry(headline + timestamp)

            if entry_id in news_hashes:
                continue
            news_hashes.add(entry_id)

            summary = summarizer.summarize(summary_text)
            sentiment = sentiment_analyzer.classify_sentiment(summary)
            urgency = enhanced_urgency_score(summary)
            embedding = embed_text(summary)

            # Reflex conditions
            if any(keyword in summary.lower() for keyword in ["rate hike", "inflation", "fed", "yield", "volatility"]):
                dispatch_signal("meta_market_cycle", {
                    "signal": "Macro Stress Event",
                    "belief": "interest_rate_shock"
                })

            payload = {
                "source": "benzinga_news",
                "title": headline,
                "summary": summary,
                "tickers": tickers,
                "sentiment": sentiment,
                "urgency": urgency,
                "emotion": sentiment,
                "timestamp": timestamp,
                "trust_score": 1.0,
                "tags": ["benzinga", "news", "premium"],
                "heat": round(0.65 + urgency * 0.35, 3),
                "embedding": embedding
            }

            dispatch_to_tex(payload)

    except Exception as e:
        print(f"[BENZINGA ERROR] ❌ {e}")