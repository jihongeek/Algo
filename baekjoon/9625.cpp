#include <stdio.h>

int a[40];
int b[40];
int k;

int main(void)
{
    scanf("%d", &k);
    for (int j = 0; j <= k; j++)
    {
        if (j == 0)
        {
            a[j] = 1;
            b[j] = 0;
        }
        else if (j == 1)
        {
            a[j] = 0;
            b[j] = 1;
        }
        else
        {
            a[j] = a[j - 1] + a[j - 2];
            b[j] = b[j - 1] + b[j - 2];
        }
    }
    printf("%d %d", a[k], b[k]);
}