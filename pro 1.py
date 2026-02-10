FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note saved!\n")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()
            if not notes:
                print("📭 No notes found.\n")
            else:
                print("\n🗒 Your Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
                print()
    except FileNotFoundError:
        print("📭 No notes file found.\n")

def delete_note():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("📭 No notes to delete.\n")
            return

        view_notes()
        num = int(input("Enter note number to delete: "))

        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(notes)
            print("🗑 Note deleted!\n")
        else:
            print("❌ Invalid note number.\n")

    except FileNotFoundError:
        print("📭 No notes file found.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    while True:
        print("📝 Note Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

main()
