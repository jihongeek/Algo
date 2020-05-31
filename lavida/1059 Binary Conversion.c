#include <stdio.h>
#include <math.h>
int main(void){
    int i,T,count,A;
    long long N,OriN;
    scanf("%d",&T);
    while (T--){
        count = 0;
        A = 0;
        scanf("%d",&N);
        OriN = N;
        while(N > 1){
            N = N /pow(10,count);
            count =  count + 1;
        }
        for (i = count;i>-1;i--){
            A = A + (OriN/(long long)pow(10,i))*pow(2,i);
            if(OriN < pow(10,i)){
                printf("%d",i);
            }
            OriN = OriN-pow(10,i);
            printf("%d\n",OriN);
        }
    }
    
}