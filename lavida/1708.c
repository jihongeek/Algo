#include <stdio.h>
int main(void){
    int fisrt,second,third,fourth = 0;
    float score = 0;
    scanf("%d %d %d %d",&fisrt,&second,&third,&fourth);
    score = fisrt - second;
    score = score * third;
    score = score / fourth;
    printf("%.2lf",score);  
}