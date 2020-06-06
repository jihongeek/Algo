#include <stdio.h>
int main(void){
    int testcase;
    int N;
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d",&N);
        if (N%2==0 && N>2){
           printf("%d %d\n",2,N-2); 
        }
        else
        {
            printf("NO\n");
        }
    }
}