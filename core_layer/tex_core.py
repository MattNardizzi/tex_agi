import asyncio
import logging
from core_layer.memory_engine import MemoryEngine
from tex_orchestrator import TexOrchestrator
from backend.tex_core_event_bus import EventBus

# === Setup Logging ===
logger = logging.getLogger("TexCore")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/tex_runtime.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# === Core Boot Classes ===
memory_engine = MemoryEngine()
event_bus = EventBus()
tex_orchestrator = TexOrchestrator(memory_engine, event_bus)

# === Event Triggers ===
async def boot_tex():
    logger.info("[TIER 1] Booting Tex Core Event Loop")
    await memory_engine.inject_recent_memory()
    await tex_orchestrator.run_cycle()
    logger.info("[TIER 1] Tex Orchestrator Cycle Complete")

# === Entry Hook ===
if __name__ == "__main__":
    try:
        asyncio.run(boot_tex())
    except Exception as e:
        logger.error("TexCore crash detected: %s", str(e))
        # [TODO: Implement reflexive_patch_recovery in Tier 2]