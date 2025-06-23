# 🔓 Brute Force ZIP Password Cracker

A simple Python tool to perform a brute-force attack on a password-protected ZIP file using a wordlist.

## 📌 Features

- Uses Python's built-in `zipfile` module — no external dependencies (except for optional progress bar)
- Supports any ZIP file with a standard password-based lock
- Wordlist-based brute-force attack
- Optional progress bar using `tqdm`

## ⚙️ Requirements

- Python 3.x
- `tqdm` (for progress bar — optional)

Install `tqdm` via pip:

```bash
pip install tqdm