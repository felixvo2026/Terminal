import json
import time
from Assets import Calculator
from Assets import Premium

def load_passwords():
    try:
        with open("Json-Daten/password.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords():
    with open("Json-Daten/password.json", "w", encoding="utf-8") as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)

def register():
    global passwords
    username = input("Username: ")
    password = input("Password: ")
    fftpremiumpassword = input("Premium Password: ")
    if fftpremiumpassword == "f  FTTerminal":
        passwords[username] = password
        save_passwords()
        print("Saved")
        while True:
            Premium.Premium()
    else:
        print("Zugang wurde verweigert")

def login():
    global passwords
    username = input("Username: ")
    password = input("Password: ")
    if username in passwords and passwords[username] == password:
        print("Logged in")
        while True:
            Premium.Premium()


def Exit():
    print("Program is terminating...")
    quit()

def help():
    for c in commands:
        print(f"-{c}: {commands[c]["description"]}")

def ShowTime():
    now = time.localtime()
    print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
    print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")


commands = {
    "exit": {
        "function": Exit,
        "description": "Exit program"
    },
    "help": {
        "function": help,
        "description": "Show help message for all commands"
    },
    "calculator": {
        "function": Calculator.Calculator,
        "description": "Calculator"
    },
    "login": {
        "function": login,
        "description": "Login"
    },
    "register": {
        "function": register,
        "description":"Register"
    },
    "time":{
        "function": ShowTime,
        "description": "Show time"
    }
}

passwords = load_passwords()

while True:
    command = input("> ").lower().replace(" ", "")
    try:
        if command == "ccal":
            Calculator.Calculator()
            continue
        commands[command]["function"]()
    except KeyError:
        print(f"Invalid command: {command}")


