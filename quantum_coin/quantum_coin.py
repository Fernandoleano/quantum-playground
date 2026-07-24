"""Quantum coin flip: a true random bit generator.

A Hadamard gate puts one qubit into an equal superposition
(|0⟩ + |1⟩)/√2. Measuring it collapses to 0 or 1 with exactly 50%
probability each. On real quantum hardware this randomness is
fundamental physics, not an algorithm — unlike classical PRNGs,
there is no seed and no pattern to predict.

(On the AerSimulator the collapse is emulated with a classical PRNG,
but the circuit itself is the real thing: run it on an actual quantum
computer and you get genuinely unpredictable bits.)
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

_sim = AerSimulator()


def _coin_circuit() -> QuantumCircuit:
    """One qubit: Hadamard, then measure. That's the whole coin."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)          # |0⟩ -> (|0⟩ + |1⟩)/√2: perfectly balanced coin
    qc.measure(0, 0) # collapse: 0 or 1, each with probability 1/2
    return qc


def random_bit() -> int:
    """Flip the quantum coin once (1 shot) and return 0 or 1."""
    compiled = transpile(_coin_circuit(), _sim)
    result = _sim.run(compiled, shots=1).result()
    # With shots=1 the counts dict has exactly one key: "0" or "1".
    outcome = next(iter(result.get_counts()))
    return int(outcome)


def random_bits(n: int) -> list[int]:
    """Return n random bits, one circuit run per bit."""
    return [random_bit() for _ in range(n)]


if __name__ == "__main__":
    bits = random_bits(16)
    print("16 quantum coin flips:", "".join(map(str, bits)))
    print(f"ones: {sum(bits)}, zeros: {len(bits) - sum(bits)}")
