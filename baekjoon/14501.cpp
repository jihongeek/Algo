#include <stdio.h>

int ts[15];
int ps[15];
int order[15];
int main(void)
{
    int n,tmp;
    int sum = 0;
    int max = 0;
    scanf("%d",&n);
    for (int i =  0; i<n; i++)
    {
        scanf("%d %d",&ts[i],&ps[i]);
    }
    
    for (int i = 0; i < n; i++)
    {
        sum = 0;
        if (i+1 + ts[i] > n) continue;

        for (int j = i; j < n;)
        {
            if (j + ts[j] > n) break;
            sum = sum +  ps[j];
            j = j + ts[j];

        }
        if (sum > max)
        {
            max = sum;
        }  
    }
    printf("%d",max);
}