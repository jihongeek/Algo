#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int cnt = 1;
    int n,m;

    scanf("%d %d",&n,&m);

    if (n <= m)
    {
        cnt++;
    }
    if (n <= m*2)
    {
        cnt = cnt + 2;
    }
    if (n < 3*m+1)
    {
        cnt++;
    }
    if (n < 2*m + 3*m+1)
    
}