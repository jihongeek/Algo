#include <stdio.h>

int main(void){
    int n,testcase;
    scanf("%d",&testcase);
    while(testcase--)
    {
        scanf("%d",&n);
        for (int i = 1;i<n+1;i++)
        {
            for (int j = 0; j < (n - i); j++)
            {
                printf(" ");
            }
            for (int j = n; j <= i; j--)
            {
                printf("%d", j);
            }
            for (int j = i; j < n; j++)
            {
                printf("%d", j);
            }
            printf("\n");
        }
        for (int i = n-1;i>0;i--)
        {
            for (int j = 0; j < (n - i); j++)
            {
                printf(" ");
            }
            for (int j = 1; j <= i; j++)
            {
                printf("%d", j);
            }
            for (int j = i-1; j > 0; j--)
            {
                printf("%d", j);
            }
            printf("\n");
        }
    }
}   