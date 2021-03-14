#include <stdio.h>
int main(void){
    int testcase,a,b;
    scanf("%d",&testcase);
    while(testcase--)
    {
        scanf("%d %d",&a,&b);
        if (a == 0 && b == 0)
        {
            break;
        }
        printf("%d\n",a+b);
    }
}