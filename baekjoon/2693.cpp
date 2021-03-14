#include <stdio.h>

int main(void)
{
    int nums[10],n,tmp;
    scanf("%d",&n);
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < 10; i++)
        {
            scanf("%d",&nums[i]);
        }
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (nums[j]>nums[j+1])
                {
                    tmp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = tmp;
                }
            }
        }
        printf("%d\n",nums[7]);    
    }
}