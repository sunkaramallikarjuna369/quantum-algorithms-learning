# Quantum Algorithms Learning Exercises

## Module 1: Qubits and Superposition

### Exercise 1.1: Qubit State Normalization

**Difficulty**: Easy

Given the following quantum states, determine which ones are valid (properly normalized) qubits:

1. |\u03c8\u27e9 = 0.6|0\u27e9 + 0.8|1\u27e9
2. |\u03c8\u27e9 = (1/\u221a2)|0\u27e9 + (1/\u221a2)|1\u27e9
3. |\u03c8\u27e9 = 0.5|0\u27e9 + 0.7|1\u27e9
4. |\u03c8\u27e9 = (2/3)|0\u27e9 + (\u221a5/3)|1\u27e9
5. |\u03c8\u27e9 = i|0\u27e9 - |1\u27e9 (where i is the imaginary unit)

**Solution Guide**:
- For each state, calculate |\u03b10|\u00b2 + |\u03b11|\u00b2
- A normalized state must satisfy |\u03b10|\u00b2 + |\u03b11|\u00b2 = 1
- Remember: for complex numbers, |a + bi|\u00b2 = a\u00b2 + b\u00b2

---

### Exercise 1.2: Measurement Probabilities

**Difficulty**: Easy

A qubit is prepared in the state:
|\u03c8\u27e9 = (\u221a3/2)|0\u27e9 + (1/2)|1\u27e9

If we measure this qubit 1000 times:

1. What is the probability of measuring 0?
2. What is the probability of measuring 1?
3. How many times would you expect to measure 0? How many times 1?

**Your Answer**:
- P(0) = ___
- P(1) = ___
- Expected 0s: ___
- Expected 1s: ___

---

### Exercise 1.3: Create a Superposition State

**Difficulty**: Medium

Create a normalized qubit state that has:
- 25% probability of measuring |0\u27e9
- 75% probability of measuring |1\u27e9

**Hint**: You need to find amplitudes \u03b10 and \u03b11 such that:
- |\u03b10|\u00b2 = 0.25
- |\u03b11|\u00b2 = 0.75
- |\u03b10|\u00b2 + |\u03b11|\u00b2 = 1

**Your State**: |\u03c8\u27e9 = ___ |0\u27e9 + ___ |1\u27e9

---

### Exercise 1.4: Equal Superposition

**Difficulty**: Easy

Write the mathematical representation of the equal superposition state |+\u27e9.

Explain why each basis state has a 50% probability of being measured.

---

## Module 2: Quantum Gates

### Exercise 2.1: Pauli-X Gate

**Difficulty**: Easy

The Pauli-X gate (bit flip) is:
X = \n[0 1]\n[1 0]\n
If a qubit starts in state |0\u27e9, what state does it become after applying the X gate?

Calculation:
X|0\u27e9 = ?

---

### Exercise 2.2: Hadamard Gate Effect

**Difficulty**: Medium

The Hadamard gate creates equal superposition:
H = (1/\u221a2) * \n[1  1]\n[1 -1]\n
1. What is H|0\u27e9?
2. What is H|1\u27e9?
3. If you apply H twice, H(H|0\u27e9), what do you get?

---

### Exercise 2.3: Quantum Gate Composition

**Difficulty**: Medium

Consider applying gates in sequence:
- Start with |0\u27e9
- Apply Hadamard (H)
- Apply Pauli-Z (Z = [[1, 0], [0, -1]])
- Apply Hadamard (H) again

What is the final state? What will you measure?

---

## Module 3: Deutsch Algorithm

### Exercise 3.1: Oracle Understanding

**Difficulty**: Easy

For each function, determine if it's CONSTANT or BALANCED:

1. f(0) = 0, f(1) = 0  → ___
2. f(0) = 1, f(1) = 1  → ___
3. f(0) = 0, f(1) = 1  → ___
4. f(0) = 1, f(1) = 0  → ___

---

### Exercise 3.2: Deutsch Algorithm Prediction

**Difficulty**: Medium

For each of the functions in Exercise 3.1, predict what the Deutsch algorithm will output (0 for CONSTANT, 1 for BALANCED):

1. f(x) = x      →  Output: ___
2. f(x) = NOT x  →  Output: ___
3. f(x) = 0      →  Output: ___
4. f(x) = 1      →  Output: ___

---

