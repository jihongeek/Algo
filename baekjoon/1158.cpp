#include <stdio.h>

int nums[5001];
int josephus[5001];
int main(void)
{
    int n,k,index,index_josephus;
    index = -1;
    int isFinished = 0;
    index_josephus = 0;
    scanf("%d %d",&n,&k);
    for (int i = 0; i < n; i++)
    {
        nums[i] = i + 1;
    }
    while (n > index_josephus)
    {
        for (int i = 0; i<k;)
        {
            if (index + 1 > n - 1) 
            {
                if (nums[index+1-n] != -1)
                {
                    i++;
                }
                index = (index + 1) - n;
            }
            else
            {
                if (nums[index+1] != -1)
                {
                    i++;
                }
                index++;
            } 
            
        }
        
        josephus[index_josephus] = nums[index];
        nums[index] = -1;
        index_josephus++;
    }
    for (int i = 0; i<n; i++)
    {
        if (n == 1)
        {
            printf("<%d>",josephus[i]);
            break;
        }
        if (i == 0)
        {
            printf("<%d, ",josephus[i]);
        }
        else if (i == n - 1)
        {
            printf("%d>",josephus[i]);
        }
        else
        {
            printf("%d, ",josephus[i]);
        }
    }
}