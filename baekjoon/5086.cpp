#include <stdio.h>

int main(void)
{
    int m,n;
    while (1)
    {
        scanf("%d %d",&m,&n);
        if (m == 0 && n == 0)
        {
            break;
        }
        if (n%m == 0)
        {
            printf("factor\n");
        }
        else if (m%n == 0)
        {
            printf("multiple\n");
        }
        else
        {
            printf("neither\n");
        }
        
        
    }
    
}