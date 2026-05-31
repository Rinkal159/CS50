def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(length(s) and firstTwo(s) and numbersInMiddle(s) and onlyAlphaAndNumbers(s)):
        return True
    else:
        return False

def length(s):
    return len(s) >= 2 and len(s) <= 6

def firstTwo(s):
    return s[0].isalpha() and s[1].isalpha()

def numbersInMiddle(s):
    isNumeric = False
    for str in s:
        if(str.isalpha()):
            if(isNumeric):
                return False

        elif(str.isnumeric()):
            if(not isNumeric):
                if(str == '0'):
                    return False
            isNumeric = True

    return True

def onlyAlphaAndNumbers(s):
    for str in s:
        if(not str.isalpha() and not str.isnumeric()):
            return False

    return True

if __name__ == "__main__":
    main()
