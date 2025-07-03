# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: real_time_engine/websocket_broadcast.py
# Tier: ΩΩΩΩΩ — WebSocket Signal Bridge (Tex ⇄ Frontend)
# Purpose: Broadcasts plain-text signals from AGI core to frontend panels (no JSON)
# ============================================================

import asyncio
from datetime import datetime
import websockets

# 🌐 Set of connected WebSocket clients
connected_clients = set()

# 🧠 WebSocket connection handler
async def handler(websocket, path):
    connected_clients.add(websocket)
    print(f"[WebSocket] 🔌 Client connected. Total: {len(connected_clients)}")
    try:
        async for _ in websocket:
            pass  # Not handling frontend messages for now
    except Exception as e:
        print(f"[WebSocket] ⚠️ Client error: {e}")
    finally:
        connected_clients.remove(websocket)
        print(f"[WebSocket] ❌ Client disconnected. Total: {len(connected_clients)}")

# 🚀 WebSocket server loop
async def websocket_server():
    print("[WebSocket] 🚀 Starting WebSocket server on ws://0.0.0.0:8765 ...")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # Keeps server alive forever

# 📡 Broadcast plain-text signal to all connected clients
async def broadcast_update(signal: str):
    if not connected_clients:
        print(f"[WebSocket] ⚠️ No clients connected for: {signal}")
        return

    dead_clients = set()
    for client in connected_clients:
        try:
            await client.send(signal)
        except Exception as e:
            print(f"[WebSocket] ⚠️ Failed to send to client: {e}")
            dead_clients.add(client)

    connected_clients.difference_update(dead_clients)
    print(f"[WebSocket] 📡 Sent: {signal} → {len(connected_clients)} client(s)")

# 🔰 Start the WebSocket server when run directly
if __name__ == "__main__":
    asyncio.run(websocket_server())