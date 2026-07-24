"""Bell state demo: the "hello world" of quantum entanglement.

We build the simplest entangled state, |Φ+⟩ = (|00⟩ + |11⟩)/√2,
run it 1024 times on a simulator, and look at the statistics.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# --- Build the circuit -------------------------------------------------
# 2 qubits, 2 classical bits to store the measurement results.
# Both qubits start in |0⟩, so the joint state is |00⟩.
qc = QuantumCircuit(2, 2)

# Hadamard on qubit 0.
# H rotates |0⟩ into an equal superposition: (|0⟩ + |1⟩)/√2.
# The joint state is now (|00⟩ + |01⟩)/√2 — qubit 0 is "both 0 and 1
# at once" (with equal amplitude), while qubit 1 is still definitely 0.
# Note: Qiskit orders bits with qubit 0 rightmost, so |01⟩ here means
# "qubit 1 is 0, qubit 0 is 1".
qc.h(0)

# CNOT with qubit 0 as control, qubit 1 as target.
# CNOT flips the target ONLY in the branches where the control is 1.
# Applied to (|00⟩ + |01⟩)/√2 it does nothing to the |00⟩ branch
# (control is 0) and flips qubit 1 in the |01⟩ branch, giving |11⟩.
# Result: (|00⟩ + |11⟩)/√2 — the Bell state.
# The two qubits are now ENTANGLED: neither has a definite value on
# its own, but their values are perfectly correlated.
qc.cx(0, 1)

# Measure both qubits into the classical bits.
# Measurement collapses the superposition: the state randomly "picks"
# one branch, with probability = |amplitude|². Each branch here has
# amplitude 1/√2, so probability (1/√2)² = 1/2.
qc.measure([0, 1], [0, 1])

# --- Why only 00 and 11, never 01 or 10? -------------------------------
# The state before measurement is (|00⟩ + |11⟩)/√2. The outcomes 01 and
# 10 have amplitude ZERO — they simply don't exist in the state. When we
# measure, we can only land on branches that are present, so we get 00
# half the time and 11 half the time. Measuring one qubit instantly
# tells you the other's value — that correlation is entanglement.

# --- Run on the local simulator ----------------------------------------
sim = AerSimulator()
# transpile() rewrites the circuit into the gate set the backend
# understands (a no-op-ish step for a circuit this simple).
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()
counts = result.get_counts()

# --- Output -------------------------------------------------------------
print("Circuit:")
print(qc.draw(output="text"))
print()
print("Measurement counts over 1024 shots:")
for outcome in sorted(counts):
    print(f"  {outcome}: {counts[outcome]}")
print()
print("Expect roughly 50/50 between 00 and 11 — and no 01 or 10 at all.")
