text = input("Input: ")
print("Output: ", end="")

for str in text:
    if(str.lower() not in ['a', 'e', 'i', 'o', 'u']):
        print(str, end="")
        
print()
