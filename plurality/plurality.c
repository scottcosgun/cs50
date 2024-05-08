#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //iterate through candidate count
    for (int i = 0; i < candidate_count; i++)
    {
        //check if vote matches with any candidates
        if (strcmp(candidates[i].name, name) == 0)
        {
            //if vote = candidate name, increase their vote count by 1
            candidates[i].votes++;
            return true;
        }
    }
    //if name does not match any candidate, do not increase any vote totals and return false.
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // print candidate that received the most votes, then a new line
    //if multiple candidates win, print them all on separate lines
    //define new variable for vote max
    int vote_max = 0;
    //iterate through vote counts to find the highest count
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > vote_max)
        {
            //store highest vote count in vote_max variable
            vote_max = candidates[i].votes;
        }
    }
    //iterate through candidate names
    for (int i = 0; i < candidate_count; i++)
    {
        //check if the number of votes = the highest count
        if (candidates[i].votes == vote_max)
        {
            //print each winning candidate on a new line
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}