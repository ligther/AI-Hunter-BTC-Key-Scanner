# AI-Hunter BTC Key Scanner

This project is a high-performance Bitcoin private key scanner written in Python. It compares randomly generated keys against a target list of Bitcoin addresses.

## Features
- Multi-core scanning with `multiprocessing`
- Live statistics (speed, attempts, hits)
- Saves matched keys to `found.txt`
- Avoids re-checking keys (uses `checked.txt`)
- Lightweight and easy to run on Linux

## Requirements
- Python 3.x
- `ecdsa` package

Install with:
```bash
pip install ecdsa
```

## Usage

1. Add target addresses (one per line) to `addresses.txt`
2. Run the scanner:
```bash
python3 finder.py
```

## File Outputs
- `found.txt` – stores addresses and matching private keys
- `checked.txt` – keeps a log of all scanned private keys

## License
MIT License