import math

def modifyVars(text):
    l = w = s = 0
    for i in text:
        if (i.isalpha()):
            l += 1

        if (i.isspace()):
            w += 1

        if (i in ['.', '!', '?']):
            s += 1

    w += 1
    return l, w, s


text = input("Text: ")

l, w, s = modifyVars(text)

l = (l / w) * 100
s = (s / w) * 100

index = int(round(0.0588 * l - 0.296 * s - 15.8))

if (index < 0):
    print("Before Grade 1")
elif (index > 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")