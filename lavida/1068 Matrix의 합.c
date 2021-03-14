#include <stdio.h>
#define MAX_R 20
#define MAX_C 20
int main(void){
    int testcase,n1,m1,n2,m2;
    int a[MAX_R][MAX_C];
    int b[MAX_R][MAX_C];
    int c[MAX_R][MAX_C];
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&n1,&m1);
        for(int i = 0; i<n1;i++)
        {
            for (int j = 0; j < m1; j++)
            {
                scanf("%d",&a[i][j]);   
            }
            
        }
        scanf("%d %d",&n2,&m2);
        for(int i = 0; i<n2;i++)
        {
            for (int j = 0; j < m2; j++)
            {
                scanf("%d",&b[i][j]);   
            }
            
        }
        if (n1 != n2 || m1 != m2)
        {
            printf("Impossible\n");
        }
        else
        {
            for(int i = 0; i<n1;i++)
            {
                for (int j = 0; j < m1; j++)
                {
                    c[i][j] = a[i][j] + b[i][j];
                    printf("%d ",c[i][j]);   
                }
                printf("\n");
            }
        }
    }
    
}