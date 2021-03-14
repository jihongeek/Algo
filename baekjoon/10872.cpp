#include <stdio.h>
int fact(int n){
    if(n == 0)
    {
        return 1;    
    }
    else
    {
        return n*fact(n-1);
    }
}
int main(void){
    int n;
    scanf("%d",&n);
    printf("%d\n",fact(n));
}