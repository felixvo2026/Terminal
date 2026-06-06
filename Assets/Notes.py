import json

class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def save(self, notes):
        notes[self.title] = self.text

class NotesManager:
    def __init__(self, username):
        self.username = username
        self.user = self.load_notes()
        self.notes = self.user[username]["notes"]

    def load_notes(self):
        try:
            with open("Json-Daten/users.json", "r", encoding="utf-8") as file:
                content = file.read().strip()

                if not content:
                    return {}

                return json.loads(content)

        except FileNotFoundError:
            return {}

        except json.JSONDecodeError:
            print("⚠️ users.json ist beschädigt")
            return {}

    def save_notes(self):
        self.user[self.username]["notes"] = self.notes

        with open("Json-Daten/users.json", "w", encoding="utf-8") as file:
            json.dump(self.user, file, indent=4, ensure_ascii=False)

    def NotesAdd(self):
        title = input("title: ")
        if title in self.notes:
            print("Notiz schon vorhanden!")
            return
        text = input("text: ")
        note = Note(title, text)
        note.save(self.notes)
        self.save_notes()
        print("✔ Saved")

    def NotesRemove(self):
        title = input("Which note to delete?")
        if title == "all":
            self.notes.clear()
            self.save_notes()
            print("✔ Deleted")
        elif title in self.notes:
            del self.notes[title]
            self.save_notes()
            print("✔ Deleted")
        else:
            print("❌ not found")

    def NotesShow(self):
        if not self.notes:
            print("No notes available.")
        else:
            for title, text in self.notes.items():
                print(f"{title}: {text}")


#nm = NotesManager()
#atexit.register(nm.save_notes)