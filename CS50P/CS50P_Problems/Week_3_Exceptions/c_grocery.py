groceries = {}

while True:
    try:
        item = input()
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

    except EOFError:
        break

sorted_groceries = dict(sorted(groceries.items())) #to sort a dictionary

for grocery in sorted_groceries:
    print(f"{sorted_groceries[grocery]} {grocery.upper()}")
