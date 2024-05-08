// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100000;

// Hash table
node *table[N];

//count number of words
int counter = 0;

// Returns true if word is in dictionary, else false
//case insensitive
bool check(const char *word)
{
    // hash word to obtain hash value
    int hash_value = hash(word);
    // access linked list at that index in the hash table
    node *cursor = table[hash_value];
    // if we reach the end of the linked list, return false
    while (cursor != NULL)
    {
        // traverse linked list, looking 1 node at a time for the word (strcasecmp)
        // if we find the word, retrun true
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        else
        {
            // set the pointer to the next element in the linked list
            cursor = cursor->next;
        }
    }
    //once we reach the end of the list, return false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // Hashes word to a number
    unsigned long hash = 5381;
    int c;
    while ((c = toupper(*word++)))
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open dictionary
    FILE *dict = fopen(dictionary, "r");
    if (dictionary == NULL)
    {
        printf("Unable to open dictionary\n");
        return false;
    }
    //word array
    char word1[LENGTH + 1];

    //read strings from file one at a time
    while (fscanf(dict, "%s", word1) != EOF)
    {
        //create new node for each word
        node *n = malloc(sizeof(node));

        //check to see if n = null
        if (n == NULL)
        {
            fclose(dict);
            return false;
        }

        //copy word from dictionary into node
        strcpy(n->word, word1);

        //hash word to obtain hash value
        int location = hash(word1);

        //insert node into hash table at that location
        n->next = table[location];
        table[location] = n;
        counter++;
    }
    //close dictionary
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (counter == 0)
    {
        return 0;
    }
    else
    {
        return counter;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //iterate through each linked list in table
    for (int i = 0; i < N; i++)
    {
        //set cursor equal to first element in each linked list
        node *cursor = table[i];
        //while there are still elements in linked list
        while (cursor != NULL)
        {
            //set tmp = cursor
            node *tmp = cursor;
            //move cursor to next element in list
            cursor = cursor->next;
            //free tmp
            free(tmp);
        }
        if (i == N - 1 && cursor == NULL)
        {
            return true;
        }
    }
    return false;
}
