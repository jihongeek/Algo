#include <stdio.h>
#include <math.h>

int main(void)
{
    int n;
    int pows[224];
    int nums[4];
    int num;
    int count  = 1;
    scanf("%d",&n);

    for (int i = 1; i<=(int)sqrt(n); i++)
    {
        pows[i] = i * i;
    }

    while (n > 0)
    {
        n = n - pows[(int)sqrt(n)];
        count++;
        if (count > 4) break;
    }
}