#include <stdio.h>
int main(void){
    int testcase,N,numplus;
    scanf("%d",&N);
    if (N ==1){
        numplus = 2;
    } else {
        numplus = N + (N - 1);
    }
    for (int i = 1;i<=N+numplus;i++){
        if (i < N){
        for (int j = 1; j <=N+numplus+1 ; j++){
            if (j==N+numplus+1){
                printf("\n");
            }
        }
    } else if (i == N){
        for (int j = 0; j <= N+numplus+1; i++){
            printf("%d",j);
            if (j==N+numplus+1){
                printf("\n");
            }
        }
        
    }
    
}