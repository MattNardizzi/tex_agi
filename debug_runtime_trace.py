import sys

def print_loaded_modules():
    print("\n🧠 Loaded user modules:\n")
    for name, module in sorted(sys.modules.items()):
        try:
            path = getattr(module, "__file__", None)
            if path and "venv" not in path and "site-packages" not in path:
                print(path)
        except Exception:
            continue

if __name__ == "__main__":
    import tex_agi  # This runs your system
    print_loaded_modules()