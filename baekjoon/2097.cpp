#include <stdio.h>
#include <cmath>
int main(void){
    long long n;
    int a;
    scanf("%lld",&n);
    if (n <= 4)
    {
        printf("%d",4);
    } 
    else 
    {
        a = (int)sqrt(n);
        if (n - a*a <= a)
        {
            printf("%d\n",(2*a-1)*2);
        }
        else
        {
            printf("%d\n",a*4);
        }
        
    }
}