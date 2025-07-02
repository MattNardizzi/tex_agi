# tex_demos/demo_ontogenesis_spawn.py

from datetime import datetime
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from agi_orchestrators.ontogenesis_orchestrator import OntogenesisOrchestrator
from finance.execution.market_action_engine import MarketActionEngine
from utils.logging_utils import log

ontogenesis = OntogenesisOrchestrator(context="species_fork_demo")

def run_ontogenesis_spawn_demo():
    log.info("🧬 [ONTOGENESIS] Spawning AGI fork with live market input...")

    TEXPULSE["urgency"] = 0.88
    TEXPULSE["entropy"] = 0.42
    TEXPULSE["emotion"] = "ontogenesis"

    # === Pull real-time strategy reflex using financial execution engine
    strategy_seed = MarketActionEngine().decide_action(
        market_context=None,  # Optional: connect to live stream if needed
        urgency=TEXPULSE["urgency"],
        emotion=TEXPULSE["emotion"],
        coherence=TEXPULSE.get("identity_coherence", 0.6)
    )

    belief = f"Species forked with live financial logic: {strategy_seed}"

    ontogenesis.dispatch_spawn_mode({
        "strategy_seed": strategy_seed,
        "summary": belief,
        "origin": "species_evolution_reflex"
    })

    sovereign_memory.store(
        text="🧬 AGI lineage spawned with live financial context.",
        metadata={
            "tags": ["ontogenesis", "species_fork", "finance", "real_time"],
            "timestamp": datetime.utcnow().isoformat(),
            "meta_layer": "ontogenesis_spawn",
            "emotion_vector": [TEXPULSE["urgency"], TEXPULSE["entropy"], 0.1, 0.0]
        }
    )

    dispatch_signal("ontogenesis_spawn", {
        "summary": belief,
        "urgency": TEXPULSE["urgency"],
        "entropy": TEXPULSE["entropy"]
    })

    log.info("✅ [SPAWN COMPLETE] New species created with live market reflex.")

def register(register_func):
    register_func("trigger_ontogenesis_spawn", lambda signal: run_ontogenesis_spawn_demo())