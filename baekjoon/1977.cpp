#include <stdio.h>

int main(void)
{
    int squares[10000];
    int index = 0;
    int sum = 0;
    int m,n;
    scanf("%d\n%d",&m,&n);
    for (int j = 1; j * j <= n; j++)
    {
        if (j * j >= m && j * j <= n)
        {
            squares[index++] = j*j;
        }
    }
    for (int i = 0; i < index; i++)
    {
        sum = sum + squares[i];
    }
    if (!index)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n%d",sum,squares[0]);
    }
    
}