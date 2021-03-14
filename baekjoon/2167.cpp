#include <stdio.h>

#define MAX 300

int main(void)
{
    int n,m,i,j,x,y,t,sum;
    int arr[300][300];

    scanf("%d %d",&n,&m);

    for (int a = 0; a<n;a++)
    {
        for (int b = 0; b<m; b++)
        {
            scanf("%d",&arr[a][b]);
        }
    }
    scanf("%d", &t);
    while (t--)
    {
        sum = 0;
        scanf("%d %d %d %d",&i,&j,&x,&y);
        for (int a = i-1; a<x;a++)
        {
            for (int b = j-1; b<y; b++)
            {
                sum = sum + arr[a][b];
            }
        }
        printf("%d\n",sum);
    }
}
