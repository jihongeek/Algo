#include <stdio.h>
#define MAX_I 20
int main(void){
    int testcase,n,m,tmp;
    int E[MAX_I];
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&n,&m);
        for (int i = 0; i<n; i++)
        {
            scanf("%d",&E[i]);
        }
        for(int i = 0; i<n;i++)
        {
            for (int j = 0; j < n-1; j++)
            {
                if (E[j] < E[j+1])
                {
                    tmp = 0;
                    tmp = E[j];
                    E[j] = E[j+1];
                    E[j+1] = tmp;    
                }
            }
            
        }
        printf("%d\n",E[n-m]);
    }
    
}