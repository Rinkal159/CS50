camelText = input("camelCase: ")

for str in camelText:
    if (str.isupper()):
        print("_", end="")
        str = str.lower()
    print(str, end="")
    
print()