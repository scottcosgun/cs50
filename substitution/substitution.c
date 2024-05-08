#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_alpha(string s);
bool no_repeats(string s);
string cipher(string s, string k);
//get key from user. 26 characters, all alpha, no repeats
//validate key, printing out error message if not valid
int main(int argc, string argv[])
{
    //check to make sure only 1 argument
    if (argc != 2)
    {
        //remind user how to use program and return 1 to quit
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //check to make sure key has 26 characters
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    //check to make sure all characters are alphabetic
    else if (only_alpha(argv[1]) == false)
    {
        printf("Key must only contain alphabetic characters\n");
        return 1;
    }
    //check to make sure no characters are repeated
    else if (no_repeats(argv[1]) != 0)
    {
        printf("Key must not contain repeated characters\n");
        return 1;
    }
    //get plaintext from user
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");
    //convert the entire key to uppercase
    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        argv[1][i] = toupper(argv[1][i]);
    }
    int textlen = strlen(plaintext);
    //initialize char array
    char ciphertext[textlen + 1];
    int position;
    //encipher text
    //iterate through each char of plaintext
    for (int i = 0; i < textlen; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                position = plaintext[i] - 65;
                ciphertext[i] = argv[1][position];
                printf("%c", ciphertext[i]);
            }
            else
            {
                position = plaintext[i] - 97;
                ciphertext[i] = tolower(argv[1][position]);
                printf("%c", ciphertext[i]);
            }
        }
        else
        {
            ciphertext[i] = plaintext[i];
            printf("%c", ciphertext[i]);
        }
    }
    //print new line
    printf("\n");
}

//check to make sure key is only alphabetic
bool only_alpha(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isalpha(s[i]) == false)
        {
            return false;
            break;
        }
    }
    return true;
}

//check to make sure no letters are repeated
bool no_repeats(string s)
{
    //iterate through each character of the string
    for (int i = 0; i < strlen(s) ; i++)
    {
        //iterate through all characters after i to check for repeats
        for (int j = i + 1 ; j < strlen(s) ; j++)
        {
            if (tolower(s[j]) == tolower(s[i]))
            {
                return 1;
            }
        }
    }
    return 0;
}
