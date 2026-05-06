#include <stdio.h>
#include <string.h>

#define MAX 9

typedef struct
{
    char *name;
    int vote;
} Candidate;

int isPresent(char vote[], Candidate c[], int TotalCandidates);
void updateVotesAndReturnWinner(int NumberOfVoters, Candidate c[], int TotalCandidates);

int main(int argc, char *argv[])
{

    int n = argc;
    if (n < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    if (n - 1 > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    Candidate c[n - 1];

    for (int i = 0; i < n - 1; i++)
    {
        c[i].name = argv[i + 1];
        c[i].vote = 0;
    }

    int NumberOfVoters;
    printf("Number of voters: ");
    scanf("%d", &NumberOfVoters);

    getchar();
    updateVotesAndReturnWinner(NumberOfVoters, c, n - 1);
}

int isPresent(char vote[], Candidate c[], int TotalCandidates)
{
    for (int i = 0; i < TotalCandidates; i++)
    {
        if (strcmp(vote, c[i].name) == 0)
        {
            return i;
        }
    }

    return -1;
}

void updateVotesAndReturnWinner(int NumberOfVoters, Candidate c[], int TotalCandidates)
{

    int max = 0;

    for (int i = 1; i <= NumberOfVoters; i++)
    {
        char vote[50];
        printf("Vote: ");
        fgets(vote, sizeof(vote), stdin);
        vote[strlen(vote) - 1] = '\0';

        int i = isPresent(vote, c, TotalCandidates);

        if (i >= 0)
        {
            c[i].vote++;
            if (c[i].vote > max)
            {
                max = c[i].vote;
            }
        }
        else
        {
            printf("Invalid vote.\n");
        }
    };

    for (int i = 0; i < TotalCandidates; i++)
    {
        if (c[i].vote == max)
        {
            printf("%s\n", c[i].name);
        }
    }
}