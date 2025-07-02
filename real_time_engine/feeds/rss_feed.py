# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/feeds/rss_feed.py
# Tier ΩΩΩ — Global RSS Stream → Enrichment → Sovereign Dispatch
# ============================================================

import time
import random
import feedparser
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime, timezone

from real_time_engine.processors.summarizer import summarizer
from real_time_engine.processors.urgency_classifier import enhanced_urgency_score
from real_time_engine.processors.embedder import embed_text
from real_time_engine.processors.dispatch_bus import dispatch_to_tex
from real_time_engine.processors.sentiment_analyzer import analyzer as sentiment_analyzer
# === Global RSS Sources ===
RSS_FEEDS = [
    # Finance & Business
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
    "https://www.bloomberg.com/feed/podcast/etf-report.xml",
    "https://www.ft.com/?format=rss",
    "http://feeds.reuters.com/reuters/businessNews",
    "https://feeds.marketwatch.com/marketwatch/topstories/",
    "https://finance.yahoo.com/news/rssindex",
    "https://news.google.com/rss/search?q=business&hl=en-US&gl=US&ceid=US:en",
    "http://feeds.bbci.co.uk/news/business/rss.xml",

    # Crypto & Forex
    "https://cointelegraph.com/rss",
    "https://bitcoinmagazine.com/.rss/full",
    "https://www.dailyfx.com/feeds/forex-market-news",
    "https://www.forexlive.com/feed/news",
    "https://www.fxstreet.com/rss/news",

    # Commodities
    "https://oilprice.com/rss/main",
    "https://www.investing.com/rss/news_301.rss",
    "https://www.investing.com/rss/news_4.rss",
    "https://www.kitco.com/rss/",

    # Macro & Central Banks
    "https://www.weforum.org/agenda/rss.xml",
    "https://seekingalpha.com/market_currents.xml",
    "https://www.zerohedge.com/fullrss.xml",
    "https://www.imf.org/en/News/rss",
    "https://www.federalreserve.gov/feeds/press_all.xml",
]

# === Deduplication Cache ===
processed_hashes = set()

# === RSS Utility Functions ===
def clean_html(html: str) -> str:
    return BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)

def hash_url(url: str) -> str:
    return hashlib.md5(url.encode("utf-8")).hexdigest()

# === Main RSS Loop ===
def start():
    print("[✅ RSS] Starting global RSS stream...")
    while True:
        for feed_url in RSS_FEEDS:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:5]:
                    url = entry.link
                    title = entry.title.strip()
                    url_hash = hash_url(url)

                    if url_hash in processed_hashes:
                        continue
                    processed_hashes.add(url_hash)

                    summary_raw = clean_html(getattr(entry, "summary", title))
                    summary = summarizer.summarize(summary_raw)
                    urgency = enhanced_urgency_score(title)
                    sentiment = sentiment_analyzer.classify_sentiment(f"{title} {summary}")
                    embedding = embed_text(summary)

                    enriched = {
                        "source": "rss",
                        "title": title,
                        "summary": summary,
                        "url": url,
                        "urgency": urgency,
                        "sentiment": sentiment,
                        "emotion": sentiment,
                        "trust_score": 1.0,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "heat": round(urgency * 0.85 + 0.1, 3),
                        "tags": ["rss", "news", "real_time"],
                        "embedding": embedding,
                    }

                    dispatch_to_tex(enriched)

            except Exception as e:
                print(f"[RSS ERROR] {feed_url} ❌ {e}")

        time.sleep(90)