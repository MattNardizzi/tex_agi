# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_chrono_xai_reflex_log.py
# Tier: ΩΩΩ∞∞ — ChronoXAI Reflection Decoder
# Purpose: Decodes recent belief + reflex events from ChronoFabric for visible justification
# ============================================================

from quantum_layer.chronofabric import chrono_mesh
from datetime import datetime
from rich import print

def show_recent_belief_events(n: int = 10):
    print(f"\n🧠 [CHRONOFABRIC TRACE] Last {n} reflexive memory events:\n")
    try:
        nodes = list(chrono_mesh.nodes(data=True))
        sorted_nodes = sorted(nodes, key=lambda x: x[1].get("timestamp", ""), reverse=True)
        count = 0

        for node_id, data in sorted_nodes:
            tags = data.get("tags", [])
            if any(tag in tags for tag in ["belief", "reflex", "explanation", "alpha", "aei"]):
                timestamp = data.get("timestamp", "unknown")
                summary = data.get("raw_text", "—")
                level = data.get("meta_layer", "general")
                emotion = data.get("emotion_vector", [])[0:2] if "emotion_vector" in data else ["?", "?"]

                print(f"[{timestamp}] 🌀 [bold cyan]{level}[/bold cyan] | Urgency={emotion[0]} | Entropy={emotion[1]}")
                print(f"• {summary}\n")

                count += 1
                if count >= n:
                    break

        if count == 0:
            print("[dim]No recent reflex or belief events found in ChronoFabric.[/dim]")

    except Exception as e:
        print(f"[ERROR] Failed to read ChronoFabric: {e}")

if __name__ == "__main__":
    show_recent_belief_events()