import time

def chatbot():

    antworten = {
        "hallo": "Hallo!",
        "wieheißtdu": "Keine Ahnung",
        "wasbistdu": "Ein Python-Chatbot",
        "waskannstdu": "Ich kann einfache Fragen beantworten.",
        "wiegehtesdir": "Mir geht es gut. Wie geht es dir?",
        "mirgehtesgut": "Sehr schön.was hast du heute vor?"
    }
    kurznachrichten = {
        "hallo": "Hallo!",
        "ok": "Bitte",
        "okay": "Bitte",
        "danke": "Sehr gerne",
        "nichts": "Ok",
        "viel": "Und was genau?",
        "gut": "Schön",

    }


    print("Chatbot")

    while True:

        user = input(">>> ").lower().replace(" ", "").replace("?", "")

        if user == "exit":
            print("Tschüss!")
            break
        if user == "time":
            nowtime()
            continue

        if user in antworten:
            print(antworten[user])
        elif user in kurznachrichten:
            print(kurznachrichten[user])
        else:
            print("Das weiß ich leider nicht!")




def nowtime():
    now = time.localtime()
    print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
    print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")
