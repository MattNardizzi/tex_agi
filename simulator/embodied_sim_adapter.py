# embodied_sim_adapter.py
# Tier ΩΩΩΩΩ.Δ — Final Reflex-Linked AGI Simulation Bridge (Unity/Dream/Godot-compatible)

import time
import socket
import json
import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.tex_memory_orchestrator import store_and_process_memory
from core_layer.reflex_engine import trigger_reflex_event

SIM_PORT = 5555
SIM_HOST = "127.0.0.1"
BUFFER_SIZE = 4096
TIMEOUT_SEC = 2.5

class EmbodiedSimAdapter:
    def __init__(self, agent_id="Tex", environment="Unity", session_id=None):
        self.agent_id = agent_id
        self.environment = environment
        self.session_id = session_id or f"sim-session-{int(time.time())}"
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(TIMEOUT_SEC)
        self.connected = False
        self.failure_count = 0

    def _trace_id(self, action_type):
        return f"{action_type}-{uuid.uuid4().hex[:8]}"

    def connect(self):
        try:
            handshake = {
                "type": "handshake",
                "agent_id": self.agent_id,
                "environment": self.environment,
                "session_id": self.session_id
            }
            self.socket.sendto(json.dumps(handshake).encode(), (SIM_HOST, SIM_PORT))
            self.connected = True
            print(f"🧠 [SIM ADAPTER] Connected to {self.environment} simulation.")
        except Exception as e:
            print(f"[SIM ADAPTER ERROR] {e}")
            self.connected = False

    def send_action(self, action):
        if not self.connected:
            self.connect()

        trace_id = self._trace_id(action.get("type", "act"))
        try:
            payload = {
                "type": "action",
                "agent_id": self.agent_id,
                "session_id": self.session_id,
                "timestamp": datetime.utcnow().isoformat(),
                "action": action,
                "trace_id": trace_id
            }
            self.socket.sendto(json.dumps(payload).encode(), (SIM_HOST, SIM_PORT))
        except Exception as e:
            print(f"[SIM ACTION ERROR] {e}")

        return trace_id

    def receive_state(self):
        try:
            data, _ = self.socket.recvfrom(BUFFER_SIZE)
            state = json.loads(data.decode())
            print(f"🌐 [SIM STATE] {state}")
            self.log_state(state)
            self.reflect_state(state)
            return state
        except socket.timeout:
            self.failure_count += 1
            print("[SIM] ⏳ No response received.")
            if self.failure_count > 3:
                trigger_reflex_event("SIMULATION_TIMEOUT", {"failures": self.failure_count})
            return None
        except Exception as e:
            print(f"[SIM RECEIVE ERROR] {e}")
            return None

    def log_state(self, state_data):
        try:
            summary = json.dumps(state_data)[:256]
            store_and_process_memory(
                text=f"Sim state: {summary}",
                emotion=state_data.get("emotion", "neutral"),
                urgency=state_data.get("urgency", 0.5),
                tags=["simulation", "embodiment"]
            )
        except Exception as e:
            print(f"[SIM MEMORY ERROR] {e}")

    def reflect_state(self, state):
        if "emotion" in state:
            TEXPULSE["mood"] = state["emotion"]
        if "urgency" in state:
            TEXPULSE["urgency"] = round(float(state["urgency"]), 4)
        if state.get("event") in ["pain", "injury", "threat"]:
            trigger_reflex_event("AGENT_DEFENSE_REFLEX", state)

    def step(self, action):
        trace_id = self.send_action(action)
        state = self.receive_state()
        return {"trace_id": trace_id, "state": state}