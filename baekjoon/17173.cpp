#include <stdio.h>

int main(void)
{
    int m,n;
    int knums[1000] = {0,};
    int multnums[1000] = {0,};
    int sum = 0;
    scanf("%d %d", &n,&m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d",&knums[i]);
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 1; knums[i]*j <= n; j++)
        {
            if (multnums[knums[i]*j-1]) continue;
            multnums[knums[i]*j-1] = 1;
        }
    }

    for (int i = 1; i < n; i++)
    {
        if (multnums[i])
            sum = sum + (i+1);
    }

    printf("%d",sum);
}