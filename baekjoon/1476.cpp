#include <stdio.h>

int main(void)
{
    int e,s,m;
    int count = 1;
    scanf("%d %d %d",&e,&s,&m);
    while(e+s+m != 3)
    {
        if (e == 1) e = 15;
        else e--;
        if (s == 1) s = 28;
        else s--;
        if (m == 1) m = 19;
        else m--;
        count++;
    }
    printf("%d",count);
}