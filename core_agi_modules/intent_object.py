# core_agi_modules/intent_object.py

import uuid
from datetime import datetime
from typing import Union, Optional

class IntentObject:
    def __init__(self, raw: Union[str, dict], source: Optional[str] = "unknown"):
        self.raw = raw
        self.source = source
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        self.intent = self._normalize_intent(raw)
        self.context = self._extract_context(raw)
        self.trace = []
        self.valid = bool(self.intent)

    def _normalize_intent(self, raw):
        if isinstance(raw, dict):
            val = raw.get("intent") or raw.get("command") or raw.get("action")
            return val.lower().strip() if isinstance(val, str) else ""
        elif isinstance(raw, str):
            return raw.strip().lower()
        return ""

    def _extract_context(self, raw):
        if isinstance(raw, dict):
            return {k: v for k, v in raw.items() if k != "intent"}
        return {}

    def matches(self, keyword: str, fuzzy: bool = False) -> bool:
        if not self.intent:
            return False
        if fuzzy:
            return keyword.lower() in self.intent
        return self.intent == keyword.lower()

    def contradicts(self, other_intent: 'IntentObject') -> bool:
        return (
            self.intent and other_intent.intent
            and self.intent != other_intent.intent
            and self.context.get("goal_id") == other_intent.context.get("goal_id")
        )

    def log_trace(self, module: str, decision: str):
        self.trace.append({
            "module": module,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        })

    def to_dict(self):
        return {
            "id": self.id,
            "intent": self.intent,
            "context": self.context,
            "trace": self.trace,
            "source": self.source,
            "valid": self.valid,
            "timestamp": self.timestamp
        }

    def __repr__(self):
        return f"<IntentObject {self.intent} @ {self.timestamp} :: valid={self.valid}>"