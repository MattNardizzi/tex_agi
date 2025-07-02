import json
import time
import random
from pathlib import Path

EMOTIONS = ["hope", "curiosity", "fear", "doubt", "confidence", "ambition"]
VARIANTS = ["MUTATION_CYCLE_1", "MUTATION_CYCLE_2", "MUTATION_CYCLE_3"]

def write_mutation_log():
    entry = {
        "timestamp": time.time(),
        "dominant_variant": random.choice(VARIANTS),
        "score": round(random.uniform(0.6, 0.99), 4),
        "sandbox_pass": random.choice([True, False]),
        "emotion": random.choice(EMOTIONS),
        "source": "tex_engine",
        "id": f"mut_{int(time.time() * 1000)}"
    }

    path = Path("memory_archive/evolution_results.jsonl")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"[✓] Logged mutation: {entry['dominant_variant']} ({entry['score']*100:.1f}%)")

if __name__ == "__main__":
    while True:
        write_mutation_log()
        time.sleep(3)