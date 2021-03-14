#include <stdio.h>
int main(void){
    long long answer;
    int a,b;
    scanf("%d %d",&a,&b);
    answer = (long long)(a+b)* (long long)(a-b);
    printf("%lld\n",answer);
}