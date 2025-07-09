from tex_signal_spine import register, dispatch_signal

def test_handler(signal):
    print("✅ Reflex was called with signal:", signal)

register("test_trigger", test_handler)
dispatch_signal("test_trigger", {"test": "value"})