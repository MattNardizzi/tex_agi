# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: reflex_ws_server.py
# Purpose: Real-time cognitive reflex broadcaster (decoupled from memory)
# ============================================================

import asyncio
import websockets

connected_clients = set()

# === WebSocket connection handler ===
async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for _ in websocket:
            pass  # Passive listener only
    finally:
        connected_clients.remove(websocket)

# === Public function: broadcast structured reflex event ===
async def broadcast_reflex(reflex_event: dict):
    if not connected_clients:
        return

    # WebSockets only send strings — use stringified reflex object
    # This is not JSON — it keeps Tex’s internal reflex structure readable and symbolic
    message = str(reflex_event)
    await asyncio.wait([client.send(message) for client in connected_clients])

# === Startup function to be called from tex_agi.py ===
def start_ws_server():
    return websockets.serve(handler, "localhost", 8001)