import sqlite3
import tkinter as tk
import sys
from datetime import datetime

DB = "notes.db"

# ================= DATABASE =================

def db():
    return sqlite3.connect(DB)

def init_db():
    with db() as c:
        c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            updated TEXT
        )
        """)

def create_note(title="New Note"):
    with db() as c:
        cur = c.execute(
            "INSERT INTO notes VALUES (NULL, ?, ?, ?)",
            (title, "", datetime.now())
        )
        return cur.lastrowid

def save_note(i, t, c):
    with db() as d:
        d.execute(
            "UPDATE notes SET title=?, content=?, updated=? WHERE id=?",
            (t, c, datetime.now(), i)
        )

def get_notes():
    with db() as c:
        return c.execute(
            "SELECT id, title FROM notes ORDER BY updated DESC"
        ).fetchall()

def get_note(i):
    with db() as c:
        return c.execute(
            "SELECT title, content FROM notes WHERE id=?",
            (i,)
        ).fetchone()

def search(q):
    with db() as c:
        return c.execute(
            "SELECT id, title FROM notes WHERE title LIKE ? OR content LIKE ?",
            (f"%{q}%", f"%{q}%")
        ).fetchall()

# ================= GUI =================

def gui():
    BG = "#1e1e1e"
    FG = "#ffffff"
    SIDE = "#2b2b2b"

    root = tk.Tk()
    root.title("Notes Pro")
    root.geometry("900x500")
    root.configure(bg=BG)

    current = {"id": None}

    sidebar = tk.Listbox(root, bg=SIDE, fg=FG)
    sidebar.pack(side="left", fill="y")

    main = tk.Frame(root, bg=BG)
    main.pack(expand=True, fill="both")

    search_box = tk.Entry(main, bg=SIDE, fg=FG)
    search_box.pack(fill="x")

    title = tk.Entry(main, bg=BG, fg=FG, font=("Arial", 14, "bold"))
    title.pack(fill="x", pady=5)

    text = tk.Text(main, bg=BG, fg=FG, insertbackground=FG)
    text.pack(expand=True, fill="both")

    def refresh(notes=None):
        sidebar.delete(0, tk.END)
        for i, t in (notes or get_notes()):
            sidebar.insert(tk.END, f"{i}:{t}")

    def load(e=None):
        if not sidebar.curselection():
            return
        i = int(sidebar.get(tk.ACTIVE).split(":")[0])
        n = get_note(i)
        current["id"] = i
        title.delete(0, tk.END)
        title.insert(0, n[0])
        text.delete("1.0", tk.END)
        text.insert("1.0", n[1])

    def new():
        i = create_note()
        refresh()
        current["id"] = i
        title.delete(0, tk.END)
        text.delete("1.0", tk.END)

    def autosave():
        if current["id"]:
            save_note(
                current["id"],
                title.get(),
                text.get("1.0", tk.END)
            )
        root.after(3000, autosave)

    def do_search(e):
        q = search_box.get()
        refresh(search(q) if q else None)

    sidebar.bind("<<ListboxSelect>>", load)
    search_box.bind("<KeyRelease>", do_search)

    tk.Button(main, text="+ New Note", command=new).pack(fill="x")

    refresh()
    autosave()
    root.mainloop()

# ================= CLI =================

def cli():
    while True:
        print("\n📝 NOTES CLI")
        print("1. List")
        print("2. New")
        print("3. View")
        print("4. Search")
        print("5. Exit")

        c = input("> ")

        if c == "1":
            for i, t in get_notes():
                print(f"{i} - {t}")

        elif c == "2":
            t = input("Title: ")
            i = create_note(t)
            c = input("Content:\n")
            save_note(i, t, c)

        elif c == "3":
            i = int(input("ID: "))
            n = get_note(i)
            if n:
                print("\n" + n[0])
                print(n[1])

        elif c == "4":
            q = input("Search: ")
            for i, t in search(q):
                print(f"{i} - {t}")

        elif c == "5":
            break

# ================= ENTRY =================

if __name__ == "__main__":
    init_db()
    if "--cli" in sys.argv:
        cli()
    else:
        gui()
