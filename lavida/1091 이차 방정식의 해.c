#include <stdio.h>
int main(void){
    int testcase;
    int a,b,c;
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d %d",&a,&b,&c);
        if (b*b-4*a*c>0){
            printf("This Equation has two answers\n");
        }
        if (b*b-4*a*c==0){
            printf("This Equation has only one answer\n");
        }
        if (b*b-4*a*c<0){
            printf("This Equation has no answer\n");
        }
    }
    
}