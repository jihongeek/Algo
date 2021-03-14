#include <stdio.h>

int count = 1;
int nums[10] = {1,1,1,1,1,1,1,1,1,1};
char roomnum[7] = {0,};
int main(void)
{
    scanf("%s",roomnum);
    for (int i = 0; roomnum[i]; i++)
    {
        if (roomnum[i] - 48 == 6 && !nums[6])
        {
            if (nums[9])
            {
                nums[9]--;
            }
            else
            {
                count++;
                for (int j = 0; j < 10; j++)
                {
                    nums[j]++;
                }
                nums[6]--;
            }
        }
        else if (roomnum[i] - 48 == 9 && !nums[9])
        {
            if (nums[6])
            {
                nums[6]--;
            }
            else
            {
                count++;
                for (int j = 0; j < 10; j++)
                {
                    nums[j]++;
                }
                nums[9]--;
            }
        }
        else
        {
            if (nums[roomnum[i] - 48])
            {
                nums[roomnum[i] - 48]--;
            }
            else
            {
                count++;
                for (int j = 0; j < 10; j++)
                {
                    nums[j]++;
                }
                nums[roomnum[i] - 48]--;
            }
            
        }
        
    }
    printf("%d",count);
}