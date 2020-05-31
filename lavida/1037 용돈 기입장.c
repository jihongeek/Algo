#include <stdio.h>
int main(void){
    int testcase;
    int N,M,N1;
    int total = 0;
    scanf("%d",&testcase);
    scanf("%d",&N);
    N1 = N;
    while (N--)
    {
        scanf("%d",&M);
        total = total + M;
    }
    printf("%d %d\n",total,total/N1);
    
}