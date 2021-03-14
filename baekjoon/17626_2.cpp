#include <stdio.h>

int main(void)
{
    int n;
    int min = 4;
    int num = 4;
    scanf("%d",&n);


    for (int i = 0; i*i <= n; i++)
    {
        for (int j = 0; j*j <= n; j++)
        {
            for (int k = 0; k*k <= n; k++)
            {
                if (i * i + j * j + k * k  == n)
                {
                    num = 3;
                }
                if (i * i + j * j == n)
                {
                    num = 2;
                }
                if (i * i == n)
                {
                    num = 1;
                }
                if (min > num)
                {
                    min  = num;
                }
            }
        }
    }
    printf("%d", min);
}