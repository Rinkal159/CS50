#include <string.h>
#include <stdio.h>

int main(void)
{
    int n;
    printf("Number of weeks taking CS50 : ");
    scanf("%d", &n);

    int hours[n];
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        printf("Week %d HW hours : ", i + 1);
        scanf("%d", &hours[i]);
        sum += hours[i];
    }

    char choice;
    printf("Enter T for total hours, Enter A for average hours per week : ");
    scanf(" %c", &choice);

    if ('T' == choice)
    {
        printf("%d hours\n", sum);
    }
    else if ('A' == choice)
    {
        printf("%.2f hours\n", sum / (float)n);
    }
}