#include <stdio.h>
int main(void){
    int testcase;
    int N,M,N1,total;
    scanf("%d",&testcase);
    while (testcase--)
    {
        total = 0;
        scanf("%d",&N);
        N1 = N;
        while (N--)
        {
            scanf("%d",&M);
            total = total + M;
        }
        printf("%d %d\n",total,total/N1);
    }
}