#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //initialize integer variable height
    int height;
    //prompt the user for a number between 1 and 8 inclusive, repeating the prompt until it satisfies the conditions
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    //construct pyramid, using height given by user
    //add rows
    for (int i = 0; i < height; i++)
        {
            //print spaces before printing # to right align
            //number of spaces depends on height. start at height-1 spaces, decrease with each row.
            for (int k = height - i; k > 1; k--)
            {
                printf(" ");
            }
            //print #
            //number of # printed corresponds to row.
            for (int j = 0; j <= i; j++)
            {
                printf("#");
            }
            printf("\n");
        }
}