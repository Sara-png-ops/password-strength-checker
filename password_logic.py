
import re
import secrets
import string

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome",
    "iloveyou", "abc123"
}


def normalize_password(password):
    substitutions = str.maketrans({
        "@": "a",
        "0": "o",
        "$": "s",
        "1": "i",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t"
    })

    normalized = password.lower().translate(substitutions)
    return re.sub(r"[^a-z]", "", normalized)


def looks_common(password):
    normalized = normalize_password(password)

    return (
        password.lower() in COMMON_PASSWORDS
        or normalized in COMMON_PASSWORDS
        or "password" in normalized
        or "qwerty" in normalized
        or "admin" in normalized
    )


def check_password(password):
    if not password:
        return 0, "EMPTY", []

    score = 0
    feedback = []

    checks = [
        (len(password) >= 8, 20, "Use at least 8 characters."),
        (len(password) >= 12, 10, "Use 12 or more characters."),
        (bool(re.search(r"[a-z]", password)), 15, "Add lowercase letters."),
        (bool(re.search(r"[A-Z]", password)), 15, "Add uppercase letters."),
        (bool(re.search(r"\d", password)), 15, "Add numbers."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), 15, "Add symbols.")
    ]

    for passed, points, message in checks:
        if passed:
            score += points
        else:
            feedback.append(message)

    common = looks_common(password)

    if common:
        score = min(score, 20)
        feedback.append("Avoid common or predictable passwords.")

    if re.search(r"(.)\1{2,}", password):
        score = max(0, score - 15)
        feedback.append("Avoid repeating characters.")

    if re.search(r"1234|2345|3456|abcd|qwer", password.lower()):
        score = max(0, score - 15)
        feedback.append("Avoid predictable sequences.")

    if common:
        strength = "VERY WEAK"
    elif score >= 80:
        strength = "VERY STRONG"
    elif score >= 60:
        strength = "STRONG"
    elif score >= 40:
        strength = "MODERATE"
    elif score > 0:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"

    return score, strength, feedback


def generate_secure_password(length=16):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+"
    ]

    password = [secrets.choice(group) for group in groups]
    all_characters = "".join(groups)

    password.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password))
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

