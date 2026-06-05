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
        #breakpoint()
        if not username:
            print("❌ Username darf nicht leer sein!")
            return

        if username in self.passwords:
            print("❌ Benutzer existiert bereits.")
            return

        password = input("Password: ").strip()

        hashed_password = self.hash_password(password)
        self.passwords[username] = {
            "password" : hashed_password,
            "role" : "user"}
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

        if self.check_password(password, self.passwords[username]["password"]):
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
            hashed_password = self.hash_password(password)
            self.passwords[username] = {
                "password": hashed_password,
                "role": "admin"}
            self.save_passwords()
            print("✅ Registrierung erfolgreich!")
            while True:
                self.premium.run()

    def admin_login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        try:
            if self.passwords[username]["role"] != "admin":
                print("Access denied")
                return
            if self.check_password(password, self.passwords[username]["password"]):
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
        try:
            if username not in self.passwords:
                print("Access denied!")
                return
            is_admin = self.passwords[username]["role"] == "admin"

            if not is_admin:
                if not self.check_password(password, self.passwords[username]["password"]):
                    print("Access denied")
                    return

            new_password = input("New Password: ").strip()
            new_hashed_password = self.hash_password(new_password)
            self.passwords[username]["password"] = new_hashed_password
            print("✅ Password changed successfully")
            self.save_passwords()
        except Exception as e:
            print(f"Error: {e}")

    def user_delete(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        try:
            if username not in self.passwords:
                print("Access denied!")
                return
            is_admin = self.passwords[username]["role"] == "admin"

            if not is_admin:
                print("Acess denied")
                return
            elif not self.check_password(password, self.passwords[username]["password"]):
                print("Access denied")
                return
            else:
                delete_user = input("Which User do you want do delete: ").strip()
                if delete_user not in self.passwords:
                    print("User not found")
                    return
                elif delete_user == username:
                    print("You cannot delete yourself")
                    return
                else:
                    del self.passwords[delete_user]
                    self.save_passwords()
                    print(f"User {delete_user} deleted successfully")

        except Exception as e:
            print(f"Error: {e}")


class Main:
    def __init__(self):
        self.history = []
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
            "adminregister": {
                "function": self.pm.admin_register,
                "description": "Admin register"
            },
            "adminlogin": {
                "function": self.pm.admin_login,
                "description": "Admin login"
            },
            "changepassword": {
                "function": self.pm.change_password,
                "description": "Change password"
            },
            "time": {
                "function": self.ShowTime,
                "description": "Show time"
            },
            "printlast": {
                "function": self.printlast,
                "description": "Last command"
            },
            "deluser": {
                "function": self.pm.user_delete,
                "description": "Delete user"
            },
            "last": {
                "function": self.last,
                "description": " Do last command"
            }
        }

    def printlast(self):
        if not self.history:
            print("No commands available")
            return
        print("Last command:", self.history[-1])

    def last(self):
        if not self.history:
            print("No commands available")
            return
        if self.history[-1] == "ccal":
            Calculator.Calculator()
            return
        self.commands[self.history[-1]]["function"]()

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
                    self.history.append(command)
                    continue

                self.commands[command]["function"]()
                if command != "last":
                    self.history.append(command)
            except KeyError:
                print(f"Invalid command: {command}")


main = Main()
main.run()

# current User und Verbesserung von logout