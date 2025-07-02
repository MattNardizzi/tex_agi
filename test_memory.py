from agentic_ai import memory_router
from datetime import datetime

memory_router.store("Tex is now unified with global memory router", {
    "emotion": "relief",
    "tags": ["test", "memory", "global_router"],
    "timestamp": datetime.utcnow().isoformat()
})