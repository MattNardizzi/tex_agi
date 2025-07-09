# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: real_time_engine/ably_broadcast.py
# Tier: ΩΩΩ — Ably Reflex Emitter for Real-Time Sovereign Events
# Purpose: Sends Ably messages to panel-facing WebSocket channels.
# ============================================================

import os
import json
import requests
from dotenv import load_dotenv

# Load .env values
load_dotenv()

# Retrieve Ably API key from environment
ABLY_KEY = os.getenv("ABLY_API_KEY")

def broadcast_update(channel_name, event_type, payload=None):
    try:
        print(f"📡 [ABLY] Emitting → {channel_name} | {event_type}")
        print(f"🔑 Using Ably Key: {ABLY_KEY[:6]}...")  # Show first few characters for sanity check

        response = requests.post(
            f"https://rest.ably.io/channels/{channel_name}/messages",
            headers={ "Content-Type": "application/json" },
            auth=(ABLY_KEY.split(":")[0], ABLY_KEY.split(":")[1]),
            data=json.dumps({
                "name": event_type,
                "data": payload or {}
            })
        )

        print(f"✅ Ably Response → Code: {response.status_code} | {response.text}")
    except Exception as e:
        print(f"❌ Ably Broadcast Error: {e}")