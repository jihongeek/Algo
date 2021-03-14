#include <stdio.h>

int rev(int x)
{
    int reved_x, num, ex , numarr[4],tensqr;
    num  = x;
    ex = 0;
    tensqr = 1;
    while(num)
    {
        numarr[ex] = num  % 10;
        ex++;
        num = num / 10;   
    }
    for (int i = ex-1; i>=0; i--)
    {
        if (i == ex-1)
        {
            num = num + numarr[i];
            continue;
        }
        tensqr = tensqr * 10;
        numarr[i] = numarr[i] * tensqr;
        num = num + numarr[i];
    }
    return num;
}

int main(void)
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d",rev(rev(x)+rev(y)));
}