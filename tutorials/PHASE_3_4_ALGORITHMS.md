# PHASE 3 & 4: QUANTUM ALGORITHMS (Weeks 5-12)

## PHASE 3: Essential Algorithms (Weeks 5-8)

### Overview
Learn the fundamental quantum algorithms that demonstrate quantum advantage.

### Topic 5: Deutsch Algorithm (Week 5)

**Problem**: Given a function f: {0,1} → {0,1}, determine if it's constant or balanced

**Classical**: O(2) calls
**Quantum**: O(1) call

**Circuit**:
```
|0⟩ ──[H]──●──[H]──[M]
           │
|1⟩ ──[H]──X──────

Oracle: U_f
```

**Key Insight**: Hadamard-Oracle-Hadamard pattern amplifies phase differences

### Topic 6: Deutsch-Jozsa Algorithm (Week 5-6)

**Problem**: Determine if n-bit function is constant or balanced
**Classical**: O(2^(n-1))
**Quantum**: O(1)

**Extension**:
- n input qubits in superposition
- 1 auxiliary qubit
- n Hadamards at start and end
- Polynomial speedup

### Topic 7: Grover's Search Algorithm (Week 6-7)

**Problem**: Search unsorted database of N items for marked element
**Classical**: O(N)
**Quantum**: O(√N)  ← Quadratic speedup

**Key Components**:
```
1. Initialize: Equal superposition
2. Oracle: Marks solution |sol⟩ → -|sol⟩
3. Diffusion: Amplifies amplitude
4. Repeat ~√N times
```

**Operations**:
- Hadamard: Create superposition
- Oracle: Phase kick-back
- Diffusion Operator: Amplitude amplification
- Measurement: Get solution

### Topic 8: Simon's Algorithm (Week 7-8)

**Problem**: Find hidden period s in function f(x) = f(x ⊕ s)
**Classical**: Exponential
**Quantum**: Polynomial

**Method**:
- Create equal superposition
- Apply oracle: |x⟩|f(x)⟩
- Measure second register
- Measure first register → orthogonal to s
- Repeat to find s

---

## PHASE 4: Advanced Algorithms (Weeks 9-12)

### Overview
Advanced algorithms with practical applications and deeper quantum mechanics.

### Topic 9: Shor's Algorithm (Week 9-10)

**Problem**: Factor large integer N = p × q
**Classical**: O(2^(n^(1/3)))
**Quantum**: O(n^3) ← Exponential speedup

**Significance**: Breaks RSA encryption

**Components**:
```
1. Classical: Reduce to period finding
2. Quantum: Find period efficiently
   - Phase estimation
   - Quantum Fourier Transform (QFT)
3. Classical: Extract factors
```

**Quantum Fourier Transform**:
- Exponential speedup in certain computations
- Core of Shor's algorithm
- Maps |x⟩ to |x̃⟩ (frequency domain)

### Topic 10: Quantum Phase Estimation (Week 10-11)

**Problem**: Given unitary U and state |ψ⟩, find eigenphase θ

**Method**:
- Controlled unitary operations
- QFT on control qubits
- Measurement gives θ in binary

**Applications**:
- Finding ground state energies
- Part of many quantum algorithms

### Topic 11: Variational Quantum Eigensolver (VQE) (Week 11)

**Problem**: Find ground state energy of molecule
**Type**: Hybrid classical-quantum

**Algorithm**:
```
1. Quantum: Prepare ansatz state
2. Quantum: Measure expectation value
3. Classical: Optimize parameters
4. Repeat until convergence
```

**Applications**:
- Drug discovery
- Materials simulation
- Energy optimization

### Topic 12: Quantum Approximate Optimization Algorithm (QAOA) (Week 12)

**Problem**: Find approximate solution to combinatorial optimization

**Examples**:
- MaxCut: Maximize edge cuts
- Traveling Salesman
- Graph coloring

**Structure**:
```
Problem Hamiltonian: H_p
Mixer Hamiltonian: H_m

U = e^(-iγH_p)e^(-iβH_m)

Vary γ, β to maximize objective
```

---

## Complexity Comparison

| Algorithm | Problem | Classical | Quantum | Factor |
|-----------|---------|-----------|---------|--------|
| Deutsch | Function type | O(2) | O(1) | 2× |
| Deutsch-Jozsa | n-bit function | O(2^(n-1)) | O(1) | Exponential |
| Grover | Search N items | O(N) | O(√N) | √N |
| Simon | Find period | Exponential | Polynomial | Exponential |
| Shor | Factor integer | O(e^(n^1/3)) | O(n^3) | Exponential |

---

## Implementation Strategy

### Phase 3 Implementation
1. Start with Deutsch algorithm
2. Extend to Deutsch-Jozsa
3. Implement Grover's algorithm
4. Study Simon's algorithm
5. Practice oracle construction

### Phase 4 Implementation
1. Understand quantum circuits deeply
2. Implement QFT
3. Build Shor's algorithm components
4. Study hybrid quantum-classical algorithms
5. Experiment with NISQ algorithms

---

## Critical Concepts

### Phase Kick-Back
Using auxiliary qubit to encode function output as phase
```
|x⟩|0⟩ → U_f → |x⟩|f(x)⟩
Phase: (-1)^f(x) |x⟩
```

### Amplitude Amplification
Core technique in Grover's algorithm
- Oracle marks solution
- Diffusion amplifies marked amplitude
- Repeat ~√N times
- Measure to get solution

### Quantum Parallelism
- Superposition allows simultaneous evaluation
- Not exploited by all quantum algorithms
- Requires interference for advantage

---

## Resources

### Key Papers
- Deutsch (1985): Deutsch Algorithm
- Deutsch & Jozsa (1992): Generalization
- Grover (1996): Search Algorithm
- Simon (1994): Hidden Subgroup
- Shor (1994): Factoring Algorithm

### Implementations
- IBM Qiskit: Algorithm tutorials
- CircQ by Google: Advanced implementations
- PennyLane: Hybrid algorithms

---

## Summary

### Phase 3 Skills
- [ ] Understand oracle construction
- [ ] Implement Deutsch algorithm
- [ ] Extend to Deutsch-Jozsa
- [ ] Build Grover's algorithm
- [ ] Analyze Simon's algorithm
- [ ] Recognize quantum advantage

### Phase 4 Skills
- [ ] Implement QFT
- [ ] Build phase estimation
- [ ] Understand Shor's algorithm
- [ ] Design VQE circuits
- [ ] Construct QAOA ansatz
- [ ] Optimize hybrid algorithms

---

## Practice Problems

1. Implement Deutsch oracle for f(x) = x
2. Extend Grover to 3-qubit search
3. Build QFT for 4-qubit system
4. Implement VQE for H2 molecule
5. Design QAOA circuit for MaxCut

---

## Milestones

- Week 5-6: Deutsch & DJ algorithms working
- Week 6-7: Grover algorithm optimized
- Week 8: Simon algorithm understood
- Week 9-10: Shor components implemented
- Week 11-12: Hybrid algorithms functional

After Phase 4, you'll be ready for:
- Research in quantum algorithms
- Industry quantum computing roles
- Advanced quantum machine learning
