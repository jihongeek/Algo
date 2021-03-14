#include <stdio.h>

int n,n1,n2,n12;

int main(void)
{
    scanf("%d %d %d",&n1,&n2,&n12);
    n = (n1+1)*(n2+1)/(n12+1)-1;
    printf("%d",n);
}