# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/tex_stream_router.py
# Purpose: Unified Stream Launcher for Real-Time Awareness
# ============================================================

import sys
import os
import threading
import time

# Add parent path for clean imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# === Real-Time Stream Modules ===
from real_time_engine.news_aggregators.rss_stream import RSSStream
from real_time_engine.news_aggregators.finnhub_stream import fetch_finnhub_news_loop
from real_time_engine.news_aggregators.rss_summarizer import summarize_and_embed_rss_batch
from real_time_engine.polygon_stream import start_polygon_stream
from real_time_engine.kafka_stream import launch_kafka_stream
from real_time_engine.real_time_decision_fusion import RealTimeDecisionFusion
from core_layer.utils.memory_utils import safe_get

# === Shared Data Stores ===
rss_data = []
finnhub_data = []
polygon_thread = None

# === RSS STREAM HANDLER ===
def launch_rss_stream():
    print("[✅ RSS STREAM STARTED]")
    global rss_data
    rss = RSSStream()

    while True:
        try:
            raw_batch = rss.get_enriched_batch(limit=5)
            if raw_batch:
                # Filter out invalid entries
                clean_batch = [entry for entry in raw_batch if isinstance(entry, dict)]
                if len(clean_batch) < len(raw_batch):
                    print(f"[PARSE WARNING] Skipped {len(raw_batch) - len(clean_batch)} non-dict RSS entries.")
                rss_data = summarize_and_embed_rss_batch(clean_batch, verbose=False)
        except Exception as e:
            print(f"[RSS ERROR] ❌ {e}")
        time.sleep(90)

def get_latest_rss_data():
    return rss_data

# === FINNHUB STREAM HANDLER ===
def launch_finnhub_stream():
    print("[✅ FINNHUB STREAM STARTED]")
    global finnhub_data

    while True:
        try:
            raw_data = fetch_finnhub_news_loop(limit=5)
            clean_data = [item for item in raw_data if isinstance(item, dict)]
            if len(clean_data) < len(raw_data):
                print(f"[PARSE WARNING] Skipped {len(raw_data) - len(clean_data)} non-dict Finnhub entries.")
            finnhub_data = clean_data
        except Exception as e:
            print(f"[FINNHUB ERROR] ❌ {e}")
        time.sleep(120)

# === POLYGON STREAM HANDLER ===
def launch_polygon_stream():
    print("[✅ POLYGON STREAM STARTED]")
    global polygon_thread

    try:
        polygon_thread = threading.Thread(target=start_polygon_stream, daemon=True)
        polygon_thread.start()
    except Exception as e:
        print(f"[POLYGON ERROR] ❌ {e}")

# === MAIN STREAM LAUNCHER ===
def run_all_streams(tex_brain=None):
    print("[🧠 TEX STREAM ROUTER] Launching real-time data streams...")

    # ✅ Sovereign Fusion Engine Init
    if tex_brain:
        try:
            fusion_engine = RealTimeDecisionFusion(brain=tex_brain)
            tex_brain.real_time_fusion_engine = fusion_engine
            tex_brain.real_time_fusion_active = True
            decision = fusion_engine.ingest_stream_data(
                sentiment_score=0.6,
                volatility_index=0.4,
                news_urgency=0.7
            )
            print(f"[FUSION DECISION] 🚀 Initial decision: {decision}")
        except Exception as e:
            print(f"[FUSION ENGINE ERROR] ❌ Failed to initialize: {e}")

    threads = [
        threading.Thread(target=launch_rss_stream, daemon=True),
        threading.Thread(target=launch_finnhub_stream, daemon=True),
        threading.Thread(target=launch_polygon_stream, daemon=True),
        threading.Thread(target=launch_kafka_stream, daemon=True),
    ]

    for thread in threads:
        thread.start()

    try:
        while True:
            time.sleep(300)
    except KeyboardInterrupt:
        print("\n[🛑 TEX STREAM ROUTER] Interrupted. Shutting down...")

# === EXECUTION ENTRYPOINT ===
if __name__ == "__main__":
    run_all_streams()

def process_stream_update(payload: dict):
    try:
        print(f"[TEX STREAM ROUTER] 🧬 Processing real-time payload: {payload}")
        # Optional: route to fusion engine or analyze payload
        # e.g., store, emit, or score
    except Exception as e:
        print(f"[ERROR] Failed to process stream payload: {e}")