#include <stdio.h>
int main(void){
    int first = 0;
    int second = 0;
    int third = 0;
    int need = 0;
    scanf("%d",&first);
    scanf("%d",&second);
    scanf("%d",&third);
    need = 20 - (first + second + third);
    printf("%d",need);
}
