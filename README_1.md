# Cyber Security Internship — DecodeLabs (2026)

This repository contains my project submissions for the Cyber Security Internship at **DecodeLabs**, completed as part of the Industrial Training Kit (Batch 2026).

> 🔗 [www.decodelabs.tech](https://www.decodelabs.tech)

## About the Internship

- **Role:** Cyber Security Intern
- **Track:** Cyber Security
- **Mode:** Remote / Virtual
- **Focus:** Hands-on, project-based learning covering defensive security logic, cryptography fundamentals, and social engineering / phishing awareness.

Each project builds toward a broader theme: **closing the gap between technical controls and human error** — starting with securing user credentials, moving to protecting data in transit, and finishing with defending against social engineering attacks.

---

## 📁 Projects

### Project 1 — Password Strength Checker 🔐
**File:** [`project1_password_strength_checker.py`](./project1_password_strength_checker.py)

A Python program that evaluates password strength (Weak / Medium / Strong) based on:
- Length (minimum 8, preferred 12+ characters)
- Presence of uppercase, lowercase, digits, and symbols
- A check against a small list of common/leaked passwords

**Key skills:** string handling, conditional logic, security fundamentals.

```bash
python3 project1_password_strength_checker.py
```

---

### Project 2 — Basic Encryption & Decryption (Caesar Cipher) 🔑
**File:** [`project2_caesar_cipher.py`](./project2_caesar_cipher.py)

Implements a classic Caesar cipher to encrypt and decrypt text using modular arithmetic:

```
Encryption: E(x) = (x + shift) mod 26
Decryption: D(x) = (x - shift) mod 26
```

Includes an interactive mode, a self-test, and an optional brute-force demonstration showing why a 25-key cipher offers minimal real-world security.

**Key skills:** encryption concepts, `ord()`/`chr()` logic, modular arithmetic.

```bash
python3 project2_caesar_cipher.py
```

---

### Project 3 — Phishing Awareness Analysis 🎣
**File:** [`project3_phishing_awareness_analysis.md`](./project3_phishing_awareness_analysis.md)

A written threat-analysis report covering:
- A non-expert **triage checklist** for evaluating suspicious messages
- Five analyzed sample messages (phishing emails, BEC/whaling, smishing, quishing, and one legitimate control email)
- A **decision tree** (Safe → Close / Suspicious → Warn User / Malicious → Block & Escalate)

**Key skills:** threat analysis, social engineering awareness, security triage.

---

## 🛠 Tech Stack
- Python 3
- Markdown (for documentation/reporting)

## 📌 Notes
These projects were built as part of a structured internship curriculum designed to build practical, portfolio-ready cyber security skills — from defensive logic, to cryptography, to human-layer threat detection.
