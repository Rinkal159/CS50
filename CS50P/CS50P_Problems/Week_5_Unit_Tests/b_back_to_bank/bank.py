def main():
    text = input("Greeting: ")
    dollar = value(text)
    print(f"${dollar}")


def value(text):
    text = text.lower().strip()
    if(text.startswith("hello")):
        return 0
    elif(text.startswith("h")):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
