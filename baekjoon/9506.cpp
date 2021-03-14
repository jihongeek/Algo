#include <stdio.h>

int main(void)
{
    int n , nums[100002] , index;
    int sum = 0;
    while (1)
    {
        index = 0;
        sum = 0;
        scanf("%d",&n);
        if (n == -1) break;
        for (int i = n; i>1; i--)
        {
            if (n % i == 0)
            { 
                sum = sum + (n/i);
                nums[index] =  (n/i);
                index++;
            }
        }
        if (sum == n)
        {
            printf("%d =",n);
            for (int i = 0; i<index; i++)
            {
                if (i == index-1) printf(" %d\n",nums[i]);
                else printf(" %d +",nums[i]);
            }
        }
        else printf("%d is NOT perfect.\n",n);
    }
    
}