### Exercise 3.3: Implement Deutsch Oracle

**Difficulty**: Hard

Implement a custom oracle for the function f(x) = x using Qiskit quantum gates.

**Code Template**:
```python
from qiskit import QuantumCircuit

def deutsch_balanced_id():
    qc = QuantumCircuit(2, name='U_f(x)')
    # Add your gates here
    # ...
    return qc
```

---

## Module 4: Multi-Qubit Systems

### Exercise 4.1: Two-Qubit State

**Difficulty**: Medium

Given a two-qubit state:
|\u03c8\u27e9 = (1/2)|00\u27e9 + (1/2)|01\u27e9 + (1/2)|10\u27e9 + (1/2)|11\u27e9

1. Is this state normalized?
2. What is the probability of measuring |00\u27e9?
3. What is the probability of measuring |11\u27e9?
4. Is this state entangled?

---

### Exercise 4.2: Bell State

**Difficulty**: Hard

The Bell state |\u0398+\u27e9 (maximally entangled state) is:
|\u0398+\u27e9 = (1/\u221a2)(|00\u27e9 + |11\u27e9)

1. Verify this state is normalized
2. What is P(measuring 00)?
3. What is P(measuring 01)?
4. Explain why this state is entangled

---

## Module 5: Quantum Circuit Implementation

### Exercise 5.1: Create Your First Quantum Circuit

**Difficulty**: Easy

Using Qiskit, create a quantum circuit that:
1. Initializes a qubit in state |0\u27e9
2. Applies a Hadamard gate to create superposition
3. Measures the qubit

**Expected Output**: About 50% measuring 0 and 50% measuring 1

---

### Exercise 5.2: Multi-gate Sequence

**Difficulty**: Medium

Create a circuit that:
1. Starts with |0\u27e9
2. Applies Hadamard
3. Applies Pauli-X
4. Applies Hadamard
5. Measures

Predicted outcome: Should measure 1 with 100% probability

Run the circuit and verify!

---

## Challenge Problems

### Challenge 1: Custom Superposition

**Difficulty**: Hard

Design a quantum circuit that creates a superposition state with:
- 30% probability of measuring |0\u27e9
- 70% probability of measuring |1\u27e9

Hint: You may need to use controlled gates and rotation gates.

---

### Challenge 2: Deutsch-Jozsa for 3 Qubits

**Difficulty**: Hard

Extend the Deutsch algorithm to work with 3 qubits. Implement oracles for at least 2 different functions and verify they are correctly classified as constant or balanced.

---

### Challenge 3: Entanglement Detection

**Difficulty**: Hard

Given a two-qubit state, write a program that:
1. Measures the state multiple times
2. Analyzes the measurement statistics
3. Determines whether the qubits are entangled or separable

---

## Answer Key

### Exercise 1.1 Solutions
Valid states: 1 (0.36 + 0.64 = 1.0), 2 (0.5 + 0.5 = 1.0), 4 (4/9 + 5/9 = 1.0)
Invalid states: 3 (0.25 + 0.49 ≠ 1.0), 5 (1 + 1 = 2 ≠ 1.0)

### Exercise 1.2 Solutions
- P(0) = 3/4 = 0.75
- P(1) = 1/4 = 0.25
- Expected 0s: 750
- Expected 1s: 250

### Exercise 1.3 Solution
|\u03c8\u27e9 = (1/2)|0\u27e9 + (\u221a3/2)|1\u27e9

### Exercise 1.4 Solution
|+\u27e9 = (1/\u221a2)|0\u27e9 + (1/\u221a2)|1\u27e9
Each amplitude has magnitude 1/\u221a2, so |1/\u221a2|\u00b2 = 1/2 = 50%

---

## Study Tips

1. **Understand the Math**: Make sure you're comfortable with:
   - Complex numbers
   - Linear algebra (vectors, matrices)
   - Probability

2. **Visualize**: Use Bloch sphere visualizations to understand quantum states

3. **Implement**: Write code for every algorithm you learn

4. **Practice**: Do exercises multiple times with different parameters

5. **Collaborate**: Discuss solutions with others and explain your reasoning

---

## Resources for Help

- IBM Qiskit Textbook: Quantum Gates and Circuits
- Nielsen & Chuang: "Quantum Computation and Quantum Information"
- YouTube: Quantum Computing Lecture Series
- Stack Overflow: quantum-computing tag

