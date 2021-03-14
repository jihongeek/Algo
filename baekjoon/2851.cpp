#include <stdio.h>

int main(void)
{
    int d, before_d, sum, num, fake_sum;
    d = 100;
    sum = 0;
    fake_sum = 0;
    for (int i = 0; i < 10; i++)
    {
        before_d = d;
        scanf("%d",&num);
        fake_sum = fake_sum + num;
        d =  100 - fake_sum;
        if (d<0) d = d*-1;
        if (d > before_d) break;
        sum = fake_sum;
    }
    printf("%d",sum);
}