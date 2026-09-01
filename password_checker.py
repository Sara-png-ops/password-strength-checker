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


# ---------- NEON COLORS ----------

BG_COLOR = "#080814"
PANEL_COLOR = "#111122"

NEON_PINK = "#ff00ff"
NEON_BLUE = "#00eaff"
NEON_GREEN = "#39ff14"
NEON_YELLOW = "#fff700"
NEON_ORANGE = "#ff8c00"
NEON_RED = "#ff1744"

TEXT_COLOR = "#ffffff"
SUBTEXT_COLOR = "#b8b8d1"


# ---------- FUNCTIONS ----------

def check_password(event=None):

    password = entry.get()
    score = 0
    suggestions = []

    if not password:

        strength_label.config(
            text="STRENGTH: --",
            fg=SUBTEXT_COLOR
        )

        progress["value"] = 0

        score_label.config(
            text="SCORE: 0 / 5"
        )

        suggestion_label.config(text="")

        return


    # ---------- COMMON PASSWORD CHECK ----------

    if password.lower() in COMMON_PASSWORDS:

        strength_label.config(
            text="⚠ VERY WEAK",
            fg=NEON_RED
        )

        progress["value"] = 0

        score_label.config(
            text="SCORE: 0 / 5",
            fg=NEON_RED
        )

        suggestion_label.config(
            text="⚠ COMMONLY USED PASSWORD!\nCHOOSE A MORE UNIQUE PASSWORD.",
            fg=NEON_RED
        )

        return


    # ---------- LENGTH ----------

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("• Use at least 8 characters")


    # ---------- UPPERCASE ----------

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("• Add an uppercase letter")


    # ---------- LOWERCASE ----------

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("• Add a lowercase letter")


    # ---------- NUMBER ----------

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("• Add a number")


    # ---------- SPECIAL CHARACTER ----------

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("• Add a special character")


    # ---------- UPDATE SCORE ----------

    progress["value"] = score

    score_label.config(
        text=f"SCORE: {score} / 5"
    )


    # ---------- PASSWORD STRENGTH ----------

    if score <= 2:

        result = "WEAK"
        color = NEON_RED

    elif score <= 4:

        result = "MEDIUM"
        color = NEON_ORANGE

    else:

        result = "STRONG"
        color = NEON_GREEN


    strength_label.config(
        text=f"STRENGTH: {result}",
        fg=color
    )

    score_label.config(
        fg=color
    )


    # ---------- SUGGESTIONS ----------

    if suggestions:

        suggestion_label.config(
            text="\n".join(suggestions),
            fg=NEON_YELLOW
        )

    else:

        suggestion_label.config(
            text="✓ EXCELLENT PASSWORD!",
            fg=NEON_GREEN
        )


# ---------- GENERATE PASSWORD ----------

def generate_password():

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

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


    # Add remaining characters

    for _ in range(8):

        password_chars.append(
            random.choice(characters)
        )


    random.shuffle(password_chars)

    password = "".join(password_chars)

    entry.delete(0, tk.END)

    entry.insert(
        0,
        password
    )

    check_password()


# ---------- SHOW / HIDE PASSWORD ----------

def toggle_password():

    if show_var.get():

        entry.config(show="")

    else:

        entry.config(show="*")


# ---------- COPY PASSWORD ----------

def copy_password():

    password = entry.get()

    if password:

        root.clipboard_clear()

        root.clipboard_append(password)

        suggestion_label.config(
            text="✓ PASSWORD COPIED TO CLIPBOARD!",
            fg=NEON_BLUE
        )

    else:

        suggestion_label.config(
            text="⚠ NOTHING TO COPY!",
            fg=NEON_RED
        )


# ---------- CLEAR ----------

def clear_fields():

    entry.delete(0, tk.END)

    strength_label.config(
        text="STRENGTH: --",
        fg=SUBTEXT_COLOR
    )

    score_label.config(
        text="SCORE: 0 / 5",
        fg=SUBTEXT_COLOR
    )

    suggestion_label.config(
        text=""
    )

    progress["value"] = 0

    show_var.set(False)

    entry.config(show="*")


# ---------- WINDOW ----------

root = tk.Tk()

root.title("Neon Password Strength Checker")

root.geometry("600x650")

root.resizable(False, False)

root.configure(
    bg=BG_COLOR
)


# ---------- STYLE ----------

style = ttk.Style()

style.theme_use("clam")


# Progress Bar

style.configure(
    "Neon.Horizontal.TProgressbar",
    troughcolor="#222238",
    background=NEON_PINK,
    bordercolor=BG_COLOR,
    lightcolor=NEON_PINK,
    darkcolor=NEON_PINK
)


