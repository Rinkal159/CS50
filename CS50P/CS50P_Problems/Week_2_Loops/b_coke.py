from math import fabs

amountDue = 50

while(True):
    print(f"Amount Due: {amountDue}")
    insertedCoin = int(input("Insert Coin: "))

    if(insertedCoin in [25, 10, 5]):
        amountDue -= insertedCoin
        if(amountDue <= 0):
            print(f"Change Owed: {int(fabs(amountDue))}")
            break
