# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/feeds/kafka_feed.py
# Tier ΩΩΩ — Kafka Stream → Sovereign Memory + Signal Fusion
# ============================================================

import os
import json
import time
from datetime import datetime
from kafka import KafkaConsumer
from dotenv import load_dotenv

from real_time_engine.memory.memory_router import store_enriched
from real_time_engine.processors.embedder import embed_text

# === Optional Signal Fusion ===
try:
    from real_time_engine.processors.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

# === Load Kafka Environment Variables ===
load_dotenv()
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "tex_realtime_data")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:9092").split(",")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "tex_realtime_consumer")

# === Kafka Consumer Listener ===
def kafka_stream_listener():
    print(f"[KAFKA FEED] 🛰️ Subscribed to topic: '{KAFKA_TOPIC}' on {KAFKA_BOOTSTRAP_SERVERS}")
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=KAFKA_GROUP_ID,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="latest",
            enable_auto_commit=True
        )

        for msg in consumer:
            try:
                data = msg.value
                now = datetime.utcnow().isoformat()

                title = data.get("title", str(data)[:80])
                urgency = float(data.get("urgency", 0.5))
                sentiment = data.get("sentiment", "neutral")
                summary = data.get("summary", title)
                embedding = embed_text(summary)

                payload = {
                    "type": "external_signal",
                    "source": "kafka",
                    "topic": KAFKA_TOPIC,
                    "timestamp": now,
                    "title": title,
                    "summary": summary,
                    "sentiment": sentiment,
                    "urgency": urgency,
                    "emotion": sentiment,
                    "trust_score": 0.92,
                    "heat": round(urgency * 0.9 + 0.1, 3),
                    "embedding": embedding,
                    "tags": ["kafka", "stream", "real_time"]
                }

                store_enriched(payload)

                if FUSION_ENABLED:
                    register_signal(payload)

            except Exception as parse_err:
                print(f"[❌ KAFKA PARSE ERROR] {parse_err}")

    except Exception as conn_err:
        print(f"[❌ KAFKA CONNECTION ERROR] {conn_err}")

# === Entry Point ===
def start_kafka_feed():
    kafka_stream_listener()

if __name__ == "__main__":
    start_kafka_feed()