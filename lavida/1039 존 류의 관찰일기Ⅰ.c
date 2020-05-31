#include <stdio.h>
#include <math.h>
int main(void){
    long long  x,w,y,z,d,r,T,A;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d %d %d %d",&x,&w,&y,&z);
        if ((w+z)/2==y)
        {
            d = w-x;
            A = x + 4*d;
        }
        else
        {
            r = w/x;
            A = x*pow(r,4);
        }
        printf("%d\n",A);
    }
    
}