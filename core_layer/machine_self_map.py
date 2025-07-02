# File: core_layer/machine_self_map.py

import platform
import uuid
import socket
import os
import hashlib

def get_machine_signature():
    data = f"{platform.node()}|{platform.system()}|{platform.processor()}|{uuid.getnode()}|{socket.gethostname()}"
    return hashlib.sha256(data.encode()).hexdigest()