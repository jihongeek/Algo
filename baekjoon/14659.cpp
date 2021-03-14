#include <stdio.h>
#define MAX_I 30000
int main(void){
    int n,max,max_enemies,count;
    int nums[MAX_I];
    scanf("%d",&n);
    for (int i = 0;i<n;i++)
    {
        scanf("%d",&nums[i]);
    }
    max = nums[0];
    count = 0;
    max_enemies = 0;
    for (int i = 1;i<n;i++)
    {
        if (nums[i]> max )
        {
            max = nums[i];
            if(max_enemies < count)
            {
                max_enemies = count;
            }
            count = 0;
        }
        else
        {
            count++;
        }
        if (count > max_enemies)
        {
            max_enemies = count;
        }
    }
    printf("%d\n",max_enemies);
}