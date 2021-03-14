#include <stdio.h>
int main(void){
    int n;
    scanf("%d",&n);
    for (int i = 1;i<n+1;i++)
    {
        if (n == 1)
        {
            printf("*");
            break;
        }
        for (int j =0 ; j <n-i; j++)
        {
         printf(" ");
        }
        for (int j = 0; j <(2*i)-1; j++)
        {
         printf("*");
        }
        for (int j = 0; j <n-i; j++)
        {
         printf(" ");
        }
        printf("\n");
    }
    for (int i = n-1;i>0;i--)
    {
        for (int j =0 ; j <n-i; j++)
        {
         printf(" ");
        }
        for (int j = 0; j <(2*i)-1; j++)
        {
         printf("*");
        }
        for (int j = 0; j <n-i; j++)
        {
         printf(" ");
        }
        printf("\n");
    }
}