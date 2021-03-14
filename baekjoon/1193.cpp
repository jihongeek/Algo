#include <stdio.h>
int main(void){
    long long n,x;
    int i,j,m,s;
    i = 1;
    n = 0;
    scanf("%lld",&x);
    while (1)
    {
        if (x == 1)
        {
            printf("1/1\n");
            break;
        }
        for (j = 1;j<i+1;j++)
        {
            n = n + 1;
            if ((i+1)%2 == 0)
            {
                s = i + 1 - j;
                m = j;
            }
            else
            {
                m = i + 1 - j;
                s = j;
            }
            if (n == x)
            {
                printf("%d/%d\n",s,m);
                break;
            }
        }
        if (n == x)
        {
            break;
        }
        i = i + 1;
    }
}
