#include <stdio.h>
int main(void){
    int t,w,h,inputn,n;
    scanf("%d",&t);
    while(t--)
    {
        n = 0;
        scanf("%d %d %d",&h,&w,&inputn);
        for (int i = 1;i<w+1;i++)
        {
            for (int j = 1;j<h+1;j++)
            {
                n = n + 1;
                if (n == inputn)
                {
                    printf("%d%02d\n",j,i);
                    break;
                }        
            }
            if (n == inputn)
            {
                break;
            }
        }
    }
}