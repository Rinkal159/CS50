#include <stdio.h>

int sort(int total, int coins[], int i, int count)
{
    // if total becomes 0, returns
    if (total == 0)
    {
        return count;
    }

    // when substracting coin from total, and still it returns postive values then don't go ahead,
    // and add 1 to existing number of coins needed
    if (total - coins[i] >= 0)
    {
        count++;
        return sort(total - coins[i], coins, i, count);
    }
    else
    {
        return sort(total, coins, i + 1, count);
    }
}

int main()
{
    // gets user input
    int total;
    do
    {
        printf("How much is the total? : ");
        scanf("%d", &total);
    } while (total < 0);

    // array of coins
    int coins[] = {25, 10, 5, 1};

    // calls function
    printf("Minimum coins needed : %d\n", sort(total, coins, 0, 0));
}
