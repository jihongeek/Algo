#include <stdio.h>
int main(void){
    long long fibonums[2],temp;
    int n;
    scanf("%d",&n);
    for (int i = 0; i<n+1;i++)
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
            temp = fibonums[1];
            fibonums[1] = fibonums[0] + fibonums[1];
            fibonums[0] = temp;
        }
    }
    printf("%lld\n",fibonums[1]);
}