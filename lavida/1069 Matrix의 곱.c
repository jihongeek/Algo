#include <stdio.h>
#define MAX_R 20
#define MAX_C 20
int main(void){
    int i,j,k,testcase,n1,m1,n2,m2,sum;
    int a[MAX_R][MAX_C];
    int b[MAX_R][MAX_C];
    int c[MAX_R][MAX_C];
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&n1,&m1);
        for(i = 0; i<n1;i++)
        {
            for (j = 0; j < m1; j++)
            {
                scanf("%d",&a[i][j]);   
            }
            
        }
        scanf("%d %d",&n2,&m2);
        for(i = 0; i<n2;i++)
        {
            for (j = 0; j < m2; j++)
            {
                scanf("%d",&b[i][j]);   
            }
            
        }
        if (n1 != m2 || n2 != m1)
        {
            printf("Impossible\n");
        }
        else
        {
            for(i = 0; i<n1;i++)
            {
                c[i][j] = 0;
                for (j = 0; j < m1; j++)
                {
                    for (k = 0; k<n1; j++)
                    c[i][j] += a[i][k] * b[k][j];
                }
                
            }
            for(i = 0; i < m1; i++)
            {
        		for(j = 0; j < m2; j++)
                {
       			printf("%d ", c[i][j]);
                }
          		printf("\n");
	        }



        }
    }
    
}