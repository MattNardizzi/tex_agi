# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/rss_stream.py
# Tier ΩΩ — Tex RSS Stream — Financial & Global Reflex Integration
# Purpose: Ingests real-time global RSS news into sovereign memory with reflexive urgency and emotion tagging.
# ============================================================

import os, sys, time, random, feedparser, re, hashlib
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from agentic_ai.sovereign_memory import sovereign_memory

try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

class RSSStream:
    def __init__(self):
        self.feeds = [
            "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
            "https://www.bloomberg.com/feed/podcast/etf-report.xml",
            "https://www.ft.com/?format=rss",
            "http://feeds.reuters.com/reuters/businessNews",
            "https://feeds.marketwatch.com/marketwatch/topstories/",
            "https://finance.yahoo.com/news/rssindex",
            "https://news.google.com/rss/search?q=business&hl=en-US&gl=US&ceid=US:en",
            "http://feeds.bbci.co.uk/news/business/rss.xml",
            "https://cointelegraph.com/rss",
            "https://bitcoinmagazine.com/.rss/full",
            "https://www.dailyfx.com/feeds/forex-market-news",
            "https://www.forexlive.com/feed/news",
            "https://www.fxstreet.com/rss/news",
            "https://oilprice.com/rss/main",
            "https://www.investing.com/rss/news_301.rss",
            "https://www.investing.com/rss/news_4.rss",
            "https://www.kitco.com/rss/",
            "https://www.weforum.org/agenda/rss.xml",
            "https://seekingalpha.com/market_currents.xml",
            "https://www.zerohedge.com/fullrss.xml",
            "https://www.imf.org/en/News/rss",
            "https://www.federalreserve.gov/feeds/press_all.xml"
        ]
        self.processed_hashes = set()

    def score_urgency(self, title):
        keywords = ["crash", "panic", "inflation", "fed", "buy", "sell", "bank", "default", "volatility", "recession"]
        score = 0.1
        for keyword in keywords:
            if keyword in title.lower():
                score += 0.2
        return round(min(score, 1.0), 2)

    def sanitize_summary(self, raw_html):
        try:
            text = BeautifulSoup(raw_html, "html.parser").get_text()
            return re.sub(r"\s+", " ", text).strip()
        except Exception:
            return ""

    def hash_url(self, url):
        return hashlib.md5(url.encode("utf-8")).hexdigest()

    def fetch_headlines(self):
        results = []
        for url in self.feeds:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    entry_url = entry.link
                    url_hash = self.hash_url(entry_url)

                    if url_hash in self.processed_hashes:
                        continue
                    self.processed_hashes.add(url_hash)

                    urgency = self.score_urgency(entry.title)
                    raw_summary = getattr(entry, "summary", "")
                    clean_summary = self.sanitize_summary(raw_summary)

                    story = {
                        "summary": entry.title,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "tags": ["rss", "news", "real_time"],
                        "emotion": random.choice(["positive", "neutral", "negative"]),
                        "urgency": urgency,
                        "entropy": round(1 - urgency, 2),
                        "pressure_score": round(urgency * 0.9 + random.uniform(0.0, 0.1), 3),
                        "url": entry_url,
                        "meta_layer": "rss_news_ingest",
                        "source": "rss",
                        "content": clean_summary
                    }

                    sovereign_memory.store(text=entry.title, metadata=story)

                    if FUSION_ENABLED:
                        register_signal(story)

                    results.append(story)

            except Exception as e:
                print(f"[RSS ERROR] {url} — {e}")
        return results

    def get_enriched_batch(self, limit=10):
        all_headlines = self.fetch_headlines()
        random.shuffle(all_headlines)
        return all_headlines[:limit]


def start_rss_stream_loop():
    rss = RSSStream()
    print("🧠 [RSS] Stream loop started.")
    while True:
        try:
            batch = rss.get_enriched_batch()
            for story in batch:
                print(f"[RSS] 🧠 {story['summary']} | Urgency: {story['urgency']} | Emotion: {story['emotion']}")
        except Exception as e:
            print(f"[RSS LOOP ERROR] {e}")
        time.sleep(90)


if __name__ == "__main__":
    start_rss_stream_loop()