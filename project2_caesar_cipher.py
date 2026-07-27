"""
DecodeLabs Cyber Security Internship - Project 2
Basic Encryption & Decryption (Caesar Cipher)

Goal:
    Implement a simple encryption and decryption technique.

Key Requirements:
    - Encrypt user text using a basic logic (Caesar cipher)
    - Decrypt the encrypted text
    - Display both encrypted and decrypted output

Key Skills:
    Encryption concepts, logic building, data protection basics

Math (IPO Model):
    Encryption: E(x) = (x + shift) % 26
    Decryption: D(x) = (x - shift) % 26

Non-alphabetic characters (spaces, punctuation, digits) are left unchanged,
so message structure/readability of ciphertext punctuation is preserved,
while letters are shifted.
"""


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using a Caesar cipher with the given integer shift."""
    result = []
    shift = shift % 26  # normalize shift so it always falls within 0-25

    for char in text:
        if char.isupper():
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        elif char.islower():
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Leave numbers, spaces, and punctuation untouched
            result.append(char)

    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt text that was encrypted using caesar_encrypt with the same shift."""
    # Decryption is just encryption with the negative shift
    return caesar_encrypt(ciphertext, -shift)


def brute_force_all_shifts(ciphertext: str) -> None:
    """
    Educational helper: demonstrates WHY the Caesar cipher is a 'lockbox, not a vault'.
    Since there are only 25 possible shifts, an attacker can try them all instantly.
    """
    print("\n--- Brute Force Demonstration (all 25 possible shifts) ---")
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {caesar_decrypt(ciphertext, shift)}")
    print("------------------------------------------------------------\n")


def main():
    print("DecodeLabs Caesar Cipher Tool\n")

    message = input("Enter the message to encrypt: ")

    while True:
        shift_input = input("Enter shift key (integer, e.g. 3): ")
        try:
            shift = int(shift_input)
            break
        except ValueError:
            print("Please enter a valid whole number.")

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\n--- Result ---")
    print(f"Original message : {message}")
    print(f"Shift key        : {shift}")
    print(f"Encrypted text   : {encrypted}")
    print(f"Decrypted text   : {decrypted}")
    print(f"Match original?  : {decrypted == message}")
    print("--------------\n")

    show_demo = input("Show brute-force demonstration of this ciphertext? (y/n): ").strip().lower()
    if show_demo == "y":
        brute_force_all_shifts(encrypted)


if __name__ == "__main__":
    # Quick automated self-test so the logic can be verified without manual input
    print("=== SELF-TEST ===")
    test_message = "Hello, DecodeLabs! Project 2026."
    test_shift = 3
    enc = caesar_encrypt(test_message, test_shift)
    dec = caesar_decrypt(enc, test_shift)
    print(f"Original : {test_message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
    print(f"Success  : {dec == test_message}\n")

    print("=== INTERACTIVE MODE ===")
    main()
