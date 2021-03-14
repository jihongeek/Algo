#include <stdio.h>

unsigned long long nPr(int n,int r)
{
    unsigned long long ret = 1;
    if (r == 1)
    {
        return n;
    }
    for (int i = n; i > n-r; i--)
    {
        ret = ret * (unsigned long long)(i);
    }

    return ret;
}

int main(void)
{
    int testcase;
    int n,m;
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&n,&m);
        if (n > (m / 2))
        {
            printf("%llu\n",nPr(m,m-n)/nPr(m-n,m-n));
        }
        else
        {
            printf("%llu\n",nPr(m,n)/nPr(n,n));
        }
        
    }    
}