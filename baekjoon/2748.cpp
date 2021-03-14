#include <stdio.h>
int main(void){
    int n;
    long long fibonums[91];
    scanf("%d",&n);
    for (int i = 0;i<n+1;i++)
    {
        if (i == 0)
        {
            fibonums[i] = 0;
        }
        else if (i == 1)
        {
            fibonums[i] = 1;
        }
        else
        {
            fibonums[i] = fibonums[i-2]+fibonums[i-1];
        }
    }
    printf("%lld\n",fibonums[n]);
}