# ---------- MAIN PANEL ----------

panel = tk.Frame(
    root,
    bg=PANEL_COLOR,
    highlightbackground=NEON_BLUE,
    highlightthickness=2
)

panel.pack(
    padx=35,
    pady=35,
    fill="both",
    expand=True
)


# ---------- TITLE ----------

title = tk.Label(
    panel,
    text="⚡ PASSWORD STRENGTH CHECKER ⚡",
    font=("Arial", 20, "bold"),
    bg=PANEL_COLOR,
    fg=NEON_PINK
)

title.pack(
    pady=(30, 10)
)


subtitle = tk.Label(
    panel,
    text="CHECK • ANALYZE • SECURE",
    font=("Arial", 10, "bold"),
    bg=PANEL_COLOR,
    fg=NEON_BLUE
)

subtitle.pack(
    pady=(0, 25)
)


# ---------- PASSWORD ENTRY ----------

entry_label = tk.Label(
    panel,
    text="ENTER YOUR PASSWORD",
    font=("Arial", 10, "bold"),
    bg=PANEL_COLOR,
    fg=NEON_BLUE
)

entry_label.pack(
    pady=(0, 8)
)


entry = tk.Entry(
    panel,
    width=30,
    show="*",
    font=("Consolas", 15),
    bg="#05050d",
    fg=NEON_GREEN,
    insertbackground=NEON_PINK,
    relief="flat",
    highlightbackground=NEON_BLUE,
    highlightcolor=NEON_PINK,
    highlightthickness=2
)

entry.pack(
    ipady=10
)

entry.bind(
    "<KeyRelease>",
    check_password
)


# ---------- SHOW PASSWORD ----------

show_var = tk.BooleanVar()


show_btn = tk.Checkbutton(
    panel,
    text="SHOW PASSWORD",
    variable=show_var,
    command=toggle_password,
    font=("Arial", 9, "bold"),
    bg=PANEL_COLOR,
    fg=NEON_BLUE,
    activebackground=PANEL_COLOR,
    activeforeground=NEON_PINK,
    selectcolor="#222238"
)

show_btn.pack(
    pady=10
)


# ---------- NEON BUTTON FUNCTION ----------

def create_button(text, command, color):

    button = tk.Button(
        panel,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg="#151526",
        fg=color,
        activebackground="#222238",
        activeforeground=TEXT_COLOR,
        relief="flat",
        cursor="hand2",
        width=28,
        highlightbackground=color,
        highlightthickness=1
    )

    button.pack(
        pady=5
    )

    return button


# ---------- BUTTONS ----------

check_btn = create_button(
    "⚡ CHECK STRENGTH",
    check_password,
    NEON_PINK
)


generate_btn = create_button(
    "✦ GENERATE STRONG PASSWORD",
    generate_password,
    NEON_GREEN
)


copy_btn = create_button(
    "▣ COPY PASSWORD",
    copy_password,
    NEON_BLUE
)


clear_btn = create_button(
    "✕ CLEAR",
    clear_fields,
    NEON_RED
)


# ---------- STRENGTH ----------

strength_label = tk.Label(
    panel,
    text="STRENGTH: --",
    font=("Arial", 15, "bold"),
    bg=PANEL_COLOR,
    fg=SUBTEXT_COLOR
)

strength_label.pack(
    pady=(20, 5)
)


score_label = tk.Label(
    panel,
    text="SCORE: 0 / 5",
    font=("Consolas", 11, "bold"),
    bg=PANEL_COLOR,
    fg=SUBTEXT_COLOR
)

score_label.pack(
    pady=5
)


# ---------- PROGRESS BAR ----------

progress = ttk.Progressbar(
    panel,
    style="Neon.Horizontal.TProgressbar",
    length=400,
    maximum=5,
    mode="determinate"
)

progress.pack(
    pady=10
)


# ---------- SUGGESTIONS ----------

suggestion_label = tk.Label(
    panel,
    text="",
    justify="center",
    font=("Arial", 10),
    bg=PANEL_COLOR,
    fg=NEON_YELLOW
)

suggestion_label.pack(
    pady=15
)


# ---------- FOOTER ----------

footer = tk.Label(
    panel,
    text="🔐 YOUR PASSWORD SECURITY MATTERS",
    font=("Arial", 8, "bold"),
    bg=PANEL_COLOR,
    fg="#777799"
)

footer.pack(
    side="bottom",
    pady=15
)


# ---------- RUN ----------

root.mainloop()

