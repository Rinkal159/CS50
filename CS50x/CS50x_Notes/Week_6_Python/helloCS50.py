from sys import *
import qrcode
import csv

# print("Hello, CS50!")

#&-----------------------------------------------------------------------------------------------------------

# name = "Rinkal"
# print("Hello, " + name) # '+' can only used for string to concate manual messages and variable, NOT gonna work out with other types like bool and number

# who = True
# print("I am" + who) # here it shows an error, because concatenating messages with '+', instead concatenate with ','

#&-----------------------------------------------------------------------------------------------------------

# isTyped = bool(input("What's your name? : "))
# if(isTyped):
#     print(f"Is input receipved? : {isTyped}") #f-string
# else:
#     print("Please input your name to print")
    
#&-----------------------------------------------------------------------------------------------------------
 
# print("Hello", "world", end="", sep=",") #by default, print has end argument value as "\n", if i make it empty then it does not add a new line and now the separator value is , instead of " "
# print("Not on a new line")

#&-----------------------------------------------------------------------------------------------------------

# name = "123"
# name = int(name) # not (int)name, but here int(name), name is the argument in conversion type function
# print(name)
# print(type(name))

#&-----------------------------------------------------------------------------------------------------------

# A = {1,2,3,4,5}
# B = {3,5,6,7,8}

# print(f"union: {A | B}") 
# print(f"intersection: {A & B}") 
# print(f"difference: {A - B}") 
# print(f"symmetrical difference: {A ^ B}") 

#&-----------------------------------------------------------------------------------------------------------

# str1 = input("String 1: ")
# str2 = input("String 2: ")

# if(str1 == str2): # == is enough to compare a string in python
#     print("Same")
# else:
#     print("Different")
    
#&-----------------------------------------------------------------------------------------------------------

# listOfYes = ["y", "Y", "yes", "YES"]
# agree = input('Do you agree? : ')

# if agree in listOfYes: #loop through whole list in "if condition" without any loop definitions, just using "in"
#     print("Agree")
# else:
#     print("Don't agree")

#&-----------------------------------------------------------------------------------------------------------

# s = "rinkal"
# t = s.upper() #does not change s

# print(f"s: {s}") 
# print(f"t: {t}")

#&-----------------------------------------------------------------------------------------------------------

#* decimal number formation
 
# x = 1
# y = 3
# print(f"{(x/y):.2 f}") # format limit of numbers after decimal, ":.<length>f" : only works in f-string
# print(1//3) # floor division, now the answer is truncated

#&-----------------------------------------------------------------------------------------------------------

#* try - except blocks

# try:
#     x = int(input("Dividend: "))
#     y = int(input("Divisor: "))
#     print(f"{(x/y):.2f}")
# except ValueError:
#     print("Only numbers allowed.")
# except ZeroDivisionError:
#     print("Cannot divide a number by zero.")

#&----------------------------------------------------------------------------------------------------------- 

#* scope of variables
 
# # varibles are not blocked scoped in python, they are functional scoped. meaning variables created inside while, for or if condition, they are accessible outside the block, but when created inside a function, they aren't accessible ouside the function.

# while(True):
#     try: 
#         n = int(input("n: ")) # n is accessible in for loop
#         if(n>0):
#             break
#     except ValueError:
#         print("Only integeres allowed")
    
# for _ in range(n):
#     print("*")
    
#&----------------------------------------------------------------------------------------------------------- 

#* print ? side by side like - ????

#^ one way
# x = 4
# for _ in range(x):
#     print("?", end="")
# print()

#^ another way
# print("?" * 4)

#&----------------------------------------------------------------------------------------------------------- 

#* sum of "list" elements without any loop

# scores = [1,2,3]
# print(sum(scores))

#&----------------------------------------------------------------------------------------------------------- 

# #* input numbers in list and sums up them

# length = int(input("Length of list: "))
# scores = []

# for i in range(length):
#     score = int(input(f"Score {i+1}: "))
#     scores.append(score)

# print(f"Sum of scores: {sum(scores)}")

#&----------------------------------------------------------------------------------------------------------- 

#* argv 

# # argv is a list, that is accessible by argv functionality from sys module and by exit, we can return from the code just like C

# if(len(argv) != 2):
#     exit(1)

# print(f"Hello, {argv[1]}")
# exit(0)

#&----------------------------------------------------------------------------------------------------------- 

# * file handling 

#^ one way
# file = open("../colors.txt", "a")
# color = input("color: ")

# file.write(f"{color}\n")
# file.close()


#^ another way - automatically closes file
# color = input("color: ")

# with open("../colors.txt", "a") as file:
#     file.write(f"{color}\n")

#&----------------------------------------------------------------------------------------------------------- 

# * QR code generator

# img = qrcode.make("https://cs50.harvard.edu/x/")
# img.save("CS50qr.png", "PNG")


#&----------------------------------------------------------------------------------------------------------- 

#* pass by reference, also in parameters just needed name of list, not needed [], same with tuple(), set{} and dicts{}

# def sum(list):
#     for i in range(len(list)):
#         list[i] *= 2

# list = [1,2,3]
# sum(list)
# print(list)

#&----------------------------------------------------------------------------------------------------------- 

#* if both dict have same keys, same values the comparesion returns True

# dict1 = {
#     "name":"rinkal",
#     "age":18
# }

# dict2 = {
#     "name":"rinkal",
#     "age":18
# }

# print(dict1==dict2)

#&----------------------------------------------------------------------------------------------------------- 

#* Read phonebook.csv

with open("phonebook.csv", "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file) # DictReader automatically ignores header row, and gives every content in the form of dictionary

    # next(reader) # to move the pointer in next row - to skip the headers, don't need in DictReader
    
    for row in reader:
        print(row["name"])
    
#&----------------------------------------------------------------------------------------------------------- 

#* Read favourites.csv - count the favourite languages

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)

    count = {}
    
    for row in reader:
        favourite = row["language"]
        
        #^ one way 
        # if favourite in count:
            # count[favourite] += 1
        # else:
            # count[favourite] = 1 
            
        #^ another way - by error handling 
        try:
            count[favourite] += 1
        except KeyError:
            count[favourite] = 1
        
    print(count)