#include <stdio.h>
int main(void){
    long long A,B,V;
    scanf("%lld %lld %lld",&A,&B,&V);
    printf("%lld",(V-B)/(A-B));
}