import random
import hashlib

def spawn_shadow_timelines(event, num=5):
    timelines = []
    for i in range(num):
        seed = f"{event['summary']}_{i}_{random.random()}"
        timeline = {
            "id": hashlib.md5(seed.encode()).hexdigest(),
            "entropy": random.uniform(0.2, 0.9),
            "collapsed": random.choice([False, True]),
            "belief_network": [
                f"axiom_{i}_{j}" for j in range(random.randint(2, 5))
            ]
        }
        timelines.append(timeline)
    return timelines

def fuse_shadow_axioms(timelines):
    surviving = [t for t in timelines if not t["collapsed"]]
    if not surviving:
        return None

    fused = set()
    for t in surviving:
        fused.update(t["belief_network"])
    return list(fused)