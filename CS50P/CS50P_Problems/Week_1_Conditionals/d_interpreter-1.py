text = input("Expression: ")

x = int( text[ 0 : text.find(" ") ] )
z = int( text[text.rfind(" ") + 1 : ] )
y = text.find(" ") + 1

match text[y]:
    case "+":
        print(f"{(x+z):.1f}")
    case "-":
        print(f"{(x-z):.1f}")
    case "*":
        print(f"{(x*z):.1f}")
    case "/":
        print(f"{(x/z):.1f}")