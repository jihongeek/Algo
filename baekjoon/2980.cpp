#include <stdio.h>
int main(void){
    int n,l,t,location,i =0;
    int drg[100][3];
    scanf("%d %d",&n,&l);
    for (int i = 0; i<n;i++)
    {
        scanf("%d %d %d",&drg[i][0],&drg[i][1],&drg[i][2]);    
    }
    while(l>0)
    {
        if (location == drg[i][0])
        {
            if(drg[i][1] != 0)
            { 
                t = t + 1;
                drg[i][1] = drg[i][1] - 1;
                continue;
            }
            else
            {
                drg[i][2] = drg[i][2] - 1
            }
            
        }

        l = l-1;
        t = t + 1;
        location = location + 1;
    }
}