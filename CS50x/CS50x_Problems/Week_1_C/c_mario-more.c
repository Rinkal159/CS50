#include <stdio.h>

int main()
{

    int n;
    do
    {
        printf("Height of pyramid: ");
        scanf("%d", &n);
    } while (n <= 0);

    // outer loop
    for (int i = 1; i <= n; i++)
    {
        // for space
        for (int k = n - i; k >= 1; k--)
        {
            printf("%s", " ");
        }

        // first half
        for (int j = 1; j <= i; j++)
        {
            printf("%s", "#");
        }
        printf("  ");

        // second half
        for (int q = 1; q <= i; q++)
        {
            printf("%s", "#");
        }
        printf("\n");
    }
}
