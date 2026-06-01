import json
import time
import hashlib
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

    def register(self):
        username = input("Username: ")
        password = input("Password: ")
        if username in self.passwords:
            print("Benutzer existiert bereits.")
            return
        fftpremiumpassword = input("Premium Password: ")
        if fftpremiumpassword == "f  FTTerminal":
            hashed_password = self.hash_password(password)
            self.passwords[username] = hashed_password
            self.save_passwords()
            print("Saved")
            while True:
                self.premium.run()
        else:
            print("Zugang wurde verweigert")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        if username in self.passwords and self.passwords[username] == self.hash_password(password):
            print("Logged in")
            while True:
                self.premium.run()
        else:
            print("Falscher Benutzername oder Passwort.")

    def hash_password(self, password):
        hasher = hashlib.sha256()
        hasher.update(password.encode("utf-8"))
        return hasher.hexdigest()



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
            "description":"Register"
        },
        "time":{
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