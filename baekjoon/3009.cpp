#include <stdio.h>
int main(void){
    int x[3];
    int y[3];
    int xnum, ynum,temp = 0;
    for (int i = 0; i<3;i++)
    {
        scanf("%d %d",&x[i],&y[i]);
    }
    if (x[0] != x[1])
    {
        if (x[1] != x[2])
        {
            xnum = x[1];
        }
        else
        {
            xnum = x[0];
        }
    }
    else
    {
        xnum = x[2];
    }
    
    if (y[0] != y[1])
    {
        if (y[1] != y[2])
        {
            ynum = y[1];
        }
        else
        {
            ynum = y[0];
        }
    }
    else
    {
        ynum = y[2];
    }
    
    
    printf("%d %d\n",xnum,ynum); 
}