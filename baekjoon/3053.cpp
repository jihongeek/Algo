#include <stdio.h>
#include <math.h>
int main(void){
    int r;
    scanf("%d",&r);
    double pi = acos(-1);
    printf("%.6lf\n",pi*(double)r*(double)r);
    printf("%.6lf\n",(double)2*(double)r*(double)r);
}