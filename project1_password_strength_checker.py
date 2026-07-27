"""
DecodeLabs Cyber Security Internship - Project 1
Password Strength Checker

Goal:
    Create a program that checks whether a password is weak, medium, or strong.

Key Requirements:
    - Check password length
    - Check use of numbers, symbols, and uppercase letters
    - Display password strength result

Key Skills:
    String handling, condition checks, security basics
"""

import string
import getpass


# A small list of extremely common passwords, used to flag obviously weak choices
# even if they technically satisfy length/character rules (e.g. "Password1!").
COMMON_PASSWORDS = {
    "password", "password1", "123456", "12345678", "qwerty",
    "letmein", "admin123", "welcome1", "iloveyou", "abc12345",
}


def check_password_strength(password: str) -> dict:
    """
    Analyze a password and return a dictionary containing:
        - individual rule checks (booleans)
        - a numeric score
        - a final strength label: Weak / Medium / Strong
        - human-readable feedback tips
    """

    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    is_common = password.lower() in COMMON_PASSWORDS

    # --- Length checks ---
    length_ok_min = length >= 8          # minimum acceptable length
    length_ok_strong = length >= 12       # preferred length for strong passwords

    # --- Scoring system ---
    # Each satisfied condition adds a point. Max possible score = 6
    score = 0
    if length_ok_min:
        score += 1
    if length_ok_strong:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Common/leaked passwords are heavily penalized regardless of score
    if is_common:
        score = 0

    # --- Classify strength ---
    if not length_ok_min or is_common:
        strength = "Weak"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # --- Build feedback tips ---
    feedback = []
    if not length_ok_min:
        feedback.append("Use at least 8 characters.")
    elif not length_ok_strong:
        feedback.append("Consider using 12+ characters for stronger security.")
    if not has_upper:
        feedback.append("Add at least one uppercase letter (A-Z).")
    if not has_lower:
        feedback.append("Add at least one lowercase letter (a-z).")
    if not has_digit:
        feedback.append("Add at least one number (0-9).")
    if not has_symbol:
        feedback.append("Add at least one special symbol (e.g. !@#$%).")
    if is_common:
        feedback.append("This password appears in common/leaked password lists. Avoid it entirely.")
    if not feedback:
        feedback.append("Great job! This password meets all recommended criteria.")

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "is_common": is_common,
        "score": score,
        "strength": strength,
        "feedback": feedback,
    }


def print_report(password: str, result: dict) -> None:
    masked = password[0] + "*" * (len(password) - 1) if password else ""
    print("\n--- Password Strength Report ---")
    print(f"Password (masked): {masked}")
    print(f"Length: {result['length']}")
    print(f"Contains uppercase letter : {result['has_upper']}")
    print(f"Contains lowercase letter : {result['has_lower']}")
    print(f"Contains digit            : {result['has_digit']}")
    print(f"Contains symbol           : {result['has_symbol']}")
    print(f"Is a common/leaked value  : {result['is_common']}")
    print(f"Score: {result['score']} / 6")
    print(f"Strength: {result['strength'].upper()}")
    print("Feedback:")
    for tip in result["feedback"]:
        print(f"  - {tip}")
    print("---------------------------------\n")


def main():
    print("DecodeLabs Password Strength Checker")
    print("(Input is hidden while typing)\n")

    try:
        password = getpass.getpass("Enter a password to check: ")
    except Exception:
        # Fallback for environments where getpass isn't supported (e.g. some IDEs)
        password = input("Enter a password to check: ")

    if not password:
        print("No password entered. Exiting.")
        return

    result = check_password_strength(password)
    print_report(password, result)


if __name__ == "__main__":
    # Demo run with sample passwords, useful for grading/testing without manual input
    demo_passwords = ["abc", "password1", "Passw0rd", "Tr0ub4dor&3", "correcthorsebatterystaple99!"]
    print("=== DEMO MODE: Testing sample passwords ===")
    for pw in demo_passwords:
        res = check_password_strength(pw)
        print_report(pw, res)

    print("=== INTERACTIVE MODE ===")
    main()
