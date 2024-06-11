# zkSync Allocation Checker

Quick Python script to check ZK allocations across many wallets.

## Requirements

1. Python (>=3.11; <4)
2. Poetry (optional)

## Usage

### Clone Repo

```bash
git clone https://github.com/vile/zksync-allocation-chcker.git
```

**Or download ZIP via HTTPS**.

### Include your wallets

List all of the wallets you want to check in `wallets.txt`.
Each line consists of a single wallet.

E.g.
```
0x0000000000000000000000000000000000000001
0x0000000000000000000000000000000000000002
0x0000000000000000000000000000000000000003
0x0000000000000000000000000000000000000004
```

### Quick Start

Make (install dependencies, start script):
```bash
make
```

### Install Requirements

If using Poetry:
```bash
poetry install --no-root
```

If using Pip:
```bash
pip install -r requirements.txt
```

### Start Script

Using Makefile:
```bash
make start
```

Invoke with Python:
```bash
python3 main.py
```