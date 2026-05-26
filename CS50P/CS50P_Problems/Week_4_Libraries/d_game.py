import random

while True:
    level = int(input("Level: "))
    if level > 0:
        break

random = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess == random:
            print("Just Right!")
            break
        elif guess > random:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        pass
