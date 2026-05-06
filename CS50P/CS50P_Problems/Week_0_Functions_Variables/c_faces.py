def main():
    text = input()
    convert(text)

def convert(text):
    if(":(" in text and ":)" in text):
        happy = text.replace(":)", "🙂")
        sad = happy.replace(":(", "🙁")
        print(sad)
    elif(":)" in text):
        happy = text.replace(":)", "🙂")
        print(happy)
    elif(":(" in text):
        sad = text.replace(":(", "🙁")
        print(sad)

main()