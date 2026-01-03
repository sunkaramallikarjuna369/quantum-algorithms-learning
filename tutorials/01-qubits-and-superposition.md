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
| Notation | 0 or 1 | ψ⟩ = α0⟩0⟩ + α1⟩1⟩ |

## Quantum State Notation (Dirac Notation)

We use **Dirac notation** (also called bra-ket notation) to represent quantum states.

### Basic Notation

- **⟩0⟩** - ket vector representing state 0
- **⟩1⟩** - ket vector representing state 1
- **ψ⟩** - a general quantum state (psi)

### Superposition State

A qubit in superposition is written as:

```
|ψ⟩ = α0|0⟩ + α1|1⟩
```

Where:

- **α0** and **α1** are **complex amplitudes** (coefficients)
- **α0** = amplitude for state 0
- **α1** = amplitude for state 1
- **Normalization condition**: |α0|² + |α1|² = 1

## Superposition Principle

Superposition is the quantum mechanical principle that a quantum system can exist in multiple states simultaneously. The key insight:

- A qubit is **not** in one definite state until measured
- The superposition state encodes all possible measurement outcomes
- Each outcome has an associated **amplitude** (a complex number)
- The **probability** of measuring outcome i is |αi|²

Example: The famous Bell state (or entangled pair):

```
|Φ⟩ = (1/√2)(|0⟩0⟩ + |1⟩1⟩)
```

This state shows equal superposition:

- Probability of measuring |00⟩ = |1/√2|² = 1/2
- Probability of measuring |11⟩ = |1/√2|² = 1/2
- The equator contains equal superpositions

## Bloch Sphere Visualization

The **Bloch sphere** is a useful geometric representation of single-qubit states:

```
        |0⟩ (North Pole)
         |
        ^
        |  }
theta   |    } qubit state position
        |  }
        \/____> phi
       /      (azimuthal angle)
      /
     /
    |1⟩ (South Pole)
```

- **North Pole**: state |0⟩
- **South Pole**: state |1⟩
- **Equator**: equal superposition of |0⟩ and |1⟩

## Mathematical Representation

A general single-qubit state is:

```
|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
```

Where:

- **θ** (theta) = polar angle (0 to π)
- **φ** (phi) = azimuthal angle (0 to 2π)
- **e^(iφ)** = phase factor

## Practical Exercise

### Question 1

If a qubit is in the state:

```
|ψ⟩ = (3/5)|0⟩ + (4/5)|1⟩
```

What is the probability of measuring 0? What is the probability of measuring 1?

### Question 2

Create a normalized superposition state with 75% probability of measuring 0 and 25% probability of measuring 1.

## Next Steps

- Review Dirac notation and practice with different states
