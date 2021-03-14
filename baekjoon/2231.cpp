#include <stdio.h>

int main(void)
{
    int n,divided_i,sum;
    int answer = 0;
    scanf("%d",&n);
    for (int i = 1;i<=n;i++)
    {
        divided_i = i;
        sum = i; 
        while(divided_i)
        {
            sum = sum + divided_i%10;
            divided_i = divided_i/10;
        }
        if (sum == n)
        {
            answer = i;
            break;
        }
    }
    printf("%d\n",answer);
}