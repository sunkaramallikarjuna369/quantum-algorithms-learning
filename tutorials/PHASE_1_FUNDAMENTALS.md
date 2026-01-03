# PHASE 1: FUNDAMENTALS (Weeks 1-2)

## Overview
This phase introduces the foundational concepts of quantum computing. You'll learn the basics of qubits, quantum gates, quantum circuits, and measurement in quantum systems. This is essential knowledge for all subsequent phases.

## Learning Objectives
By the end of Phase 1, you should understand:
- What qubits are and how they differ from classical bits
- Superposition and its quantum mechanical basis
- Basic quantum gates and their operations
- How to construct and visualize quantum circuits
- Measurement and quantum state collapse
- Basic quantum notation (Dirac notation)

---

## Week 1: Qubits and Superposition

### Topic 1.1: What is a Qubit?

#### Classical Bit vs Quantum Bit

**Classical Bit:**
```
State: Always 0 or 1
Value: Definite and deterministic
Example: Computer memory (transistor is ON or OFF)
```

**Quantum Bit (Qubit):**
```
State: 0, 1, or BOTH (superposition)
Value: Probabilistic until measured
Example: Electron spin (up, down, or both simultaneously)
```

### Topic 1.2: Dirac Notation (Ket-Bra Notation)

We represent quantum states using special mathematical notation:

```
|0\u27e9  "ket zero" - basis state 0
|1\u27e9  "ket one"  - basis state 1
\u27e8\u03c8| "bra psi"  - dual state (conjugate transpose)
|\u03c8\u27e9  "ket psi"  - quantum state vector
```

#### Representing States as Vectors

```
|0\u27e9 = [1]    |1\u27e9 = [0]
      [0]          [1]
```

### Topic 1.3: Superposition

#### Definition
A qubit can exist in a linear combination of basis states:
```
|\u03c8\u27e9 = \u03b10|0\u27e9 + \u03b11|1\u27e9
```

Where:
- \u03b10, \u03b11 are complex amplitudes
- |\u03b10|\u00b2 = probability of measuring 0
- |\u03b11|\u00b2 = probability of measuring 1
- Normalization: |\u03b10|\u00b2 + |\u03b11|\u00b2 = 1

#### Examples

**Equal Superposition:**
```
|+\u27e9 = (1/\u221a2)|0\u27e9 + (1/\u221a2)|1\u27e9
P(0) = 1/2 = 50%
P(1) = 1/2 = 50%
```

**Weighted Superposition:**
```
|\u03c8\u27e9 = (\u221a3/2)|0\u27e9 + (1/2)|1\u27e9
P(0) = 3/4 = 75%
P(1) = 1/4 = 25%
```

### Topic 1.4: Measurement and Collapse

#### The Measurement Problem

When we measure a qubit in superposition:

```
1. System collapses to one basis state
2. Result is probabilistic
3. Superposition is destroyed
4. Subsequent measurements give same result
```

#### Example

Qubit state: |\u03c8\u27e9 = (3/5)|0\u27e9 + (4/5)|1\u27e9

```
Measurement results (repeated 1000 times):
- Measure 0: ~360 times (probability = 9/25 = 36%)
- Measure 1: ~640 times (probability = 16/25 = 64%)

After first measurement:
If measured 0 → state becomes |0\u27e9
If measured 1 → state becomes |1\u27e9
```

### Practice Exercises (Week 1)

**Exercise 1.1:** Normalize the state
```
Given: |\u03c8\u27e9 = a|0\u27e9 + b|1\u27e9
Find a and b such that |a|\u00b2 + |b|\u00b2 = 1
Condition: P(0) = 0.6, P(1) = 0.4
```

**Exercise 1.2:** Calculate probabilities
```
Given: |\u03c8\u27e9 = (2/\u221a13)|0\u27e9 + (3/\u221a13)|1\u27e9
Find: P(0) and P(1)
```

---

## Week 2: Quantum Gates and Circuits

### Topic 2.1: Single-Qubit Gates

Quantum gates are unitary transformations that modify quantum states.

#### Pauli Gates

**Pauli-X (Bit Flip):**
```
X = [0 1]    Effect: X|0\u27e9 = |1\u27e9, X|1\u27e9 = |0\u27e9
    [1 0]    (Similar to NOT gate)
```

**Pauli-Y:**
```
Y = [0 -i]   Effect: Y|0\u27e9 = i|1\u27e9, Y|1\u27e9 = -i|0\u27e9
    [i  0]
```

**Pauli-Z (Phase Flip):**
```
Z = [1  0]   Effect: Z|0\u27e9 = |0\u27e9, Z|1\u27e9 = -|1\u27e9
    [0 -1]
```

#### Hadamard Gate (H)

The Hadamard gate creates superposition:

