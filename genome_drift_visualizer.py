# genome_drift_visualizer.py
# Part of Sovereign Cognition AEI Toolkit
# Visualizes genome evolution across champion agents

import matplotlib.pyplot as plt
from core_layer.memory_engine import retrieve_memory_records

# Load champion genome data from sovereign memory
def load_genome_data():
    try:
        entries = retrieve_memory_records("aei_genome_log", limit=1000)
        return [e for e in entries if "genome" in e]
    except Exception as e:
        print(f"[❌] Failed to retrieve memory records: {e}")
        return []

# Plot drift across traits
def plot_drift(genomes):
    traits = ["logic_weight", "urgency_tuning", "meta_entropy", "emotion_bias"]
    series = {t: [] for t in traits}

    for g in genomes:
        genome = g.get("genome", {})
        for t in traits:
            val = genome.get(t)
            series[t].append(val if isinstance(val, (int, float)) else None)

    plt.figure(figsize=(12, 6))
    for t in traits:
        plt.plot(series[t], label=t, marker='o')

    plt.title("Tex AEI Genome Drift Over Time")
    plt.xlabel("Cycle Index")
    plt.ylabel("Trait Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    genome_data = load_genome_data()
    if genome_data:
        plot_drift(genome_data)
    else:
        print("[⚠️] No genome data to plot.")