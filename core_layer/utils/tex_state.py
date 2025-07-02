from threading import Lock
from typing import Dict, Any

class TexState:
    def __init__(self):
        self._lock = Lock()
        self._state: Dict[str, Any] = {}

    def update_state(self, key: str, value: Dict[str, Any]):
        with self._lock:
            self._state[key] = value
            print(f"[TEX_STATE] ✅ Stored '{key}' with:", value)

    def get_state(self) -> Dict[str, Any]:
        with self._lock:
            print("[TEX_STATE] 📡 Fetching current state:", self._state)
            return dict(self._state)

tex_state = TexState()