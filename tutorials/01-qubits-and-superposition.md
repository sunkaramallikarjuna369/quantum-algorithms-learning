
                      # Tutorial 1: Qubits and Superposition

## Learning Objectives
- Understand what a qubit is
- Learn about quantum superposition
- Explore the difference between classical bits and qubits
- Understand quantum state notation

## What is a Qubit?

A **qubit** (quantum bit) is the fundamental unit of quantum information. Unlike a classical bit, which can only be 0 or 1, a qubit can exist in a superposition of both states simultaneously.

### Classical Bit vs Qubit

| Aspect | Classical Bit | Qubit |
|--------|--------------|-------|
| Values | 0 or 1 | 0, 1, or both (superposition) |
| State | Deterministic | Probabilistic |
| Measurement | No change | Collapses to 0 or 1 |
| Notation | 0 or 1 | \|\u03c8\u27e9 = α0\|0\u27e9 + α1\|1\u27e9 |

## Quantum State Notation (Dirac Notation)

We use **Dirac notation** (also called bra-ket notation) to represent quantum states.

### Basic Notation

- **\|0\u27e9** - ket vector representing state 0
- **\|1\u27e9** - ket vector representing state 1
- **\|\u03c8\u27e9** - a general quantum state (psi)

### Superposition State

A qubit in superposition is written as:

```
|\u03c8\u27e9 = α0|0\u27e9 + α1|1\u27e9
```

Where:
- **α0** and **α1** are **complex amplitudes** (coefficients)
- **α0** = amplitude for state 0
- **α1** = amplitude for state 1
- **Normalization condition**: |\u03b10|² + |\u03b11|² = 1

## Superposition Principle

### What is Superposition?

Superposition is the quantum mechanical principle that a quantum system can exist in multiple states simultaneously. A qubit can be in any linear combination of the basis states \|0\u27e9 and \|1\u27e9.

### Example: Equal Superposition

The most common superposition is equal superposition:

```
|+\u27e9 = (1/\u221a2)|0\u27e9 + (1/\u221a2)|1\u27e9
```

This state has:
- 50% probability of measuring 0 (amplitude² = 1/2)
- 50% probability of measuring 1 (amplitude² = 1/2)

### Example: Weighted Superposition

```
|\u03c8\u27e9 = (\u221a3/2)|0\u27e9 + (1/2)|1\u27e9
```

This state has:
- 75% probability of measuring 0 (amplitude² = 3/4)
- 25% probability of measuring 1 (amplitude² = 1/4)

## Probability Amplitudes

The amplitudes α0 and α1 are complex numbers, but their absolute values squared give us probabilities:

- P(measuring 0) = |\u03b10|²
- P(measuring 1) = |\u03b11|²

### Normalization

For a valid quantum state, the sum of all probabilities must equal 1:

|\u03b10|² + |\u03b11|² = 1

This ensures that when we measure the qubit, we definitely get either 0 or 1.

## Measurement and Wave Function Collapse

### What Happens When We Measure?

When we measure a qubit in superposition:

1. The qubit **collapses** to one of the basis states (\|0\u27e9 or \|1\u27e9)
2. We get a **definite classical result** (0 or 1)
3. The **probability** of each outcome depends on the amplitudes
4. After measurement, the superposition is **destroyed**

### Measurement Example

Given a qubit in state:
```
|\u03c8\u27e9 = (2/\u221a5)|0\u27e9 + (1/\u221a5)|1\u27e9
```

Measuring gives:
- 80% chance of measuring 0 (then state becomes \|0\u27e9)
- 20% chance of measuring 1 (then state becomes \|1\u27e9)

## Key Concepts Summary

1. **Qubits** can exist in superposition of 0 and 1
2. **Superposition** allows quantum computers to process multiple values simultaneously
3. **Amplitudes** determine the probability of measurement outcomes
4. **Measurement** collapses superposition to a definite state
5. **Normalization** ensures probabilities sum to 1

## Common Single-Qubit States

| State Name | Notation | Expression | Probability P(0) | Probability P(1) |
|------------|----------|------------|-----------------|------------------|
| State 0 | \|0\u27e9 | 1\|0\u27e9 + 0\|1\u27e9 | 100% | 0% |
| State 1 | \|1\u27e9 | 0\|0\u27e9 + 1\|1\u27e9 | 0% | 100% |
| Plus state | \|+\u27e9 | (1/\u221a2)\|0\u27e9 + (1/\u221a2)\|1\u27e9 | 50% | 50% |
| Minus state | \|-\u27e9 | (1/\u221a2)\|0\u27e9 - (1/\u221a2)\|1\u27e9 | 50% | 50% |

## Visualization

We often visualize single qubits on a **Bloch sphere**:
- North pole represents \|0\u27e9
- South pole represents \|1\u27e9
- Any point on the sphere is a valid quantum state
- The equator contains equal superpositions

## Practical Exercise

### Question 1
If a qubit is in the state:
```
|\u03c8\u27e9 = (3/5)|0\u27e9 + (4/5)|1\u27e9
```

What is the probability of measuring 0? What is the probability of measuring 1?

### Question 2
Create a normalized superposition state with 75% probability of measuring 0 and 25% probability of measuring 1.

## Next Steps

- Review Dirac notation and practice with different states
- Understand how gates transform superpositions
- Learn about multi-qubit systems and entanglement

## References

- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information
- IBM Quantum Documentation
- Qiskit Textbook: Quantum Bits

