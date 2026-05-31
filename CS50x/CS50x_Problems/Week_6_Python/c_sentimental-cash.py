def sort(total, coins, i, count):
    if (total == 0):
        return count

    if (total - coins[i] >= 0):
        count += 1
        return sort(total - coins[i], coins, i, count)
    else:
        return sort(total, coins, i + 1, count)


while(True):
    try:
        total = float(input("How much is the total? : "))
        if total > 0:
            break
    except ValueError:
        continue


total*=100
coins = [25, 10, 5, 1]
print(f"Minimum coins needed : { sort( total, coins, 0, 0 ) }", )