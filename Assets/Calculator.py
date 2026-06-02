import math

def Calculator():
    rechnung = input("> calculation: ").replace(",",".")

    try:
        for zeichen in rechnung:
            if zeichen not in "0123456789+-*/().√sqrtpi":
                raise ValueError

        result = eval(rechnung,{"__builtins__": None}, {"sqrt": math.sqrt, "pi": math.pi})
        print(result)

    except ZeroDivisionError:
        print("❌ Division by zero")
    except ValueError:
        print("❌ Not a number")
    except :
        print("❌ Invalid input")