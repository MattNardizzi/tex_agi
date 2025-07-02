# ============================================================
# QAOA Execution via PennyLane for Tex AGI
# ============================================================

import pennylane as qml
from pennylane import numpy as np

def execute_qaoa(n_qubits=2, steps=2, weights=None):
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit(params):
        for i in range(n_qubits):
            qml.Hadamard(wires=i)

        for i in range(steps):
            qml.CNOT(wires=[0, 1])
            qml.RZ(params[i], wires=1)
            qml.CNOT(wires=[0, 1])
            qml.RX(params[i + steps], wires=0)
            qml.RX(params[i + steps], wires=1)

        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

    if weights is None:
        weights = np.random.uniform(0, np.pi, 2 * steps)

    return circuit(weights).tolist()