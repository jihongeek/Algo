#include <stdio.h>

int zero[40];
int one[40];
int n,t;

int main(void)
{
    scanf("%d",&t);
    for (int i = 0; i<t; i++)
    {
        scanf("%d",&n);
        for (int j = 0; j<=n; j++)
        {
            if (j == 0)
            {
                zero[j] = 1;
                one[j] = 0;
            }
            else if (j == 1)
            {
                zero[j] = 0;
                one[j] = 1;
            }
            else
            {
                zero[j] = zero[j-1] +zero[j-2];
                one[j] = one[j-1] + one[j-2];
            }
        }
        printf("%d %d\n",zero[n],one[n]);
    }
}