# Quantum Circuit Simulation with Qiskit

This repository demonstrates a simple quantum circuit using Qiskit, which applies a Hadamard gate, a CNOT gate, and performs measurement on two qubits. The circuit is simulated using Qiskit's AerSimulator.

## Prerequisites

Ensure you have Python installed along with Qiskit. You can install Qiskit using:

```sh
pip install qiskit qiskit-aer matplotlib
```

## Quantum Circuit Overview

- A **Hadamard gate** is applied to the first qubit, creating a superposition state.
- A **CNOT (CX) gate** entangles the two qubits.
- Both qubits are **measured** into classical bits.
- The circuit is simulated using **Qiskit's AerSimulator**.
- The results are visualized using **matplotlib**.

## Code

```python
#Imports
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

#HADAMARD GATE
qc.h(0)

#CNOT GATE
qc.cx(0, 1)

#To measure both qubits
qc.measure([0, 1], [0, 1])
simulator = AerSimulator()
#Transpile the Circuit
compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)

result = job.result()
counts = result.get_counts()
print("Measurement results:", counts)

plot_histogram(counts)
plt.show()
```

## Running the Simulation

Save the script and execute it using Python:

```sh
python quantum_circuit.py
```

After execution, you will see an output showing the measurement results in the form of bitstring counts, along with a histogram visualization of the results.

## Expected Results

Since the Hadamard gate creates superposition and the CNOT gate entangles the qubits, the expected results should be roughly **50% |00> and 50% |11>** for a large number of shots.

## License

This project is licensed under the MIT License.

