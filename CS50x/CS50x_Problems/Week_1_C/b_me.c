#include <stdio.h>

int main()
{
    // gets user input
    char name[50];
    printf("What is your name? - ");
    fgets(name, sizeof(name), stdin);

    // geets user with hello
    printf("hello, %s", name);
}
