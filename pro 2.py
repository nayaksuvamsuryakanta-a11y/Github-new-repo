import tkinter as tk
from tkinter import messagebox

FILE_NAME = "notes.txt"

# ---------- Functions ----------

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
        selected = notes_list.curselection()[0]
        notes_list.delete(selected)
        save_notes()
    except IndexError:
        messagebox.showwarning("Warning", "Select a note to delete!")

# ---------- GUI ----------

root = tk.Tk()
root.title("📝 Note Taking App")
root.geometry("400x450")

# Title
title = tk.Label(root, text="Note Taking App", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Entry
note_entry = tk.Entry(root, width=40)
note_entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Note", width=20, command=add_note)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected Note", width=20, command=delete_note)
delete_btn.pack(pady=5)

# Listbox
notes_list = tk.Listbox(root, width=45, height=15)
notes_list.pack(pady=10)

# Load existing notes
load_notes()

root.mainloop()
