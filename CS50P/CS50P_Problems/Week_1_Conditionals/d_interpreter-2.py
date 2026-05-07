text = input("Expression: ")

x, y, z = text.split(" ")

match text[y]:
    case "+":
        print(f"{(x+z):.1f}")
    case "-":
        print(f"{(x-z):.1f}")
    case "*":
        print(f"{(x*z):.1f}")
    case "/":
        print(f"{(x/z):.1f}")
