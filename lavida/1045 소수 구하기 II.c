#include <stdio.h>
int main(void){
    int T,PN,a,b,A;
    scanf("%d",&T);
    while (T--){
        PN = 0;
        scanf("%d %d",&a, &b);
        for (a; a<b+1; a++){
            if (a==2){
                PN = PN + 1;
                continue;
            }
            for (int i = 2; i < a; i++){
                if (a%i==0){
                    A = 0;
                    break;
                } 
                A = 1;
            }
            if(A==1){
                PN = PN + 1;
            }
        }
        printf("%d\n",PN);
    }
    
}