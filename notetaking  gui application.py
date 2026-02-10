import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
from datetime import datetime


# --- डेटाबेस सेटअप (Database Logic) ---
def init_db():
    conn = sqlite3.connect("pro_notes.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes 
                      (id INTEGER PRIMARY KEY, title TEXT, content TEXT, date TEXT)''')
    conn.commit()
    return conn


# --- मुख्य एप्लिकेशन क्लास ---
class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Python Notes")
        self.root.geometry("900x600")
        self.root.configure(bg="#2c3e50")

        self.conn = init_db()
        self.current_note_id = None

        # UI Styles
        self.font_main = ("Segoe UI", 12)
        self.font_bold = ("Segoe UI", 14, "bold")

        self.setup_ui()
        self.load_notes_list()

    def setup_ui(self):
        # Left Panel (Sidebar for List)
        self.sidebar = tk.Frame(self.root, width=300, bg="#34495e")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.sidebar, text="मारे नोट्स", font=self.font_bold, bg="#34495e", fg="white").pack(pady=10)

        # Search Box
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.load_notes_list())
        self.search_entry = tk.Entry(self.sidebar, textvariable=self.search_var, font=self.font_main, bg="#ecf0f1")
        self.search_entry.pack(fill=tk.X, padx=10, pady=5)
        self.search_entry.insert(0, "खोजें...")

        self.notes_listbox = tk.Listbox(self.sidebar, font=self.font_main, bg="#ecf0f1", selectbackground="#3498db")
        self.notes_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.notes_listbox.bind("<<ListboxSelect>>", self.get_note_details)

        # Right Panel (Editor)
        self.editor_frame = tk.Frame(self.root, bg="#2c3e50")
        self.editor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Title Entry
        self.title_label = tk.Entry(self.editor_frame, font=("Segoe UI", 18, "bold"), bg="#2c3e50", fg="white",
                                    insertbackground="white", borderwidth=0)
        self.title_label.pack(fill=tk.X, padx=20, pady=(20, 5))
        self.title_label.insert(0, "शीर्षक (Title)")

        # Content ScrolledText
        self.content_area = scrolledtext.ScrolledText(self.editor_frame, font=self.font_main, bg="#ffffff", undo=True)
        self.content_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Buttons
        self.btn_frame = tk.Frame(self.editor_frame, bg="#2c3e50")
        self.btn_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Button(self.btn_frame, text="नया नोट (New)", command=self.clear_screen, bg="#f1c40f", width=15).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="सेव करें (Save)", command=self.save_note, bg="#2ecc71", fg="white",
                  width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="डिलीट (Delete)", command=self.delete_note, bg="#e74c3c", fg="white",
                  width=15).pack(side=tk.RIGHT, padx=5)

    def load_notes_list(self):
        self.notes_listbox.delete(0, tk.END)
        query = "SELECT id, title FROM notes WHERE title LIKE ? ORDER BY id DESC"
        search_text = f"%{self.search_var.get()}%" if self.search_var.get() != "खोजें..." else "%%"

        cursor = self.conn.cursor()
        cursor.execute(query, (search_text,))
        self.note_records = cursor.fetchall()
        for _, title in self.note_records:
            self.notes_listbox.insert(tk.END, f" 📝 {title}")

    def save_note(self):
        title = self.title_label.get()
        content = self.content_area.get("1.0", tk.END).strip()
        date_str = datetime.now().strftime("%d-%m-%Y %H:%M")

        if not title or title == "शीर्षक (Title)":
            messagebox.showwarning("Error", "कृपया शीर्षक लिखें!")
            return

        cursor = self.conn.cursor()
        if self.current_note_id:
            cursor.execute("UPDATE notes SET title=?, content=?, date=? WHERE id=?",
                           (title, content, date_str, self.current_note_id))
        else:
            cursor.execute("INSERT INTO notes (title, content, date) VALUES (?, ?, ?)", (title, content, date_str))

        self.conn.commit()
        self.load_notes_list()
        messagebox.showinfo("Success", "नोट सुरक्षित कर लिया गया है!")

    def get_note_details(self, event):
        try:
            index = self.notes_listbox.curselection()[0]
            self.current_note_id = self.note_records[index][0]

            cursor = self.conn.cursor()
            cursor.execute("SELECT title, content FROM notes WHERE id=?", (self.current_note_id,))
            note = cursor.fetchone()

            self.title_label.delete(0, tk.END)
            self.title_label.insert(0, note[0])
            self.content_area.delete("1.0", tk.END)
            self.content_area.insert(tk.END, note[1])
        except IndexError:
            pass

    def delete_note(self):
        if self.current_note_id:
            if messagebox.askyesno("Confirm", "क्या आप वाकई इसे डिलीट करना चाहते हैं?"):
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM notes WHERE id=?", (self.current_note_id,))
                self.conn.commit()
                self.clear_screen()
                self.load_notes_list()
        else:
            messagebox.showwarning("Warning", "डिलीट करने के लिए कोई नोट चुनें!")

    def clear_screen(self):
        self.current_note_id = None
        self.title_label.delete(0, tk.END)
        self.title_label.insert(0, "शीर्षक (Title)")
        self.content_area.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    # Python documentation for reference on [Tkinter](https://docs.python.org)
    root.mainloop()
