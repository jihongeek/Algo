#include <stdio.h>

int n;
int nums[20] = {1,};

void hanoi(int num, int from, int to, int other)
{
    if (num == 0)
    {
        return;   
    }
    hanoi(num-1, from, other, to);
    printf("%d %d\n",from+1,to+1);
    hanoi(num-1, other, to, from);
}

int main(void)
{
    scanf("%d",&n);
    for (int i = 1; i<n+1; i++)
    {
        nums[i] = 2*nums[i-1]+1;
    }
    printf("%d\n",nums[n-1]); 
    hanoi(n,0,2,1);
}