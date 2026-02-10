import tkinter as tk
from tkinter import messagebox

FILE_NAME = "notes.txt"
dark_mode = False

# ---------- Theme Colors ----------

LIGHT = {
    "bg": "#ffffff",
    "fg": "#000000",
    "entry_bg": "#f0f0f0",
    "button_bg": "#e0e0e0",
    "list_bg": "#ffffff"
}

DARK = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "entry_bg": "#2e2e2e",
    "button_bg": "#3a3a3a",
    "list_bg": "#2e2e2e"
}

# ---------- Functions ----------

def apply_theme(theme):
    root.configure(bg=theme["bg"])
    title.config(bg=theme["bg"], fg=theme["fg"])
    note_entry.config(bg=theme["entry_bg"], fg=theme["fg"])
    notes_list.config(bg=theme["list_bg"], fg=theme["fg"])
    add_btn.config(bg=theme["button_bg"], fg=theme["fg"])
    delete_btn.config(bg=theme["button_bg"], fg=theme["fg"])
    theme_btn.config(bg=theme["button_bg"], fg=theme["fg"])


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme(DARK if dark_mode else LIGHT)


def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                notes_list.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass


def save_notes():
    with open(FILE_NAME, "w") as file:
        for i in range(notes_list.size()):
            file.write(notes_list.get(i) + "\n")


def add_note():
    note = note_entry.get()
    if note.strip() == "":
        messagebox.showwarning("Warning", "Note cannot be empty!")
        return

    notes_list.insert(tk.END, note)
    note_entry.delete(0, tk.END)
    save_notes()


def delete_note():
    try:
        index = notes_list.curselection()[0]
        notes_list.delete(index)
        save_notes()
    except IndexError:
        messagebox.showwarning("Warning", "Select a note to delete!")

# ---------- GUI ----------

root = tk.Tk()
root.title("📝 Note App (Dark Mode)")
root.geometry("420x480")

title = tk.Label(root, text="Note Taking App", font=("Arial", 16, "bold"))
title.pack(pady=10)

note_entry = tk.Entry(root, width=40, font=("Arial", 11))
note_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Note", width=22, command=add_note)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected Note", width=22, command=delete_note)
delete_btn.pack(pady=5)

theme_btn = tk.Button(root, text="Toggle Dark / Light Mode", width=22, command=toggle_theme)
theme_btn.pack(pady=5)

notes_list = tk.Listbox(root, width=45, height=15)
notes_list.pack(pady=10)

# Load data & apply default theme
load_notes()
apply_theme(LIGHT)

root.mainloop()
