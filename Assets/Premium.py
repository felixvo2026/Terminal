#import json
import os
import time
from Assets import Calculator
from Assets import Notes
from Assets import KI_Chatbot

def Premium():
    while True:
        commando = input(">> ").lower().replace(" ", "")

        try:
            if commando == "ccal":
                Calculator.Calculator()
                continue
            if commando == "h":
                print(1/0)
                continue

            commandos[commando]["function"]()
        except KeyError:
            print(f"Invalid command: {commando}")

def Exit():
    print("Program is terminating...")
    quit()

def help():
    for c in commandos:
        print(f"-{c}: {commandos[c]["description"]}")

def ShowTime():
    now = time.localtime()
    print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
    print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

def logout():
    print("You have logged out")
    quit()

def changedir():
    try:
        dir = input("To which directory do you want to change to: ")
        os.chdir(dir)
    except:
        print("No Directory")

def getcwd():
    print(os.getcwd())

def listdir():
    print(os.listdir())

commandos = {
    "exit": {
        "function": Exit,
        "description": "Exit program"
    },
    "help": {
        "function": help,
        "description": "Show help message"
    },
    "notesadd": {
        "function": Notes.nm.NotesAdd,
        "description": "Add notes"
    },
    "notesremove": {
        "function": Notes.nm.NotesRemove,
        "description": "Remove notes"
    },
    "notesshow": {
        "function": Notes.nm.NotesShow,
        "description": "Show notes"
    },
    "calculator": {
        "function": Calculator.Calculator,
        "description": "Calculator"
    },
    "logout": {
        "function": logout,
        "description": "Logout"
    },
    "time":{
        "function": ShowTime,
        "description": "Show time"
    },
    "chatbot": {
        "function": KI_Chatbot.chatbot,
        "description": "Chatbot"
    },
    "fftcwd": {
        "function": getcwd,
        "description": "Print current working directory"
    },
    "fftlist": {
        "function": listdir,
        "description": "Print list of files"
    },
    "fftchange": {
        "function": changedir,
        "description": "Change the current working directory"
    }
}