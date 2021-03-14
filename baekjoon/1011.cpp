#include <stdio.h>
int main(void){
    int x,y,n,t,k,count;
    scanf("%d",&t);
    while(t--)
    {
        count = 0;
        scanf("%d %d",&x,&y);
        k = x;
        n = x;
        while (1)
        {
            if (n == y)
            {
                printf("%d\n",count);
                break;
            }
            if (y <= n+k+1)
            {
                k = 1;
            }
            else
            {
                k = k + 1;
            }
            count = count + 1;
            n = n + k;
        }
        
    }
}