
import tkinter as tk
from tkinter import ttk

from password_logic import check_password, generate_secure_password


# ============================================================
# COLORS - NEON THEME
# ============================================================

BG = "#090014"
PANEL = "#12001f"
NEON_PINK = "#ff00ff"
NEON_CYAN = "#00ffff"
NEON_GREEN = "#39ff14"
NEON_YELLOW = "#ffff00"
NEON_RED = "#ff1744"
WHITE = "#ffffff"
GRAY = "#b9a7c7"

STRENGTH_COLORS = {
    "NO PASSWORD": NEON_RED,
    "VERY WEAK": NEON_RED,
    "WEAK": "#ff6600",
    "MEDIUM": NEON_YELLOW,
    "STRONG": NEON_CYAN,
    "VERY STRONG": NEON_GREEN,
}


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Neon Password Strength Checker")

try:
    root.state("zoomed")
except tk.TclError:
    root.geometry("1100x750")

root.minsize(900, 600)
root.configure(bg=BG)


# ============================================================
# STYLE
# ============================================================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Neon.Horizontal.TProgressbar",
    troughcolor="#1b0928",
    background=NEON_CYAN,
    bordercolor=NEON_CYAN,
    lightcolor=NEON_CYAN,
    darkcolor=NEON_CYAN,
    thickness=18
)


# ============================================================
# FUNCTIONS
# ============================================================

def update_strength(event=None):
    password = password_entry.get()

    score, strength, suggestions = check_password(password)
    color = STRENGTH_COLORS[strength]

    progress["value"] = score

    strength_label.config(
        text=strength,
        fg=color
    )

    score_label.config(
        text=f"Security Score: {score}/100",
        fg=color
    )

    suggestions_text.delete("1.0", tk.END)

    if not suggestions:
        suggestions_text.insert(
            tk.END,
            "Excellent! Your password meets the current checks."
        )
    else:
        for suggestion in suggestions:
            suggestions_text.insert(
                tk.END,
                "• " + suggestion + "\n"
            )


def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="•")
        show_button.config(text="SHOW")
    else:
        password_entry.config(show="")
        show_button.config(text="HIDE")


def generate_password():
    password = generate_secure_password(16)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    update_strength()


def clear_password():
    password_entry.delete(0, tk.END)
    suggestions_text.delete("1.0", tk.END)

    progress["value"] = 0

    strength_label.config(
        text="NO PASSWORD",
        fg=NEON_RED
    )

    score_label.config(
        text="Security Score: 0/100",
        fg=WHITE
    )

    suggestions_text.insert(
        tk.END,
        "Enter a password to begin."
    )


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()


# ============================================================
# MAIN CONTAINER
# ============================================================

main_frame = tk.Frame(root, bg=BG)

main_frame.pack(
    fill="both",
    expand=True,
    padx=50,
    pady=35
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    main_frame,
    text="⚡ NEON PASSWORD STRENGTH CHECKER ⚡",
    font=("Arial", 28, "bold"),
    bg=BG,
    fg=NEON_CYAN
)

title_label.pack(pady=(10, 5))


subtitle_label = tk.Label(
    main_frame,
    text="Analyze your password security in real time",
    font=("Arial", 13),
    bg=BG,
    fg=GRAY
)

subtitle_label.pack(pady=(0, 25))


# ============================================================
# NEON LINE
# ============================================================

neon_line = tk.Frame(
    main_frame,
    bg=NEON_PINK,
    height=3
)

neon_line.pack(fill="x", pady=(0, 30))


# ============================================================
# PASSWORD PANEL
# ============================================================

password_panel = tk.Frame(
    main_frame,
    bg=PANEL,
    highlightbackground=NEON_PINK,
    highlightthickness=2
)

password_panel.pack(
    fill="x",
    padx=30,
    pady=10
)


password_label = tk.Label(
    password_panel,
    text="ENTER PASSWORD",
    font=("Arial", 12, "bold"),
    bg=PANEL,
    fg=NEON_PINK
)

password_label.pack(
    anchor="w",
    padx=25,
    pady=(20, 8)
)


