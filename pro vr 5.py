import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


class AdvancedNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Pro Notes")
        self.root.geometry("900x600")

        # Database Setup
        self.conn = sqlite3.connect("notes.db")
        self.cursor = self.conn.cursor()

        # Ensure correct table structure
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

        self.current_notes_ids = []
        self.setup_ui()
        self.load_notes()
        self.autosave()

    def setup_ui(self):
        self.bg = "#1e1e1e"
        self.fg = "#ffffff"
        self.sidebar_bg = "#2b2b2b"

        self.root.configure(bg=self.bg)

        self.sidebar = tk.Frame(self.root, width=250, bg=self.sidebar_bg)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.sidebar, text="My Notes", font=("Arial", 14, "bold"),
                 bg=self.sidebar_bg, fg=self.fg).pack(pady=10)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.load_notes())
        self.search_entry = tk.Entry(self.sidebar, textvariable=self.search_var,
                                     bg=self.bg, fg=self.fg)
        self.search_entry.pack(fill=tk.X, padx=10, pady=5)

        self.notes_listbox = tk.Listbox(self.sidebar, font=("Arial", 11), bd=0,
                                        bg=self.sidebar_bg, fg=self.fg)
        self.notes_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.notes_listbox.bind('<<ListboxSelect>>', self.view_note)

        tk.Button(self.sidebar, text="+ New Note", command=self.clear_editor,
                  bg="#4CAF50", fg="white").pack(fill=tk.X, padx=10, pady=5)
        tk.Button(self.sidebar, text="Delete Selected", command=self.delete_note,
                  bg="#f44336", fg="white").pack(fill=tk.X, padx=10, pady=5)

        self.editor_frame = tk.Frame(self.root, bg=self.bg)
        self.editor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.title_entry = tk.Entry(self.editor_frame, font=("Arial", 18, "bold"),
                                    bd=0, bg=self.bg, fg=self.fg)
        self.title_entry.pack(fill=tk.X, padx=20, pady=(20, 10))
        self.title_entry.insert(0, "Note Title")

        self.content_text = tk.Text(self.editor_frame, font=("Arial", 12), undo=True,
                                    wrap=tk.WORD, bd=0, bg=self.bg, fg=self.fg,
                                    insertbackground=self.fg)
        self.content_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Button(self.root, text="💾 Save Changes", command=self.save_note,
                  font=("Arial", 10, "bold")).place(relx=0.9, rely=0.05, anchor="ne")

    def save_note(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M")

        if not title:
            messagebox.showwarning("Warning", "Title cannot be empty!")
            return

        selection = self.notes_listbox.curselection()

        if selection:
            note_id = self.current_notes_ids[selection[0]]
            self.cursor.execute("UPDATE notes SET title=?, content=?, timestamp=? WHERE id=?",
                                (title, content, time_now, note_id))
        else:
            self.cursor.execute("INSERT INTO notes (title, content, timestamp) VALUES (?, ?, ?)",
                                (title, content, time_now))

        self.conn.commit()
        self.load_notes()

    def load_notes(self):
        self.notes_listbox.delete(0, tk.END)
        search_query = f"%{self.search_var.get()}%"
        self.cursor.execute(
            "SELECT id, title FROM notes WHERE title LIKE ? ORDER BY timestamp DESC",
            (search_query,)
        )
        rows = self.cursor.fetchall()

        self.current_notes_ids = [row[0] for row in rows]
        for row in rows:
            self.notes_listbox.insert(tk.END, row[1])

    def view_note(self, event):
        selection = self.notes_listbox.curselection()
        if selection:
            idx = selection[0]
            note_id = self.current_notes_ids[idx]
            self.cursor.execute("SELECT title, content FROM notes WHERE id=?", (note_id,))
            note = self.cursor.fetchone()

            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, note[0])
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", note[1])

    def delete_note(self):
        selection = self.notes_listbox.curselection()
        if selection:
            note_id = self.current_notes_ids[selection[0]]
            if messagebox.askyesno("Confirm", "Delete this note?"):
                self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
                self.conn.commit()
                self.clear_editor()
                self.load_notes()

    def clear_editor(self):
        self.notes_listbox.selection_clear(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "New Note Title")
        self.content_text.delete("1.0", tk.END)

    def autosave(self):
        if self.notes_listbox.curselection():
            self.save_note()
        self.root.after(3000, self.autosave)


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedNotesApp(root)
    root.mainloop()
