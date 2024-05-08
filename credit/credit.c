#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //amex - 15 digits, starts with 34 or 37
    //mastercard - 16 digits, starts with 51, 52, 53, 54, 55
    //visa - 13 or 16 digits, starts with 4
    //4003600000000014 % 10 = 4 (remainder)
    //first prompt the user for a credit card number
    //next calculate the checksum
    //then check for card length and starting digits
    //if it matches checksum and card length and starting digit requirements, print out card type
    //get card number
    long card = get_long("Please enter your credit card number: ");
    //count digits
    int i = 0;
    long n = card;
    while (n>=1)
    {
        n = n / 10;
        i++;
    }
    //determine if length is valid
    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    //calculate checksum
    int sum1 = 0;
    int sum2 = 0;
    //split long into digits, starting with second to last digit.
    //first calculate the sum of digits that will not be multiplied by 2
    int d;
    long split1 = card;
    while (split1 >= 1)
    {
        d = (split1 % 10);
        sum2 = sum2 + d;
        split1 = split1 / 100;
    }
    //now calculate sum of every other digit multiplied by 2, starting with second to last.
    long split2 = (card/10);
    int dig;
    int prod;
    int num1;
    int num2;
    while (split2 >= 1)
    {
        dig = (split2 % 10);
        prod = (dig * 2);
        split2 = split2 /100;
        //if the product is greater than 10, we need to split it into individual digits before adding
        if (prod >= 10)
        {
            num1 = prod % 10;
            num2 = prod /10;
            sum1 = sum1 + num1 + num2;
        }
        else
        {
            sum1 = sum1 + prod;
        }
    }
    //add up the two sums
    int sum3 = sum1 + sum2;
    int x = i;
    long card2 = card;
    //last digit must be zero. If not, it is invalid
    if (sum3 % 10 != 0)
    {
        printf("INVALID\n");
    }
    //determine if AMEX
    else if (i == 15)
    {
        while (x > 2)
        {
            card2 = card2 / 10;
            x--;
        }
        if (card2 % 10 == 4 || card2 % 10 == 7)
        {
            if (card2 / 10 == 3)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (i == 13)
    {
        while (x > 1)
        {
            card2 = card2 / 10;
            x--;
        }
        if (card2 == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (i == 16)
    {
        while (x > 2)
        {
            card2 = card2 / 10;
            x--;
        }
        if (card2 / 10 == 4)
        {
            printf("VISA\n");
        }
        else if (card2 % 10 <= 5 && card2 % 10 >= 1)
        {
            if (card2 / 10 == 5)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (card2 / 10 < 4 || card2 / 10 > 5)
        {
            printf("INVALID\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}