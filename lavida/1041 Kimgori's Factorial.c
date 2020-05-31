#include <stdio.h>
int main(void){
    int T,N,total,i;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&N);
        total = 1;
        for (int i = 1;i<N+1;i++){
            if (total % i == 0)
            {
                total = total / i;
            } else
            {
            total = total * i;
            }
        }
        printf("%d\n",total);
    }
    
}