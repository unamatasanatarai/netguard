# NetGuard Key Generator

Generate authentication keys from a NetGuard challenge code — available as a web UI, Python script, and Bash script.

🌐 **Online version**: https://unamatasanatarai.github.io/netguard-key-generator/

---

## What it does

NetGuard devices issue a challenge code during authentication. This tool derives the possible response keys by computing:

```
MD5(challenge + "NetGuard3")  →  v3 key
MD5(challenge + "NetGuard2")  →  v2 key
```

---

## Usage

### Web UI (`index.html`)

Open `index.html` in any browser, or use the hosted version above.

- Paste or type your challenge code — keys and QR codes generate instantly
- Click the hash to select all text
- Use the **⧉** button to copy to clipboard

### Python (`netguard_keygen.py`)

```bash
python3 netguard_keygen.py <challenge_code>
```

**Example:**
```bash
python3 netguard_keygen.py 784019874562340ghjsfdk
```

**Output:**
```
Possible keys:
a1b2c3d4e5f6...   ← v3
9f8e7d6c5b4a...   ← v2
```

**Help:**
```bash
python3 netguard_keygen.py --help
```

### Bash (`netguard_keygen.sh`)

```bash
./netguard_keygen.sh <challenge_code>
```

Works on macOS (`md5`) and Linux (`md5sum`). No dependencies required.

**Example:**
```bash
./netguard_keygen.sh 784019874562340ghjsfdk
```

---

## Files

| File | Description |
|---|---|
| `index.html` | Self-contained web UI with live key generation and QR codes |
| `netguard_keygen.py` | CLI key generator (Python 3, no extra dependencies) |
| `netguard_keygen.sh` | CLI key generator (Bash, macOS & Linux compatible) |
