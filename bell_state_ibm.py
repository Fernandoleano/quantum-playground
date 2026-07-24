"""Bell state on REAL IBM quantum hardware.

Same circuit as bell_state.py — only the backend changes. Instead of
simulating on your CPU, the circuit is sent to IBM's cloud, queued,
and executed on actual superconducting qubits.

Setup:
  1. Create a free account at https://quantum.ibm.com
  2. Copy your API token (Account Settings -> API token)
  3. Put it in the .env file in this directory:
       IBM_QUANTUM_TOKEN=your_real_token_here
     (.env is gitignored — the token never leaves your machine.)

Expect different results than the simulator: real hardware is noisy,
so a few 01/10 counts WILL appear. That gap between theory and
hardware is the central engineering problem of quantum computing.
"""

import os
import sys
from pathlib import Path

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2


def load_token() -> str:
    """Read IBM_QUANTUM_TOKEN from the environment or the local .env file."""
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if not token:
        env_file = Path(__file__).parent / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line.startswith("IBM_QUANTUM_TOKEN="):
                    token = line.split("=", 1)[1].strip()
    if not token:
        sys.exit("No token found. Set IBM_QUANTUM_TOKEN in .env — see docstring.")
    return token


def build_bell() -> QuantumCircuit:
    """Identical circuit to bell_state.py: H then CNOT then measure."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def main() -> None:
    token = load_token()

    # Connect to IBM Quantum. This validates the token over the network.
    print("Connecting to IBM Quantum...")
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token=token)

    # Pick the least-busy real device (not a cloud simulator).
    backend = service.least_busy(operational=True, simulator=False)
    print(f"Selected backend: {backend.name} ({backend.num_qubits} qubits)")

    # Transpile matters here: the circuit must be rewritten into the
    # device's native gate set and mapped onto physically connected qubits.
    qc = build_bell()
    compiled = transpile(qc, backend)

    # Submit the job. Real devices have a queue — this can take minutes.
    print("Submitting job (may queue behind other users)...")
    sampler = SamplerV2(mode=backend)
    job = sampler.run([compiled], shots=1024)
    print(f"Job ID: {job.job_id()}")

    result = job.result()
    counts = result[0].data.c.get_counts()

    print()
    print("Counts from real quantum hardware:")
    for outcome in sorted(counts):
        print(f"  {outcome}: {counts[outcome]}")
    print()
    print("Note the small 01/10 counts — that's real hardware noise.")


if __name__ == "__main__":
    main()
