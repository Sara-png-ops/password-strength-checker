import tkinter as tk
from tkinter import ttk
import re
import random
import string

# ---------- COMMON PASSWORDS ----------
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
    "iloveyou"
}


# ---------- FUNCTIONS ----------

def check_password(event=None):
    password = entry.get()
    score = 0
    suggestions = []

    if not password:
        strength_label.config(
            text="Strength:",
            foreground="black"
        )
        progress["value"] = 0
        suggestion_label.config(text="")
        score_label.config(text="Score: 0/5")
        return

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        strength_label.config(
            text="Strength: Very Weak",
            foreground="red"
        )
        progress["value"] = 0
        score_label.config(text="Score: 0/5")
        suggestion_label.config(
            text="⚠️ This is a commonly used password.\n"
                 "Please choose a more unique password."
        )
        return

    # Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("• Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("• Add an uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("• Add a lowercase letter")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("• Add a number")

    # Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("• Add a special character")

    progress["value"] = score
    score_label.config(text=f"Score: {score}/5")

    # Strength
    if score <= 2:
        result = "Weak"
        color = "red"
    elif score <= 4:
        result = "Medium"
        color = "orange"
    else:
        result = "Strong"
        color = "green"

    strength_label.config(
        text=f"Strength: {result}",
        foreground=color
    )

    if suggestions:
        suggestion_label.config(
            text="\n".join(suggestions)
        )
    else:
        suggestion_label.config(
            text="Excellent Password!"
        )


def generate_password():
    # Guarantee every required character type
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining = 8
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password_chars = [
        uppercase,
        lowercase,
        number,
        special
    ]

    password_chars += [
        random.choice(characters)
        for _ in range(remaining)
    ]

    random.shuffle(password_chars)

    password = "".join(password_chars)

    entry.delete(0, tk.END)
    entry.insert(0, password)

    check_password()


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
    else:
        entry.config(show="*")


def copy_password():
    password = entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        suggestion_label.config(
            text="Password copied to clipboard!"
        )
    else:
        suggestion_label.config(
            text="Nothing to copy."
        )


def clear_fields():
    entry.delete(0, tk.END)

    strength_label.config(
        text="Strength:",
        foreground="black"
    )

    score_label.config(text="Score: 0/5")

    suggestion_label.config(text="")

    progress["value"] = 0


# ---------- WINDOW ----------

root = tk.Tk()

root.title("Password Strength Checker")
root.geometry("500x500")
root.resizable(False, False)


# ---------- TITLE ----------

title = ttk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 18, "bold")
)

title.pack(pady=15)


# ---------- PASSWORD BOX ----------

entry = ttk.Entry(
    root,
    width=35,
    show="*",
    font=("Arial", 12)
)

entry.pack()

entry.bind("<KeyRelease>", check_password)


# ---------- SHOW PASSWORD ----------

show_var = tk.BooleanVar()

show_btn = ttk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password
)

show_btn.pack(pady=5)


# ---------- BUTTONS ----------

check_btn = ttk.Button(
    root,
    text="Check Strength",
    command=check_password
)

check_btn.pack(pady=5)


generate_btn = ttk.Button(
    root,
    text="Generate Strong Password",
    command=generate_password
)

generate_btn.pack(pady=5)


copy_btn = ttk.Button(
    root,
    text="Copy Password",
    command=copy_password
)

copy_btn.pack(pady=5)


clear_btn = ttk.Button(
    root,
    text="Clear",
    command=clear_fields
)

clear_btn.pack(pady=5)


# ---------- STRENGTH ----------

strength_label = ttk.Label(
    root,
    text="Strength:",
    font=("Arial", 12, "bold")
)

strength_label.pack(pady=8)


score_label = ttk.Label(
    root,
    text="Score: 0/5",
    font=("Arial", 10)
)

score_label.pack()


progress = ttk.Progressbar(
    root,
    length=300,
    maximum=5
)

progress.pack(pady=8)


# ---------- SUGGESTIONS ----------

suggestion_label = ttk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 10)
)

suggestion_label.pack(pady=10)


# ---------- RUN ----------

root.mainloop()