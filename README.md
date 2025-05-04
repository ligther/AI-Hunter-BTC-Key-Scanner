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



☕ Support This Project

If you find this project useful or interesting, consider supporting it with a small tip — it helps keep the development going!

💰 Bitcoin (BTC) Address:
1MPGytt78v9xR74b9qgPkfKUjTeWPuw8AK

USDT
TB6VpfxQN9hzitMDQxw4kxs4wqAGdyEahG
Other ways to support:

⭐ Star this repository

🗣 Share it with others

🧠 Contribute improvements or feedback
