import time

def deutsch():

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
        "viel": "Und was genau?"
    }


    print("Chatbot")

    while True:

        user = input(">>> ").lower().replace(" ", "").replace("?", "")

        if user == "ende":
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

def english():

    answers = {
        "hello": "Hello!",
        "whatisyourname": "No idea",
        "whatareyou": "A Python chatbot",
        "whatcanyoudo": "I can answer simple questions.",
        "howareyou": "I'm doing well. How are you?",
        "iamfine": "Very nice. What are you planning to do today?"
    }

    short_messages = {
        "hello": "Hello!",
        "ok": "You're welcome",
        "okay": "You're welcome",
        "thanks": "My pleasure",
        "nothing": "Ok",
        "alot": "And what exactly?"
    }

    print("Chatbot")

    while True:

        user = input(">>> ").lower().replace(" ", "").replace("?", "").replace("'", "a")

        if user == "end":
            print("Goodbye!")
            break

        if user == "time":
            nowtime()
            continue

        if user in answers:
            print(answers[user])

        elif user in short_messages:
            print(short_messages[user])

        else:
            print("Unfortunately, I don't know that!")




def nowtime():
    now = time.localtime()
    print(f"date: {now.tm_mday}.{now.tm_mon}.{now.tm_year}")
    print(f"time: {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

def chatbot():
    try:
        language = input("Which language? ").lower()
        languages[language]()
    except KeyError:
        print("Language not found")


languages = {
    "english": english,
    "deutsch": deutsch,
}