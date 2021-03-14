#include <stdio.h>

int main(void)
{
    int n,max,i,j,a,b,cnt;
    while (scanf("%d %d",&i,&j) != EOF)
    {
        printf("%d %d ",i,j);
        max = 0;
        if (i > j)
        {
            int tmp;
            tmp = i;
            i = j;
            j = tmp;
        }
        for (i; i <= j; i++)
        {
            a = i;
            cnt = 1;
            while (a > 1)
            {

                if(!(a%2))
                {
                    a = a/2;
                }
                else
                {
                    a = a *3+1;
                }
                cnt = cnt + 1;
            }
            if (cnt > max)
            {   
                max = cnt;
            }
        }
        printf("%d\n",max);
    }
}