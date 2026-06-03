import json
import time
import bcrypt
from Assets import Calculator
from Assets import Premium


class PasswordManager:
    def __init__(self):
        self.passwords = self.load_passwords()
        self.premium = Premium.Premium()

    def load_passwords(self):
        try:
            with open("Json-Daten/password.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open("Json-Daten/password.json", "w", encoding="utf-8") as file:
            json.dump(self.passwords, file, indent=4, ensure_ascii=False)
        with open("Backup/Json-Daten/password.json", "w", encoding="utf-8") as file:
            json.dump(self.passwords, file, indent=4, ensure_ascii=False)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    def check_password(self, password, hashed):
        try:
            return bcrypt.checkpw(password.encode(), hashed.encode())
        except Exception as e:
            print(f"❌ Fehler: {e}")
            return False

    def register(self):
        username = input("Username: ").strip()

        if not username:
            print("❌ Username darf nicht leer sein!")
            return

        if username in self.passwords:
            print("❌ Benutzer existiert bereits.")
            return

        if username.endswith("!"):
            print("❌ Benutzername nicht möglich!")
            return

        password = input("Password: ").strip()

        hashed_password = self.hash_password(password)
        self.passwords[username] = hashed_password
        self.save_passwords()
        print("✅ Registrierung erfolgreich!")
        while True:
            self.premium.run()

    def login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username not in self.passwords:
            print("❌ Benutzer nicht gefunden!")
            return

        if self.check_password(password, self.passwords[username]):
            print("✅ Login erfolgreich!")
            while True:
                self.premium.run()
        else:
            print("❌ Falscher Benutzername oder Passwort.")

    def admin_register(self):
        username = input("Username: ").strip()

        if not username:
            print("❌ Username darf nicht leer sein!")
            return

        if username in self.passwords:
            print("❌ Benutzer existiert bereits.")
            return

        password = input("Password: ").strip()
        admin_password = input("Admin Password: ").strip()
        if admin_password == "f  FTTerminal":
            username += "!"
            hashed_password = self.hash_password(password)
            self.passwords[username] = hashed_password
            self.save_passwords()
            print("✅ Registrierung erfolgreich!")
            while True:
                self.premium.run()

    def admin_login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        try:
            breakpoint()
            username += "!"
            if self.check_password(password, self.passwords[username]):
                print("✅ Login erfolgreich!")
                while True:
                    self.premium.run()
            else:
                print("❌ Falscher Benutzername oder Passwort.")
        except Exception as e:
            print(f"Error: {e}")

    def change_password(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if not self.check_password(password, self.passwords[username]) and not username.endswith("!"):
            print("Access denied!")
            return
        else:
            new_password = input("New Password: ").strip()
            new_hashed_password = self.hash_password(new_password)
            self.passwords[username] = new_hashed_password
            print("✅ Password changed successfully")
            self.save_passwords()

class Main:
    def __init__(self):
        self.pm = PasswordManager()
        self.commands = {
            "exit": {
                "function": self.Exit,
                "description": "Exit program"
            },
            "help": {
                "function": self.help,
                "description": "Show help message for all commands"
            },
            "calculator": {
                "function": Calculator.Calculator,
                "description": "Calculator"
            },
            "login": {
                "function": self.pm.login,
                "description": "Login"
            },
            "register": {
                "function": self.pm.register,
                "description": "Register"
            },
            "admin_register": {
                "function": self.pm.admin_register,
                "description": "Admin register"
            },
            "admin_login": {
                "function": self.pm.admin_login,
                "description": "Admin login"
            },
            "change_password": {
                "function": self.pm.change_password,
                "description": "Change password"
            },
            "time": {
                "function": self.ShowTime,
                "description": "Show time"
            }
        }

    def Exit(self):
        print("Program is terminating...")
        quit()

    def help(self):
        for c in self.commands:
            print(f'-{c}: {self.commands[c]["description"]}')

    def ShowTime(self):
        now = time.localtime()
        print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
        print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    def run(self):
        while True:
            command = input("> ").lower().replace(" ", "")
            try:
                if command == "ccal":
                    Calculator.Calculator()
                    continue
                self.commands[command]["function"]()
            except KeyError:
                print(f"Invalid command: {command}")


main = Main()
main.run()

#Admin mit User löschen, Passwort ändern