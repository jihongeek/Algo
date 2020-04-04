#include <stdio.h>
int main(void){
    int first,second,third,fourth,fifth,sixth = 0;
    scanf("%d %d %d %d %d",&first,&second,&third,&fourth,&fifth);
    sixth = (first*first+second*second+third*third+fourth*fourth+fifth*fifth)%10;
    printf("%d",sixth);
}