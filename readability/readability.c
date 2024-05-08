#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int main(void)
{
    string s = get_string("Text: ");
    float letters = count_letters(s);
    float words = count_words(s);
    float sentences = count_sentences(s);
    //index = 0.0588 * L - 0.296 * S - 15.8
    //where L is the average number of letters per 100 words in the text
    float L = (letters / words) * 100.00;
    //and S is the average number of sentences per 100 words in the text.
    float S = (sentences / words) * 100.00;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 1 && index < 16)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}
int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i ++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}
int count_words(string text)
{
    int words = 1;
    for (int j = 0, len = strlen(text); j < len; j++)
    {
        if (text[j] == ' ')
        {
            words++;
        }
    }
    return words;
}
int count_sentences(string text)
{
    int sentences = 0;
    for (int k = 0, len = strlen(text); k < len; k++)
    {
        if (text[k] == '.' || text[k] == '!' || text[k] == '?')
        {
            sentences++;
        }
    }
    return sentences;
}