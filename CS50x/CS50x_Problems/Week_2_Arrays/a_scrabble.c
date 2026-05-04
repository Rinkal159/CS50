#include <ctype.h>
#include <string.h>
#include <stdio.h>

int addPoints(int points[], char value[]);

int main(void)
{
    int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    char first[50], second[50];
    printf("Player 1 : ");
    fgets(first, sizeof(first), stdin);
    printf("Player 2 : ");
    fgets(second, sizeof(second), stdin);

    int firstSum = addPoints(points, first);
    int secondSum = addPoints(points, second);

    if (firstSum > secondSum)
    {
        printf("Player 1 wins");
    }
    else if (secondSum > firstSum)
    {
        printf("Player 2 wins");
    }
    else
    {
        printf("Tie!");
    }
}

int addPoints(int points[], char value[])
{

    int sum = 0;
    for (int i = 0, n = strlen(value) - 1; i < n; i++)
    {

        value[i] = toupper(value[i]);
        if (value[i] < 65 || value[i] > 90)
        {
            continue;
        }

        value[i] -= 65;

        sum += points[(int)value[i]];
    }

    return sum;
}
