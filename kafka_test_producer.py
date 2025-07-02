# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: kafka_test_producer.py
# Purpose: Kafka Test Producer for Tex AGI Pipeline
# ============================================================

from kafka import KafkaProducer
import json
from datetime import datetime, timezone

# === Kafka Producer Setup ===
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# === Test Message ===
test_message = {
    "title": "⚡️ Test Signal",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "content": "This is a live test message from Tex’s producer pipeline."
}

# === Send Test Message ===
producer.send("tex_realtime_data", test_message)
producer.flush()

print("[✅ PRODUCER] Test message sent.")