```
H = (1/\u221a2) * [1  1]    
              [1 -1]

Effect:
H|0\u27e9 = (1/\u221a2)(|0\u27e9 + |1\u27e9) = |+\u27e9
H|1\u27e9 = (1/\u221a2)(|0\u27e9 - |1\u27e9) = |-\u27e9

Key property: H\u00b2 = I (applying twice gives identity)
```

#### Phase Gates

**S Gate:**
```
S = [1 0]    (Phase shift of 90\u00b0)
    [0 i]
```

**T Gate:**
```
T = [1     0   ]    (Phase shift of 45\u00b0)
    [0 e^(i\u03c0/4)]
```

### Topic 2.2: Quantum Circuits

#### Circuit Notation

A quantum circuit shows:
```
Input lines: |\u03c8\u27e9 \u2500\u2500[Gate]\u2500\u2500[Gate]\u2500\u2500> Output
         measurement
```

#### Basic Circuit Example 1

```
Create superposition:

|0\u27e9 \u2500\u2500[H]\u2500\u2500 Result: (1/\u221a2)(|0\u27e9 + |1\u27e9)
```

#### Basic Circuit Example 2

```
Bit flip then measure:

|0\u27e9 \u2500\u2500[X]\u2500\u2500[M] Result: Always measure 1
            |
          Classical bit
```

#### Multi-Gate Circuit

```
|0\u27e9 \u2500\u2500[H]\u2500\u2500[X]\u2500\u2500[H]\u2500\u2500[M]

Steps:
1. H|0\u27e9 = (1/\u221a2)(|0\u27e9 + |1\u27e9)
2. X(1/\u221a2)(|0\u27e9 + |1\u27e9) = (1/\u221a2)(|1\u27e9 + |0\u27e9)  [same]
3. H(1/\u221a2)(|1\u27e9 + |0\u27e9) = |1\u27e9
4. Measure: always get 1
```

### Topic 2.3: Quantum Gate Properties

#### Unitarity
All quantum gates must be unitary:
```
U\u2020 U = I  (where U\u2020 is conjugate transpose)

This ensures:
- Reversibility (except measurement)
- Probability conservation
- No information loss (in principle)
```

#### Composability
Gates can be composed:
```
U_total = U_n ... U_2 U_1

Applied right to left:
U_total|\u03c8\u27e9 = U_n(U_(n-1)(...(U_1|\u03c8\u27e9)...))
```

### Practice Exercises (Week 2)

**Exercise 2.1:** Apply Pauli-X gate
```
Compute: X[(1/\u221a2)|0\u27e9 + (1/\u221a2)|1\u27e9]
Expected: (1/\u221a2)|1\u27e9 + (1/\u221a2)|0\u27e9 = same state
```

**Exercise 2.2:** Apply Hadamard twice
```
Compute: H(H|0\u27e9)
Expected: |0\u27e9  (back to original)
```

**Exercise 2.3:** Design a circuit
```
Goal: Create a qubit that measures 0 with 100% probability
Requirement: Start with |0\u27e9

Hint: Not all gates will help. Think about which gates
preserve |0\u27e9.
```

---

## Summary of Phase 1

### Key Concepts
1. **Qubits**: Quantum bits that can be in superposition
2. **Superposition**: Linear combination of basis states
3. **Amplitude**: Complex number coefficient, |amplitude|\u00b2 = probability
4. **Measurement**: Collapses superposition to definite state
5. **Quantum Gates**: Unitary operations on qubits
6. **Hadamard**: Creates equal superposition
7. **Pauli Gates**: X (bit flip), Y, Z (phase flip)
8. **Circuits**: Sequence of quantum operations

### Skills Developed
- [ ] Calculate probabilities from amplitudes
- [ ] Normalize quantum states
- [ ] Understand measurement and collapse
- [ ] Apply quantum gates manually
- [ ] Design simple quantum circuits
- [ ] Understand gate composition

### Common Mistakes to Avoid

1. **Confusing amplitude with probability**
   ```
   WRONG: |0\u27e9 = 0.7
   RIGHT: |\u03c8\u27e9 = 0.7|0\u27e9 + ...
   ```

2. **Forgetting normalization**
   ```
   |\u03b10|\u00b2 + |\u03b11|\u00b2 must equal 1
   ```

3. **Assuming measurement is reversible**
   ```
   Measurement collapses state permanently
   ```

4. **Gate order matters**
   ```
   [H][X]|\u03c8\u27e9 \u2260 [X][H]|\u03c8\u27e9 (usually)
   ```

### Next Steps
Once you master Phase 1:
1. Review exercises and ensure 100% understanding
2. Practice mental simulation of simple circuits
3. Implement gates in Qiskit
4. Move to Phase 2: Core Concepts

---

## Resources for Phase 1

- **Textbook**: Nielsen & Chuang, Chapters 1-2
- **Online**: IBM Qiskit Textbook - Quantum States and Qubits
- **Videos**: YouTube "Quantum Computing for Beginners" (3Blue1Brown series)
- **Interactive**: IBM Quantum Composer (online simulator)
