#include <stdio.h>
int w,h,x,y,min;
int main(void){
    min = 2000;
    scanf("%d %d %d %d",&x,&y,&w,&h);
    if (w - x < min)
    {
        min = w -x;
    }
    if (h - y < min)
    {
        min = h - y;

    }
    if (x < min)
    {
        min = x;

    }
    if (y < min)
    {
        min = y;
    }
    printf("%d\n",min);
}