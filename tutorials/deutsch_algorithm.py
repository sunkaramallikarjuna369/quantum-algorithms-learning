"""
Deutsch Algorithm Implementation using Qiskit

The Deutsch algorithm determines if a function is balanced or constant.
- Constant function: f(0) = f(1)
- Balanced function: f(0) != f(1)

Classical: Requires 2 function evaluations
Quantum: Requires only 1 function evaluation (O(1) vs O(n))
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np


def deutsch_constant_0():
    """
    Oracle for constant function f(x) = 0
    Identity operation on second qubit
    """
    qc = QuantumCircuit(2, name='U_f(constant 0)')
    # Do nothing for constant 0
    return qc


def deutsch_constant_1():
    """
    Oracle for constant function f(x) = 1
    Apply Z gate to second qubit
    """
    qc = QuantumCircuit(2, name='U_f(constant 1)')
    qc.z(1)
    return qc


def deutsch_balanced_id():
    """
    Oracle for balanced function f(x) = x (Identity)
    Apply CNOT gate
    """
    qc = QuantumCircuit(2, name='U_f(balanced id)')
    qc.cx(0, 1)  # CNOT: control=qubit0, target=qubit1
    return qc


def deutsch_balanced_not():
    """
    Oracle for balanced function f(x) = NOT x
    Apply CNOT then X gate on first qubit
    """
    qc = QuantumCircuit(2, name='U_f(balanced not)')
    qc.x(0)
    qc.cx(0, 1)
    qc.x(0)
    return qc


def deutsch_algorithm(oracle, oracle_name):
    """
    Implement the Deutsch Algorithm
    
    Steps:
    1. Initialize with |01> state (qubit0=0, qubit1=1)
    2. Apply Hadamard gates to both qubits
    3. Apply oracle U_f
    4. Apply Hadamard to first qubit
    5. Measure first qubit
    
    Result:
    - Measure 0: function is CONSTANT
    - Measure 1: function is BALANCED
    """
    
    # Create quantum circuit
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(qr, cr)
    
    # Step 1: Initialize to |01> state
    # qubit 0: |0>
    # qubit 1: |1>
    qc.x(qr[1])  # Apply X to flip qubit 1 to |1>
    
    # Step 2: Apply Hadamard gates to both qubits
    # This creates superposition
    qc.h(qr[0])
    qc.h(qr[1])
    
    # Step 3: Apply the oracle
    qc.append(oracle, qr)
    
    # Step 4: Apply Hadamard to first qubit
    qc.h(qr[0])
    
    # Step 5: Measure first qubit
    qc.measure(qr[0], cr[0])
    
    # Run the circuit
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    # Analyze results
    if '0' in counts:
        prob_0 = counts['0'] / 1000
    else:
        prob_0 = 0
    
    if '1' in counts:
        prob_1 = counts['1'] / 1000
    else:
        prob_1 = 0
    
    # Determine if constant or balanced
    if prob_0 > 0.9:  # Mostly measuring 0
        result_type = "CONSTANT"
    else:  # Mostly measuring 1
        result_type = "BALANCED"
    
    return qc, result_type, counts


def main():
    print("=" * 60)
    print("Deutsch Algorithm Demonstration")
    print("=" * 60)
    
    test_cases = [
        (deutsch_constant_0(), "f(x) = 0 (Constant)"),
        (deutsch_constant_1(), "f(x) = 1 (Constant)"),
        (deutsch_balanced_id(), "f(x) = x (Balanced)"),
        (deutsch_balanced_not(), "f(x) = NOT x (Balanced)"),
    ]
    
    for oracle, description in test_cases:
        print(f"\nTesting: {description}")
        print("-" * 60)
        
        qc, result_type, counts = deutsch_algorithm(oracle, description)
        
        print(f"Result Type: {result_type}")
        print(f"Measurement counts: {counts}")
        print(f"Circuit:")
        print(qc)
    
    print("\n" + "=" * 60)
    print("Algorithm Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
