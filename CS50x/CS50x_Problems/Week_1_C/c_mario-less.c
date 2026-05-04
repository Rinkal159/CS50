#include <stdio.h>

int main()
{
    int n;
    do
    {
        printf("Height of pyramid: ");
        scanf("%d", &n);
    } while (n <= 0 || sizeof(n) != 4);

    // outer loop
    for (int i = 1; i <= n; i++)
    {
        // prints space
        for (int k = n - 1; k >= i; k--)
        {
            printf("%s", " ");
        }

        // prints #
        for (int j = 1; j <= i; j++)
        {
            printf("%s", "#");
        }
        printf("\n");
    }
}
