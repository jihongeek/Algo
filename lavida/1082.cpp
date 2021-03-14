#include <stdio.h>

int main(void)
{
    int testcase;
    int n,m;
    long long sum;
    
    scanf("%d",&testcase);
    
    while (testcase--)
    {
        sum = 0;
        scanf("%d %d", &n, &m);
        for (int i = n; i <= m; i++)
        {
            sum = sum + i;
        }
        printf("%lld\n", sum);
    }
}