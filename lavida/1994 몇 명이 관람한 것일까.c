#include <stdio.h>
int main(void){
    int a,b,c,d,e,f,g,avg,total;
    scanf("%d %d %d %d %d %d %d",&a,&b,&c,&d,&e,&f,&g);
    total = a+b+c+d+e+f+g;
    avg = (total)/7;
    printf("%d\n%d",total,avg);
}