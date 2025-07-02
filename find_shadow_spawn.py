import os

def find_spawn_calls(root_dir="."):
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".py"):
                full_path = os.path.join(dirpath, file)
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "spawn_shadow_agent" in line:
                            print(f"🔍 Found in {full_path}:{i}")
                            print(f"    → {line.strip()}\n")

find_spawn_calls()