#include <stdio.h>
int main(void){
    int n;
    scanf("%d",&n);
    while (1)
    {
        if (n - 3 == 0 || n - 1  == 0)
        {
            printf("SK\n");
            break;    
        }
        else if (n - 3 > 0)
        {
            n = n - 3;   
        }
        else if (n - 1 > 0)
        {
            n = n - 1;   
        }
        else
        {
            printf("CY\n");
            break;
        }
        if (n - 3 == 0 || n - 1  == 0)
        {
            printf("CY\n");
            break;    
        }
        else if (n - 3 > 0)
        {
            n = n - 3;   
        }
        else if (n - 1 > 0)
        {
            n = n - 1;   
        }
        else
        {
            printf("SK\n");
            break;
        }
    }
}