#include <stdio.h>
long long n;
int main(void){
    int i = 2;
    int j = 1;
    scanf("%lld",&n);
    while (1)
    {
        if (n == 1)
        {
            printf("1\n");
            break;
        }
        if (n >= i && n < i+j*6)
        {
            printf("%d",j+1);
            break;
        }
        i = i + j*6;
        j = j + 1;
    }    
}