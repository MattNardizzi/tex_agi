from utils.logging_utils import log

SIGNAL_WEIGHTS = {
    "run_demo_ontogenesis_spawn": 1.0,
    "run_demo_world_model_simulation": 1.0,
    "run_demo_reality_rewrite": 1.0,
    "meta:collapse:totality": 1.0
}

def mutate_reflex_engine(reason="unspecified failure"):
    print(f"\n🧠 [CORA] Reflex engine mutation initiated. Reason: {reason}")

    for signal, weight in SIGNAL_WEIGHTS.items():
        new_weight = weight * 0.85
        SIGNAL_WEIGHTS[signal] = new_weight
        print(f"  ↪️ Adjusted weight: {signal} → {new_weight:.4f}")

    log.info(f"[CORA] Reflex weights mutated due to: {reason}")