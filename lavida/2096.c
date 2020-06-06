#include <stdio.h> 
#include <math.h>
#define MAX_I 50

int main(void){
    int T,m,max,min;
    int M[MAX_I];
    scanf("%d",&T);
    while (T--)
    {
        min = 1001;
        max = -1001;
        scanf("%d",&m);

        for (int i = 0;i<m;i++)
        {
            scanf("%d",&M[i]);
            if (min > M[i])
            {
                min = M[i];
            }
            if (max < M[i])
            {
                max = M[i];
            }
        }
        if (abs(max - min)%5==0)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }

    }
}