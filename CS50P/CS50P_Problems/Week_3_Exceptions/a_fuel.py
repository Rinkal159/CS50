while True:
    try:
        text = input("Fraction: ")
        x = int(text[0 : text.find("/")])
        y = int(text[text.find("/") + 1 : ])

        if (x > y) or (x < 0) or (y < 0):
            raise ValueError

        fuel = round(( x / y) * 100)
        break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if (fuel <= 1):
    print("E")
elif (fuel >= 99):
    print("F")
else:
    print(f"{fuel}%")
