#include <stdio.h>
int main(void){
    int T,MO,MY,WO,WY,total;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d %d %d %d",&MO,&WO,&MY,&WY);
        total = 0;
        if (WO + WY >0)
        {
            total = total + WO + WY;
            printf("%d\n",total);       
        } else if ( MY > 0 ){
            printf("%d\n",1);       
        } else
        {
            printf("Not Attended\n");
        }
    }
    
}