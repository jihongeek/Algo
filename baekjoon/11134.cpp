#include <stdio.h>

int testcase;
long long n, c, day;
int main(void)
{
    scanf("%d",&testcase);
    while (testcase--)
    {
        day = 0;
        scanf("%lld %lld",&n,&c);
        day = n/c;
        if (n%c != 0 && n%c<c)
        {
            day++;
        }
        printf("%lld\n",day);
    }
        
}