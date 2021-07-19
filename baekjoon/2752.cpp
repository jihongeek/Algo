#include <stdio.h>

int main(void)
{
    int a,b,c;
    int max,min,mid;
    scanf("%d %d %d",&a,&b,&c);
    max = a;
    min = a;
    mid = a;

    if (b > max) max = b;
    if (b < min) min = b;
    if (c > max) max = c;
    if (c < min) min = c;
    if (b != max && b != min) mid = b;
    if (c != max && c != min) mid = c;
    printf("%d %d %d",min,mid,max);
}