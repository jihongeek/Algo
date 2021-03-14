#include <stdio.h>

int main(void)
{
    int n, sticks[100000],max,count;
    scanf("%d",&n);
    count = 0;
    max = 0;
    for (int i = n-1; i>=0; i--)
    {
        scanf("%d\n",&sticks[i]);
    }
    for (int i = 0; i<n; i++)
    {
        if (max < sticks[i])
        {
            max = sticks[i];
            count++;
        }
    }
    printf("%d\n",count);
}