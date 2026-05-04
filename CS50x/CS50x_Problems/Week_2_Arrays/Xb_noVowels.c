#include <ctype.h>
#include <string.h>
#include <stdio.h>

void replaceVowel(char word[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word.");
        return 1;
    }

    replaceVowel(argv[1]);

    printf("%s\n", argv[1]);
}

void replaceVowel(char word[])
{
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        switch (word[i])
        {
        case 'a':
            word[i] = '6';
            break;

        case 'e':
            word[i] = '3';
            break;

        case 'i':
            word[i] = '1';
            break;

        case 'o':
            word[i] = '0';
            break;

        default:
            break;
        }
    }
}