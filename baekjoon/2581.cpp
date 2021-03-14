#include <stdio.h>
#include <math.h>
#define MAX_I 10000
int sum,isprime,k;
int numbers[MAX_I];
int main(void){
    int m,n;
    scanf("%d",&m);
    scanf("%d",&n);
    for (int i = 2; i<n+1;i++)
    {
        if (i == 1)
        {
            continue;
        }
        if (i == 2 && i >= m)
        {
            sum = sum + i;
            numbers[k] = i;
            k = k + 1;
            continue;
        }
        for (int j = 2; j<i;j++)
        {
            if (i%j == 0)
            {
                isprime = 0;
                break;
            }
            else
            {
                isprime = 1;
            }
        }   
        if (isprime == 1 && i>=m)
        {
            sum = sum + i;
            numbers[k] = i;
            k = k + 1;
        }
    }
    if (numbers[0] == 0)
    {
        printf("%d\n",-1);        
    }
    else
    {
        printf("%d\n",sum);
        printf("%d\n",numbers[0]);
    }
    
}