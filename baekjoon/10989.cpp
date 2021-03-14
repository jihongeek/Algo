#include <stdio.h>
int inputnums[10001];
int main(void)
{
    int n,x;
    scanf("%d",&n);
    for (int i = 0; i<n; i++)
    {
        scanf("%d",&x);
        inputnums[x-1] = inputnums[x-1] + 1;
    }
    for (int i = 0; i<10000; i++)
    {
        for (int j = 0; j<inputnums[i]; j++)
        {
            printf("%d\n",i+1);
        }   
    }
}