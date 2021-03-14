#include <stdio.h>

int main(void)
{
    int testcase;
    scanf("%d",&testcase);
    while(testcase--)
    {
        int h,w,n;
        scanf("%d %d %d",&h,&w,&n);
        if (!(n % h))
        {
            printf("%d%02d\n",h,n/h);
        }
        else
        {
            printf("%d%02d\n",n%h,n/h+1);
        }
        
    }
}