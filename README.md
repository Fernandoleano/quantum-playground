# ⚛️ Quantum Playground — Learning Qiskit

A hands-on sandbox for learning quantum computing with [Qiskit](https://www.ibm.com/quantum/qiskit)
on macOS (Apple Silicon). Everything runs locally on the Aer simulator —
no cloud account needed.

## Setup

The virtual environment lives in `.venv` (Python 3.13). Activate it:

```bash
source .venv/bin/activate
```

If you're setting up from scratch (e.g. after cloning):

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Deactivate anytime with `deactivate`.

## Scripts

### `bell_state.py` — entanglement demo

```bash
python bell_state.py
```

Builds the Bell state (|00⟩ + |11⟩)/√2 with a Hadamard + CNOT, measures
1024 times. **Expected output:** an ASCII circuit diagram, then counts
that are roughly 50/50 between `00` and `11` (e.g. `00: 510, 11: 514`).
You will **never** see `01` or `10` — those outcomes have zero amplitude
in the entangled state. The exact split varies run to run; that's
quantum measurement statistics, not a bug.

### `quantum_coin.py` — true random bit generator

```bash
python quantum_coin.py
```

Flips a "quantum coin" 16 times: one qubit, Hadamard, measure, 1 shot
per bit. **Expected output:** a 16-character bitstring like
`0110100111010010` plus a ones/zeros tally. Different every run.

Use it from your own code:

```python
from quantum_coin import random_bit, random_bits

random_bit()      # 0 or 1
random_bits(8)    # e.g. [1, 0, 0, 1, 1, 0, 1, 0]
```

## Jupyter

Jupyter is installed for interactive experimenting:

```bash
jupyter notebook
```

Inside a notebook you can draw circuits graphically
(`qc.draw("mpl")` — matplotlib is installed too) and plot histograms
with `qiskit.visualization.plot_histogram(counts)`.

## Key concepts in 30 seconds

- **Qubit**: like a bit, but can be in a *superposition* — a weighted
  blend of 0 and 1 — until measured.
- **Hadamard (H)**: turns |0⟩ into an equal 50/50 superposition.
- **CNOT (cx)**: flips the target qubit only when the control is 1;
  applied after H it creates *entanglement*.
- **Entanglement**: qubits whose outcomes are correlated — measuring
  one instantly determines the other, even though each alone is random.
- **Measurement**: collapses superposition to a definite 0/1, with
  probability equal to the amplitude squared.
