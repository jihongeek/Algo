#include <stdio.h>
int main(void){
    int n,i;
    i = 1;
    scanf("%d",&n);
    while (1)
    {
        if (n <= 5)
        {
            printf("%d\n",n);
            break;
        }
        if (i < n && i+4 >= n)
        {
            if ((((i+4 - 1)/4)+1) % 2 == 0)
            {
                printf("%d\n",n-i+1);
                break;
            }
            else
            {
                printf("%d\n",i+4-n+1);
                break;
            }
        }
        else
        {
            i = i + 4;
        }
    }
    
}