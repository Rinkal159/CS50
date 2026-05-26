import pyfiglet
import sys
import random

def zeroCLA():
    text = input("Input: ")
    print(pyfiglet.figlet_format(text, font=random.choice(pyfiglet.FigletFont.getFonts())))

def twoCLA():
    try:
        if(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
            sys.exit("Invalid usage")

        f = pyfiglet.Figlet(font=sys.argv[2])
        text = input("Input: ")
        print(f.renderText(text))

    except pyfiglet.FontNotFound:
        sys.exit("Invalid usage")

if len(sys.argv) == 1:
    zeroCLA()
elif len(sys.argv) == 3:
    twoCLA()
else:
    sys.exit("Invalid usage")
