#include <stdio.h>
int main(void){
    long long a,b,c,x = 0;
    scanf("%lld %lld %lld",&a,&b,&c);
    if (b>=c)
    {
        printf("%d",-1);
    }
    else
    {
        printf("%lld",a/(c-b)+1);
    }
    
}