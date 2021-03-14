#include <stdio.h>
#include <math.h>
int main(void){
    int x1,y1,r1,x2,y2,r2,t;
    double d;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d %d %d %d",&x1,&y1,&r1,&x2,&y2,&r2);
        d = sqrt(pow(x1-x2,2)+pow(y1-y2,2));
        if (d < (double)(r1+r2))
        {
            if (d<abs((double)(r1)-(double)(r2))||(d == 0 && r1 == r2)||d == 0)
            {
                printf("0\n");
            }
            else
            {
                printf("2\n");
            }
        }
        else if (d == (double)(r1 + r2))
        {
            printf("1\n");    
        }
        else
        {
            printf("-1\n");    
        }
        
        
    }
}