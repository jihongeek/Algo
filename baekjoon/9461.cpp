#include <stdio.h>
int main(void){
    int n,t;
    long long fibonums[101];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for (int i = 0;i<n;i++)
        {
            if (i < 3)
            {
                fibonums[i] = 1;
            }
            else
            {
                fibonums[i] = fibonums[i-3]+fibonums[i-2];
            }
        }
        printf("%lld\n",fibonums[n-1]);
    }
}