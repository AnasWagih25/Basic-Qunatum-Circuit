# Quantum Circuit Simulation with Qiskit

This repository demonstrates a simple quantum circuit using Qiskit, which applies a Hadamard gate, a CNOT gate, and performs measurement on two qubits. The circuit is simulated using Qiskit's AerSimulator.

## Prerequisites

Ensure you have Python installed along with Qiskit. You can install Qiskit using:

```sh
pip install qiskit qiskit-aer
```

## Quantum Circuit Overview

- A **Hadamard gate** is applied to the first qubit, creating a superposition state.
- A **CNOT (CX) gate** entangles the two qubits.
- Both qubits are **measured** into classical bits.
- The circuit is simulated using **Qiskit's AerSimulator**.

## Code

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a quantum circuit with two qubits and two classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT (CX) gate with the first qubit as control and the second as target
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Use the AerSimulator from qiskit_aer
simulator = AerSimulator()

# Transpile the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Run the simulation by directly calling the simulator
job = simulator.run(compiled_circuit, shots=1024)

# Get and print the results
result = job.result()
counts = result.get_counts()
print("Measurement results:", counts)
```

## Running the Simulation

Save the script and execute it using Python:

```sh
python quantum_circuit.py
```

After execution, you will see an output showing the measurement results in the form of bitstring counts.

## Expected Results

Since the Hadamard gate creates superposition and the CNOT gate entangles the qubits, the expected results should be roughly **50% |00> and 50% |11>** for a large number of shots.

## License

This project is licensed under the MIT License.
