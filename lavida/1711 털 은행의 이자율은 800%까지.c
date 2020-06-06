#include <stdio.h>
int main(void){
    int A,B;
    float total;
    scanf("%d %d",&A,&B);
    total = (float)A + (float)A*0.01*(float)B;
    printf("%.1lf",total);
}