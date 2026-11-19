
import re
import secrets
import string

COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin123",
    "welcome123",
    "letmein",
    "iloveyou",
    "abc123",
    "monkey",
    "dragon",
    "football",
    "sunshine",
    "princess",
    "login",
    "passw0rd",
}

SYMBOLS = "!@#$%^&*()_+-=[]{}"

def looks_common(password):
    lowered = password.lower()

    # Detect common passwords with numbers or symbols added
    simplified = re.sub(r"[0-9!@#$%^&*()_+\-=\[\]{}.,?]", "", lowered)

    substitutions = str.maketrans({
        "@": "a",
        "4": "a",
        "3": "e",
        "1": "i",
        "!": "i",
        "0": "o",
        "$": "s",
        "5": "s",
        "7": "t",
    })

    normalized = lowered.translate(substitutions)

    return (
        lowered in COMMON_PASSWORDS
        or simplified in COMMON_PASSWORDS
        or normalized in COMMON_PASSWORDS
    )


def check_password(password):
    score = 0
    suggestions = []

    if not password:
        return 0, "NO PASSWORD", ["Enter a password to check."]

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 10
    else:
        suggestions.append("Use at least 12 characters for better security.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append("Add special characters.")

    if looks_common(password):
        score = min(score, 20)
        suggestions.append("Avoid common or predictable passwords.")

    if re.search(r"(.)\1\1", password):
        score = max(0, score - 10)
        suggestions.append("Avoid repeated characters.")

    sequences = [
        "1234", "2345", "3456", "4567",
        "5678", "6789", "abcd", "qwerty",
        "asdf", "zxcv"
    ]

    if any(sequence in password.lower() for sequence in sequences):
        score = max(0, score - 15)
        suggestions.append("Avoid predictable keyboard or number sequences.")

    if score < 30:
        strength = "VERY WEAK"
    elif score < 50:
        strength = "WEAK"
    elif score < 70:
        strength = "MEDIUM"
    elif score < 90:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, suggestions


def generate_secure_password(length=16):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    pools = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        SYMBOLS
    ]

    all_characters = "".join(pools)

    password_characters = [
        secrets.choice(pool) for pool in pools
    ]

    password_characters += [
        secrets.choice(all_characters)
        for _ in range(length - len(password_characters))
    ]

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)
