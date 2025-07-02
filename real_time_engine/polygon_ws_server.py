# ============================================================
# 🟢 Polygon WebSocket Stream → Broadcast to UI Dashboard
# Streams: NASDAQ, SPY, VIX, BTC, ETH
# ============================================================

import asyncio
import websockets
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

POLYGON_API_KEY = "fnAXorRdl8Dt7VlycmP_iXx_Wz2ucaS6"
POLYGON_URL = "wss://socket.polygon.io/stocks"

# === WebSocket Connection Manager ===
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: Dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

manager = ConnectionManager()

# === WebSocket Endpoint for UI Dashboard ===
@app.websocket("/ws/polygon")
async def polygon_dashboard_feed(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# === Startup Hook ===
@app.on_event("startup")
async def start_polygon_stream():
    asyncio.create_task(stream_polygon_data())

# === Polygon Stream Listener ===
last_prices = {}

async def stream_polygon_data():
    try:
        async with websockets.connect(POLYGON_URL) as ws:
            await ws.send(json.dumps({
                "action": "auth",
                "params": POLYGON_API_KEY
            }))

            await ws.send(json.dumps({
                "action": "subscribe",
                "params": "T.SPY,T.QQQ,T.VIX,T.BTCUSD,T.ETHUSD"
            }))

            while True:
                message = await ws.recv()
                parsed = json.loads(message)
                result = {}

                for item in parsed:
                    symbol = item.get("sym")
                    price = item.get("p") or item.get("c")
                    if not symbol or price is None:
                        continue

                    prev_price = last_prices.get(symbol)
                    last_prices[symbol] = price

                    change = None
                    direction = "neutral"
                    if prev_price:
                        change = round(((price - prev_price) / prev_price) * 100, 2)
                        direction = "up" if change > 0 else "down" if change < 0 else "neutral"

                    label_map = {
                        "SPY": "spy",
                        "QQQ": "nasdaq",
                        "VIX": "vix",
                        "BTCUSD": "btc",
                        "ETHUSD": "eth"
                    }

                    label = label_map.get(symbol)
                    if label:
                        result[label] = {
                            "price": round(price, 2),
                            "change": change,
                            "direction": direction
                        }

                if result:
                    await manager.broadcast(result)

    except Exception as e:
        print(f"[POLYGON STREAM ERROR] {e}")
        await asyncio.sleep(3)