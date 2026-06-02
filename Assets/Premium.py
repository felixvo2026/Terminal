#import json
import os
import time
from Assets import Calculator
from Assets import Notes
from Assets import KI_Chatbot

class Premium:
    def __init__(self):
        self.nm = Notes.NotesManager()
        self.ki = KI_Chatbot.Ki_Chatbot()
        self.commandos = {
            "exit": {
                "function": self.Exit,
                "description": "Exit program"
            },
            "help": {
                "function": self.help,
                "description": "Show help message"
            },
            "notesadd": {
                "function": self.nm.NotesAdd,
                "description": "Add notes"
            },
            "notesremove": {
                "function": self.nm.NotesRemove,
                "description": "Remove notes"
            },
            "notesshow": {
                "function": self.nm.NotesShow,
                "description": "Show notes"
            },
            "calculator": {
                "function": Calculator.Calculator,
                "description": "Calculator"
            },
            "logout": {
                "function": self.logout,
                "description": "Logout"
            },
            "time": {
                "function": self.ShowTime,
                "description": "Show time"
            },
            "chatbot": {
                "function": self.ki.run,
                "description": "Chatbot"
            },
            "fftcwd": {
                "function": self.getcwd,
                "description": "Print current working directory"
            },
            "fftlist": {
                "function": self.listdir,
                "description": "Print list of files"
            },
            "fftchange": {
                "function": self.changedir,
                "description": "Change the current working directory"
            }
        }

    def run(self):
        while True:
            commando = input(">> ").lower().replace(" ", "")

            try:
                if commando == "ccal":
                    Calculator.Calculator()
                    continue

                self.commandos[commando]["function"]()
            except KeyError:
                print(f"Invalid command: {commando}")

    def Exit(self):
        print("Program is terminating...")
        quit()

    def help(self):
        for c in self.commandos:
            print(f'-{c}: {self.commandos[c]["description"]}')

    def ShowTime(self):
        now = time.localtime()
        print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
        print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    def logout(self):
        print("You have logged out")
        quit()

    def changedir(self):
        try:
            dir = input("To which directory do you want to change to: ")
            os.chdir(dir)
        except:
            print("No Directory")

    def getcwd(self):
        print(os.getcwd())

    def listdir(self):
        print(os.listdir())

