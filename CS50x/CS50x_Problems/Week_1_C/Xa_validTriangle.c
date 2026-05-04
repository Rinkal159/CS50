#include <stdio.h>

int isValidTriangle(int a, int b, int c);

int main(void)
{
    int a, b, c;
    printf("a : ");
    scanf("%d", &a);
    printf("b : ");
    scanf("%d", &b);
    printf("c : ");
    scanf("%d", &c);

    int result = isValidTriangle(a, b, c);
    if (result < 0)
    {
        printf("Triangle sides must not have non positive values.");
    }
    else if (result == 1)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }
}

int isValidTriangle(int a, int b, int c)
{
    if (a < 0 || b < 0 || c < 0)
    {
        return -1;
    }
    if ((a + b) <= c || (b + c) <= a || (a + c) <= b)
    {
        return 0;
    }
    return 1;
}
