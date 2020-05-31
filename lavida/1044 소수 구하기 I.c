#include <stdio.h>
int main(void){
    int N,T,A;
    scanf("%d",&T);
    while (T--){
        scanf("%d",&N);
        for (int i = 2; i < N; i++){
            if (N%i==0){
                A = 0;
                break;
            } else {
                A = 1;
            }
        }
        if (N == 2){
            A = 1;
        }
        if (A == 1){
            printf("Prime\n");
        } else {
            printf("Not Prime\n");
        }
    }
    
}