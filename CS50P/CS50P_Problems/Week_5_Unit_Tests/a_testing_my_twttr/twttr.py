def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    for str in word:
        if(str.lower() in ['a', 'e', 'i', 'o', 'u']):
            word = word.replace(str, "")

    return word


if __name__ == "__main__":
    main()
