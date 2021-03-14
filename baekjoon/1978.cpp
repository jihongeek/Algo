#include <stdio.h>
#define MAX_I 100
int count,isprime;
int main(void){
    int numbers[MAX_I];
    int n;
    scanf("%d",&n);
    for (int i = 0; i<n;i++)
    {
        scanf("%d",&numbers[i]);
        if (numbers[i] == 1)
        {
            continue;
        }
        if (numbers[i] == 2)
        {
            count += 1;
        }
        for (int j = 2; j<numbers[i];j++)
        {
            if (numbers[i]%j == 0)
            {
                isprime = 0;
                break;
            }
            else
            {
                isprime = 1;
            }
            
        }   
        if (isprime == 1)
        {
            count += 1;
        }
    }
    printf("%d\n",count);
}