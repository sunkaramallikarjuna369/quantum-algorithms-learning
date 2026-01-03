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
|ψ⟩ = |ψ₁⟩ ⊗ |ψ₂⟩ (tensor product)
Computational basis: |00⟩, |01⟩, |10⟩, |11⟩
```

#### Example: Product State

```
|ψ⟩ = |0⟩ ⊗ |+⟩ = |0⟩|+⟩ = |0+⟩ = (1/√2)(|00⟩ + |01⟩)
```

### Topic 3.2: Entanglement

#### Definition

A multi-qubit state is entangled if it CANNOT be written as a product of single-qubit states.

#### Bell States (Maximally Entangled)

```
|Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩) Maximally entangled
|Φ⁻⟩ = (1/√2)(|00⟩ - |11⟩)
|Ψ⁺⟩ = (1/√2)(|01⟩ + |10⟩)
|Ψ⁻⟩ = (1/√2)(|01⟩ - |10⟩)
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
For product state: (1/√2)(|00⟩ + |01⟩)
```

#### Correlated Measurement

```
For Bell state: (1/√2)(|00⟩ + |11⟩)
If measure qubit 1 and get 0: Qubit 2 MUST be 0 (100% probability)
If measure qubit 1 and get 1: Qubit 2 MUST be 1 (100% probability)
```

### Practice Exercises (Week 3)

**Exercise 3.1:** Identify Entanglement

```
Determine which states are entangled:
1. (1/√2)(|00⟩ + |11⟩)
2. (1/2)(|00⟩ + |01⟩ + |10⟩ + |11⟩)
3. |01⟩
4. (1/√2)(|0⟩ + |1⟩) ⊗ (1/√2)(|0⟩ + |1⟩)
```

---

## Week 4: Two-Qubit Gates and Bell Circuits

### Topic 4.1: CNOT Gate (Controlled-NOT)

#### Matrix Representation

```
CNOT = [1 0 0 0]
        [0 1 0 0]
        [0 0 0 1]
        [0 0 1 0]
```

#### Operation

```
Control qubit: Determines if target flips
CNOT|00⟩ = |00⟩
CNOT|01⟩ = |01⟩
CNOT|10⟩ = |11⟩ (target flips)
CNOT|11⟩ = |10⟩ (target flips)
```

### Topic 4.2: Creating Bell States

#### Circuit to Create |Φ⁺⟩

```
Qubit 0: |0⟩ ──[H]──■── |
Qubit 1: |0⟩ ──────⊕── (CNOT)

Steps:
1. H|0⟩ = (1/√2)(|0⟩ + |1⟩)
2. CNOT[(1/√2)(|0⟩ + |1⟩)⊗|0⟩] = (1/√2)(|00⟩ + |11⟩)
```

### Topic 4.3: Other Two-Qubit Gates

#### SWAP Gate

```
Exchanges states of two qubits
SWAP|01⟩ = |10⟩
```

#### Controlled-Z

```
Applies Z gate to target if control is |1⟩
```

### Practice Exercises (Week 4)

**Exercise 4.1:** CNOT Application

```
Compute: CNOT[(1/√2)(|0⟩ + |1⟩) ⊗ |0⟩]
Expected: Create a Bell state
```

**Exercise 4.2:** Bell State Measurement

```
For |Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩):
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
   H|0⟩⊗|0⟩ → (product)
   CNOT[(H|0⟩⊗|0⟩)] → entangled
```

## Resources for Phase 2

- IBM Qiskit: Multi-Qubit Gates tutorial
- Nielsen & Chuang: Chapters 1.3-1.4
- "Entanglement Explained" articles
- Bell State measurement simulations