# ============================================================
# PASSWORD ENTRY
# ============================================================

entry_frame = tk.Frame(password_panel, bg=PANEL)

entry_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 20)
)

password_entry = tk.Entry(
    entry_frame,
    font=("Arial", 18),
    bg="#050008",
    fg=WHITE,
    insertbackground=NEON_CYAN,
    relief="flat",
    show="•"
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=12,
    padx=(0, 10)
)

password_entry.bind("<KeyRelease>", update_strength)


show_button = tk.Button(
    entry_frame,
    text="SHOW",
    command=toggle_password,
    font=("Arial", 10, "bold"),
    bg="#21002f",
    fg=NEON_CYAN,
    activebackground=NEON_CYAN,
    activeforeground=BG,
    relief="flat",
    padx=20,
    pady=12,
    cursor="hand2"
)

show_button.pack(side="right")


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(password_panel, bg=PANEL)

button_frame.pack(pady=(0, 25))


generate_button = tk.Button(
    button_frame,
    text="⚡ GENERATE PASSWORD",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg="#260033",
    fg=NEON_GREEN,
    activebackground=NEON_GREEN,
    activeforeground=BG,
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
)

generate_button.pack(side="left", padx=8)


clear_button = tk.Button(
    button_frame,
    text="✕ CLEAR",
    command=clear_password,
    font=("Arial", 11, "bold"),
    bg="#260033",
    fg=NEON_PINK,
    activebackground=NEON_PINK,
    activeforeground=BG,
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
)

clear_button.pack(side="left", padx=8)


copy_button = tk.Button(
    button_frame,
    text="COPY",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#260033",
    fg=NEON_CYAN,
    activebackground=NEON_CYAN,
    activeforeground=BG,
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
)

copy_button.pack(side="left", padx=8)


# ============================================================
# RESULTS PANEL
# ============================================================

results_panel = tk.Frame(
    main_frame,
    bg=PANEL,
    highlightbackground=NEON_CYAN,
    highlightthickness=2
)

results_panel.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)


strength_title = tk.Label(
    results_panel,
    text="PASSWORD STRENGTH",
    font=("Arial", 12, "bold"),
    bg=PANEL,
    fg=NEON_CYAN
)

strength_title.pack(pady=(25, 5))


strength_label = tk.Label(
    results_panel,
    text="NO PASSWORD",
    font=("Arial", 32, "bold"),
    bg=PANEL,
    fg=NEON_RED
)

strength_label.pack(pady=5)


score_label = tk.Label(
    results_panel,
    text="Security Score: 0/100",
    font=("Arial", 14, "bold"),
    bg=PANEL,
    fg=WHITE
)

score_label.pack(pady=(0, 15))


progress = ttk.Progressbar(
    results_panel,
    style="Neon.Horizontal.TProgressbar",
    orient="horizontal",
    mode="determinate",
    maximum=100
)

progress.pack(
    fill="x",
    padx=60,
    pady=(0, 25)
)


# ============================================================
# SECURITY ANALYSIS
# ============================================================

suggestions_label = tk.Label(
    results_panel,
    text="SECURITY ANALYSIS",
    font=("Arial", 12, "bold"),
    bg=PANEL,
    fg=NEON_PINK
)

suggestions_label.pack(
    anchor="w",
    padx=60,
    pady=(5, 8)
)


suggestions_text = tk.Text(
    results_panel,
    height=6,
    font=("Arial", 12),
    bg="#050008",
    fg=WHITE,
    insertbackground=NEON_CYAN,
    relief="flat",
    wrap="word"
)

suggestions_text.pack(
    fill="both",
    expand=True,
    padx=60,
    pady=(0, 25)
)

suggestions_text.insert(
    tk.END,
    "Enter a password to begin."
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="🔐 Neon Password Security Tool  •  Python + Tkinter",
    font=("Arial", 10),
    bg=BG,
    fg=GRAY
)

footer.pack(pady=(0, 12))


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()

# START APPLICATION
# ============================================================

root.mainloop()
