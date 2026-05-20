import math

def Calculator():
    rechnung = input("> calculation: ")

    try:
        result = eval(rechnung,{"__builtins__": None}, {"sqrt": math.sqrt, "pi": math.pi})
        print(result)

    except:
        print("❌ Invalid invoice")