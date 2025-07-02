# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/real_world_adapter.py
# Tier ΩΩΩ∞Ω — Reflex-Integrated Embodiment Adapter (Vector + Chrono Only)
# Purpose: Enables AGI-body interaction via loopless reflex interfaces, no symbolic traces.
# ============================================================

from datetime import datetime
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_signal_spine import dispatch_signal

class RealWorldAdapter:
    def __init__(self, mode="sim", device_map=None):
        self.mode = mode
        self.device_map = device_map or {}
        self.state_log = []
        self.last_state_vector = {}

    def connect(self):
        print(f"🧠 [EMBODIMENT] Connecting in {self.mode} mode...")
        if self.mode == "camera":
            print("📷 Camera stream active (placeholder)")
        elif self.mode == "robot":
            print("🤖 Connected to robot controller (simulated)")

        timestamp = datetime.utcnow().isoformat()
        memory_router.store(
            text=f"[CONNECT] Embodiment mode: {self.mode}",
            metadata={
                "type": "embodiment_event",
                "tags": ["embodiment", "connect"],
                "emotion": "ready",
                "trust_score": 0.95,
                "timestamp": timestamp
            }
        )

        encode_event_to_fabric(
            raw_text=f"Embodiment initialized in mode: {self.mode}",
            emotion_vector=[0.6, 0.2, 0.1, 0.0],
            entropy_level=0.2,
            tags=["embodiment", "connect", self.mode]
        )

    def send_motor_command(self, direction="forward"):
        now = datetime.utcnow().isoformat()
        print(f"🦿 [ACTUATOR] Moving {direction}...")
        self.state_log.append({"action": direction, "timestamp": now})
        self.last_state_vector["last_movement"] = direction

        memory_router.store(
            text=f"[ACTUATOR] Moved {direction}",
            metadata={
                "type": "motor_action",
                "tags": ["motor", "action"],
                "direction": direction,
                "mode": self.mode,
                "emotion": "intent",
                "timestamp": now
            }
        )

        encode_event_to_fabric(
            raw_text=f"Movement executed: {direction}",
            emotion_vector=[0.7, 0.3, 0.0, 0.1],
            entropy_level=0.3,
            tags=["actuator", "motor", direction]
        )

        dispatch_signal("motor_command_issued", {
            "direction": direction,
            "mode": self.mode,
            "summary": f"Motor movement command: {direction}"
        })

        return True

    def sensor_triggered(self, sensor_id="touch", trigger=True):
        """
        Reflex-safe method to acknowledge sensor input.
        The `trigger` argument should be explicitly passed in from a real stimulus.
        """
        now = datetime.utcnow().isoformat()
        if trigger:
            memory_router.store(
                text=f"[SENSOR] {sensor_id} activated",
                metadata={
                    "type": "sensor_trigger",
                    "tags": ["sensor", sensor_id],
                    "sensor_id": sensor_id,
                    "emotion": "alert",
                    "timestamp": now
                }
            )

            encode_event_to_fabric(
                raw_text=f"Sensor triggered: {sensor_id}",
                emotion_vector=[0.8, 0.5, 0.1, 0.0],
                entropy_level=0.5,
                tags=["sensor", sensor_id, "reflex"]
            )

            dispatch_signal("sensor_input", {
                "sensor_id": sensor_id,
                "summary": f"Sensor {sensor_id} activated",
                "priority": "adaptive"
            })

        return trigger

    def capture_image(self):
        now = datetime.utcnow().isoformat()
        frame_id = f"image_frame_{now}"
        print(f"📸 [CAMERA] Captured frame: {frame_id}")

        memory_router.store(
            text=f"[CAMERA] Image captured: {frame_id}",
            metadata={
                "type": "vision_capture",
                "tags": ["camera", "image"],
                "frame_id": frame_id,
                "emotion": "observing",
                "timestamp": now
            }
        )

        encode_event_to_fabric(
            raw_text=f"Visual frame captured: {frame_id}",
            emotion_vector=[0.6, 0.4, 0.1, 0.0],
            entropy_level=0.4,
            tags=["vision", "camera", "capture"]
        )

        dispatch_signal("vision_input", {
            "frame_id": frame_id,
            "summary": f"Image frame captured: {frame_id}"
        })

        return frame_id

    def connect_device(self, device_type, port):
        print(f"[DEVICE] Connecting {device_type} on port {port}...")
        now = datetime.utcnow().isoformat()
        self.device_map[device_type] = port

        memory_router.store(
            text=f"[DEVICE] {device_type} connected on {port}",
            metadata={
                "type": "device_connection",
                "tags": ["device", device_type],
                "port": port,
                "device_type": device_type,
                "emotion": "establishing",
                "timestamp": now
            }
        )

        encode_event_to_fabric(
            raw_text=f"{device_type} connected on port {port}",
            emotion_vector=[0.5, 0.2, 0.0, 0.0],
            entropy_level=0.25,
            tags=["device", "connect", device_type]
        )

    def get_state_log(self):
        return self.state_log

    def report_status(self):
        return {
            "mode": self.mode,
            "connected_devices": list(self.device_map.keys()),
            "last_action": self.state_log[-1] if self.state_log else None,
            "last_vector": self.last_state_vector
        }