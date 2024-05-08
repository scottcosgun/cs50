#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg;
    for (int i = 0; i <= height; i++)//iterate through rows
    {
        for (int j = 0; j <= width; j++)//iterate through pixels in rows
        {
            avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0);//find avg of RGB
            //set each value of RGB to avg value for each pixel
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;
    for (int i = 0; i < height; i++)//iterate through rows
    {
        for (int j = 0; j < width; j++)//iterate through pixels in rows
        {
            sepiaRed = round((0.393 * image[i][j].rgbtRed) + (0.769 *image[i][j].rgbtGreen) + (0.189 * image[i][j].rgbtBlue));
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            sepiaGreen = round((0.349 * image[i][j].rgbtRed) + (0.686 *image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue));
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            sepiaBlue = round((0.272 * image[i][j].rgbtRed) + (0.534 *image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue));
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //create an array to store temp values
    RGBTRIPLE temp[height][width];
    for (int i = 0; i <= height; i++)//iterate through rows
    {
        if (width % 2 == 0)//if even
        {
            for (int j = 0; j < (width/2); j++)//iterate through first half of pixels in a row
            {
                int ref = width - j - 1;//pixel opposite to pixel j in row
                temp[i][j] = image[i][j];//store image pixel in temp array
                image[i][j] = image[i][ref];//swap out on left and replace it with opposite pixel on right
                image[i][ref] = temp[i][j];//put values for pixel on left into opposite pixel on right
            }
        }
        else
            for (int j = 0; j < (width -1)/2; j++)
            {
                int ref = width - j - 1;
                temp[i][j] = image[i][j];//store image pixel in temp array
                image[i][j] = image[i][ref];//swap out on left and replace it with opposite pixel on right
                image[i][ref] = temp[i][j];//put values for pixel on left into opposite pixel on right
            }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];//make copy of original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    int red = 0;
    int green = 0;
    int blue = 0;
    float numsquares = 0.00;
    for (int i = 0; i < height; i++)//iterate through rows
    {
        for (int j = 0; j < width; j++)//iterate through pixels
        {
            for (int x = -1; x <= 1; x++)//iterate vertically through pixels top to bottom
            {
                for (int y = -1; y <= 1; y++)//iterate horizontally through pixels left to right
                {
                    if ((i + x) >= 0 && (i + x) <= (height - 1) && (j + y) >= 0 && (j + y) <= (width - 1))//check conditions
                    {
                        red += copy[i + x][j + y].rgbtRed;
                        green += copy[i + x][j + y].rgbtGreen;
                        blue += copy[i + x][j + y].rgbtBlue;
                        numsquares++;
                    }
                }
            }
            image[i][j].rgbtRed = round(red/numsquares);
            image[i][j].rgbtGreen = round(green/numsquares);
            image[i][j].rgbtBlue = round(blue/numsquares);
            red = green = blue = 0;
            numsquares = 0.00;
        }
    }
    return;
}
