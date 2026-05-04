#include <ctype.h>
#include <string.h>
#include <stdio.h>

int check(char password[]);

int main(void)
{
    char password[100];
    printf("Enter your password: ");
    fgets(password, sizeof(password), stdin);

    if (check(password) == 1)
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol!\n");
        return 1;
    }

    printf("Your password is valid!\n");
    return 0;
}

int check(char password[])
{
    int upper = 0;
    int lower = 0;
    int number = 0;
    int symbol = 0;

    for (int i = 0, n = strlen(password); i < n; i++)
    {
        if (upper && lower && number && symbol)
        {
            break;
        }

        if (!upper)
        {
            upper = isupper(password[i]) ? upper + 1 : upper;
        }

        if (!lower)
        {
            lower = islower(password[i]) ? lower + 1 : lower;
        }

        if (!number)
        {
            number = isdigit(password[i]) ? number + 1 : number;
        }

        if (!symbol)
        {
            symbol = !isalnum(password[i]) && isprint(password[i]) ? symbol + 1 : symbol;
        }
    }

    if (!upper || !lower || !number || !symbol)
    {
        return 1;
    }
    return 0;
}