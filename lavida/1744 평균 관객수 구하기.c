#include <stdio.h>
int main(void){
    int a,b,c,d,e,f,g;
    float avg;
    scanf("%d %d %d %d %d %d %d",&a,&b,&c,&d,&e,&f,&g);
    avg = (float)(a+b+c+d+e+f+g)/7;
    printf("%.2lf",avg);
}