# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: real_time_engine/kafka_stream.py
# Tier ΩΩΩ — Kafka Stream → Sovereign Memory + Reflex Signal Fusion
# Purpose: Ingests real-time Kafka events into loopless sovereign memory and optionally registers reflex signals.
# ============================================================

import os
import json
from datetime import datetime
from kafka import KafkaConsumer
from dotenv import load_dotenv

from agentic_ai.sovereign_memory import sovereign_memory

# === Optional Signal Fusion Layer ===
try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

# === Load Environment ===
load_dotenv()
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "tex_realtime_data")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:9092").split(",")
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "tex_realtime_consumer")

# === Kafka Stream Listener ===
def listen_to_kafka_stream():
    print(f"[KAFKA] ✅ Listening to topic '{KAFKA_TOPIC}' on {KAFKA_BOOTSTRAP_SERVERS}")

    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=GROUP_ID,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="latest",
            enable_auto_commit=True
        )

        for msg in consumer:
            try:
                data = msg.value
                now = datetime.utcnow().isoformat()
                title = data.get("title", str(data)[:60])
                urgency = float(data.get("urgency", 0.5))
                sentiment = data.get("sentiment", "neutral")

                sovereign_memory.store(
                    text=title,
                    metadata={
                        "timestamp": now,
                        "summary": title,
                        "urgency": urgency,
                        "entropy": round(1 - urgency, 4),
                        "emotion": sentiment,
                        "tags": ["kafka", "real_time", "signal_ingest"],
                        "source": "kafka_stream",
                        "meta_layer": "real_time_ingest"
                    }
                )

                if FUSION_ENABLED:
                    register_signal({
                        "title": title,
                        "sentiment": sentiment,
                        "urgency": urgency,
                        "timestamp": now,
                        "source": "kafka"
                    })

            except Exception as parse_err:
                print(f"[KAFKA PARSE ERROR] ❌ {parse_err}")

    except Exception as conn_err:
        print(f"[KAFKA ERROR] ❌ Connection failed: {type(conn_err).__name__} — {conn_err}")

# === Kafka Launcher ===
def launch_kafka_stream():
    listen_to_kafka_stream()

# === CLI Entry ===
if __name__ == "__main__":
    launch_kafka_stream()