# Quantum Algorithms Quick Reference

## Quantum State Notation

### Dirac Notation (Ket-Bra)

```
|ψ⟩ = quantum state (ket)
⟨ψ| = dual state (bra)
⟨ψ|φ⟩ = inner product
```

### Basis States

```
|0⟩ = [1, 0]ᵀ (computational zero)
|1⟩ = [0, 1]ᵀ (computational one)
```

### Superposition

```
|ψ⟩ = α0|0⟩ + α1|1⟩
where |α0|² + |α1|² = 1
```

## Essential Quantum Gates

### Single-Qubit Gates

#### Pauli Gates

```
I (Identity): [1 0]
X (Pauli-X): [0 1]
Z (Pauli-Z): [1 0]
             [0 1]  [1 0]  [0 -1]
Y (Pauli-Y): [0 -i]
             [i 0]
```

#### Hadamard Gate

```
H = (1/√2) * [1  1]
             [1 -1]

Effect:
H|0⟩ = (1/√2)(|0⟩ + |1⟩) = |+⟩
H|1⟩ = (1/√2)(|0⟩ - |1⟩) = |-⟩
H² = I
```

#### Phase Gates

```
S (Phase): [1 0]
T (T-gate): [1 0]
            [0 i]   [0 e^(iπ/4)]
```

### Two-Qubit Gates

#### CNOT (CX) - Controlled-NOT

```
CNOT: [1 0 0 0]
      [0 1 0 0]
      [0 0 0 1]
      [0 0 1 0]

Effect: Flips target qubit if control qubit is |1⟩
```

#### SWAP Gate

```
Swaps the states of two qubits
```

## Common Quantum States

```
|0⟩ = [1, 0]ᵀ    P(0)=100%, P(1)=0%
|1⟩ = [0, 1]ᵀ    P(0)=0%, P(1)=100%
|+⟩ = (|0⟩+|1⟩)/√2  P(0)=50%, P(1)=50%
|-⟩ = (|0⟩-|1⟩)/√2  P(0)=50%, P(1)=50%
|+i⟩ = (|0⟩+i|1⟩)/√2 P(0)=50%, P(1)=50%
|-i⟩ = (|0⟩-i|1⟩)/√2 P(0)=50%, P(1)=50%
```

### Bell States (Entangled)

```
|Φ⁺⟩ = (|00⟩ + |11⟩)/√2
|Φ⁻⟩ = (|00⟩ - |11⟩)/√2
|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
|Ψ⁻⟩ = (|01⟩ - |10⟩)/√2
```

## Quantum Algorithms at a Glance

### Deutsch Algorithm

```
Problem: Determine if f: {0,1} → {0,1} is constant or balanced
Classical: O(2) function calls
Quantum: O(1) function call

Algorithm:
1. Initialize |0⟩|1⟩
2. Apply Hadamard to both
3. Apply oracle U_f
4. Apply Hadamard to first qubit
5. Measure first qubit
   → 0 means constant
   → 1 means balanced
```

### Deutsch-Jozsa Algorithm

```
Extends Deutsch to n-bit functions
Classical: O(2^(n-1)) calls
Quantum: O(1) call
```

### Grover's Search Algorithm

```
Problem: Search unsorted database of N items for marked item
Classical: O(N)
Quantum: O(√N)

Key Components:
- Oracle: marks the solution state
- Diffusion operator: amplifies probability amplitude
- Repeat ~√N times
```

### Shor's Algorithm

```
Problem: Factor large integers
Classical: Exponential time
Quantum: Polynomial time

Applications:
- Breaking RSA encryption
- Key exchange systems
```

## Qiskit Quick Start

### Basic Circuit Creation

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

# Create circuit
qc = QuantumCircuit(1)  # 1 qubit
qc.h(0)  # Apply Hadamard
qc.measure_all()  # Measure all

# Simulate
sim = AerSimulator()
job = sim.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)
```

### Common Operations

```python
qc.x(qubit)         # Pauli-X (bit flip)
qc.y(qubit)         # Pauli-Y
qc.z(qubit)         # Pauli-Z
qc.h(qubit)         # Hadamard
qc.s(qubit)         # S gate
qc.t(qubit)         # T gate
qc.rx(theta, qubit) # Rotation around X
qc.ry(theta, qubit) # Rotation around Y
qc.rz(theta, qubit) # Rotation around Z
qc.cx(control, target)  # CNOT
qc.measure(qubit, cbit) # Measure
```

## Key Quantum Computing Principles

### Superposition
- A quantum system can exist in multiple states simultaneously
- Collapses to single state upon measurement
- Enables quantum parallelism

### Entanglement
- Qubits can be correlated such that state of one depends on others
- Correlation persists across space
- No classical analogue
- Used in many quantum algorithms

### Interference
- Quantum amplitudes can add constructively or destructively
- Algorithms amplify correct answers, cancel incorrect ones
- Key to quantum speedup

### Measurement
- Irreversible process
- Collapses superposition to single state
- Can only be done once (destroys information)
- Result is probabilistic

## Complexity Comparison

| Problem | Classical | Quantum | Algorithm |
|---------|-----------|---------|----------|
| Function evaluation | O(n) | O(1) | Deutsch-Jozsa |
| Database search | O(N) | O(√N) | Grover |
| Integer factoring | O(e^(n^(1/3))) | O(n³) | Shor |
| Linear systems | O(n³) | O(log²n) | HHL |

## Important Definitions

**Qubit**: Quantum bit - basic unit of quantum information

**Superposition**: Linear combination of basis states

**Entanglement**: Correlation between qubits

**Amplitude**: Complex number coefficient in superposition

**Measurement**: Process of determining quantum state value

**Oracle**: Black-box function in quantum algorithms

**Diffusion operator**: Amplification mechanism in Grover's algorithm

**Phase kick-back**: Using auxiliary qubit to encode function output

## Bloch Sphere

Visualizes single-qubit states:

- North pole: |0⟩
- South pole: |1⟩
- Equator: Superposition states
- Any point on sphere: Valid quantum state

## Resources

- IBM Qiskit Textbook
- Nielsen & Chuang Textbook
- Qiskit Documentation: qiskit.org
- Online Quantum Simulator: IBM Quantum
