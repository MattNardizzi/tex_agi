import json

with open("memory_archive/swarm_feed_backup.jsonl", "r") as f:
    for i, line in enumerate(f, 1):
        try:
            json.loads(line)
        except Exception as e:
            print(f"❌ Line {i} error: {e}")
