#include <stdio.h>
#include <math.h>
#define MAX_I 20
int main(void){
    int T,N,total,avg,min;
    int S[MAX_I];
    scanf("%d",&T);
    while (T--)
    {
        total = 0;
        min = 0;
        scanf("%d",&N);
        for (int i = 0;i<N;i++)
        {
            scanf("%d",&S[i]);
            total = total + S[i];
        }
        avg = total/N;
        for (int i = 0; i<N;i++)
        {
            if (abs(avg - S[i]) < abs(avg - min))
            {
                min = S[i];
            }
        }
        printf("%d\n",min); 
    }
}