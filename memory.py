import tkinter as tk
from tkinter import messagebox
import random

# =========================
# WINDOW
# =========================
root = tk.Tk()
root.title("Visual Memory Game")
root.geometry("700x600")
root.configure(bg="#111827")

# =========================
# DATA GAME
# =========================
level = 1
score = 0
lives = 3

sequence = []
player_sequence = []

showing = False

buttons = []

colors = [
    "#3B82F6",
    "#22C55E",
    "#F97316",
    "#EC4899"
]

# =========================
# LABEL
# =========================
title_label = tk.Label(
    root,
    text="VISUAL MEMORY GAME",
    font=("Arial", 24, "bold"),
    bg="#111827",
    fg="white"
)

title_label.pack(pady=20)

info_label = tk.Label(
    root,
    text="Level: 1   Score: 0   Lives: ❤️❤️❤️",
    font=("Arial", 14),
    bg="#111827",
    fg="white"
)

info_label.pack(pady=10)

status_label = tk.Label(
    root,
    text="Klik START GAME",
    font=("Arial", 12),
    bg="#111827",
    fg="#D1D5DB"
)

status_label.pack(pady=10)

# =========================
# FRAME GRID
# =========================
grid_frame = tk.Frame(root, bg="#111827")
grid_frame.pack(pady=20)

# =========================
# UPDATE LABEL
# =========================
def update_info():

    global level
    global score
    global lives

    info_label.config(
        text=f"Level: {level}   Score: {score}   Lives: {'❤️' * lives}"
    )

# =========================
# FLASH BUTTON
# =========================
def flash(index):

    button = buttons[index]

    color = colors[index]

    button.config(bg=color)

    root.after(
        500,
        lambda: button.config(bg="#1F2937")
    )

# =========================
# PLAYER CLICK
# =========================
def click(index):

    global showing
    global player_sequence

    if showing == True:
        return

    player_sequence.append(index)

    flash(index)

    # CHECK
    current = len(player_sequence) - 1

    if player_sequence[current] != sequence[current]:

        wrong()

        return

    # WIN
    if len(player_sequence) == len(sequence):

        win()

# =========================
# WRONG
# =========================
def wrong():

    global lives
    global player_sequence

    lives = lives - 1

    update_info()

    if lives == 0:

        messagebox.showerror(
            "GAME OVER",
            f"Score kamu: {score}"
        )

        reset_game()

    else:

        messagebox.showwarning(
            "SALAH",
            f"Nyawa sisa: {lives}"
        )

        player_sequence = []

        show_sequence()

# =========================
# WIN
# =========================
def win():

    global level
    global score

    score = score + (level * 10)

    level = level + 1

    update_info()

    messagebox.showinfo(
        "BENAR",
        "Level Naik!"
    )

    start_game()

# =========================
# SHOW SEQUENCE
# =========================
def show_sequence():

    global showing

    showing = True

    status_label.config(
        text="Ingat urutannya..."
    )

    for i in range(len(sequence)):

        root.after(
            i * 800,
            lambda x=sequence[i]: flash(x)
        )

    root.after(
        len(sequence) * 800,
        player_turn
    )

# =========================
# PLAYER TURN
# =========================
def player_turn():

    global showing

    showing = False

    status_label.config(
        text="Sekarang giliran kamu!"
    )

# =========================
# START GAME
# =========================
def start_game():

    global sequence
    global player_sequence

    player_sequence = []

    sequence = []

    start_button.pack_forget()

    # RANDOM SEQUENCE
    for i in range(level + 2):

        number = random.randint(0, 3)

        sequence.append(number)

    show_sequence()

# =========================
# RESET GAME
# =========================
def reset_game():

    global level
    global score
    global lives
    global sequence
    global player_sequence

    level = 1
    score = 0
    lives = 3

    sequence = []
    player_sequence = []

    update_info()

    status_label.config(
        text="Klik START GAME"
    )

    start_button.pack(pady=20)

# =========================
# BUTTON GRID
# =========================
for i in range(4):

    button = tk.Button(
        grid_frame,
        width=12,
        height=6,
        bg="#1F2937",
        relief="flat",
        command=lambda x=i: click(x)
    )

    button.grid(
        row=i // 2,
        column=i % 2,
        padx=10,
        pady=10
    )

    buttons.append(button)

# =========================
# START BUTTON
# =========================
start_button = tk.Button(
    root,
    text="START GAME",
    font=("Arial", 16, "bold"),
    bg="#2563EB",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    command=start_game
)

start_button.pack(pady=20)

# =========================
# RUN
# =========================
root.mainloop()