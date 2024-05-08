#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string s);
//create a function called rotate that outputs a char and takes a char and an int as input
char rotate(char c, int n);
//user must input key k, which must be a positive integer, as a command-line argument
int main(int argc, string argv[])
{
    //check to make sure only 1 argument
    if (argc != 2)
    {
        //remind user how to use program and return 1 to quit
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //check to make sure k is an integer
    if (only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //convert arg[v] from string to int
    int k = atoi(argv[1]);
    //prompt user for string 'plaintext'
    string text = get_string("plaintext:  ");
    //print "ciphertext: "
    printf("ciphertext: ");
    //output plaintext's ciphertext
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        char cipher = rotate(text[i], k);
        printf("%c", cipher);
    }
    //After outputting ciphertext, print a newline and exit by returning 0
    printf("\n");
    return 0;
}

//check to make sure k is an integer
bool only_digits(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isdigit(s[i]) == false)
        {
            return false;
            break;
        }
    }
    return true;
}
char rotate(char c, int n)
{
    //while n is larger than 26 (letters in alphabet), keep subtracting by 26 until it falls between 0 and 25.
    while (n > 26)
    {
        n = n - 26;
    }
    //check to see if char c is a letter
    if (isalpha(c))
    {
        int new = c + n;
        //Wrap around so if k = 1, z becomes a, and Z becomes A, and so on.
        //Preserve letters and preserve case
        if (isalpha(new) == false)
        {
            new = new - 26;
        }
        return new;
    }
    //non-alphabetical characters should be left unchanged.
    else
    {
        return c;
    }
}