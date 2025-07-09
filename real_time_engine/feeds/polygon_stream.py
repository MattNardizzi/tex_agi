# ============================================================
# 🔊 Tex Polygon Reflex Stream
# File: real_time_engine/feeds/polygon_feed.py
# Tier: ΩΩΩΩΩ+++ — Polygon Stream Fusion to Sovereign Memory + Reflex
# Purpose: Pulls Polygon OHLCV + news, enriches, classifies, embeds, and routes to Tex with real-time signal triggers
# ============================================================

import os, requests, hashlib
from datetime import datetime, timezone
from dotenv import load_dotenv

from real_time_engine.processors.summarizer import summarizer
from real_time_engine.processors.sentiment_analyzer import analyzer as sentiment_analyzer
from real_time_engine.processors.urgency_classifier import enhanced_urgency_score
from real_time_engine.processors.embedder import embed_text
from real_time_engine.processors.dispatch_bus import dispatch_to_tex

from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE

# === Configuration ===
load_dotenv()
API_KEY = os.getenv("POLYGON_API_KEY")
if not API_KEY:
    raise ValueError("❌ POLYGON_API_KEY is missing. Check your .env and load_dotenv().")

SYMBOLS = os.getenv("POLYGON_SYMBOLS", "AAPL,TSLA,QQQ,MSFT,NVDA").split(",")
VOLUME_THRESHOLD = 100_000_000
NEWS_LIMIT = 5

# === Deduplication Caches ===
news_hashes = set()
agg_hashes = set()


def hash_entry(entry: str) -> str:
    return hashlib.md5(entry.encode("utf-8")).hexdigest()


# === Polygon News Reflex Trigger ===
def trigger_polygon_news():
    url = f"https://api.polygon.io/v2/reference/news?limit={NEWS_LIMIT}&apiKey={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        articles = response.json().get("results", [])

        for article in articles:
            headline = article.get("title", "Untitled")
            tickers = article.get("tickers", [])
            timestamp = article.get("published_utc") or datetime.now(timezone.utc).isoformat()
            entry_id = hash_entry(headline + timestamp)

            if entry_id in news_hashes:
                continue
            news_hashes.add(entry_id)

            summary = summarizer.summarize(headline)
            sentiment = sentiment_analyzer.classify_sentiment(summary)
            urgency = enhanced_urgency_score(summary)
            embedding = embed_text(summary)

            # === Reflex Injection Hooks
            lower_summary = summary.lower()
            if "options" in lower_summary and ("volatility" in lower_summary or "spike" in lower_summary):
                dispatch_signal("meta_market_cycle", {
                    "signal": "Options Vol Spike",
                    "belief": "volatility_choke"
                })

            if any(word in lower_summary for word in ["powell", "inflation", "rate hike", "hawkish"]):
                dispatch_signal("meta_market_cycle", {
                    "signal": "Fed Hawkish Hint",
                    "belief": "policy_contradiction"
                })

            payload = {
                "source": "polygon_news",
                "title": headline,
                "summary": summary,
                "tickers": tickers,
                "sentiment": sentiment,
                "urgency": urgency,
                "emotion": sentiment,
                "timestamp": timestamp,
                "trust_score": 1.0,
                "tags": ["polygon", "news", "real_time"],
                "heat": round(0.6 + urgency * 0.4, 3),
                "embedding": embedding
            }

            dispatch_to_tex(payload)

    except Exception as e:
        print(f"[POLYGON NEWS ERROR] ❌ {e}")


# === Polygon OHLCV Reflex Trigger ===
def trigger_polygon_aggregates():
    for symbol in SYMBOLS:
        url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={API_KEY}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            result = response.json().get("results", [])[0]

            timestamp = datetime.utcfromtimestamp(result["t"] / 1000).replace(tzinfo=timezone.utc).isoformat()
            entry_id = hash_entry(symbol + timestamp)

            if entry_id in agg_hashes:
                continue
            agg_hashes.add(entry_id)

            open_price = result["o"]
            close_price = result["c"]
            percent_change = ((close_price - open_price) / open_price) * 100

            if percent_change <= -2.5:
                urgency = TEXPULSE.get("urgency", 0.92)
                entropy = TEXPULSE.get("entropy", 0.78)

                print(f"📉 [CONTRADICTION] {symbol} dropped {percent_change:.2f}% — triggering tex_fin_reflex")

                dispatch_signal("tex_fin_reflex", {
                    "symbol": symbol,
                    "detected_change": percent_change,
                    "reason": f"{symbol} dropped more than 2.5% intraday. Reflex engagement required.",
                    "trigger_type": "price_drop"
                }, urgency=urgency, entropy=entropy, source="polygon_feed")

            summary = f"{symbol} closed at {close_price} on volume {result['v']:,}."
            urgency = 0.2 if result["v"] < VOLUME_THRESHOLD else 0.85
            sentiment = "neutral"
            embedding = embed_text(summary)

            payload = {
                "source": "polygon_agg",
                "title": f"{symbol} OHLCV",
                "summary": summary,
                "symbol": symbol,
                "open": open_price,
                "high": result["h"],
                "low": result["l"],
                "close": close_price,
                "volume": result["v"],
                "timestamp": timestamp,
                "urgency": urgency,
                "sentiment": sentiment,
                "emotion": sentiment,
                "trust_score": 1.0,
                "tags": ["polygon", "ohlcv", "real_time"],
                "heat": round(0.5 + urgency * 0.4, 3),
                "embedding": embedding
            }

            dispatch_to_tex(payload)

        except Exception as e:
            print(f"[AGG ERROR] ❌ {symbol} → {e}")


# === Sovereign Reflex Pulse Entrypoint ===
def pulse_polygon_stream():
    """
    This function is designed to be triggered by Tex's reflex system or cortex router.
    It pulls the latest data once — no loops, no blocking.
    """
    print("📡 [POLYGON REFLEX] Single pulse initiated.")
    try:
        trigger_polygon_news()
        trigger_polygon_aggregates()
    except Exception as e:
        print(f"[POLYGON PULSE ERROR] ❌ {e}")