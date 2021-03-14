#include <stdio.h>
int main(void){
    int n;
    long long fibonums[116];
    scanf("%d",&n);
    for (int i = 1;i<n+1;i++)
    {
        if (i < 4)
        {
            fibonums[i] = 1;
        }
        else
        {
            fibonums[i] = fibonums[i-3]+fibonums[i-1];
        }
    }
    printf("%lld\n",fibonums[n]);
}