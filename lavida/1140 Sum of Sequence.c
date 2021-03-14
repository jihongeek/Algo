#include <stdio.h>
#define MAX_I 10000
int main(void){
    int T,K,N,sum,count;
    int L[MAX_I];
    scanf("%d",&T);
    while (T--)
    {
        count = 0;
        scanf("%d %d",&N,&K);
        for (int i = 0;i<N;i++)
        {
            scanf("%d",&L[i]);
        }
        for (int j = 0;j<N;j++)
        {
            sum = 0;
            for (int i = j;i<N;i++)
            {
                sum = sum + L[i];
                if (sum % K == 0)
                {
                    count = count + 1;
                }
            }
        }
        printf("%d\n",count);
    }
    
}