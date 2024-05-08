#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    //ignore non-letter characters
    //should be case insensitive
    //points[0]=a, points[1]=b...points[25]=z
    //keep track of the score
    int score = 0;
    //iterate through word, calculating score for each character
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            //A is represented by 65 in ASCII, we can subtract each uppecase letter by A to get corresponding digit
            score += (POINTS[word[i] - 'A']);
        }
        else if (islower(word[i]))
        {
            //subtract each lowercase letter by a to get corresponding digit in points
            score += (POINTS[word[i] - 'a']);
        }
    }
    return score;
}
