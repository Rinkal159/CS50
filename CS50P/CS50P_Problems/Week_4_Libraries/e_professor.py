import random

def main():
    level = get_level()

    i = 1
    j = 1
    score = 0

    while i <= 10:
        x = generate_integer(level)
        y = generate_integer(level)

        while j <= 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if (ans == ( x + y )):
                    break
            except ValueError:
                pass

            if j != 3:
                print("EEE")
            j = j + 1

        if j == 4:
            print(x + y)
            score = score - 1

        score = score + 1
        j = 1
        i = i + 1

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass




def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)



if __name__ == "__main__":
    main()
