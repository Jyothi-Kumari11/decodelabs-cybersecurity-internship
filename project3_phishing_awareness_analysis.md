# DecodeLabs Cyber Security Internship — Project 3
## Phishing Awareness Analysis

**Goal:** Analyze sample emails/messages to identify phishing attempts, list red flags, and explain why each message is unsafe (or safe).

---

## 1. Triage Toolkit — Non-Expert Checklist

Use this checklist on any incoming email or message before clicking, replying, or acting on it:

1. **Sender check** — Does the display name match the actual email address/domain? (Expand the sender field, don't trust the display name alone.)
2. **Domain check** — Is the domain spelled correctly? Watch for typosquatting (`amaz0n.com`), extra words (`yourcompany-secure-login.com`), or long nested subdomains hiding the real root domain.
3. **Urgency/emotion check** — Does the message pressure you with urgency, fear, authority, curiosity, or a reward?
4. **Link check** — Hover over links (without clicking) to see the true destination URL. Does it match the claimed sender?
5. **Attachment check** — Are there unexpected attachments, especially with extensions like `.iso`, `.js`, `.scr`, or `.html`?
6. **Request check** — Is it asking for a password, MFA code, payment change, or a bypass of normal procedure?
7. **Grammar/formatting check** — Are there inconsistencies, odd spacing, or mismatched fonts/logos?
8. **Verification check** — Can this be confirmed through a separate, known channel (e.g., calling a verified phone number)?

**Decision outcome:**
- **Safe → Close** (no action needed, or proceed normally)
- **Suspicious → Warn User** (flag internally, don't click, verify via separate channel)
- **Malicious → Block & Escalate** (report to security team, do not interact further)

---

## 2. Sample Message Analysis

Below are five sample messages (written for training purposes) analyzed using the checklist above.

### Sample 1 — "IT Password Expiry" Email

> From: IT Support Team <it-support@decodelabs-secure.com>
> Subject: URGENT: Your password expires in 2 hours
>
> Dear User,
> Your account password will expire today. Click the link below immediately to keep access to your account:
> http://decodelabs.tech.password-renew-portal.net/login
> Failure to act will result in permanent account lockout.
> IT Support Team

**Red flags identified:**
- **Sender-domain mismatch**: claims to be DecodeLabs IT, but the domain is `decodelabs-secure.com`, not the real company domain.
- **Urgency/fear trigger**: "2 hours," "permanent lockout" — designed to short-circuit careful thinking.
- **Subdomain trap in the link**: `decodelabs.tech` appears to be a subdomain of the real attacker-owned root domain `password-renew-portal.net` (read right to left to find the true root).
- **Generic greeting**: "Dear User" instead of the recipient's actual name.

**Verdict:** **Malicious → Block & Escalate.** This is a credential-harvesting phishing attempt using urgency and a spoofed/lookalike domain.

---

### Sample 2 — Routine Project Update (Legitimate)

> From: Sarah Lee <sarah.lee@decodelabs.tech>
> Subject: Q3 Project Status Update – Non-Urgent
>
> Hi team,
> Please review the attached project status document at your earliest convenience. No immediate action is required.
> Thanks,
> Sarah

**Analysis:**
- Sender domain matches the legitimate company domain.
- No urgency, no unusual request, no suspicious link or attachment type.
- Tone and content are consistent with normal internal communication.

**Verdict:** **Safe → Close.** No red flags present.

---

### Sample 3 — "CEO" Wire Transfer Request (Business Email Compromise)

> From: CEO – Strictly Confidential <ceo.urgent@executive-update.com>
> Subject: IMMEDIATE ACTION REQUIRED: Transfer Authorization
>
> Process the attached wire transfer instruction immediately. This is critical and must remain strictly confidential. Do not discuss with anyone. Bypass standard procedure.
> Thank you.

**Red flags identified:**
- **Authority impersonation**: pretends to be the CEO to demand unquestioned compliance.
- **Urgency**: "immediately," "IMMEDIATE ACTION REQUIRED."
- **Secrecy demand**: "strictly confidential," "do not discuss with anyone" — a classic isolation tactic to prevent verification.
- **Bypass request**: explicitly asks to skip normal approval procedure.
- **Sender domain**: not the company's real domain, and CEOs rarely email finance staff directly for wire transfers outside standard process.

**Verdict:** **Malicious → Block & Escalate.** Textbook Business Email Compromise (BEC) / whaling attempt. Any such request should be verified by phone through a known, independently-sourced number — never by replying to the email.

---

### Sample 4 — SMS "Package Delivery" Smishing

> Text message: "Your package could not be delivered. Update your address here: bit.ly/pkg-redelvry2026 — reply STOP to opt out."

**Red flags identified:**
- **Unsolicited link via SMS** (smishing), often timed around shopping seasons.
- **Shortened URL** hides the true destination, making it impossible to verify the domain before clicking.
- **Generic message** with no order number, courier name, or recipient name.
- **Slight misspelling** ("redelvry") — a common evasion tactic to dodge spam filters.

**Verdict:** **Suspicious → Warn User** (treat as malicious in practice; do not click). Users should navigate directly to the courier's official app/site to check delivery status instead.

---

### Sample 5 — QR Code "Account Recovery" Poster (Quishing)

> Physical flyer posted near an office printer: "Scan to verify your Google Workspace account and avoid lockout." (QR code image, no additional text)

**Red flags identified:**
- **Unsolicited QR code** demanding a scan — a hallmark of "quishing."
- **No verifiable sender** — a poster has no email header or domain to check.
- **Bypasses desktop URL filters** by pushing the user to scan with an unmanaged mobile device.
- **Vague, generic claim** ("avoid lockout") designed to trigger fear without specifics.

**Verdict:** **Malicious → Block & Escalate.** Report the physical poster to building security/IT; do not scan.

---

## 3. Summary Decision Tree

```
Incoming Message
      │
      ▼
Sender & domain match? ──No──► MALICIOUS → Block & Escalate
      │Yes
      ▼
Urgency / fear / authority / secrecy present? ──Yes──► SUSPICIOUS → Warn User → Verify via separate channel
      │No
      ▼
Unexpected link/attachment/request? ──Yes──► SUSPICIOUS → Warn User
      │No
      ▼
SAFE → Close
```

## 4. Key Takeaway

Phishing exploits the gap between a technical control and a human reaction. Every red flag above maps to a cognitive trigger — urgency, authority, curiosity, or fear/greed — designed to make someone act before they verify. The **Pause → Verify → Report** habit closes that gap, regardless of how the attack is delivered (email, SMS, QR code, or voice).
