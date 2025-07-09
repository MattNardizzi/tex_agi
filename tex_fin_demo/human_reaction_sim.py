import time
from datetime import datetime

def simulate_human_reaction(signal: dict) -> dict:
    time.sleep(7)  # Human delay
    return {
        "action": "HOLD" if signal['volatility'] < 0.5 else "BUY",
        "reason": "Based on chart pattern",
        "timestamp": datetime.utcnow().isoformat()
    }