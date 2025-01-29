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