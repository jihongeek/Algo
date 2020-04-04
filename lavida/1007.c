#include <stdio.h>
int main(void){
    double T,N =0;
    double O = 0;
    scanf("%lf\n%lf",&T,&N);
    O = N / (1 + T * 0.01);
    printf("%.2lf",O);
}
