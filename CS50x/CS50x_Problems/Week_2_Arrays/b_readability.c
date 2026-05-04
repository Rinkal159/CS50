#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>

float l = 0;
float w = 0;
float s = 0;

void modifyVars(char text[]);

int main(void)
{
    char text[1000];
    printf("Text: ");
    fgets(text, sizeof(text), stdin);

    modifyVars(text);

    l = (l / w) * 100;
    s = (s / w) * 100;

    int index = round(0.0588 * l - 0.296 * s - 15.8);

    if (index < 0)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

void modifyVars(char text[])
{
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        if (isspace(text[i]))
        {
            w++;
        }

        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s++;
        }
    }
}
