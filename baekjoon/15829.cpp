#include <stdio.h>

long long bigPow(long long x, long long n)
{
    long long powedNum = 1;
    if (x == 0)
    {
        return 0;
    }
    else if (n == 0)
    {
        return 1;
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            powedNum = powedNum * x;
        }
    }
    return powedNum;
    
}

int main(void)
{
    int l;
    long long hash = 0;
    char string[51];
    scanf("%d",&l);
    scanf("%s",&string);
    for (int i = 0; i < l; i++)
    {
        hash = hash + (long long)(string[i]-'a'+1)*bigPow(31,i);
    }
    hash = hash % 1234567891LL;
    printf("%lld",hash);
}