#include <stdio.h>

int main(void)
{
    int rate[3],min_i,min;
    min_i = 3;
    min=101;
    for (int i = 0;i<3;i++)
    {
        scanf("%d",&rate[i]);
        if (rate[i] < min)
        {
            min = rate[i];
            min_i = i;
        }
    }
    if (rate[0] + rate[1] + rate[2] >= 100)
    {
        printf("OK\n");
    }
    else
    {
        if (min_i == 0)
        {
            printf("Soongsil");
        }
        else if (min_i == 1)
        {
            printf("Korea");
        }
        else
        {
            printf("Hanyang");
        }
    }
    
}