# 🖥️ Terminal Application

Ein professionelles Terminal-Programm mit OOP, Sicherheit & mehrsprachigem Chatbot.

## ✨ Features

- 🔐 **Sichere Authentifizierung** (bcrypt Hashing)
- 📝 **Notizen-Manager** (JSON Speicherung + Backup)
- 🤖 **Multilingual Chatbot** (Deutsch & English)
- 🧮 **Calculator** (mit Sicherheit)
- 📁 **File Management** (cd, ls, pwd)
- ⏰ **System Info** (Datum & Uhrzeit)

## 🛠️ Technologie

- **Language:** Python 3.10+
- **Security:** bcrypt Password Hashing
- **Architecture:** Object-Oriented Programming (OOP)
- **Data Storage:** JSON mit automatischen Backups

## 📦 Installation

```bash
git clone https://github.com/felixvo2026/Terminal.git
cd Terminal
pip install bcrypt
python main.py
```bash

##🚀 Wie man es benutzt
Code
> register        # Neuen Account erstellen
> login           # Einloggen
>> notesadd       # Notiz hinzufügen
>> chatbot        # Chatbot starten
>> time           # Uhrzeit anzeigen
>> exit           # Beenden


##🏗️ Architektur
Code
Terminal/
├── main.py              (PasswordManager + Main Klasse)
├── Assets/
│   ├── Notes.py        (NotesManager Klasse)
│   ├── Premium.py      (Premium Klasse)
│   ├── KI_Chatbot.py   (Ki_Chatbot Klasse)
│   └── Calculator.py   (Calculator)
└── Json-Daten/         (Daten + Backup)

##🔒 Sicherheit
✅ bcrypt Password Hashing - Passwörter sind NICHT im Klartext gespeichert ✅ Automatische Backups - Daten sind doppelt gespeichert ✅ Salt-basiertes Hashing - Jedes Passwort hat eigenen Salt

📚 Was ich gelernt habe
Object-Oriented Programming (OOP)
bcrypt Password Hashing
JSON Datenspeicherung
Git & GitHub Workflows
Mehrsprachige Programme

##👨‍💻 Autor
Felix - 12 Jahre - Learning Python & Security 🚀
