#include <stdio.h>
int main(void){
    int i,T,x,sum,sos;
    scanf("%d",&T);
    while (T--)
    {   
    scanf("%d",&x);
        i = 1;
        sos = 0;
        while (i<x+1){
        sum = i*(i+1)/2;
        sos = sos + sum;
        i = i + 1;
        }
        printf("%d\n",sos);
    }
    
}