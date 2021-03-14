#include <stdio.h>

int main(void)
{
    int testcase;
    long long n,m,sum;
    
    scanf("%d",&testcase);
    
    while (testcase--)
    {
        sum = 0;
        scanf("%lld %lld", &n, &m);
        sum = (n+m)*((m-n)+1)/2;
        printf("%lld\n", sum);
    }
}