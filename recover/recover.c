#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
    //ensure correct usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");//declare pointer "input" and open file
    //check to make sure file exists
    if (!input)
    {
        printf("Could not open %s\n", argv[1]);
        return 2;
    }
    //initialize variables
    unsigned char buffer[512];//buffer of 512 bytes
    char jpeg[8];
    int n = 0;//counter variable
    FILE *img = NULL; //declare pointer for image file
    while (fread(buffer, 512, 1, input) == 1) //while there is still memory left to read
    {
        //check if this is the start of a new jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            //check if this is the first jpeg
            if (n > 0)//if this is not the first jpeg, close the previous one
            {
                fclose(img);
            }

            sprintf(jpeg, "%03i.jpg", n);//initialize file
            n++;
            img = fopen(jpeg, "w");//write jpeg to new file
            fwrite(&buffer, 512, 1, img);
        }
        else
        {
            //if a jpeg has already been found
            if (n > 0)
            {
                //keep writing to it
                fwrite(&buffer, 512, 1, img);
            }
        }
    }
    //close all files
    fclose(img);
    fclose(input);
    return 0;
}