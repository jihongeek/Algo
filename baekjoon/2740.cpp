#include <stdio.h>

int m1[10001], m2[10001];
int multiplied_m[10001];
int main(void)
{
    int n, m, k, x, index, index_mult;

    scanf("%d %d",&n,&m);
    index = 0;
    for (int i = 0; i< n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d",&m1[index]);
            index++;    
        }    
    }
    
    scanf("%d %d",&m,&k);
    index = 0;
    for (int i = 0; i < m; i++)
    {
        x = i;
        for (int j = 0; j < k; j++)
        {
            scanf("%d",&m2[x]);
            x = x + m; 
        }    
    }
    x = 0;
    for (int i = 0; i < n; i++)
    {
        index_mult = 0;
        for (int j = 0; j < k; j++)
        {
            for (int p = 0; p < m; p++)
            {
                multiplied_m[index] = multiplied_m[index] + m1[x+p] * m2[index_mult];
                index_mult++;
            }
            index++;   
        }
        x = x + m; 
    }

    for (int i = 0; i < n*k; i++)
    {
        if ((i + 1) % n == 0)
        {
            if (i != n*k - 1)
            {
                printf("%d\n", multiplied_m[i]);
            }
            else
            {
                printf("%d", multiplied_m[i]);
            }
        }
        else
        {
            printf("%d ",multiplied_m[i]);
        }
    }
}
