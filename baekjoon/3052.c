#include <stdio.h>
int main(void){
    int nums[10];
    int num = 0;
    int count = 0;
    for (int i = 0;i<10;i++)
    {
        scanf("%d",&num);
        nums[i] = num % 42;
    }
    for (int i = 0;i<10;i++)
    {
        for (int j = 1 ;j<10;j++)
        {
            if(nums[i] =! nums[j])
            {
                count = count + 1;
            }
        }
    }
    printf("%d\n",count);
}