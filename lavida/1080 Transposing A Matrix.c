#include <stdio.h>
#define MAX_R 100
#define MAX_C 100
int main(void){
    int testcase,a,b;
    int m[MAX_R][MAX_C];
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&a,&b);
        for(int i = 0; i<a;i++)
        {
            for (int j = 0; j < b; j++)
            {
                scanf("%d",&m[i][j]);
            }
        }
        for(int i = 0; i<b;i++)
        {
            for (int j = 0; j < a; j++)
            {
                printf("%d ",m[j][i]);
            }
            printf("\n");
        }
    }
    
}