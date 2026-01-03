# PHASE 2: CORE CONCEPTS (Weeks 3-4)

## Overview
In Phase 2, you'll deepen your quantum knowledge by exploring multi-qubit systems, entanglement, and advanced quantum gates. These concepts form the foundation for understanding quantum algorithms.

## Learning Objectives
- Understand entanglement and Bell states
- Master two-qubit and multi-qubit gates (CNOT, SWAP)
- Learn about quantum entanglement measurement
- Understand tensor products and multi-qubit states
- Recognize quantum correlations vs classical correlations
- Implement and analyze multi-qubit circuits

---

## Week 3: Multi-Qubit Systems

### Topic 3.1: Tensor Products

#### Two-Qubit States
```
|\u03c8\u27e9 = |\u03c8\u2081\u27e9 \u2297 |\u03c8\u2082\u27e9  (tensor product)

Computational basis:
|00\u27e9, |01\u27e9, |10\u27e9, |11\u27e9
```

#### Example: Product State
```
|\u03c8\u27e9 = |0\u27e9 \u2297 |+\u27e9 = |0\u27e9|+\u27e9 = |0+\u27e9
       = (1/\u221a2)(|00\u27e9 + |01\u27e9)
```

### Topic 3.2: Entanglement

#### Definition
A multi-qubit state is entangled if it CANNOT be written as a product of single-qubit states.

#### Bell States (Maximally Entangled)
```
|\u0393\u207a\u27e9 = (1/\u221a2)(|00\u27e9 + |11\u27e9)  Maximally entangled
|\u0393⁻\u27e9 = (1/\u221a2)(|00\u27e9 - |11\u27e9)
|\u0398\u207a\u27e9 = (1/\u221a2)(|01\u27e9 + |10\u27e9)
|\u0398⁻\u27e9 = (1/\u221a2)(|01\u27e9 - |10\u27e9)
```

#### Properties of Entanglement
```
1. Measurements are correlated
2. Cannot be created locally
3. No classical information transfer
4. Powers quantum algorithms
```

### Topic 3.3: Measurement in Multi-Qubit Systems

#### Independent Measurement
```
Measure qubit 1: Get 0 or 1
Measure qubit 2: Independent result

For product state: (1/\u221a2)(|00\u27e9 + |01\u27e9)
```

#### Correlated Measurement
```
For Bell state: (1/\u221a2)(|00\u27e9 + |11\u27e9)

If measure qubit 1 and get 0:
  Qubit 2 MUST be 0 (100% probability)
If measure qubit 1 and get 1:
  Qubit 2 MUST be 1 (100% probability)
```

### Practice Exercises (Week 3)

**Exercise 3.1:** Identify Entanglement
```
Determine which states are entangled:
1. (1/\u221a2)(|00\u27e9 + |11\u27e9)
2. (1/2)(|00\u27e9 + |01\u27e9 + |10\u27e9 + |11\u27e9)
3. |01\u27e9
4. (1/\u221a2)(|0\u27e9 + |1\u27e9) \u2297 (1/\u221a2)(|0\u27e9 + |1\u27e9)
```

---

## Week 4: Two-Qubit Gates and Bell Circuits

### Topic 4.1: CNOT Gate (Controlled-NOT)

#### Matrix Representation
```
CNOT =  [1 0 0 0]
        [0 1 0 0]
        [0 0 0 1]
        [0 0 1 0]
```

#### Operation
```
Control qubit: Determines if target flips

CNOT|00\u27e9 = |00\u27e9
CNOT|01\u27e9 = |01\u27e9
CNOT|10\u27e9 = |11\u27e9  (target flips)
CNOT|11\u27e9 = |10\u27e9  (target flips)
```

### Topic 4.2: Creating Bell States

#### Circuit to Create |\u0393\u207a\u27e9

```
Qubit 0: |0\u27e9 \u2500\u2500[H]\u2500\u2500\u25a0\u2500\u2500
                    |
Qubit 1: |0\u27e9 \u2500\u2500\u2500\u2500\u25a1\u2500\u2500
                 (CNOT)

Steps:
1. H|0\u27e9 = (1/\u221a2)(|0\u27e9 + |1\u27e9)
2. CNOT[(1/\u221a2)(|0\u27e9 + |1\u27e9)\u2297|0\u27e9]
   = (1/\u221a2)(|00\u27e9 + |11\u27e9)
```

### Topic 4.3: Other Two-Qubit Gates

#### SWAP Gate
```
Exchanges states of two qubits
SWAP|01\u27e9 = |10\u27e9
```

#### Controlled-Z
```
Applies Z gate to target if control is |1\u27e9
```

### Practice Exercises (Week 4)

**Exercise 4.1:** CNOT Application
```
Compute: CNOT[(1/\u221a2)(|0\u27e9 + |1\u27e9) \u2297 |0\u27e9]
Expected: Create a Bell state
```

**Exercise 4.2:** Bell State Measurement
```
For |\u0393\u207a\u27e9 = (1/\u221a2)(|00\u27e9 + |11\u27e9):

1. Measure qubit 1 → get 0
2. What is P(measure qubit 2 as 0)?

Answer: 100%
```

---

## Summary of Phase 2

### Key Concepts Learned
1. **Tensor Products**: Combining single-qubit states
2. **Entanglement**: Non-local correlations
3. **Bell States**: Maximally entangled two-qubit states
4. **CNOT Gate**: Creates entanglement
5. **Measurement Correlation**: Entanglement shows in statistics

### Skills Achieved
- [ ] Compute tensor products
- [ ] Identify entangled states
- [ ] Analyze measurement correlations
- [ ] Create Bell states
- [ ] Design multi-qubit circuits
- [ ] Understand quantum correlations

### Critical Insights
```
1. Entanglement ≠ Communication
   (Cannot use it to send information)

2. Entanglement enables quantum advantage
   (Exponential state space)

3. CNOT creates entanglement from product states
   H|0\u27e9\u2297|0\u27e9 → (product)
   CNOT[(H|0\u27e9\u2297|0\u27e9)] → entangled
```

---

## Resources for Phase 2

- IBM Qiskit: Multi-Qubit Gates tutorial
- Nielsen & Chuang: Chapters 1.3-1.4
- "Entanglement Explained" articles
- Bell State measurement simulations
