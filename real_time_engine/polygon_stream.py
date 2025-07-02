# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/polygon_stream.py
# Tier ΩΩΩ — Polygon API → Market Feed + Goal Seeding (Tex Cortex)
# Purpose: Ingests real-time Polygon market data + news into sovereign memory and fuses urgent signals for reflex loops.
# ============================================================

import os, sys, time, requests, hashlib
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from agentic_ai.sovereign_memory import sovereign_memory

try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

API_KEY = os.getenv("POLYGON_API_KEY")
SYMBOLS = ["AAPL", "TSLA", "QQQ", "MSFT", "NVDA"]
VOLUME_THRESHOLD = 100_000_000
NEWS_LIMIT = 5

news_hashes = set()
agg_hashes = set()

def hash_entry(entry_str):
    return hashlib.md5(entry_str.encode("utf-8")).hexdigest()

def fetch_polygon_news():
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

            payload = {
                "summary": headline,
                "timestamp": timestamp,
                "tags": ["polygon", "news", "market"],
                "emotion": "neutral",
                "urgency": 0.6,
                "entropy": 0.5,
                "pressure_score": 0.6,
                "meta_layer": "polygon_news_ingest",
                "source": "polygon_news",
                "tickers": tickers
            }

            sovereign_memory.store(text=headline, metadata=payload)
            if FUSION_ENABLED:
                register_signal(payload)

            if any(word in headline.lower() for word in ["sell", "crash", "collapse", "surge", "record", "openai"]):
                goal = {
                    "summary": f"Respond to: {headline}",
                    "timestamp": timestamp,
                    "tags": ["goal", "news_reaction"],
                    "emotion": "alert",
                    "urgency": 0.85,
                    "entropy": 0.7,
                    "pressure_score": 0.9,
                    "meta_layer": "goal_seed",
                    "source": "polygon_news"
                }
                sovereign_memory.store(text=goal["summary"], metadata=goal)

    except Exception as e:
        print(f"[POLYGON NEWS ERROR] ❌ {e}")

def fetch_polygon_aggregates():
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

            payload = {
                "summary": f"{symbol} OHLCV data",
                "timestamp": timestamp,
                "tags": ["polygon", "ohlcv", "market"],
                "urgency": 0.5,
                "entropy": 0.6,
                "pressure_score": 0.5,
                "meta_layer": "polygon_ohlcv_ingest",
                "source": "polygon_agg",
                "symbol": symbol,
                "open": result["o"],
                "high": result["h"],
                "low": result["l"],
                "close": result["c"],
                "volume": result["v"]
            }

            sovereign_memory.store(text=payload["summary"], metadata=payload)
            if FUSION_ENABLED:
                register_signal(payload)

            if result["v"] > VOLUME_THRESHOLD:
                goal = {
                    "summary": f"Investigate unusual volume in {symbol}",
                    "timestamp": timestamp,
                    "tags": ["goal", "volume_spike"],
                    "urgency": 0.9,
                    "entropy": 0.8,
                    "pressure_score": 0.9,
                    "emotion": "curious",
                    "meta_layer": "goal_seed",
                    "source": "polygon_agg"
                }
                sovereign_memory.store(text=goal["summary"], metadata=goal)

        except Exception as e:
            print(f"[AGG ERROR] {symbol} ❌ {e}")

def polygon_data_loop():
    while True:
        fetch_polygon_news()
        fetch_polygon_aggregates()
        time.sleep(90)

def start_polygon_stream():
    polygon_data_loop()

if __name__ == "__main__":
    polygon_data_loop()

def fetch_latest_market_summary():
    try:
        url = f"https://api.polygon.io/v2/aggs/ticker/SPY/prev?adjusted=true&apiKey={API_KEY}"
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        result = response.json().get("results", [])[0]

        return {
            "symbol": "SPY",
            "change_percent": round(((result["c"] - result["o"]) / result["o"]) * 100, 2),
            "close": result["c"],
            "volume": result["v"],
            "timestamp": datetime.utcfromtimestamp(result["t"] / 1000).isoformat(),
            "volatility_score": round(abs(result["h"] - result["l"]) / result["o"], 4)
        }

    except Exception as e:
        print(f"[MARKET SUMMARY ERROR] ❌ {e}")
        return {
            "symbol": "SPY",
            "change_percent": 0.0,
            "close": 0.0,
            "volume": 0,
            "timestamp": datetime.utcnow().isoformat(),
            "volatility_score": 0.0
        }