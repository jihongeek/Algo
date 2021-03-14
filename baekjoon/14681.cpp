#include <stdio.h>
int main(void){
    int x,y;
    scanf("%d",&x);
    scanf("%d",&y);
    if (x>0 && y>0)
    {
        printf("%d\n",1);
    }
    else if (x<0 && y>0)
    {
        printf("%d\n",2);
        
    }
    else if (x<0 && y<0)
    {
        printf("%d\n",3);
        
    }
    else
    {
        printf("%d\n",4);

    }
}