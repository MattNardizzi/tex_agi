from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Use a set to prevent duplicate WebSocket connections
connected_clients = set()

# CORS: Allow any origin for now (tighten later in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/aei")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print(f"🔌 New WebSocket connection: {websocket.client}")
    try:
        while True:
            await websocket.receive_text()  # Keeps connection alive
    except WebSocketDisconnect:
        print("⚠️ WebSocket disconnected")
        connected_clients.discard(websocket)
    except Exception as e:
        print(f"❌ WebSocket error: {e}")
        connected_clients.discard(websocket)

# === Broadcast Utility ===
async def broadcast_update(message: str):
    dead_clients = []
    for client in connected_clients:
        try:
            await client.send_text(message)
        except Exception as e:
            print(f"❌ Failed to send message to client {client.client}: {e}")
            dead_clients.append(client)

    # Clean up disconnected clients
    for client in dead_clients:
        connected_clients.discard(client)