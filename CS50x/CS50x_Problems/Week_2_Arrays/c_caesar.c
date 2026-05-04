#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int convertIntoInt(char argv[]);
void encryptText(char text[], int key);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = convertIntoInt(argv[1]);
    if (key < 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    char text[50];
    printf("plaintext: ");
    fgets(text, sizeof(text), stdin);

    encryptText(text, key);

    printf("ciphertext: %s", text);
    return 0;
}

int convertIntoInt(char argv[])
{
    char *invalid;

    long key = strtol(argv, &invalid, 10);

    if (*invalid != '\0')
    {
        return -1;
    }
    return key;
}

void encryptText(char text[], int key)
{
    for (int i = 0, n = strlen(text) - 1; i < n; i++)
    {
        if (!isalpha(text[i]))
        {
            continue;
        }
        if (isupper(text[i]))
        {
            text[i] = (char)(((text[i] - 65) + key) % 26) + 65;
        }
        else
        {
            text[i] = (char)(((text[i] - 97) + key) % 26) + 97;
        }
    }
}
