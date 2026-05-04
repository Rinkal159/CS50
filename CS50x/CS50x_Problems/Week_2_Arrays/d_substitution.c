#include <string.h>
#include <ctype.h>
#include <stdio.h>

int validArgv(char argv[]);
void encryptText(char text[], char key[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    if (validArgv(argv[1]))
    {
        printf("Invalid key.\n");
        return 1;
    }

    char text[100];
    printf("plaintext: ");
    fgets(text, sizeof(text), stdin);

    encryptText(text, argv[1]);
    printf("ciphertext: %s", text);

    return 0;
}

int validArgv(char argv[])
{
    int count[26];

    for (int i = 0, n = sizeof(count) / sizeof(count[0]); i < n; i++)
    {
        count[i] = 0;
    }

    for (int i = 0, n = strlen(argv); i < n; i++)
    {
        if (!isalpha(argv[i]))
        {
            return 1;
        }

        if (count[toupper(argv[i]) - 65] >= 1)
        {
            return 1;
        }
        count[toupper(argv[i]) - 65]++;
    }

    return 0;
}

void encryptText(char text[], char key[])
{
    for (int i = 0, n = strlen(text) - 1; i < n; i++)
    {
        if (!isalpha(text[i]))
        {
            continue;
        }

        if (islower(text[i]))
        {
            text[i] = tolower(key[text[i] - 97]);
        }
        else
        {
            text[i] = toupper(key[text[i] - 65]);
        }
    }
}