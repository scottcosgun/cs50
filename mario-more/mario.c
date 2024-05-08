#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    //height-1 spaces
    //number of hashes corresponding to row
    //two spaces for gap
    //number of hashes corresponding to row
    for (int i = 0; i < height; i++)
    //integer i = 0, set top row as row 0
    {
        for (int s = height - 1; s > i; s--)
        //s = spaces on left. we start out with height-1 spaces on left and decrease with each descending row
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        //print hash on left. j = 0, i = row #. Row zero, print one #. increase for each descending row
        {
            printf("#");
        }
        printf("  ");
        //two spaces in between hashes
        for (int right = i; right >= 0; right--)
        //right starts out as i, row #, and for each descending row increases. match left number of hashes.
        {
            printf("#");
        }
        printf("\n");
    }
}